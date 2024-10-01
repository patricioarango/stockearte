from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect
import random
import string
import os,grpc
import logging
from google.protobuf.json_format import MessageToJson
import sqlalchemy as sa
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)

app = create_app('flask.cfg')

DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+DB_USER+':'+DB_PASSWORD+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME+'?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    product = sa.Column(sa.String(255))
    product_code = sa.Column(sa.String(255))

class Size(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    size = sa.Column(sa.String(255))

class Color(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    color = sa.Column(sa.String(255))

class Article(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    id_product = sa.Column(sa.Integer)
    article = sa.Column(sa.String(255))
    photo_url = sa.Column(sa.String(255))
    id_size = sa.Column(sa.Integer)
    id_color = sa.Column(sa.Integer)
    stock = sa.Column(sa.Integer)    

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def index():
    return render_template('home.html')

@app.route("/novedades", methods=["GET"])
def novedades():
    return render_template('novedades.html')

@app.route('/product')
def product():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        product_stub = ProductServiceStub(channel)
        response = product_stub.FindAll(Product())  
    return render_template('product.html', productos=response.product)

def generate_product_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        product_stub = ProductServiceStub(channel)

        if request.method == 'POST':
          
            nombre = request.form.get('product')
            img = request.form.get('img')
            codigo = request.form.get('code')  
            color = request.form.get('color')
            size = request.form.get('size')
           
            nuevo_producto = Product(
                product=nombre,
                code=codigo,
                img=img,
                color=color,
                size=size,
                enabled=True 
            )
            codeExists = product_stub.FindProductByCode(ProductCodeRequest(code=codigo))
            if codeExists.idProduct > 0:
                nuevo_producto.code = generate_product_code()
            try:
                producto_response = product_stub.SaveProduct(nuevo_producto)
                print("Producto agregado: ", producto_response)

                return redirect(url_for('product'))
            
            except grpc.RpcError as e:
                print("Error al agregar el producto: ", e)
                return f"Error al agregar el producto: {str(e)}", 500

        return render_template('add_product.html',codigo_producto=generate_product_code())

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = ProductServiceStub(channel)
    
        producto = stub.GetProduct(Product(idProduct=id))  
        
        if request.method == 'POST':
            producto.product = request.form['product']
            producto.img = request.form['img']
            producto.color = request.form['color']
            producto.size = request.form['size']
            producto.enabled = 'enabled' in request.form
            
            try:
                stub.SaveProduct(producto)  
                return redirect(url_for('product'))
            except grpc.RpcError as e:
                return f"Error al actualizar el producto: {str(e)}", 500

        return render_template('edit_product.html', producto=producto, )

from google.protobuf.empty_pb2 import Empty




@app.route('/my_products')
def store_products():
    user_store_id = session.get('user_id')
    productos_tienda = get_products_by_store(user_store_id)
    return render_template('my_products.html', productos=productos_tienda,idStore=user_store_id)






if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)