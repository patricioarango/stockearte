from . import endpoints_catalogos_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db,Catalog,CatalogProducts,Product,ProductStock

@endpoints_catalogos_blueprint.route("/endpoint_catalogos", methods=["GET"])
def endpoint_catalogos():
    resp = jsonify(message="hello world")
    return resp

@endpoints_catalogos_blueprint.route('/get_catalogs', methods=['GET'])
def get_catalogs():
    id_store = request.args.get('id_store')
    if id_store:
        catalogs = Catalog.query.filter_by(id_store=id_store).all()
    else:
        catalogs = Catalog.query.all() 

    print(f'Catálogos encontrados para id_store {id_store}: {len(catalogs)}') 

    return jsonify([{
        'id_catalog': catalog.id_catalog,
        'catalog': catalog.catalog,
        'id_store': catalog.id_store
    } for catalog in catalogs])
    
# Endpoint para agregar un nuevo catálogo
@endpoints_catalogos_blueprint.route('/add_catalog', methods=['POST'])
def add_catalog():
    data = request.json
    catalog_name = data.get('catalog')
    id_store = data.get('id_store')
    
    new_catalog = Catalog(catalog=catalog_name, id_store=id_store)
    db.session.add(new_catalog)
    db.session.commit()

    return jsonify({'message': 'Catálogo agregado exitosamente'}), 201

# Endpoint para editar un catálogo existente
@endpoints_catalogos_blueprint.route('/edit_catalog/<int:id>', methods=['PUT'])
def edit_catalog(id):
    catalog = Catalog.query.get_or_404(id)
    data = request.json
    catalog.catalog = data.get('catalog')
    #catalog.id_store = data.get('id_store')

    db.session.commit()
    return jsonify({'message': 'Catálogo editado exitosamente'})

@endpoints_catalogos_blueprint.route('/catalogs/<int:id_catalog>/add_product', methods=['POST'])
def add_product(id_catalog):  
    data = request.json
    id_product = data.get('id_product')

    existing_entry = CatalogProducts.query.filter_by(id_catalog=id_catalog, id_product=id_product).first()
    if existing_entry:
        return jsonify({'message': 'El producto ya está en el catálogo.'}), 400
    
    catalog_product = CatalogProducts(id_catalog=id_catalog, id_product=id_product)
    db.session.add(catalog_product)
    db.session.commit()

    return jsonify({'message': 'Producto agregado al catálogo exitosamente'}), 201


# Endpoint para obtener todos los productos
@endpoints_catalogos_blueprint.route('/get_products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id_product': product.id_product, 'product_name': product.product_name} for product in products])

@endpoints_catalogos_blueprint.route('/stores/<int:id_store>/products', methods=['GET'])
def get_productos_por_tienda(id_store):
    product_stocks = ProductStock.query.filter_by(id_store=id_store).all()

    products = []
    for stock in product_stocks:
        product = Product.query.get(stock.id_product)  
        if product:
            products.append({
                'idProduct': product.id_product,
                'productName': product.product,
                'code': product.code,
                'color': product.color,
                'size': product.size,
                'img': product.img,
                'stock': stock.stock  
            })

    if not products:
        return jsonify({'message': 'No hay productos disponibles en esta tienda.'}), 404

    return jsonify(products), 200

# Endpoint para eliminar un producto del catálogo
@endpoints_catalogos_blueprint.route('/catalogs/<int:id_catalog>/remove_product', methods=['DELETE'])
def remove_product_from_catalog(id_catalog):
    data = request.json  
    id_product = data.get('id_product')
    
    catalog_product = CatalogProducts.query.filter_by(id_catalog=id_catalog, id_product=id_product).first()
    if not catalog_product:
        return jsonify({'message': 'El producto no está en el catálogo.'}), 404
    
    db.session.delete(catalog_product)
    db.session.commit()

    return jsonify({'message': 'Producto eliminado del catálogo exitosamente'}), 200



