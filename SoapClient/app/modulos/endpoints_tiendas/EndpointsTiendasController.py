from . import endpoints_tiendas_blueprint
from flask import jsonify,request
from flask import current_app as app
from zeep import Client
import os,requests

@endpoints_tiendas_blueprint.route("/stores", methods=["GET"])
def endpoint_stores():
   
    resp = jsonify(usuarios={"stores": "stores"})
    return resp

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs", methods=["GET"])
def catalogos_by_store(id_store):
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    response = client.service.getCatalogos(id_store)
    catalogos = []
    for catalogo in response:
        catalogos.append({
            'id_catalog': catalogo.id_catalog,
            'name': catalogo.catalog,
            'id_store': catalogo.id_store,
        })
    resp = jsonify(catalogs=catalogos)
    return resp

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs/<int:id_catalog>/products", methods=["GET"])
def get_products_of_catalog(id_store,id_catalog):
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    response = client.service.getProductsCatalogo(id_catalog=id_catalog)
    catalogo_productos = []
    catalogo = None
    if response.catalogo:
        catalogo = {
            'id_catalog': response.catalogo.id_catalog,
            'name': response.catalogo.catalog,
            'id_store': response.catalogo.id_store
        }
    for producto in response.productos:
        catalogo_productos.append({
            'id_product': producto.id_product,
            'productName': producto.product,
            'productCode': producto.code,
            'color': producto.color,
            'size': producto.size,
            'img': producto.img
        })
    respuesta = {
        'catalogo': catalogo,
        'productos': catalogo_productos
    }
    return jsonify(catalogoProductos=respuesta)

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs", methods=["POST"])
def add_catalog(id_store):
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    id_catalog = 0
    catalog = ""
    id_store = 0
    enabled = True
    print(data)
    if(data['enabled']):
        enabled = data['enabled']

    if(data['catalog'] and data['id_store']):
        catalog = data['catalog']
        id_store = int(data['id_store'])
        
    if(data["id_catalog"]):
        id_catalog = data["id_catalog"]
            
    response = client.service.saveCatalogo(id_catalog=id_catalog,catalog=catalog,id_store=id_store,enabled=enabled)

    respuesta = {
        'id_catalog': response.id_catalog,
        'catalog': response.catalog,
        'id_store': response.id_store,
        'enabled': response.enabled,
    }
    return jsonify(catalogo=respuesta)

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs/<int:id_catalog>", methods=["PUT"])
def add_producto_to_catalog():