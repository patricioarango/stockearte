from . import orden_de_compra_blueprint
from kafka import KafkaConsumer,KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json
from app.models import Orden_de_compra,Talle,Color,Articulo,Producto,Orden_de_compra_item,Orden_de_despacho
from flask import current_app as app
import datetime
from app.models import db

TOPIC_NAME = "orden-de-compra"

@orden_de_compra_blueprint.route('/ver_ordenes_de_compra', methods=['GET'])
def ver_ordenes_de_compra():
    ordenes_de_compra = Orden_de_compra.query.order_by(Orden_de_compra.id.desc()).all()
    return render_template('listado_odc.html', ordenes_de_compra=ordenes_de_compra)

@orden_de_compra_blueprint.route('/ver_orden_de_despacho/<int:id>', methods=['GET'])
def ver_orden_de_despacho(id):
    orden_de_despacho = Orden_de_despacho.query.filter_by(id = id).first()
    return render_template('orden_de_despacho.html', orden_de_despacho=orden_de_despacho)
    
@orden_de_compra_blueprint.route('/orden_de_compra', methods=['GET'])
def consumer_orden_de_compra():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=os.getenv("SERVER-KAFKA-BROKER"),
        client_id = "CONSUMER_CLIENT_ID_24",
        group_id = "CONSUMER_GROUP_PROV24",
        auto_offset_reset = 'earliest',
        enable_auto_commit = True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    while True:
        for message in consumer:
            orden_de_compra_store = message.value 
            print("orden_de_compra_store")
            print(orden_de_compra_store)
            orden_de_compra = Orden_de_compra(
                id_odc_externa = orden_de_compra_store['idPurchaseOrder'],
                id_store = orden_de_compra_store["store"]['idStore'],
                store_code = orden_de_compra_store["store"].get('storeCode', 'storeCodeDefault'),
                fecha_solicitud = orden_de_compra_store['createdAt'],
                estado = orden_de_compra_store['state'],
                procesado = 0
            )
            db.session.add(orden_de_compra)
            db.session.commit()
            for item in orden_de_compra_store['orderItems']:
                orden_de_compra_item = Orden_de_compra_item(
                    id_orden_de_compra = orden_de_compra.id,
                    codigo_producto = item['productCode'],
                    cantidad_solicitada = item['requestedAmount'],
                    color = item['color'],
                    talle = item['size']
                )
                db.session.add(orden_de_compra_item)
                db.session.commit()
            print(f"Message received: {orden_de_compra_store}")
            procesar_ordenes_de_compra_solicitadas()
    return render_template('orden_de_compra.html', ordenes_de_compra=orden_de_compra)    
    

def chequearStockIncorrecto(orden_de_compra_items):
    print(orden_de_compra_items)
    res = []
    for item in orden_de_compra_items:
        if item.cantidad_solicitada <= 0:
            res.append({'codigo_producto': 'Producto codigo: ' + item.codigo_producto, 'error': ' Cantidad solicitada incorrecta'})

def chequearProductosInexistentes(orden_de_compra_items):
    res = []
    for item in orden_de_compra_items:
        producto = Producto.query.filter_by(codigo_producto = item.codigo_producto).first()
        if producto is None:    
            res.append({'codigo_producto': 'Producto codigo: ' + item.codigo_producto, 'error': ' Producto no encontrado'})
    return res            
      
def chequearArticulosInexistentes(ordenes_de_compra_items):
    res = []
    for item in ordenes_de_compra_items:
        producto = Producto.query.filter_by(codigo_producto = item.codigo_producto).first()
        color = Color.query.filter_by(color = item.color).first()
        talle = Talle.query.filter_by(talle = item.talle).first()

        if producto is None:
            res.append({'codigo_producto': item.codigo_producto, 'error': ' Producto no encontrado'})
            continue  
        if color is None:
            res.append({'codigo_producto': item.codigo_producto, 'error': ' Color no encontrado'})
            continue 
        if talle is None:
            res.append({'codigo_producto': item.codigo_producto, 'error': ' Talle no encontrado'})
            continue 

        articulo = Articulo.query.filter_by(id_producto=producto.id, id_color=color.id, id_talle=talle.id).first()
        if articulo is None:
            res.append({'codigo_producto': item.codigo_producto, 'error': ' Articulo no encontrado'}) 
            
    return res

def chequearArticulosStockInsuficiente(ordenes_de_compra_items):
    res = []
    for item in ordenes_de_compra_items:
        color = Color.query.filter_by(color=item.color).first()
        talle = Talle.query.filter_by(talle=item.talle).first()
        producto = Producto.query.filter_by(codigo_producto=item.codigo_producto).first()
        articulo = Articulo.query.filter_by(
            id_producto=producto.id, id_color=color.id, id_talle=talle.id
        ).filter(Articulo.stock >= item.cantidad_solicitada).first()

        if articulo is None:
            res.append({'codigo_producto': item.codigo_producto, 'error': ' El stock del artículo es insuficiente'})

    return res

@orden_de_compra_blueprint.route('/procesar_ordenes_de_compra_solicitadas_por_url', methods=['GET'])
def procesar_ordenes_de_compra_solicitadas_por_url():
    return procesar_ordenes_de_compra('SOLICITADA')

def procesar_ordenes_de_compra_solicitadas():
    return procesar_ordenes_de_compra('SOLICITADA')

def procesar_ordenes_de_compra_aceptadas_pausadas():
    return procesar_ordenes_de_compra('ACEPTADA')

