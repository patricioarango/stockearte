from . import catalogos_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json
from app.models import Catalog,CatalogProducts,Product
from flask import current_app as app
import datetime
from app.models import db
import requests

@catalogos_blueprint.route("/catalogos", methods=["GET"])
def catalogos():
    resp = jsonify(message="hello catalogos world")
    return resp

@catalogos_blueprint.route('/catalogs', methods=['GET'])
def get_catalogs():
    # URL del endpoint de la API que devuelve los catálogos
    url = 'http://localhost:5003/get_catalogs'
    response = requests.get(url)

    if response.status_code == 200:
        catalogs = response.json()  # Obtener la lista de catálogos en formato JSON
        # Renderizar el template HTML pasando la lista de catálogos
        return render_template('catalog_list.html', catalogs=catalogs)
    else:
        print(f'Error al obtener catálogos: {response.status_code}')
        return render_template('catalog_list.html', catalogs=[])  # En caso de error, pasa una lista vacía

 # Agregar un nuevo catálogo
@catalogos_blueprint.route('/catalogs/new', methods=['GET', 'POST'])
def add_catalog():
    if request.method == 'POST':
        catalog_name = request.form['catalog']
        id_store = 1#request.form['id_store']

        # Enviar solicitud POST al endpoint de la API
        url = 'http://localhost:5003/add_catalog'
        response = requests.post(url, json={'catalog': catalog_name, 'id_store': id_store})

        if response.status_code == 201:
            return redirect(url_for('catalogos.get_catalogs'))
        else:
            print(f'Error al agregar catálogo: {response.status_code}')
            return redirect(url_for('catalogos.add_catalog'))

    return render_template('add_catalog.html')

# Editar un catálogo
@catalogos_blueprint.route('/catalogs/edit/<int:id>', methods=['GET', 'POST'])
def edit_catalog(id):
    # Obtener catálogo actual
    url = f'http://localhost:5003/get_catalogs'  # Endpoint para obtener los catálogos
    response = requests.get(url)

    if response.status_code == 200:
        catalogs = response.json()
        catalog = next((cat for cat in catalogs if cat['id_catalog'] == id), None)

        if request.method == 'POST':
            catalog_name = request.form['catalog']
            id_store = 1#request.form['id_store']

            # Enviar solicitud PUT al endpoint de la API
            url = f'http://localhost:5003/edit_catalog/{id}'
            response = requests.put(url, json={'catalog': catalog_name, 'id_store': id_store})

            if response.status_code == 200:
                return redirect(url_for('catalogos.get_catalogs'))
            else:
                print(f'Error al editar catálogo: {response.status_code}')
                return redirect(url_for('catalogos.edit_catalog', id=id))

        return render_template('edit_catalog.html', catalog=catalog)
    else:
        print(f'Error al obtener catálogo: {response.status_code}')
        return redirect(url_for('catalogos.get_catalogs'))

# Eliminar un catálogo
@catalogos_blueprint.route('/catalogs/delete/<int:id>', methods=['POST'])
def delete_catalog(id):
    # Enviar solicitud DELETE al endpoint de la API
    url = f'http://localhost:5003/delete_catalog/{id}'
    response = requests.delete(url)

    if response.status_code == 200:
        return redirect(url_for('catalogos.get_catalogs'))
    else:
        print(f'Error al eliminar catálogo: {response.status_code}')
        return redirect(url_for('catalogos.get_catalogs'))   
    
@catalogos_blueprint.route('/catalogs/<int:id_catalog>/new_product', methods=['GET', 'POST'])
def add_product_to_catalog(id_catalog): 
    if request.method == 'POST':
        id_product = request.form['id_product']
        url = f'http://localhost:5003/catalogs/{id_catalog}/add_product'
        response = requests.post(url, json={'id_product': id_product})

        if response.status_code == 201:
            # En vez de redirigir, recargar los productos asociados
            return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))
        else:
            print(f'Error al agregar producto: {response.status_code}, {response.text}')  # Agrega más detalles sobre el error
            return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))

    # Obtener todos los productos disponibles
    products = Product.query.all()  

    # Obtener los productos asociados al catálogo
    catalog_products = CatalogProducts.query.filter_by(id_catalog=id_catalog).all()

    # Unir información del producto a partir de catalog_products
    catalog_product_details = []
    for catalog_product in catalog_products:
        product = Product.query.get(catalog_product.id_product)  # Obtener el producto por id
        if product:
            catalog_product_details.append({
                'catalog_product': catalog_product,
                'product_name': product.product  # Suponiendo que `product` es el nombre del producto
            })

    return render_template('add_product_to_catalog.html', id_catalog=id_catalog, products=products, catalog_product_details=catalog_product_details)



