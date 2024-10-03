import datetime
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
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

class Producto(db.Model):
    __tablename__ = 'producto'
    id = sa.Column(sa.Integer, primary_key=True)
    codigo_producto = sa.Column(sa.String(255))

class Talle(db.Model):
    __tablename__ = 'talle'
    id = sa.Column(sa.Integer, primary_key=True)
    talle = sa.Column(sa.String(255))

class Color(db.Model):
    __tablename__ = 'color'
    id = sa.Column(sa.Integer, primary_key=True)
    color = sa.Column(sa.String(255))

class Articulo(db.Model):
    __tablename__ = 'articulo'
    id_producto = sa.Column(sa.Integer, primary_key=True)  
    articulo = sa.Column(sa.String(255))
    url_foto = sa.Column(sa.String(255))
    id_talle = sa.Column(sa.Integer)  
    id_color = sa.Column(sa.Integer)
    stock = sa.Column(sa.Integer)   

class Orden_de_compra(db.Model):
    __tablename__ = 'orden_de_compra'
    id = sa.Column(sa.Integer, primary_key=True)
    id_store = sa.Column(sa.Integer)
    estado = sa.Column(sa.String(255))
    observaciones = sa.Column(sa.Text)
    fecha_creacion = sa.Column(sa.DateTime)
    fecha = sa.Column(sa.DateTime)
    procesado = sa.Column(sa.Integer)   

class Orden_de_compra_item(db.Model):
    __tablename__ = 'orden_de_compra_item'
    id = sa.Column(sa.Integer, primary_key=True)
    id_orden_de_compra = sa.Column(sa.Integer)
    codigo_producto = sa.Column(sa.String(255))
    color = sa.Column(sa.String(255))
    talle = sa.Column(sa.String(255))
    cantidad_solicitada = sa.Column(sa.Integer)  

with app.app_context():
    db.create_all()

def chequearStockIncorrecto(orden_de_compra_items):
    res = []
    for item in orden_de_compra_items:
        if item.cantidad_solicitada <= 0:
            res.append({'codigo_producto': 'Producto codigo: ' + item.codigo_producto, 'error': 'Cantidad solicitada incorrecta'})

def chequearProductosInexistentes(orden_de_compra_items):
    res = []
    for item in orden_de_compra_items:
        producto = Producto.query.filter_by(codigo_producto = item.codigo_producto).first()
        if producto is None:    
            res.append({'codigo_producto': 'Producto codigo: ' + item.codigo_producto, 'error': 'Producto no encontrado'})
    return res            
      
def chequearArticulosInexistentes(ordenes_de_compra_items):
    res = []
    for item in ordenes_de_compra_items:
        color = Color.query.filter_by(color = item.color).first()
        talle = Talle.query.filter_by(talle = item.talle).first()
        producto = Producto.query.filter_by(codigo_producto = item.codigo_producto).first()
        articulo = Articulo.query.filter_by(id_producto = producto.id).filter_by(id_color = color.id).filter_by(id_talle = talle.id).first()
        if articulo is None:
            res.append({'codigo_producto': 'Producto codigo: ' + item.codigo_producto, 'error': 'Articulo no encontrado'}) 
    return res

def chequearArticulosStockInsuficiente(ordenes_de_compra_items):
    res = []
    for item in ordenes_de_compra_items:
        color = Color.query.filter_by(color = item.color).first()
        talle = Talle.query.filter_by(talle = item.talle).first()
        producto = Producto.query.filter_by(codigo_producto = item.codigo_producto).first()
        articulo = Articulo.query.filter_by(id_producto = producto.id).filter_by(id_color = color.id).filter_by(id_talle = talle.id).filter(Articulo.stock >= item.cantidad_solicitada).first()
        if articulo is None:
            res.append({'codigo_producto': 'Producto codigo: ' + item.codigo_producto, 'error': 'El stock del articulo es insuficiente'}) 
    return res

@app.route('/procesar_ordenes_de_compra', methods=["GET"])
def procesar_ordenes_de_compra():
    ordenes = Orden_de_compra.query.filter_by(procesado = 0).filter_by(estado = 'SOLICITADA').all()
    for orden in ordenes:
        if orden.observaciones is None:
            orden.observaciones = ""
        
        #paso 1 - Chequeo de Stock Incorrecto. Con uno incorrecto ya se rechaza la orden
        ordenes_items = Orden_de_compra_item.query.filter_by(id_orden_de_compra = orden.id).all()
        stockIncorrecto = chequearStockIncorrecto(ordenes_items)
        if stockIncorrecto:
            orden.estado = 'RECHAZADA'
            orden.procesado = 1
            for item in stockIncorrecto:
                orden.observaciones += item['codigo_producto'] + item['error'] + '\n'

        #paso 2 - Chequeo de productos inexistentes. Con uno ya se rechaza la orden
        productosInexistentes = chequearProductosInexistentes(ordenes_items)
        if productosInexistentes:
            orden.estado = 'RECHAZADA'
            orden.procesado = 1
            for item in chequearProductosInexistentes:
                orden.observaciones += item['codigo_producto'] + item['error'] + '\n'

        #paso 3 - Chequeo Artículo existentes (puedo tener el producto pero no el artículo)
        
        articulosInexistentes = chequearArticulosInexistentes(ordenes_items)
        if articulosInexistentes:
            orden.estado = 'RECHAZADA'
            orden.procesado = 1
            for item in articulosInexistentes:
                orden.observaciones += item['codigo_producto'] + item['error'] + '\n'

        # solo en caso de que esten todos y los stock sean suficientes, se acepta y despacha
        # si llego hasta acá es porque todos los articulos pedidos existen  
        stockInsuficiente = chequearArticulosStockInsuficiente(ordenes_items)
        if len(stockInsuficiente) > 0:
            orden.estado = 'ACEPTADA'
            orden.procesado = 0
            for item in stockInsuficiente:
                orden.observaciones += item['codigo_producto'] + item['error'] + '\n'

        orden.fecha = datetime.datetime.now()    
        db.session.commit()
    result = {'a': 'b'}
    return result, 200

@app.route("/", methods=["GET"])
def index():
    return render_template('home.html')

@app.route("/novedades", methods=["GET"])
def novedades():
    return render_template('novedades.html')










if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)