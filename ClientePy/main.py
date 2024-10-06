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

from product_pb2 import Product
from product_pb2 import Product, ProductCodeRequest

from product_pb2_grpc import ProductServiceStub  

from productStock_pb2 import ProductStock, ProductsStock, ProductAndStoreRequest

from productStock_pb2_grpc import ProductStockServiceStub

from purchaseOrder_pb2 import PurchaseOrder,PurchaseAndStoreRequest

from purchaseOrder_pb2_grpc import PurchaseOrderServiceStub

from orderItem_pb2 import OrderItem

from orderItem_pb2_grpc import OrderItemServiceStub

import logging

from google.protobuf.json_format import MessageToJson

from datetime import datetime

logger = logging.getLogger(__name__)

app = create_app('flask.cfg')

#creo conexion momentanea con base de datos local
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/stockearte'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/stockearte'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://avnadmin:AVNS_ylqtAU8JPG7TNXz0mDD@mysql-1d36c064-pato-ef11.a.aivencloud.com:25628/stockeartedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Rol(db.Model):
    __tablename__ = 'rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(255))
    enabled = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Rol id={self.id_rol} rol={self.rol} enabled={self.enabled}>'
    
def checkSessionManager():
    if 'user_id' not in session or session['roleName']!='manager':
        return redirect('/login')
    
def checkSessionAdmin():
    if 'user_id' not in session or session['roleName']!='admin':
        return redirect('/login')
    
def checkSession():
    if 'user_id' not in session:
        return redirect('/login')    
    
@app.route("/nuevohome", methods=['GET'])
def nuevohome():
    checkSession()
    return render_template('home.html')
    
@app.route("/login", methods=['POST'])
def login():
    logger.info("/login  %s", request.form['username'])
    
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = UsersServiceStub(channel)
        response = stub.ValidateUser(User(username=request.form['username'], password=request.form['password']))
        user = MessageToJson(response)
    
    logger.info("user : %s", response.username)
   
    if user == "{}":
        flash('Datos incorrectos', 'danger')
        return redirect('/')
    else:
        session['user_id'] = response.idUser
        session['username'] = response.username
        session['roleName'] = response.role.roleName
        session['name'] = response.name
        session['lastname'] = response.lastname
        session['user_store_id'] = response.store.idStore  
        session['user_store_name'] = response.store.storeName

        print("Contenido de la sesión:", session)

        return redirect('/nuevohome')


@app.route("/logout",methods = ['GET'])
def logout():
    logger.info("/logout")
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('roleName', None)
    session.pop('name', None)
    session.pop('lastname', None)
    session.pop('user_store_id', None)
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
    return render_template('store_list.html', stores=response.store)

@app.route('/stores/add', methods=['GET', 'POST'])
def add_store():
    
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        print(os.getenv("SERVIDOR-GRPC"))
        store_stub = StoreServiceStub(channel)
        code_error = ""
        store_name = ""
        address = ""
        city = ""
        state = ""
        if request.method == 'POST':
            store_name = request.form['storeName']
            code = request.form['code']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            # si el codigo existe, igual guardo la tienda pero sin codigo 
            # y lo redirigo al edit tienda
            new_store = Store(
                storeName=store_name,
                code=code,
                address=address,
                city=city,
                state=state,
                enabled=True
            )
            try:
                codeExists = store_stub.FindStoreByCode(Store(code=code))
                if codeExists.idStore > 0:
                    new_store.code = ""
                    code_error = "El código ingresado ya existía. Por favor, ingrese un nuevo código"
                else: 
                    response = store_stub.SaveStore(new_store)
                    return redirect(url_for('store_list'))
            except grpc.RpcError as e:
                print("Error al agregar la tienda: ", e)

        return render_template('add_store.html',store_name=store_name,address=address,city=city,state=state,code_error=code_error)
    
@app.route('/edit/store/<int:idStore>', methods=['GET', 'POST'])
def edit_store(idStore):
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        store_stub = StoreServiceStub(channel)
        storegrpc = store_stub.GetStore(Store(idStore=idStore))
        
        if request.method == 'POST':
            print("request.form")
            print(request.form)
            storegrpc.storeName = request.form['storeName']
            storegrpc.code = request.form['code']
            storegrpc.address = request.form['address']
            storegrpc.city = request.form['city']
            storegrpc.state = request.form['state']
            storegrpc.enabled = 'enabled' in request.form
            try:
                store_stub.SaveStore(storegrpc)  
                return redirect(url_for('store_list'))
            
            except grpc.RpcError as e:
                return f"Error al actualizar la tienda: {str(e)}", 500

        return render_template('edit_store.html', store=storegrpc)


