from flask import Blueprint
endpoints_catalogos_blueprint = Blueprint("endpoints_catalogos", __name__)

from . import EndpointsCatalogosController