from . import endpoints_informes_blueprint
from flask import Flask, render_template, request, flash, redirect, session, json, url_for, redirect,jsonify
import os,json
from sqlalchemy import text
from flask import current_app as app
from zeep import Client

@endpoints_informes_blueprint.route("/informes", methods=["GET"])
def informes():
    wsdl = os.getenv("SOAP_WSDL_INFORMES")
    client = Client(wsdl=wsdl)
    informes = []
    response = client.service.getAllInformes()
    for informe in response:
        informes.append({
            'product_code': informe.product_code,
            'cantidad_pedida': informe.cantidad_pedida,
            'created_at': informe.created_at,
            'state': informe.state,
            'id_store': informe.id_store,
            'store_code': informe.store_code,
        })
    return jsonify(informes),200    

@endpoints_informes_blueprint.route("/informesByStore", methods=["GET"])
def informesByStore():
    """
    Obtiene los informes de una tienda específica.
    ---
    tags:
      - Informes
    parameters:
      - name: id_store
        in: query
        type: integer
        required: true
        description: ID de la tienda para la cual se obtienen los informes
    responses:
      200:
        description: Lista de informes obtenida exitosamente
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  product_code:
                    type: string
                    description: Código del producto en el informe
                  cantidad_pedida:
                    type: integer
                    description: Cantidad pedida en el informe
                  created_at:
                    type: string
                    format: date-time
                    description: Fecha de creación del informe
                  state:
                    type: string
                    description: Estado del informe
                  id_store:
                    type: integer
                    description: ID de la tienda del informe
                  store_code:
                    type: string
                    description: Código de la tienda del informe
      400:
        description: ID de tienda requerido
      500:
        description: Error interno al obtener los informes desde el servicio SOAP
    """
    wsdl = os.getenv("SOAP_WSDL_INFORMES") 
    client = Client(wsdl=wsdl)
    
    id_store = request.args.get('id_store')    

    response = client.service.getAllInformesByStore(store_id=int(id_store)) 

    informes = []
    for informe in response: 
        informes.append({
            'product_code': informe.product_code,
            'cantidad_pedida': informe.cantidad_pedida,
            'created_at': informe.created_at,
            'state': informe.state,
            'id_store': informe.id_store,
            'store_code': informe.store_code,
        })
    
    return jsonify(informes), 200



