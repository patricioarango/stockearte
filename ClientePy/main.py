from app import create_app
#from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect

import random
import string
import os,grpc

from user_pb2 import User

from user_pb2_grpc import UsersServiceStub

from store_pb2 import Store

from store_pb2_grpc import StoreServiceStub

from role_pb2 import Role

from role_pb2_grpc import RoleServiceStub

import logging

from google.protobuf.json_format import MessageToJson

logger = logging.getLogger(__name__)

app = create_app('flask.cfg')

#creo conexion momentanea con base de datos local
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/stockearte'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/stockearte'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://avnadmin:AVNS_ylqtAU8JPG7TNXz0mDD@mysql-1d36c064-pato-ef11.a.aivencloud.com:25628/stockeartedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# class Store(db.Model):
#     __tablename__ = 'store'
#     id_store = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     store = db.Column(db.String(255), nullable=True)
#     code = db.Column(db.String(255), nullable=True)
#     address = db.Column(db.String(255), nullable=True)
#     city = db.Column(db.String(255), nullable=True)
#     state = db.Column(db.String(255), nullable=True)
#     enabled = db.Column(db.Boolean, default=True)
    
#     def __repr__(self):
#         return f'<Store id={self.id_store} store={self.store} enabled={self.enabled}>'

# Modelo para la tabla 'user'

#class User(db.Model):
  #  __tablename__ = 'user'
    # id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # username = db.Column(db.String(255), nullable=True)
    # name = db.Column(db.String(255), nullable=True)
    # lastname = db.Column(db.String(255), nullable=True)
    # password = db.Column(db.String(255), nullable=True)
    # enabled = db.Column(db.Boolean, default=True)
    # id_rol = db.Column(db.Integer, nullable=True)
    # id_store = db.Column(db.Integer, nullable=True)
    
# class User(db.Model):
#     __tablename__ = 'user'
#     idUser = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(255), nullable=True)
#     name = db.Column(db.String(255), nullable=True)
#     lastname = db.Column(db.String(255), nullable=True)
#     password = db.Column(db.String(255), nullable=True)
#     enabled = db.Column(db.Boolean, default=True)
#         # id_rol = db.Column(db.Integer, nullable=True)
#         # id_store = db.Column(db.Integer, nullable=True)

# Modelo para la tabla 'rol'
class Rol(db.Model):
    __tablename__ = 'rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(255))
    enabled = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Rol id={self.id_rol} rol={self.rol} enabled={self.enabled}>'

def checkSessionAdmin():
    if 'user_id' not in session or session['roleName']!='admin':
        return redirect('/login')
    
@app.route("/nuevohome", methods=['GET'])
def nuevohome():
    checkSessionAdmin();
    return render_template('home.html')
    
@app.route("/login", methods=['POST'])
def login():
    logger.info("/login  %s",request.form['username'])
    
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = UsersServiceStub(channel)
        response = stub.ValidateUser(User(username=request.form['username'],password=request.form['password']))
        user=MessageToJson(response)
    
    logger.info("user : %s",response.username)
   
    if user=="{}":
        flash('Datos incorrectos','danger')
        return redirect('/')
    else:
        session['user_id']=response.idUser
        session['username']=response.username
        session['roleName']=response.role.roleName
        session['name']=response.name
        session['lastname']=response.lastname
        return redirect('/nuevohome')

@app.route("/logout",methods = ['GET'])
def logout():
    logger.info("/logout")
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('name', None)
    session.pop('lastname', None)
    return redirect('/')

@app.route("/", methods=["GET"])
def index():
    return render_template('login.html')

@app.route("/home", methods=["GET"])
def  home():
    return render_template('index.html')

@app.route('/store_list')
def store_list():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = StoreServiceStub(channel)
        response = stub.FindAll(Store()) 
        print(response)
    return render_template('store_list.html', stores=response.store)

