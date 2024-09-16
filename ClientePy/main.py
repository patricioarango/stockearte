from app import create_app
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = create_app('flask.cfg')

#creo conexion momentanea con base de datos local
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/stockearte'
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

# Ruta para eliminar una tienda
@app.route('/delete/<int:id_store>')
def delete_store(id_store):
    store = Store.query.get_or_404(id_store)
    db.session.delete(store)
    db.session.commit()
    return redirect(url_for('store_list'))

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)