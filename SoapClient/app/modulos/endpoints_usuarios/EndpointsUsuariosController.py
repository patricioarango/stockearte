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
    """
    Agrega un nuevo usuario.
    ---
    tags:
      - Usuarios
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nombre:
                type: string
                description: Nombre del usuario
                example: "Juan"
              apellido:
                type: string
                description: Apellido del usuario
                example: "Pérez"
              username:
                type: string
                description: Nombre de usuario
                example: "juanperez"
              password:
                type: string
                description: Contraseña del usuario
                example: "contraseña123"
    responses:
      201:
        description: Usuario agregado exitosamente
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  description: Mensaje de éxito
                  example: "Usuario agregado exitosamente."
      400:
        description: Solicitud inválida
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Descripción del error
                  example: "El nombre es requerido."
      500:
        description: Error interno al agregar el usuario
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Descripción del error
                  example: "Error al conectar con el servicio."
    """
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
    """
    Inicia sesión de un usuario.
    ---
    tags:
      - Usuarios
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                description: Nombre de usuario
                example: "juanperez"
              password:
                type: string
                description: Contraseña del usuario
                example: "contraseña123"
    responses:
      200:
        description: Inicio de sesión exitoso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: object
                  properties:
                    status:
                      type: string
                      description: Estado del inicio de sesión
                      example: "success"
                user:
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
                    id_store:
                      type: integer
                      description: ID de la tienda
                    id_role:
                      type: integer
                      description: ID del rol del usuario
                    role:
                      type: string
                      description: Rol del usuario
      400:
        description: Solicitud inválida (usuario o contraseña faltantes)
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Mensaje de error
                  example: "Username and password are required"
      500:
        description: Error interno al iniciar sesión
        content:
          application/json:
            schema:
              type: object
              properties:
                error:
                  type: string
                  description: Mensaje de error
                  example: "Error al conectar con el servicio."
    """
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
    """
    Obtiene los filtros de un usuario específico.
    ---
    tags:
      - Informes
    parameters:
      - name: id_user
        in: path
        required: true
        description: ID del usuario para el que se desean obtener los filtros.
        schema:
          type: integer
    responses:
      200:
        description: Lista de filtros del usuario.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id_user_filter:
                    type: integer
                    description: ID del filtro de usuario.
                  filter:
                    type: string
                    description: El filtro aplicado.
                  id_user:
                    type: integer
                    description: ID del usuario.
                  cod_prod:
                    type: string
                    description: Código del producto.
                  date_from:
                    type: string
                    format: date
                    description: Fecha de inicio del filtro.
                  date_to:
                    type: string
                    format: date
                    description: Fecha de fin del filtro.
                  state:
                    type: string
                    description: Estado del filtro.
                  id_store:
                    type: integer
                    description: ID de la tienda.
                  enabled:
                    type: boolean
                    description: Indica si el filtro está habilitado.
      404:
        description: Usuario no encontrado.
    """
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
    """
    Guarda o actualiza los filtros de un usuario específico.
    ---
    tags:
      - Informes
    parameters:
      - name: id_user
        in: path
        required: true
        description: ID del usuario para el que se desea guardar el filtro.
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              id_user_filter:
                type: integer
                description: ID del filtro de usuario (0 para crear uno nuevo).
              filter:
                type: string
                description: El filtro a aplicar.
              id_user:
                type: integer
                description: ID del usuario.
              cod_prod:
                type: string
                description: Código del producto.
              date_from:
                type: string
                format: date
                description: Fecha de inicio del filtro.
              date_to:
                type: string
                format: date
                description: Fecha de fin del filtro.
              state:
                type: string
                description: Estado del filtro.
              id_store:
                type: integer
                description: ID de la tienda.
              enabled:
                type: boolean
                description: Indica si el filtro está habilitado.
    responses:
      200:
        description: Filtro guardado o actualizado exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                id_user_filter:
                  type: integer
                  description: ID del filtro guardado.
                filter:
                  type: string
                  description: El filtro aplicado.
                id_user:
                  type: integer
                  description: ID del usuario.
                cod_prod:
                  type: string
                  description: Código del producto.
                date_from:
                  type: string
                  format: date
                  description: Fecha de inicio del filtro.
                date_to:
                  type: string
                  format: date
                  description: Fecha de fin del filtro.
                state:
                  type: string
                  description: Estado del filtro.
                id_store:
                  type: integer
                  description: ID de la tienda.
                enabled:
                  type: boolean
                  description: Indica si el filtro está habilitado.
      400:
        description: Error en la solicitud debido a datos faltantes o incorrectos.
    """
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
    """
    Obtiene un filtro específico de un usuario por su ID.
    ---
    tags:
      - Informes
    parameters:
      - name: id_user
        in: path
        required: true
        description: ID del usuario al que pertenece el filtro.
        schema:
          type: integer
      - name: id_user_filter
        in: path
        required: true
        description: ID del filtro que se desea obtener.
        schema:
          type: integer
    responses:
      200:
        description: Filtro del usuario obtenido exitosamente.
        content:
          application/json:
            schema:
              type: object
              properties:
                id_user_filter:
                  type: integer
                  description: ID del filtro de usuario.
                filter:
                  type: string
                  description: El filtro aplicado.
                id_user:
                  type: integer
                  description: ID del usuario.
                cod_prod:
                  type: string
                  description: Código del producto.
                date_from:
                  type: string
                  format: date
                  description: Fecha de inicio del filtro.
                date_to:
                  type: string
                  format: date
                  description: Fecha de fin del filtro.
                state:
                  type: string
                  description: Estado del filtro.
                id_store:
                  type: integer
                  description: ID de la tienda.
                enabled:
                  type: boolean
                  description: Indica si el filtro está habilitado.
      404:
        description: Filtro no encontrado.
    """
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