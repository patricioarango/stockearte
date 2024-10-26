from . import catalogos_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json
from app.models import Catalog,CatalogProducts,Product,ProductStock
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
    id_store = session.get('user_store_id')
    print("ID de tienda obtenido de la sesión:", id_store)

    if not id_store:
        print("Error: No se encontró el ID de la tienda en la sesión.")
        return render_template('catalog_list.html', catalogs=[])  

    url = f'http://localhost:5005/stores/{id_store}/catalogs'
    response = requests.get(url)
    print("a ver que trae el intermedio:", response.json())

    if response.status_code == 200:
        catalogs = response.json().get("catalogs", [])
        return render_template('catalog_list.html', catalogs=catalogs)
    else:
        print(f'Error al obtener catálogos: {response.status_code}')
        return render_template('catalog_list.html', catalogs=[])  

# Agregar un nuevo catálogo
@catalogos_blueprint.route('/catalogs/new', methods=['GET', 'POST'])
def add_catalog():
    if request.method == 'POST':
        catalog_name = request.form['catalog']
        id_store = session.get('user_store_id')
        print("contenido de la session:", session)

        if not id_store:
            print("Error: No se encontró el ID de la tienda en la sesión.")
            return redirect(url_for('catalogos.add_catalog'))
        
        url = f'http://localhost:5005/stores/{id_store}/catalogs'
        response = requests.post(url, json={
            'catalog': catalog_name,
            'id_store': id_store,
            'enabled': True  
        })

        if response.status_code == 200:
            return redirect(url_for('catalogos.get_catalogs'))
        else:
            print(f'Error al agregar catálogo: {response.status_code} - {response.text}')
            return redirect(url_for('catalogos.add_catalog'))

    return render_template('add_catalog.html')


# Editar un catálogo
@catalogos_blueprint.route('/catalogs/edit/<int:id>', methods=['GET', 'POST'])
def edit_catalog(id):
    url = f'http://localhost:5003/get_catalogs'  
    response = requests.get(url)

    if response.status_code == 200:
        catalogs = response.json()
        catalog = next((cat for cat in catalogs if cat['id_catalog'] == id), None)

        if request.method == 'POST':
            catalog_name = request.form['catalog']
            id_store = session.get('user_store_id')

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
        catalog = Catalog.query.get(id_catalog)
        id_store = catalog.id_store if catalog else None
        
        url = f'http://localhost:5005/stores/{id_store}/catalogs/{id_catalog}/products/{id_product}'
        response = requests.put(url, json={'id_product': id_product})

        if response.status_code == 201:
            return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))
        else:
            print(f'Error al agregar producto: {response.status_code}, {response.text}')  
            return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))

    catalog = Catalog.query.get(id_catalog)
    products = []

    if catalog:
        id_store = catalog.id_store  
        url = f'http://localhost:5003/stores/{id_store}/products'
    
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        if isinstance(json_response, list):
            products = json_response 
        else:
            products = json_response.get('productos', []) 
    else:
        print(f'Error al obtener productos de la tienda: {response.status_code}, {response.text}')
        products = []  

    catalog_products = CatalogProducts.query.filter_by(id_catalog=id_catalog).all()
    catalog_product_details = []

    for catalog_product in catalog_products:
        product = Product.query.get(catalog_product.id_product)  
        if product:
            catalog_product_details.append({
                'catalog_product': catalog_product,
                'product_name': product.product  
            })

    print("Detalles de los productos del catálogo:", catalog_product_details)

    return render_template('add_product_to_catalog.html', 
                           id_catalog=id_catalog, 
                           products=products, 
                           catalog_product_details=catalog_product_details)



@catalogos_blueprint.route('/catalogs/<int:id_catalog>/remove_product', methods=['POST'])
def remove_product_from_catalog_view(id_catalog):
    data = request.form  
    id_product = data.get('id_product')

    catalog = Catalog.query.get(id_catalog)
    id_store = catalog.id_store if catalog else None

    url = f'http://localhost:5005/stores/{id_store}/catalogs/{id_catalog}/products/{id_product}'

    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url, headers=headers, json={})

    if response.status_code == 200:
        return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))
    else:
        print(f'Error al eliminar producto: {response.status_code}, {response.text}') 
        return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))







