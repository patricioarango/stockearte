from app import create_app
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import logging
from google.protobuf.json_format import MessageToJson
from app.models import Talle,Color,Articulo,Producto
from app.models import db
from sqlalchemy.orm import aliased
from app.modulos.orden_de_compra import OrdenDeCompraController  
from kafka import KafkaProducer

logger = logging.getLogger(__name__)

app = create_app('flask.cfg')


@app.route("/", methods=["GET"])
def index():
    return render_template('home.html')

@app.route("/novedades", methods=["GET"])
def novedades():
    return render_template('novedades.html')

@app.route('/product', methods=['GET'])
def lista_productos():
    productos = Producto.query.all()
    for producto in productos:
        producto.articulos = Articulo.query.filter_by(id_producto=producto.id).all()
    return render_template('product.html', productos=productos)

@app.route('/add_product', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        codigo_producto = request.form['codigo_producto']
        
        if not codigo_producto:  
            flash('El código del producto es obligatorio', 'danger')
            return redirect(url_for('nuevo_producto'))

        nuevo_producto = Producto(codigo_producto=codigo_producto)
        db.session.add(nuevo_producto)
        db.session.commit()
        flash('Producto creado exitosamente', 'success')

        return redirect(url_for('lista_productos'))

    return render_template('add_product.html')

@app.route('/list_articles/<int:producto_id>', methods=['GET'])
def list_articles(producto_id):
    color_alias = aliased(Color)
    talle_alias = aliased(Talle)
    producto = Producto.query.filter_by(id=producto_id).first()
    articulosdelproducto = db.session.query(
    Articulo,
    color_alias.color.label('color_value'),
    talle_alias.talle.label('talle_value')
        ).join(color_alias, Articulo.id_color == color_alias.id) \
        .join(talle_alias, Articulo.id_talle == talle_alias.id) \
        .filter(Articulo.id_producto == producto_id).all()

    return render_template('list_articles.html', producto=producto, articulosdelproducto=articulosdelproducto)

@app.route('/add_article_to_product/<int:producto_id>', methods=['GET', 'POST'])
def add_article_to_product(producto_id):
    producto = Producto.query.get(producto_id)
    talles = Talle.query.all()
    colores = Color.query.all()

    if request.method == 'POST':
        nombre_articulo = request.form['articulo']
        url_foto = request.form['url_foto']
        id_talle = request.form['id_talle']
        id_color = request.form['id_color']
        stock = request.form['stock']

        nuevo_articulo = Articulo(
            id_producto=producto_id,
            articulo=nombre_articulo,
            url_foto=url_foto,
            id_talle=id_talle,
            id_color=id_color,
            stock=stock
        )
        db.session.add(nuevo_articulo)
        db.session.commit()
        enviarNovedadKafka(nuevo_articulo)
        flash('Artículo creado exitosamente', 'success')
        return redirect(url_for('list_articles', producto_id=producto_id))

    return render_template('add_article_to_product.html', producto=producto, talles=talles, colores=colores)

def enviarNovedadKafka(articulo):
    color = Color.query.get(articulo.id_color)
    talle = Talle.query.get(articulo.id_talle)
    producto = Producto.query.get(articulo.id_producto)
    articulo.color = color.color
    articulo.talle = talle.talle
    articulo.producto = producto.codigo_producto
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    articulo_dict = {
        "producto_nombre": articulo.articulo,
        "producto": articulo.producto,
        "color": articulo.color,
        "talle": articulo.talle,
        "url_foto": articulo.url_foto
        }
    producer.send('novedades', articulo_dict)
    producer.close()
    return redirect(url_for('list_articles', producto_id=articulo.id_producto))

@app.route('/edit_article/<int:articulo_id>', methods=['GET', 'POST'])
def edit_article(articulo_id):
    articulo = Articulo.query.get(articulo_id)

    talles = Talle.query.all()
    colores = Color.query.all()

    if request.method == 'POST':
        articulo.stock = request.form['stock']

        db.session.commit()
        flash('Artículo editado exitosamente', 'success')
        OrdenDeCompraController.procesar_ordenes_de_compra_aceptadas_pausadas()
        return redirect(url_for('list_articles', producto_id=articulo.id_producto))

    return render_template('edit_article.html', articulo=articulo, talles=talles, colores=colores)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)