# Ruta para listar usuarios
@app.route('/users')
def list_users():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = UsersServiceStub(channel)
        response = stub.FindAll(User()) 
        store_stub = StoreServiceStub(channel)
        stores_response = store_stub.FindAll(Store())
    return render_template('list_users.html', users=response.user,tiendas=stores_response.store)

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
    

@app.route('/product')
def product():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        product_stub = ProductServiceStub(channel)
        response = product_stub.FindAll(Product())  
        print("productos test: ",response)
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

@app.route('/add_product_to_store/<int:idStore>', methods=['GET', 'POST'])
def add_product_to_store(idStore):
    product_list = []
    productosdelatienda = []
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = ProductServiceStub(channel)
        productuStockstub = ProductStockServiceStub(channel)
        try:
            response = stub.FindAll(Empty())
            product_list = response.product
            product_stocks = get_products_by_store(idStore)

        except grpc.RpcError as e:
            print("Error al obtener productos: ", e)
            return f"Error al obtener productos: {str(e)}", 500

    if request.method == 'POST':
        selected_product_id = request.form["id_product"];

        with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
            stub = ProductStockServiceStub(channel)
            product_stock_request = ProductStock(
                    product=Product(idProduct=int(selected_product_id)),
                    store=Store(idStore=idStore),
                    stock=0)
            try:
                stub.SaveProductStock(product_stock_request)
                return redirect("/add_product_to_store/" + str(idStore))
            except grpc.RpcError as e:
                print(f"Error al guardar el stock del producto {selected_product_id}: ", e)
                return f"Error al guardar el stock del producto: {str(e)}", 500
            
    return render_template('add_product_to_store.html', idStore=idStore, products=product_list,productosdelatienda=product_stocks)


@app.route('/my_products')
def store_products():
    checkSessionManager()
    user_store_id = session.get('user_id')
    print("User Store ID de mis productos: ", user_store_id)
    productos_tienda = get_products_by_store(user_store_id)
    return render_template('my_products.html', productos=productos_tienda,idStore=user_store_id)

def get_products_by_store(store_id):
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        product_stock_stub = ProductStockServiceStub(channel)
        store_request = ProductAndStoreRequest(idStore=store_id)
        try:
            response = product_stock_stub.FindAllByStore(store_request)  
            products = []
            print(response)
            for product_stock in response.productStock:
                product = product_stock.product
                products.append({
                    'idProduct': product.idProduct,
                    'productName': product.product,
                    'code': product.code,
                    'size': product.size,
                    'color': product.color,
                    'stock': product_stock.stock
                })
            return products
        except grpc.RpcError as e:
            print(f"Error al obtener productos de la tienda: {str(e)}")
            return []

@app.route('/edit_stock/<int:id>', methods=['GET', 'POST'])
def edit_stock(id):
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        stub = ProductStockServiceStub(channel)

        stock_response = stub.GetProductStock(ProductAndStoreRequest(idProduct=id))
        
        if request.method == 'POST':
            nuevo_stock = int(request.form['stock'])
            stock_response.stock = nuevo_stock
            
            try:
                stub.SaveProductStock(stock_response)
                return redirect(url_for('store_products'))
            except grpc.RpcError as e:
                return f"Error al actualizar el stock: {str(e)}", 500
        
        return render_template('edit_stock.html', producto=stock_response)

@app.route('/purchase_orders')
def list_purchase_orders():
    checkSessionManager()
    user_store_id = session.get('user_store_id')
    
    try:
        # Abrir el canal gRPC
        with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
            # Crear el stub para el servicio de órdenes de compra
            purchaseorder_stub = PurchaseOrderServiceStub(channel)
            
            # Crear la solicitud para buscar órdenes por tienda
            store_request = PurchaseAndStoreRequest(idStore=user_store_id)
            
            # Hacer la llamada gRPC al servidor para obtener las órdenes de compra
            response = purchaseorder_stub.FindAllByStore(store_request)
            
            # Procesar la respuesta
            purchase_orders = []
            for purchase_order in response.purchaseOrderWithItem:
                items = []
                
                # Procesar cada ítem dentro de la orden de compra
                for item in purchase_order.items:
                    items.append({
                        'idOrderItem': item.idOrderItem,
                        'productCode': item.productCode,
                        'color': item.color,
                        'size': item.size,
                        'requestedAmount': item.requestedAmount
                    })
                
                # Agregar la orden de compra con sus ítems a la lista
                purchase_orders.append({
                    'idPurchaseOrder': purchase_order.idPurchaseOrder,
                    'observation': purchase_order.observation,
                    'state': purchase_order.state,
                    'createdAt': purchase_order.createdAt,
                    'purchaseOrderDate': purchase_order.purchaseOrderDate,
                    'receptionDate': purchase_order.receptionDate,
                    'store': {
                        'idStore': purchase_order.store.idStore,
                        'storeName': purchase_order.store.storeName
                    },
                    'items': items
                })
            
            # Renderizar la página de órdenes de compra con los datos obtenidos
            return render_template('list_purchase_orders.html', purchase_orders=purchase_orders, idStore=user_store_id)
    
    except grpc.RpcError as e:
        print(f"Error al obtener órdenes de compra: {e.code()}, {e.details()}")
        return "Error al obtener órdenes de compra", 500

