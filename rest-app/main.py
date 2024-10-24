from app import create_app
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import logging
from app.models import Catalog,CatalogProducts,Product
from app.models import db


logger = logging.getLogger(__name__)

app = create_app('flask.cfg')

def checkSessionManager():
    if 'user_id' not in session or session['roleName']!='manager':
        return redirect('/login')
    
def checkSessionAdmin():
    if 'user_id' not in session or session['roleName']!='admin':
        return redirect('/login')
    
def checkSession():
    if 'user_id' not in session:
        return redirect('/login')    

@app.route("/nuevohome", methods=["GET"])
def nuevohome():
    checkSession()
    return render_template('home.html')

import requests

@app.route("/login", methods=['POST'])
def login():
    logger.info("/login  %s", request.form['username'])

    url = 'http://localhost:5003/endpoint_validate_user'
    
    payload = {
        "username": request.form['username'],
        "password": request.form['password']
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        logger.error("Error en la petición REST: %s", e)
        flash('Error al comunicarse con el servidor', 'danger')
        return redirect('/')
    
    user = response.json() 
    
    logger.info("user : %s", user.get('username'))

    if not user or user == {}:
        flash('Datos incorrectos', 'danger')
        return redirect('/')
    else:
        session['user_id'] = user.get('idUser')
        session['username'] = user.get('username')
        session['roleName'] = user.get('role', {}).get('roleName')
        session['name'] = user.get('name')
        session['lastname'] = user.get('lastname')
        session['user_store_id'] = user.get('store', {}).get('idStore')
        session['user_store_name'] = user.get('store', {}).get('storeName')

        print("Contenido de la sesión:", session)

        return redirect('/nuevohome')



@app.route("/logout",methods = ['GET'])
def logout():
    logger.info("/logout")
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('roleName', None)
    session.pop('name', None)
    session.pop('lastname', None)
    session.pop('user_store_id', None)
    return redirect('/')

@app.route("/", methods=["GET"])
def index():
    return render_template('login.html')

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5003, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)