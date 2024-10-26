from flask import Blueprint
endpoints_informes_blueprint = Blueprint("endpoints_informes", __name__)

from . import EndpointsInformesController