from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os, csv, requests
from werkzeug.security import generate_password_hash
from . import usuarios_blueprint

from flask import current_app as app
import datetime
from app.models import db

@usuarios_blueprint.route("/list_user", methods=["GET"])
def list_user():
    users = get_users() 
    return render_template('list_user.html', usuarios=users)


@usuarios_blueprint.route("/usuarios", methods=["GET"])
def usuarios():
    print("Endpoint /usuarios llamado")  
    users = get_users()
    print("Usuarios recibidos:", users)  
    return render_template('list_user.html', usuarios=users)


def get_users():
    url = 'http://localhost:5005/users' 
    response = requests.get(url)
    
    print("Código de estado:", response.status_code) 
    
    if response.status_code == 200:
        print("Respuesta completa:", response.text) 
        users = response.json().get("usuarios", []) 
        app.logger.info(f'Usuarios obtenidos: {users}')  
        return users
    else:
        app.logger.error(f'Error al obtener usuarios: {response.status_code}')
    
    return []


@usuarios_blueprint.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            file_data = file.read().decode("utf-8")
            return process_csv(file_data)
        else:
            flash("Por favor, sube un archivo CSV válido.", "error")
    return render_template('upload_file.html')


def process_csv(file_data):
    csv_reader = csv.reader(file_data.splitlines())
    errores = []
    registros_correctos = []

    for linea_num, row in enumerate(csv_reader, start=1):
        try:
            nombre, apellido, username, password, id_role, code= row
        except ValueError:
            errores.append({'linea': linea_num, 'error': 'Formato incorrecto de la línea', 'data': row})
            continue

        if not nombre or not apellido or not username or not password or not id_role or not code:
            errores.append({'linea': linea_num, 'error': 'Campos vacíos', 'data': row})
            continue

        if check_duplicate_user(username):
            errores.append({'linea': linea_num, 'error': 'Usuario duplicado', 'data': row})
            continue
        
        store = get_store_by_code(code)
        if not store:
            errores.append({'linea': linea_num, 'error': 'Codigo de tienda inválido', 'data': row})
            continue

        if not store['enabled']:
            errores.append({'linea': linea_num, 'error': 'Tienda deshabilitada', 'data': row})
            continue
        
        registros_correctos.append(row)

    for registro in registros_correctos:
        send_to_add_user_endpoint(registro)

    return render_template('upload_file.html', errores=errores, registros_correctos=registros_correctos)


def check_duplicate_user(username):
    url = f'http://localhost:5003/get_user_by_username/{username}'
    response = requests.get(url)
    return response.status_code == 200

def get_store_by_code(code):
    url = f'http://localhost:5003/get_store_by_code/{code}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_store_by_idStore(id_store):
    url = f'http://localhost:5003/get_store_by_idStore/{id_store}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def send_to_add_user_endpoint(registro):
    url = 'http://localhost:5005/users'
    data = {
        'nombre': registro[0],
        'apellido': registro[1],
        'username': registro[2],
        'password': registro[3],
        'id_role': registro[4],
        'id_store': registro[5]
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        try:
            json_response = response.json()
            app.logger.info(f'Usuario agregado: {registro[2]}')
            return json_response
        except requests.exceptions.JSONDecodeError:
            app.logger.error("La respuesta no contiene JSON.")
            return None
    else:
        app.logger.error(f'Error al agregar usuario {registro[2]}: {response.text}')
        return None
