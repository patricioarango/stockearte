from flask import Blueprint
endpoints_tiendas_blueprint = Blueprint("endpoints_tiendas", __name__)

from . import EndpointsTiendasController