from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os, csv, requests
from werkzeug.security import generate_password_hash
from . import usuarios_blueprint

from flask import current_app as app
import datetime
from app.models import db


@usuarios_blueprint.route("/usuarios", methods=["GET"])
def usuarios():
    # Obtener la lista de usuarios desde el servicio externo o base de datos
    users = get_users()  # Asume que tienes una función para esto
    return render_template('upload_file.html', usuarios=users)

# Función para obtener todos los usuarios (puedes modificarla según tu implementación)
def get_users():
    url = 'http://localhost:5003/get_all_users'  # Cambia esta URL según tu API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Devuelve la lista de usuarios
    return []


# Ruta para la subida de archivos CSV y procesamiento
@usuarios_blueprint.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Guardar el archivo subido
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            file_data = file.read().decode("utf-8")
            return process_csv(file_data)
        else:
            flash("Por favor, sube un archivo CSV válido.", "error")
    return render_template('upload_file.html')

# Función para procesar el archivo CSV
def process_csv(file_data):
    csv_reader = csv.reader(file_data.splitlines())
    errores = []
    registros_correctos = []

    for linea_num, row in enumerate(csv_reader, start=1):
        try:
            nombre, apellido, username, password, id_role, id_store = row
        except ValueError:
            errores.append({'linea': linea_num, 'error': 'Formato incorrecto de la línea', 'data': row})
            continue

        # Validaciones de campos vacíos
        if not nombre or not apellido or not username or not password or not id_role or not id_store:
            errores.append({'linea': linea_num, 'error': 'Campos vacíos', 'data': row})
            continue

        # Validación de duplicidad de usuario
        if check_duplicate_user(username):
            errores.append({'linea': linea_num, 'error': 'Usuario duplicado', 'data': row})
            continue

        # Validación de tienda
        store = get_store_by_idStore(id_store)
        if not store:
            errores.append({'linea': linea_num, 'error': 'ID de tienda inválido', 'data': row})
            continue

        if not store['enabled']:
            errores.append({'linea': linea_num, 'error': 'Tienda deshabilitada', 'data': row})
            continue

        # Si pasa todas las validaciones
        registros_correctos.append(row)

    # Enviar los registros correctos al endpoint externo
    for registro in registros_correctos:
        send_to_add_user_endpoint(registro)

    # Mostrar los arrays de errores y registros correctos en la vista
    return render_template('upload_file.html', errores=errores, registros_correctos=registros_correctos)

# Función para validar duplicidad de usuarios mediante una llamada al endpoint
def check_duplicate_user(username):
    # Cambiar la URL a la nueva dirección del servicio de usuarios
    url = f'http://localhost:5003/get_user_by_username/{username}'  # Cambia el puerto si es necesario
    response = requests.get(url)
    return response.status_code == 200

# Función para obtener tienda por código
def get_store_by_code(code):
    # Cambiar la URL a la nueva dirección del servicio de tiendas
    url = f'http://localhost:5003/get_store_by_code/{code}'   # Cambia el puerto si es necesario
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_store_by_idStore(id_store):
    # Cambiar la URL a la nueva dirección del servicio de tiendas
    url = f'http://localhost:5003/get_store_by_idStore/{id_store}'  # Cambia el puerto si es necesario
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def send_to_add_user_endpoint(registro):
    # Cambiar la URL a la nueva dirección del servicio de creación de usuarios
    url = 'http://localhost:5003/add_user'  # Cambia el puerto si es necesario
    data = {
        'nombre': registro[0],
        'apellido': registro[1],
        'username': registro[2],
        'password': generate_password_hash(registro[3]),  # Cifrado de contraseña
        'id_role': registro[4],
        'id_store': registro[5]
    }
    response = requests.post(url, json=data)

    # Manejar la respuesta
    if response.status_code == 200:
        app.logger.info(f'Usuario agregado: {registro[2]}')
    else:
        app.logger.error(f'Error al agregar usuario {registro[2]}: {response.text}')
    return response.json()