@app.route('/stores/add', methods=['GET', 'POST'])
def add_store():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        print(os.getenv("SERVIDOR-GRPC"))
        store_stub = StoreServiceStub(channel)

        if request.method == 'POST':
            store_name = request.form['storeName']
            code = request.form['code']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']

            new_store = Store(
                storeName=store_name,
                code=code,
                address=address,
                city=city,
                state=state,
                enabled=True
            )
            # Llamar al método gRPC para agregar la nueva tienda
            try:
                response = store_stub.SaveStore(new_store)
                print("Tienda agregada: ", response)
                return redirect(url_for('store_list'))
            except grpc.RpcError as e:
                print("Error al agregar la tienda: ", e)

        return render_template('add_store.html')
    
@app.route('/edit/store/<int:idStore>', methods=['GET', 'POST'])
def edit_store(idStore):
    # Conectar con el servidor gRPC
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        store_stub = StoreServiceStub(channel)
        
        # Obtener detalles de la tienda a editar
        response = store_stub.GetStore(Store(idStore=idStore))

        if request.method == 'POST':
            # Recolectar los datos del formulario
            updated_store = Store(
                idStore=idStore,
                storeName=request.form['storeName'],
                code=request.form['code'],
                address=request.form['address'],
                city=request.form['city'],
                state=request.form['state'],
                enabled='enabled' in request.form  # Checkbox para 'enabled'
            )
            # Enviar los datos actualizados mediante gRPC
            store_stub.SaveStore(updated_store)

            # Redirigir a la lista de tiendas después de la actualización
            return redirect(url_for('store_list'))

        # Renderizar el formulario de edición con los datos actuales de la tienda
        return render_template('edit_store.html', store=response)


# Ruta para listar usuarios
@app.route('/users')
def list_users():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = UsersServiceStub(channel)
        response = stub.FindAll(User()) 
    return render_template('list_users.html', users=response.user)

# Ruta para agregar un nuevo usuario
@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        print(os.getenv("SERVIDOR-GRPC"))
        user_stub = UsersServiceStub(channel)

        store_stub = StoreServiceStub(channel)
        stores_response = store_stub.FindAll(Store())
        stores = stores_response.store 
        
        role_stub = RoleServiceStub(channel)
        roles_response = role_stub.FindAll(Role())
        roles = roles_response.role  

        if request.method == 'POST':
            role_id = int(request.form['idRole'])
            store_id = int(request.form['idStore'])
            new_user = User(
                username=request.form['username'],
                name=request.form['name'],
                lastname=request.form['lastname'],
                password=request.form['password'],
                enabled=True,
                role=Role(idRole=role_id), 
                store=Store(idStore=store_id) 
            )

            try:
                response = user_stub.AddUser(new_user)
                print("Usuario agregado: ", response)
                return redirect(url_for('list_users'))
            except grpc.RpcError as e:
                print("Error al agregar el usuario: ", e)

        return render_template('add_user.html', stores=stores, roles=roles)


# Ruta para editar un usuario
@app.route('/users/edit/<int:idUser>', methods=['GET', 'POST'])
def edit_user(idUser):
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        print(os.getenv("SERVIDOR_GRPC"))

        user_stub = UsersServiceStub(channel)
        response = user_stub.GetUser(User(idUser=idUser))

        store_stub = StoreServiceStub(channel)
        stores_response = store_stub.FindAll(Store())
        stores = stores_response.store 
        
        role_stub = RoleServiceStub(channel)
        roles_response = role_stub.FindAll(Role())
        roles = roles_response.role 

        print("respues de roles: ",roles)

        if request.method == 'POST':
            role_id = int(request.form['idRole'])
            store_id = int(request.form['idStore'])

            updated_user = User(
                idUser=idUser,
                username=request.form['username'],
                name=request.form['name'],
                lastname=request.form['lastname'],
                password=request.form['password'],
                enabled='enabled' in request.form,
                role=Role(idRole=role_id), 
                store=Store(idStore=store_id) 
            )
            user_stub.AddUser(updated_user)
            return redirect(url_for('list_users'))

        print("respuesta ", response)
        return render_template('edit_user.html', user=response, stores=stores, roles=roles)


