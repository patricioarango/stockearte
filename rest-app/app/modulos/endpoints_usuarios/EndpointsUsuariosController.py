from . import endpoints_usuarios_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json

from flask import current_app as app
import datetime
from app.models import db, User, Store


@endpoints_usuarios_blueprint.route("/endpoint_usuarios", methods=["GET"])
def endpoint_usuarios():
    resp = jsonify(message="hello world")
    return resp


@endpoints_usuarios_blueprint.route("/get_users", methods=["GET"])
def get_users():
    users = User.query.all()
    print(f'Usuarios encontrados: {len(users)}')  # Debugging
    return jsonify([{
        'id_user': user.id_user,
        'name': user.name,
        'lastname': user.lastname,
        'username': user.username,
        'id_role': user.id_role,
        'id_store': user.id_store,
        'enabled': user.enabled
    } for user in users])

@endpoints_usuarios_blueprint.route("/get_store_by_code/<code>", methods=["GET"])
def get_store_by_code(code):
    app.logger.debug(f'Buscando tienda con código: {code}')  
    store = Store.query.filter_by(code=code).first()
    
    if store:
        app.logger.debug(f'Tienda encontrada: {store}')  
        return jsonify({'id_store': store.id_store, 'enabled': store.enabled}), 200
    else:
        app.logger.warning(f'Tienda no encontrada para el código: {code}')  
        return jsonify({'error': 'Store not found'}), 404



@endpoints_usuarios_blueprint.route("/get_user_by_username/<username>", methods=["GET"])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({
            'id_user': user.id_user,
            'name': user.name,
            'lastname': user.lastname,
            'username': user.username,
            'enabled': user.enabled
        }), 200
    return jsonify({'error': 'User not found'}), 404


@endpoints_usuarios_blueprint.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    username = data.get('username')
    password = data.get('password')
    id_role = data.get('id_role')
    id_store = data.get('id_store')

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Usuario duplicado'}), 400

    store = Store.query.filter_by(id_store=id_store).first()
    if not store:
        return jsonify({'error': 'Código de tienda inválido'}), 400

    if not store.enabled:
        return jsonify({'error': 'Tienda deshabilitada'}), 400
    
    if not all([nombre, apellido, username, password, id_role, id_store]):
        return jsonify({"error": "Faltan datos"}), 400

    new_user = User(
        name=nombre, 
        lastname=apellido, 
        username=username, 
        password=password, 
        id_role=id_role, 
        id_store=id_store,
        enabled=True  
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuario agregado exitosamente"}), 200
    except Exception as e:
        db.session.rollback()  
        app.logger.error(f'Error al agregar usuario: {e}')
        return jsonify({"error": "Error al agregar usuario"}), 500

@endpoints_usuarios_blueprint.route("/get_store_by_idStore/<int:id_store>", methods=["GET"])
def get_store_by_idStore(id_store):
    app.logger.debug(f'Buscando tienda con id_store: {id_store}')  
    store = Store.query.filter_by(id_store=id_store).first()
    
    if store:
        app.logger.debug(f'Tienda encontrada: {store}')  
        return jsonify({'id_store': store.id_store, 'code': store.code, 'enabled': store.enabled}), 200
    else:
        app.logger.warning(f'Tienda no encontrada para id_store: {id_store}')  
        return jsonify({'error': 'Store not found'}), 404
