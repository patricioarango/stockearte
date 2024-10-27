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
    print("respuesta ",response.json())

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


@catalogos_blueprint.route('/catalogs/edit/<int:id>', methods=['GET', 'POST'])
def edit_catalog(id):
    id_store = session.get('user_store_id')
    print("ID de tienda obtenido de la sesión:", id_store)

    if id_store is None:
        print("Error: no se encontró el id_store en la sesión.")
        return redirect(url_for('catalogos.get_catalogs'))

    url = f'http://localhost:5005/stores/{id_store}/catalogs'
    response = requests.get(url)

    if response.status_code == 200:
        catalogs = response.json().get("catalogs", [])
        catalog = next((cat for cat in catalogs if cat['id_catalog'] == id), None)

        if catalog is None:
            print(f"Error: catálogo con id {id} no encontrado.")
            return redirect(url_for('catalogos.get_catalogs'))

        if request.method == 'POST':
            catalog_name = request.form['catalog']
            update_url = f'http://localhost:5005/stores/{id_store}/catalogs/{id}'
            response = requests.put(update_url, json={
                'catalog': catalog_name,
                'id_catalog': id,
                'id_store': id_store,
                'enabled': True  
            })

            if response.status_code == 200:
                return redirect(url_for('catalogos.get_catalogs'))
            else:
                print(f'Error al editar catálogo: {response.status_code} - {response.text}')
                return redirect(url_for('catalogos.edit_catalog', id=id))

        return render_template('edit_catalog.html', catalog=catalog)

    else:
        print(f'Error al obtener catálogos: {response.status_code}')
        return redirect(url_for('catalogos.get_catalogs'))


@catalogos_blueprint.route('/catalogs/delete/<int:id>', methods=['POST'])
def delete_catalog(id):
    id_store = session.get('user_store_id')
    print("ID de tienda obtenido de la sesión:", id_store)

    if id_store is None:
        print("Error: no se encontró el id_store en la sesión.")
        return redirect(url_for('catalogos.get_catalogs'))

    url = f'http://localhost:5005/stores/{id_store}/catalogs'
    response = requests.get(url)

    if response.status_code == 200:
        catalogs = response.json().get("catalogs", [])
        catalog = next((cat for cat in catalogs if cat['id_catalog'] == id), None)

        if catalog is None:
            print(f"Error: catálogo con id {id} no encontrado.")
            return redirect(url_for('catalogos.get_catalogs'))

        print("Contenido del catálogo:", catalog)

        catalog_name = catalog['name'] 

        update_url = f'http://localhost:5005/stores/{id_store}/catalogs/{id}'
        response = requests.put(update_url, json={
            'catalog': catalog_name,  
            'enabled': False  
        })

        if response.status_code == 200:
            return redirect(url_for('catalogos.get_catalogs'))
        else:
            print(f'Error al cambiar el estado del catálogo: {response.status_code} - {response.text}')
            return redirect(url_for('catalogos.get_catalogs'))
    else:
        print(f'Error al obtener catálogos: {response.status_code}')
        return redirect(url_for('catalogos.get_catalogs'))

@catalogos_blueprint.route('/catalogs/<int:id_catalog>/new_product', methods=['GET', 'POST'])
def add_product_to_catalog(id_catalog):
    id_store = session.get('user_store_id')
    if request.method == 'POST':
        id_product = request.form['id_product']
        
        if not id_store:
            flash('No se pudo obtener el ID de la tienda.', 'danger')
            return redirect(url_for('catalogos.some_route'))

        url = f'http://localhost:5005/stores/{id_store}/catalogs/{id_catalog}/products/{id_product}'
        response = requests.put(url, json={'id_product': id_product})

        if response.status_code == 200:
            print(f'Producto agregado correctamente al catálogo: {id_product}')
            return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))
        else:
            print(f'Error al agregar producto: {response.status_code}, {response.text}')  
            flash('Error al agregar producto al catálogo.', 'danger')

    products_url = f'http://localhost:5005/stores/{id_store}/products'
    products_response = requests.get(products_url)

    if products_response.status_code == 200:
        all_products = products_response.json().get('productos', [])  
    else:
        print(f'Error al obtener productos de la tienda: {products_response.status_code}, {products_response.text}')
        all_products = []  

    catalog_products_url = f'http://localhost:5005/stores/{id_store}/catalogs/{id_catalog}/products'
    catalog_products_response = requests.get(catalog_products_url)

    if catalog_products_response.status_code == 200:
        catalog_products = catalog_products_response.json().get('catalogoProductos', {}).get('productos', [])
    else:
        print(f'Error al obtener productos del catálogo: {catalog_products_response.status_code}, {catalog_products_response.text}')
        catalog_products = []  

    print("Productos obtenidos del catálogo:", catalog_products)

    return render_template('add_product_to_catalog.html', 
                           id_catalog=id_catalog, 
                           products=all_products,         
                           catalog_products=catalog_products)  



@catalogos_blueprint.route('/catalogs/<int:id_catalog>/remove_product', methods=['POST'])
def remove_product_from_catalog_view(id_catalog):
    data = request.form  
    id_product = data.get('id_product')
    id_store = session.get('user_store_id')
    url = f'http://localhost:5005/stores/{id_store}/catalogs/{id_catalog}/products/{id_product}'

    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url, headers=headers, json={})

    if response.status_code == 200:
        return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))
    else:
        print(f'Error al eliminar producto: {response.status_code}, {response.text}') 
        return redirect(url_for('catalogos.add_product_to_catalog', id_catalog=id_catalog))







