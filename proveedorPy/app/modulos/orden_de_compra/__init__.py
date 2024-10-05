from flask import Blueprint
orden_de_compra_blueprint = Blueprint("orden_de_compra", __name__,static_folder='archivos')

from . import OrdenDeCompraController