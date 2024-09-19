from app import create_app
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import random
import string

app = create_app('flask.cfg')

#creo conexion momentanea con base de datos local
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:110902@localhost:3306/stockearte'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Store(db.Model):
    __tablename__ = 'store'
    id_store = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store = db.Column(db.String(255), nullable=True)
    code = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    state = db.Column(db.String(255), nullable=True)
    enabled = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Store id={self.id_store} store={self.store} enabled={self.enabled}>'

# Modelo para la tabla 'user'
class User(db.Model):
    __tablename__ = 'user'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True)
    lastname = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    enabled = db.Column(db.Boolean, default=True)
    id_rol = db.Column(db.Integer, nullable=True)
    id_store = db.Column(db.Integer, nullable=True)
    
    
# Modelo para la tabla 'rol'
class Rol(db.Model):
    __tablename__ = 'rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(255))
    enabled = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Rol id={self.id_rol} rol={self.rol} enabled={self.enabled}>'

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/home", methods=["GET"])
def  home():
    return render_template('index.html')

@app.route('/store_list')
def store_list():
    stores = Store.query.all()
    return render_template('store_list.html', stores=stores)

# Ruta para agregar una nueva tienda
@app.route('/add', methods=['GET', 'POST'])
def add_store():
    if request.method == 'POST':
        store_name = request.form['store']
        code = request.form['code']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        new_store = Store(store=store_name, code=code, address=address, city=city, state=state)
        db.session.add(new_store)
        db.session.commit()
        return redirect(url_for('store_list'))
    return render_template('add_store.html')

# Ruta para editar una tienda
@app.route('/edit/<int:id_store>', methods=['GET', 'POST'])
def edit_store(id_store):
    store = Store.query.get_or_404(id_store)
    if request.method == 'POST':
        store.store = request.form['store']
        store.code = request.form['code']
        store.address = request.form['address']
        store.city = request.form['city']
        store.state = request.form['state']
        store.enabled = 'enabled' in request.form
        db.session.commit()
        return redirect(url_for('store_list'))
    return render_template('edit_store.html', store=store)

# Ruta para listar usuarios
@app.route('/users')
def list_users():
    users = User.query.all()
    stores = Store.query.all()
    print(stores)
    return render_template('list_users.html', users=users,stores=stores)

# Ruta para agregar un nuevo usuario
@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        lastname = request.form['lastname']
        password = request.form['password']
        id_rol = request.form['id_rol']
        id_store = request.form['id_store']
        new_user = User(username=username,name=name, lastname=lastname, password=password, id_rol=id_rol, id_store=id_store)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_users'))
    
    roles = Rol.query.all()
    stores = Store.query.all()
    return render_template('add_user.html',roles=roles,stores=stores)

# Ruta para editar un usuario
@app.route('/users/edit/<int:id_user>', methods=['GET', 'POST'])
def edit_user(id_user):
    user = User.query.get_or_404(id_user)
    if request.method == 'POST':
        user.username = request.form['username']
        user.name = request.form['name']
        user.lastname = request.form['lastname']
        user.password = request.form['password']
        user.id_rol = request.form['id_rol']
        user.id_store = request.form['id_store']
        user.enabled = 'enabled' in request.form
        db.session.commit()
        return redirect(url_for('list_users'))
    roles = Rol.query.all()
    stores = Store.query.all()
    return render_template('edit_user.html', user=user,roles=roles,stores=stores)

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