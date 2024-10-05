from . import orden_de_compra_blueprint
from kafka import KafkaConsumer
import os,json
from app.models import Orden_de_compra,Talle,Color,Articulo,Producto,Orden_de_compra_item
from flask import current_app as app
import datetime
from app.models import db

TOPIC_NAME = "orden_de_compra"

@orden_de_compra_blueprint.route('/orden_de_compra', methods=['GET'])
def consumer_orden_de_compra():
    ssl_cafile = os.path.join(app.static_folder, 'archivos', 'ca.pem')
    ssl_certfile = os.path.join(app.static_folder, 'archivos', 'service.cert')
    ssl_keyfile = os.path.join(app.static_folder, 'archivos', 'service.key')
    '''
    consumer = KafkaConsumer(
        TOPIC_NAME,
        #bootstrap_servers=f"kafka-871a578-pato-ef11.j.aivencloud.com:25630",
        bootstrap_servers=os.getenv("SERVER-KAFKA-BROKER"),
        client_id = "CONSUMER_CLIENT_ID",
        group_id = "CONSUMER_GROUP_PROV1",
        auto_offset_reset = 'earliest', 
        enable_auto_commit = False,
        value_deserializer = lambda x: json.loads(x.decode('utf-8'))
    )
    '''
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=f"kafka-871a578-pato-ef11.j.aivencloud.com:25630",
        client_id = "CONSUMER_CLIENT_ID",
        group_id = "CONSUMER_GROUP_PROV23",
        security_protocol="SSL",
        ssl_cafile=ssl_cafile,
        ssl_certfile=ssl_certfile,
        ssl_keyfile=ssl_keyfile,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    while True:
        for message in consumer:
            print("message")
            print(message)
            orden_de_compra_store = message.value 
            print(orden_de_compra_store)
            orden_de_compra = Orden_de_compra(
                id_odc_externa = orden_de_compra_store['id'],
                fecha_solicitud = orden_de_compra_store['fecha_creacion'],
                estado = orden_de_compra_store['estado'],
                procesado = 0
            )
            db.session.add(orden_de_compra)
            db.session.commit()
            print(f"Message received: {orden_de_compra_store}")

    result = {'a': 'beeeeeee'}
    return result, 200

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

        orden.fecha_procesamiento = datetime.datetime.now()    
        db.session.commit()
    result = {'a': 'b'}
    return result, 200