# Modelos de Producto
class Product(db.Model):
    __tablename__ = 'product'
    id_product = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(255))
    code = db.Column(db.String(10))
    img = db.Column(db.String(255))
    enabled = db.Column(db.Boolean, default=True)
    size = db.Column(db.String(255)) 
    color = db.Column(db.String(255))  

    # Relación con stock
    stocks = db.relationship('ProductStock', backref='product', lazy='joined', cascade='all, delete-orphan')

class ProductStock(db.Model):
    __tablename__ = 'product_stock'
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, db.ForeignKey('product.id_product'))
    id_store = db.Column(db.Integer, db.ForeignKey('store.id_store'))
    stock = db.Column(db.Integer)

    # Relaciones
    store = db.relationship('Store', backref='product_stocks')

@app.route('/product', methods=['GET'])
def productos():
    productos = Product.query.all()
    
    # Traer las tiendas asociadas con cada producto
    productos_con_tiendas = []
    for producto in productos:
        # Obtener la primera tienda asociada (si hay)
        stock = ProductStock.query.filter_by(id_product=producto.id_product).first()
        tienda = stock.store.store if stock else "Sin tienda"
        productos_con_tiendas.append({
            'producto': producto,
            'tienda': tienda
        })
    
    return render_template('product.html', productos=productos)



# Función para generar códigos de producto
def generate_product_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Rutas de producto

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('product')
        img = request.form.get('img')
        codigo = generate_product_code()
        color = request.form.get('color')
        size = request.form.get('size')
        tienda_id = request.form.get('tienda')  # Obtener el ID de la tienda seleccionada
        
        # Crear el nuevo producto
        producto = Product(product=nombre, code=codigo, img=img, color=color, size=size)

        try:
            # Agregar el nuevo producto
            db.session.add(producto)
            db.session.commit()  # Necesario para generar el ID del producto

            # Asignar el producto a la tienda seleccionada con stock 0
            producto_stock = ProductStock(
                id_product=producto.id_product,
                id_store=tienda_id,
                stock=0  # Stock inicial 0
            )
            db.session.add(producto_stock)
            db.session.commit()  # Guardar la relación del producto con la tienda

            return redirect(url_for('productos'))
        except Exception as e:
            db.session.rollback() 
            return f"Error al agregar el producto: {str(e)}", 500

    tiendas = Store.query.all()  # Obtener todas las tiendas para el formulario
    return render_template('add_product.html', tiendas=tiendas)


@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    producto = Product.query.get_or_404(id)
    
    if request.method == 'POST':
        producto.product = request.form['product']
        producto.code = request.form['code']
        producto.img = request.form['img']
        producto.color = request.form['color']
        producto.size = request.form['size']
        producto.enabled = 'enabled' in request.form

        # Limpiar stocks existentes
        existing_stocks = ProductStock.query.filter_by(id_product=producto.id_product).all()
        existing_stock_dict = {stock.id_store: stock for stock in existing_stocks}

        tienda_id = request.form.get('tienda')
        stock = request.form.get('stock')

        if tienda_id:
            tienda_id = int(tienda_id)
            stock = int(stock) if stock else 0

            if tienda_id in existing_stock_dict:
                # Actualizar stock existente
                existing_stock = existing_stock_dict[tienda_id]
                existing_stock.stock = stock
            else:
                # Crear nuevo stock
                producto_stock = ProductStock(
                    id_product=producto.id_product,
                    id_store=tienda_id,
                    stock=stock
                )
                db.session.add(producto_stock)

        db.session.commit()
        return redirect(url_for('productos'))

    tiendas = Store.query.all()

    # Obtener el stock actual para el producto
    stock_entry = ProductStock.query.filter_by(id_product=id).first()
    stock = stock_entry.stock if stock_entry else 0
    tienda_id = stock_entry.id_store if stock_entry else None

    return render_template('edit_product.html', producto=producto, tiendas=tiendas, stock=stock, tienda_id=tienda_id)

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)