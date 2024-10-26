from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id_user = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    lastname = sa.Column(sa.String(255))
    username = sa.Column(sa.String(255))
    password = sa.Column(sa.String(255))
    id_role = sa.Column(sa.Integer)
    id_store = sa.Column(sa.Integer)
    enabled = sa.Column(sa.Boolean)

class Role(db.Model):
    __tablename__ = 'role'
    id_role = sa.Column(sa.Integer, primary_key=True)
    role = sa.Column(sa.String(255))
    enabled = sa.Column(sa.Boolean)

class Product(db.Model):
    __tablename__ = 'product'
    id_product = sa.Column(sa.Integer, primary_key=True) 
    product = sa.Column(sa.String(255))
    code = sa.Column(sa.String(255))
    color = sa.Column(sa.String(255))  
    size = sa.Column(sa.String(255))
    img = sa.Column(sa.String(255))
    enabled = sa.Column(sa.Boolean)  

class ProductStock(db.Model):
    __tablename__ = 'product_stock'
    id_product_stock = sa.Column(sa.Integer, primary_key=True) 
    id_product = sa.Column(sa.Integer)
    id_store = sa.Column(sa.Integer)
    stock = sa.Column(sa.Integer) 

class Store(db.Model):
    __tablename__ = 'store'
    id_store = sa.Column(sa.Integer, primary_key=True) 
    store = sa.Column(sa.String(255))
    code = sa.Column(sa.String(255))
    address = sa.Column(sa.String(255))  
    city = sa.Column(sa.String(255))
    state = sa.Column(sa.String(255))
    enabled = sa.Column(sa.Boolean)  
 
class Catalog(db.Model):
    __tablename__ = 'catalog'
    id_catalog = sa.Column(sa.Integer, primary_key=True) 
    catalog = sa.Column(sa.String(255))
    id_store = sa.Column(sa.Integer)

class CatalogProducts(db.Model):
    __tablename__ = 'catalog_products'
    id_catalog_products = sa.Column(sa.Integer, primary_key=True) 
    id_catalog = sa.Column(sa.Integer)  
    id_product = sa.Column(sa.Integer)  

class UserFilters(db.Model):
    __tablename__ = 'user_filters'
    id_user_filter = sa.Column(sa.Integer, primary_key=True)
    id_user = sa.Column(sa.Integer)
    filter = sa.Column(sa.String(255))
    cod_prod = sa.Column(sa.String(255))
    date_from = sa.Column(sa.String(255))
    date_to = sa.Column(sa.String(255))
    state = sa.Column(sa.String(255))
    id_store = sa.Column(sa.Integer)
    enabled = sa.Column(sa.Boolean)

class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.String(255))
    id_dispatch_order = sa.Column(sa.Integer)
    purchase_order_date = sa.Column(sa.String(255))
    observation = sa.Column(sa.Text)
    reception_date = sa.Column(sa.String(255))
    state = sa.Column(sa.String(255))
    id_store = sa.Column(sa.Integer)

class OrderItem(db.Model):
    __tablename__ = 'order_item'
    id = sa.Column(sa.Integer, primary_key=True)
    purchase_order_id = sa.Column(sa.Integer)
    color = sa.Column(sa.String(255))
    size = sa.Column(sa.String(255))
    product_code = sa.Column(sa.String(255))
    send = sa.Column(sa.Boolean)
    requested_amount = sa.Column(sa.Integer)
        