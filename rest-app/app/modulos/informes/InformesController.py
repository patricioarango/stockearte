from . import informes_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db
import requests

from datetime import datetime 

@informes_blueprint.route("/informes", methods=["GET"])
def informes():

    product_code = request.args.get('product_code', '')  
    desde = request.args.get('desde', '') 
    hasta = request.args.get('hasta', '')  
    estado = request.args.get('estado', '')  
    tienda = request.args.get('tienda', '')  

    id_filter = request.args.get('idFilter', '')  

    filtroUsado = {
        'idUserFilter': id_filter,
        'productCode': product_code,
        'state': estado,
        'store': tienda,
        'startDate': desde,
        'endDate': hasta
    }

    print('filtro usado:')
    print(id_filter)

    id_user = 1  

    response = requests.get('http://localhost:5003/endpoint_informes')

    if response.status_code != 200:
        return f"Error al obtener las órdenes de compra: {response.status_code}", 500

    responseFiltro = requests.get(f'http://localhost:5003/endpoint_filtros?id_user={id_user}')
    
    if responseFiltro.status_code != 200:
        return f"Error al obtener los filtros: {responseFiltro.status_code}", 500

    data = response.json()

    purchase_orders = []
    for resp in data:
        purchase_orders.append({
            'cantidadPedida': resp['cantidad_pedida'],
            'createdAt': resp['created_at'],
            'idPurchaseOrder': resp['id_purchase_order'],
            'productCode': resp['product_code'],
            'state': resp['state'],
            'store': {
                'idStore': resp['id_store'],
                'storeName': resp['id_store']  
            }
        })

    filtros = []
    for filtro in responseFiltro.json():
        date_from = filtro['date_from']
        date_to = filtro['date_to']

        filtros.append({
            'idUserFilter': filtro['id_user_filter'],
            'idUser': filtro['id_user'],
            'filter': filtro['filter'],
            'productCode': filtro['cod_prod'] if filtro['cod_prod'] else '', 
            'dateFrom': datetime.strptime(date_from.split(' ')[0], '%Y-%m-%d').strftime('%Y-%m-%d') if date_from else '',  
            'dateTo': datetime.strptime(date_to.split(' ')[0], '%Y-%m-%d').strftime('%Y-%m-%d') if date_to else '',  
            'state': filtro['state'] if filtro['state'] else '',  
            'store': {
                'idStore': filtro['id_store'] if filtro['id_store'] else '',  
                'storeName': filtro['id_store'] if filtro['id_store'] else '' 
            },
            'enabled': filtro['enabled']  
        })

    print(filtros) 

    filtered = []
    try:
        desde_date = datetime.strptime(desde, '%Y-%m-%d') if desde else None
        hasta_date = datetime.strptime(hasta, '%Y-%m-%d') if hasta else None
    except ValueError:
        return render_template('list_purchase_orders.html', purchase_orders=[])

    for order in purchase_orders:
        order_date = datetime.strptime(order['createdAt'], '%Y-%m-%d')

        if product_code and product_code.lower() not in order['productCode'].lower():
            continue
        if estado and estado.lower() not in order['state'].lower():
            continue
        if tienda and str(tienda) != str(order['store']['storeName']):
            continue
        if desde_date and hasta_date:
            if order_date < desde_date or order_date > hasta_date:
                continue
        elif desde_date:
            if order_date != desde_date:
                continue
        elif hasta_date:
            if order_date != hasta_date:
                continue

        filtered.append(order)

    return render_template('list_informes.html', purchase_orders=filtered, filtros=filtros, filtroUsado=filtroUsado)


@informes_blueprint.route('/addInformes', methods=['GET', 'POST']) 
def add_filtro(): 
    product_code = request.args.get('product_code', '') or request.form.get('product_code', '')
    desde = request.args.get('desde', '') or request.form.get('desde', '')
    hasta = request.args.get('hasta', '') or request.form.get('hasta', '')
    estado = request.args.get('estado', '') or request.form.get('estado', '')
    tienda = request.args.get('tienda', '') or request.form.get('tienda', '')

    id_filter = request.args.get('idFilter', '') or request.form.get('idFilter', '')

    print(f'id_filter: {id_filter}')

    filtro = {
        'idFilter': id_filter,
        'name': "",  
        'productCode': product_code,
        'state': estado,
        'store': tienda,
        'startDate': desde,
        'endDate': hasta,
        'enabled': True 
    }

    if id_filter:
        responseFiltro = requests.get(f'http://localhost:5003/endpoint_filtro?id_user_filter={id_filter}')

        if responseFiltro.status_code != 200:
            return f"Error al obtener el filtro: {responseFiltro.status_code}", 500

        dataFiltro = responseFiltro.json()

        filtro['name'] = dataFiltro.get('filter', "")  
        filtro['enabled'] = dataFiltro.get('enabled', False)

    if request.method == 'POST':
        filtro['name'] = request.form['name']
        filtro['productCode'] = request.form['productCode']
        filtro['state'] = request.form['state']
        filtro['store'] = request.form['store']
        filtro['startDate'] = request.form['startDate']
        filtro['endDate'] = request.form['endDate']
        filtro['enabled'] = request.form.get('enabled', 'off') == 'on' 

 
        print(request.form.get('enabled', 'off') == 'on')

        response = guardar_filtro_helper(filtro, id_filter)

        if response and response.status_code in (200, 201):  # 200 para editar, 201 para crear
            flash("Filtro guardado con éxito")
        else:
            flash("Error al guardar el filtro")

        return redirect(url_for('informes.informes'))

    return render_template('add_filtro.html', filtro=filtro)


def guardar_filtro_helper(filtro, id_filter=None):
    data = {
        "id_user": 1,  #TODO: endpoint real
        "filter": filtro['name'],
        "cod_prod": filtro['productCode'],
        "date_from": filtro['startDate'],
        "date_to": filtro['endDate'],
        "state": filtro['state'],
        "id_store": int(filtro['store']) if filtro['store'] else None, 
        "enabled": filtro['enabled']  
    }

    if id_filter:
        data["id_user_filter"] = id_filter

    with app.test_request_context():
        with app.test_client() as client:
            response = client.post("/guardar_filtro", json=data)
            print(f"Respuesta de guardar_filtro: {response.data}")  
            return response


