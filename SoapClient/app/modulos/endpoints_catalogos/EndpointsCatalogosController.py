from . import endpoints_catalogos_blueprint
from flask import jsonify
from flask import current_app as app
from zeep import Client
import os

@endpoints_catalogos_blueprint.route("/catalogos", methods=["GET"])
def catalogos():
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    response = client.service.getCatalogos(id_store = 1)
    catalogos = []
    for catalogo in response:
        catalogos.append({
            'id_catalog': catalogo.id_catalog,
            'catalog': catalogo.catalog,
            'id_store': catalogo.id_store,
            'enabled': catalogo.enabled
        })
   
    resp = jsonify(catalogos=catalogos)
    return resp