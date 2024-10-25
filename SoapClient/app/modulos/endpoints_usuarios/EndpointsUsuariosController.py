from . import endpoints_usuarios_blueprint
from flask import jsonify,request
from flask import current_app as app
from zeep import Client
import os,requests

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
            'storeName': usuario.store.store,
            'storeCode': usuario.store.code,
            'id_role': usuario.role.id_role,
            'role': usuario.role.role,
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

@endpoints_usuarios_blueprint.route("/login", methods=["POST"])
def login():
    wsdl = os.getenv("SOAP_WSDL_USUARIOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    if data:
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return {"error": "Username and password are required"}, 400
        
        username = data.get('username')
        password = data.get('password')
        response = client.service.userLogin(username=username, password=password)
        user = {
            'id_user': response.user.id_user,
            'name': response.user.name,
            'lastname': response.user.lastname,
            'username': response.user.username,
            'storeName': response.user.store.store,
            'storeCode': response.user.store.code,
            'id_role': response.user.role.id_role,
            'role': response.user.role.role,
        }
        message = {"status": "success"}
        respuesta = {
            "message": message,
            "user": user
        }
        return jsonify(respuesta)
    return {"error": "No data provided"}, 400
    
@endpoints_usuarios_blueprint.route("/test_login", methods=["GET"])
def test_login():
    url = "http://localhost:5005/login"
    data = {
        "username": "johndoe1234",
        "password": "securepassword"
    }
    response = requests.post(url, json=data)
    print(response.json())
    return response.json()