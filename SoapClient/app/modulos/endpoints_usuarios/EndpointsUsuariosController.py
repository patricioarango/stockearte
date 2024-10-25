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

@endpoints_usuarios_blueprint.route("/login", methods=["POST"])
def login():
    wsdl = os.getenv("SOAP_WSDL_USUARIOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    if data:
        username = data.get('username')
        password = data.get('password')
        
        # Check if username and password are provided
        if not username or not password:
            return {"error": "Username and password are required"}, 400
        
        username = data.get('username')
        password = data.get('password')
        response = client.service.userLogin(username=username, password=password)
        print("response")
        print(response)
        return {response},200
    return {"error": "No data provided"}, 400
    
@endpoints_usuarios_blueprint.route("/test_login", methods=["GET"])
def test_login():
    url = "http://localhost:5005/login"
    data = {
        "username": "johndoe1234",
        "password": "securepassword"
    }
    try:
        response = requests.post(url, json=data)
        print(response)
        
        # Check if the response is successful
        if response.status_code == 200:
            return response.json(), response.status_code
        else:
            return {"error": "Login failed"}, response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error while sending POST request: {e}")
        return {"error": "Request failed"}, 500