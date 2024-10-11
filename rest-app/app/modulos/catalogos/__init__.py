from flask import Blueprint
catalogos_blueprint = Blueprint("catalogos", __name__)

from . import CatalogosController