from . import endpoints_catalogos_blueprint
from flask import jsonify
from flask import current_app as app
from zeep import Client, exceptions 
import os 
import base64
from flask import Response
from flask import request

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
            'id_store': catalogo.id_store
        })
   
    resp = jsonify(catalogos=catalogos)
    return resp

@endpoints_catalogos_blueprint.route("/catalogos/pdf", methods=["GET"])
def catalogos_pdf():
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    
    id_catalog = request.args.get('id_catalog', type=int)

    if id_catalog is None:
        return jsonify(error="El id_catalog es requerido."), 400 

    try:
        response = client.service.getCatalogoPdf(id_catalog=id_catalog)

        if isinstance(response, bytes):
            encoded_pdf = base64.b64encode(response).decode('utf-8')
            return jsonify(pdf_data=encoded_pdf)
        else:
            app.logger.error("La respuesta no es un objeto bytes.")
            return jsonify(error="La respuesta no es un objeto bytes.")
    except exceptions.Error as e:
        app.logger.error(f"Error al consumir el servicio SOAP para obtener PDF: {e}")
        return jsonify(error="No se pudo obtener el PDF desde el servicio SOAP")

