from flask import Blueprint
informes_blueprint = Blueprint("informes", __name__)

from . import InformesController