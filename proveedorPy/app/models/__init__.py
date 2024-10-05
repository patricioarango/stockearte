from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()

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
    id_odc_externa = sa.Column(sa.Integer)
    store_code = sa.Column(sa.String(255))
    estado = sa.Column(sa.String(255))
    observaciones = sa.Column(sa.Text)
    fecha_solicitud = sa.Column(sa.DateTime)
    fecha_procesamiento = sa.Column(sa.DateTime)
    fecha_recepcion = sa.Column(sa.DateTime)
    procesado = sa.Column(sa.Integer)   

class Orden_de_compra_item(db.Model):
    __tablename__ = 'orden_de_compra_item'
    id = sa.Column(sa.Integer, primary_key=True)
    id_orden_de_compra = sa.Column(sa.Integer)
    codigo_producto = sa.Column(sa.String(255))
    color = sa.Column(sa.String(255))
    talle = sa.Column(sa.String(255))
    cantidad_solicitada = sa.Column(sa.Integer)      