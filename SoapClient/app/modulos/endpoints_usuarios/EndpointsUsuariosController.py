from . import endpoints_usuarios_blueprint
from flask import jsonify,request
from flask import current_app as app
from zeep import Client
import os

@endpoints_usuarios_blueprint.route("/users", methods=["GET"])
def endpoint_usuarios():
    wsdl = os.getenv("SOAP_WSDL_USUARIOS")
    client = Client(wsdl=wsdl)
    response = client.service.getAllUsers()
    usuarios = []
    for usuario in response:
        usuarios.append({
            'id_user': usuario.id_user,
            'name': usuario.name,
            'lastname': usuario.lastname,
            'username': usuario.username,
            'storeName': "falta StoreName", #TO-DO
            'storeCode': "falta storeCode", #TO-DO
        })
   
    resp = jsonify(usuarios=usuarios)
    return resp

@endpoints_usuarios_blueprint.route("/users", methods=["POST"])
def add_user():
    wsdl = os.getenv("SOAP_WSDL_USUARIOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    if data:
        new_user_data = {
        'name': data['nombre'],
        'lastname': data['apellido'],
        'username': data['username'],
        'password': data['password'],
        'storeCode': 'tienda1' #TO-DO
        }
    
    response = client.service.addUser(user=new_user_data)
    return response