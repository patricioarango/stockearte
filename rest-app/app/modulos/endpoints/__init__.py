from flask import Blueprint
endpoints_blueprint = Blueprint("endpoints", __name__)

from . import EndpointsController