def procesar_ordenes_de_compra(tipoDeEstado):
    ordenes = Orden_de_compra.query.filter_by(procesado = 0).filter_by(estado = tipoDeEstado).all()
    if ordenes:
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

                orden.fecha_procesamiento = datetime.datetime.now()    
                db.session.commit()
                break
            #paso 2 - Chequeo de productos inexistentes. Con uno ya se rechaza la orden
            productosInexistentes = chequearProductosInexistentes(ordenes_items)
            if productosInexistentes:
                orden.estado = 'RECHAZADA'
                orden.procesado = 1
                for item in productosInexistentes:
                    orden.observaciones += item['codigo_producto'] + item['error'] + '\n'

                orden.fecha_procesamiento = datetime.datetime.now()    
                db.session.commit()
                break
            #paso 3 - Chequeo Artículo existentes (puedo tener el producto pero no el artículo)
            articulosInexistentes = chequearArticulosInexistentes(ordenes_items)
            if articulosInexistentes:
                orden.estado = 'RECHAZADA'
                orden.procesado = 1
                for item in articulosInexistentes:
                    orden.observaciones += item['codigo_producto'] + item['error'] + '\n'

                orden.fecha_procesamiento = datetime.datetime.now()    
                db.session.commit()
                break
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
                break    
            else:
                orden.procesado = 1
                id_orden_de_despacho = crearOrdenDeDespacho(orden)
                descontarStock(ordenes_items)
                orden.estado = 'ACEPTADA'
                orden.id_orden_de_despacho = id_orden_de_despacho
                orden.fecha_procesamiento = datetime.datetime.now()    
                db.session.commit()
                break
        return enviarMensajeKafkaStore(orden.id)

@orden_de_compra_blueprint.route('/enviar_mensaje', methods=['GET'])
def enviar_mensaje():    
    id = 1
    return enviarMensajeKafkaStore(id)


def enviarMensajeKafkaStore(id_orden):
    orden = Orden_de_compra.query.filter_by(id = id_orden).first()
    print(orden)
    store_topic = orden.store_code + "_solicitudes"
    # chequeamos si el topic del store existe o lo creamos
    res = checkIFKafkaTopicExists(store_topic)
    if(res == False):
        createKafkaTopic(store_topic)

    producer = KafkaProducer(
        bootstrap_servers=os.getenv("SERVER-KAFKA-BROKER"),
        value_serializer=lambda v: json.dumps(v).encode('utf-8'), 
    )
    id_orden_de_despacho = orden.id_orden_de_despacho if True else 0
    message_dict = {
        "id": orden.id_odc_externa,
        "estado": orden.estado,
        "observaciones": orden.observaciones,
        "id_store": orden.id_store,
        "id_orden_de_despacho": id_orden_de_despacho
        }
    producer.send(store_topic,message_dict)
    print(f"Message sent: {message_dict}")
    producer.close()
    return "mensaje enviado",200

def checkIFKafkaTopicExists(topic_name):
    admin_client = KafkaAdminClient(
    bootstrap_servers=os.getenv("SERVER-KAFKA-BROKER"),
    client_id='admin-client'
    )
    topics = admin_client.list_topics()
    print(topics)
    return topic_name in topics

def createKafkaTopic(topic_name):
    admin_client = KafkaAdminClient(
    bootstrap_servers=os.getenv("SERVER-KAFKA-BROKER"),
    client_id='admin-client'
    )
    topic_list = []
    topic_list.append(NewTopic(name=topic_name, num_partitions=1, replication_factor=1))
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    except TopicAlreadyExistsError:
        print(f"Topic {topic_name} already exists")
    admin_client.close()

def crearOrdenDeDespacho(orden_de_compra):
    orden_de_despacho = Orden_de_despacho(
        id_orden_de_compra = orden_de_compra.id,
        id_odc_externa = orden_de_compra.id_odc_externa,
        fecha_estimada_de_envio = datetime.datetime.now() + datetime.timedelta(days=2)
    )
    db.session.add(orden_de_despacho)
    db.session.commit()
    return orden_de_despacho.id   

def descontarStock(ordenes_items):
    for item in ordenes_items:
        color = Color.query.filter_by(color=item.color).first()
        talle = Talle.query.filter_by(talle=item.talle).first()
        producto = Producto.query.filter_by(codigo_producto=item.codigo_producto).first()
        articulo = Articulo.query.filter_by(
            id_producto=producto.id, id_color=color.id, id_talle=talle.id
        ).first()
        articulo.stock -= item.cantidad_solicitada
        db.session.commit()

def enviarMensajeKafkaOrdenDeDespacho(id_orden_de_compra):  
    orden_de_despacho = Orden_de_despacho.query.filter_by(id_orden_de_compra = id_orden_de_compra).first()  
    orden = Orden_de_compra.query.filter_by(id = orden_de_despacho.id_orden_de_compra).first()
    store_topic = orden.store_code + "_despacho"
    # chequeamos si el topic del store existe o lo creamos
    res = checkIFKafkaTopicExists(store_topic)
    if(res == False):
        createKafkaTopic(store_topic)

    producer = KafkaProducer(
        bootstrap_servers=os.getenv("SERVER-KAFKA-BROKER"),
        value_serializer=lambda v: json.dumps(v).encode('utf-8'), 
    )
    message_dict = {
        "id_orden_de_despacho": orden_de_despacho.id,
        "id_orden_de_compra": orden_de_despacho.id_odc_externa,
        "fecha_estimada_envio": orden_de_despacho.fecha_estimada_de_envio
        
        }
    producer.send(store_topic,message_dict)
    print(f"Message sent: {message_dict}")
    producer.close()
    return "mensaje enviado",200