@app.route('/new_purchase_order', methods=['GET', 'POST'])
def new_purchase_order():
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        purchaseorder_stub = PurchaseOrderServiceStub(channel)
        user_store_id = session.get('user_store_id')
        store_name = session.get('user_store_name')
        
        # Crear la tienda asociada
        store = Store(
            idStore=user_store_id,
            storeName=store_name
        )
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        # Crear la nueva orden de compra
        new_order = PurchaseOrder(
            observation=" ",  # Observación vacía
            state="SOLICITADA",  # Estado inicial
            createdAt=current_date,  # Fecha de creación
            purchaseOrderDate=" ",  # Fecha de la orden de compra
            receptionDate=" ",  
            store=store  # Tienda asociada
        )     
        try:
            # Enviar la orden de compra al servidor gRPC
            response = purchaseorder_stub.AddPurchaseOrder(new_order)
            # Redirigir a la pantalla de ítems con el ID de la nueva orden
            new_order_id = response.idPurchaseOrder  # Asegúrate de que el servidor gRPC devuelva el ID
            return redirect(url_for('view_order_items', id=new_order_id))
        
        except grpc.RpcError as e:
            print(f"Error al agregar la orden de compra: {e}")
            return render_template('error.html', error_message="Hubo un error al intentar agregar la orden de compra.")


@app.route('/view_order_items/<int:id>', methods=['GET', 'POST'])
def view_order_items(id):
    checkSessionManager()
    user_store_id = session.get('user_id')
    productos_tienda = get_products_by_store(user_store_id)
    # Conexión al canal gRPC
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        purchase_order_stub = PurchaseOrderServiceStub(channel)
        order_item_stub = OrderItemServiceStub(channel)
        
        # Obtener la orden de compra usando el stub
        try:
            order = purchase_order_stub.GetPurchaseOrder(PurchaseOrder(idPurchaseOrder=id))
        except grpc.RpcError as e:
            print(f"Error al obtener la orden de compra: {e}")
            return render_template('error.html', error_message="No se pudo obtener la orden de compra.")

        # Inicializa una lista para los items
        order_items = order.items  # Accede directamente a los ítems desde la orden

        # Si el método es POST, significa que estamos agregando un nuevo item
        if request.method == 'POST':
            idProduct = int(request.form['idProduct'])
            requested_amount = int(request.form['requested_amount'])

            # Open gRPC channel inside the POST request handling block
            with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
                stub = ProductServiceStub(channel)
                response = stub.GetProduct(Product(idProduct=idProduct))
                print("PRODUCTO: ", response.product)

                purchaseOrder = PurchaseOrder(
                    idPurchaseOrder=id,
                    )
                

                new_item = OrderItem(
                    purchaseOrder=purchaseOrder,
                    productCode=response.code,  
                    color=response.color,               
                    size=response.size,                 
                    requestedAmount=requested_amount
                )

                try:
                    order_item_stub.SaveOrderItem(new_item)  # Llamada gRPC para agregar el nuevo item
                except grpc.RpcError as e:
                    print(f"Error al agregar el ítem: {e}")
                    return render_template('error.html', error_message="No se pudo agregar el ítem.")

                # Redirigimos para evitar doble envío de formularios al refrescar
                return redirect(url_for('view_order_items', id=id))
    print("productos: ", productos_tienda)
    return render_template('view_order_items.html', order=order, order_items=order_items, productos_tienda=productos_tienda)

@app.route('/view_order_items_list/<int:id>', methods=['GET'])
def view_order_items_list(id):
    checkSessionManager()
    user_store_id = session.get('user_id')
    
    # Conexión al canal gRPC
    with grpc.insecure_channel(os.getenv("SERVIDOR-GRPC")) as channel:
        purchase_order_stub = PurchaseOrderServiceStub(channel)
        
        # Obtener la orden de compra usando el stub
        try:
            order = purchase_order_stub.GetPurchaseOrder(PurchaseOrder(idPurchaseOrder=id))
        except grpc.RpcError as e:
            print(f"Error al obtener la orden de compra: {e}")
            return render_template('error.html', error_message="No se pudo obtener la orden de compra.")

        # Inicializa una lista para los items
        order_items = order.items  # Accede directamente a los ítems desde la orden

    return render_template('view_order_items_list.html', order=order, order_items=order_items)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)