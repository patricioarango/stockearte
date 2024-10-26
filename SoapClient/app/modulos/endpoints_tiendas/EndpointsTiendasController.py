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
    
    # Valores predeterminados
    id_catalog = data.get("id_catalog", 0)
    catalog = data.get("catalog", "")
    enabled = data.get("enabled", True)

    print("Datos recibidos:", data)

    # Llamada al servicio SOAP
    response = client.service.saveCatalogo(
        id_catalog=id_catalog,
        catalog=catalog,
        id_store=id_store,
        enabled=enabled
    )

    respuesta = {
        'id_catalog': response.id_catalog,
        'catalog': response.catalog,
        'id_store': response.id_store,
        'enabled': response.enabled,
    }
    return jsonify(catalogo=respuesta)

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs/<int:id_catalog>/products/<int:id_product>", methods=["PUT"])
def add_producto_to_catalog(id_store,id_catalog,id_product):
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    if id_catalog <= 0:
        return jsonify({"error": "Invalid catalog ID."}), 400

    if id_product <= 0:
        return jsonify({"error": "Invalid product ID."}), 400

    response = client.service.addProductToCatalog(id_catalog=id_catalog,id_product=id_product)
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

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs/<int:id_catalog>/products/<int:id_product>", methods=["DELETE"])
def remove_producto_from_catalog(id_store,id_catalog,id_product): 
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    if id_catalog <= 0:
        return jsonify({"error": "Invalid catalog ID."}), 400

    if id_product <= 0:
        return jsonify({"error": "Invalid product ID."}), 400

    response = client.service.removeProductFromCatalog(id_catalog=int(id_catalog),id_product=int(id_product))
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

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/products", methods=["GET"])
def productosPorStore(id_store):
    wsdl = os.getenv("SOAP_WSDL_PRODUCTOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    productos = []
    response = client.service.getProductsByStore(id_store=int(id_store))
    for producto in response:
        productos.append({
            'id_product': producto.id_product,
            'productName': producto.product,
            'productCode': producto.code,
            'color': producto.color,
            'size': producto.size,
            'img': producto.img,
            'stock': producto.stock,
            'id_store': producto.id_store,
        })

    return jsonify(productos=productos)