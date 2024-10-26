from flask import Blueprint
endpoints_usuarios_blueprint = Blueprint("endpoints_usuarios", __name__)

from . import EndpointsUsuariosController