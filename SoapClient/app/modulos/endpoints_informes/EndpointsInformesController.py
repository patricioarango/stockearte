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
