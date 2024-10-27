from . import endpoints_usuarios_blueprint
from flask import jsonify,request
from flask import current_app as app
from zeep import Client
import os,requests

@endpoints_usuarios_blueprint.route("/users", methods=["GET"])
def endpoint_usuarios():
    """
    Obtiene todos los usuarios.
    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Lista de usuarios obtenida exitosamente
        content:
          application/json:
            schema:
              type: object
              properties:
                usuarios:
                  type: array
                  items:
                    type: object
                    properties:
                      id_user:
                        type: integer
                        description: ID del usuario
                      name:
                        type: string
                        description: Nombre del usuario
                      lastname:
                        type: string
                        description: Apellido del usuario
                      username:
                        type: string
                        description: Nombre de usuario
                      storeName:
                        type: string
                        description: Nombre de la tienda
                      storeCode:
                        type: string
                        description: Código de la tienda
                      id_role:
                        type: integer
                        description: ID del rol del usuario
                      role:
                        type: string
                        description: Nombre del rol del usuario
      500:
        description: Error interno al obtener los usuarios
    """
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
    user = None
    if data:
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return {"error": "Username and password are required"}, 400
        
        username = data.get('username')
        password = data.get('password')
        response = client.service.userLogin(username=username, password=password)
        message = {"status": "username or password incorrect"}
        if(response.user):
            user = {
                'id_user': response.user.id_user,
                'name': response.user.name,
                'lastname': response.user.lastname,
                'username': response.user.username,
                'storeName': response.user.store.store,
                'storeCode': response.user.store.code,
                'id_store': response.user.store.id_store,
                'id_role': response.user.role.id_role,
                'role': response.user.role.role,
            }
            message = {"status": "success"}
        respuesta = {
            "message": message,
            "user": user
        }
        return jsonify(respuesta),200
    return {"error": "No data provided"}, 400
    
@endpoints_usuarios_blueprint.route("/users/<int:id_user>/filter", methods=["GET"])
def getUserFilters(id_user):
    wsdl = os.getenv("SOAP_WSDL_INFORMES")
    client = Client(wsdl=wsdl)
    filters = []
    response = client.service.getUserFilters(id_user=id_user)
    for filter in response:
        filters.append({
            'id_user_filter': filter.id_user_filter,
            'filter': filter.filter,
            'id_user': filter.id_user,
            'cod_prod': filter.cod_prod,
            'date_from': filter.date_from,
            'date_to': filter.date_to,
            'state': filter.state,
            'id_store': filter.id_store,
            'enabled': filter.enabled,
        })
    return jsonify(filters),200


@endpoints_usuarios_blueprint.route("/users/<int:id_user>/filters", methods=["POST"])
def saveUserFilters(id_user):
    wsdl = os.getenv("SOAP_WSDL_INFORMES")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    
    id_user_filter = data.get("id_user_filter", 0)
    filter = data.get("filter", "")
    id_user = data.get("id_user", 0)
    cod_prod = data.get("cod_prod", "")
    date_from = data.get("date_from", "")
    date_to = data.get("date_to", "")
    state = data.get("state", "")
    id_store = data.get("id_store", 0)
    enabled = data.get("enabled", True) if data.get("enabled") is not None else True

    response = client.service.saveUserFilters(
        id_user_filter=id_user_filter,
        filter=filter,
        id_user=id_user,
        cod_prod=cod_prod,
        date_from=date_from,
        date_to=date_to,
        state=state,
        id_store=id_store,
        enabled=enabled
    )

    respuesta = {
        "id_user_filter": response.id_user_filter,
        "filter": response.filter,
        "id_user": response.id_user,
        "cod_prod": response.cod_prod,
        "date_from": response.date_from,
        "date_to": response.date_to,
        "state": response.state,
        "id_store": response.id_store,
        "enabled": response.enabled
    }
    return jsonify(respuesta)

@endpoints_usuarios_blueprint.route("/users/<int:id_user>/filters/<int:id_user_filter>", methods=["GET"])
def getUserFilter(id_user,id_user_filter):
    wsdl = os.getenv("SOAP_WSDL_INFORMES")
    client = Client(wsdl=wsdl)
    response = client.service.getUserFilterById(id_user_filter=id_user_filter)
    print(response)
    user_filter = {
        'id_user_filter': response.id_user_filter,
        'filter': response.filter,
        'id_user': response.id_user,
        'cod_prod': response.cod_prod,
        'date_from': response.date_from,
        'date_to': response.date_to,
        'state': response.state,
        'id_store': response.id_store,
        'enabled': response.enabled,
    }
    return jsonify(user_filter),200