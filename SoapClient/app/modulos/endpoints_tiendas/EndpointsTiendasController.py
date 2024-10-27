from . import endpoints_tiendas_blueprint
from flask import jsonify,request
from flask import current_app as app
from zeep import Client
import os,requests

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs", methods=["GET"])
def catalogos_by_store(id_store):
    """
    Obtiene la lista de catálogos para una tienda específica.
    ---
    tags:
      - Catalogos
    parameters:
      - name: id_store
        in: path
        type: integer
        required: true
        description: ID de la tienda para obtener sus catálogos
    responses:
      200:
        description: Lista de catálogos obtenida correctamente para la tienda especificada
        content:
          application/json:
            schema:
              type: object
              properties:
                catalogs:
                  type: array
                  items:
                    type: object
                    properties:
                      id_catalog:
                        type: integer
                        description: ID del catálogo
                      name:
                        type: string
                        description: Nombre del catálogo
                      id_store:
                        type: integer
                        description: ID de la tienda asociada al catálogo
                      enabled:
                        type: boolean
                        description: Indica si el catálogo está habilitado
      400:
        description: Error en la solicitud para obtener catálogos
      404:
        description: Tienda no encontrada
    """
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    response = client.service.getCatalogos(id_store)
    catalogos = []
    for catalogo in response:
        catalogos.append({
            'id_catalog': catalogo.id_catalog,
            'name': catalogo.catalog,
            'id_store': catalogo.id_store,
            'enabled': catalogo.enabled
        })
    resp = jsonify(catalogs=catalogos)
    return resp

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs/<int:id_catalog>/products", methods=["GET"])
def get_products_of_catalog(id_store,id_catalog):
    """
    Obtiene la lista de productos de un catálogo específico de una tienda.
    ---
    tags:
      - Catalogos
    parameters:
      - name: id_store
        in: path
        type: integer
        required: true
        description: ID de la tienda
      - name: id_catalog
        in: path
        type: integer
        required: true
        description: ID del catálogo del cual obtener productos
    responses:
      200:
        description: Lista de productos obtenida correctamente para el catálogo especificado
        content:
          application/json:
            schema:
              type: object
              properties:
                catalogoProductos:
                  type: object
                  properties:
                    catalogo:
                      type: object
                      properties:
                        id_catalog:
                          type: integer
                          description: ID del catálogo
                        name:
                          type: string
                          description: Nombre del catálogo
                        id_store:
                          type: integer
                          description: ID de la tienda asociada al catálogo
                    productos:
                      type: array
                      items:
                        type: object
                        properties:
                          id_product:
                            type: integer
                            description: ID del producto
                          productName:
                            type: string
                            description: Nombre del producto
                          productCode:
                            type: string
                            description: Código del producto
                          color:
                            type: string
                            description: Color del producto
                          size:
                            type: string
                            description: Tamaño del producto
                          img:
                            type: string
                            description: URL de la imagen del producto
      400:
        description: Error en la solicitud para obtener productos del catálogo
      404:
        description: Catálogo o tienda no encontrados
    """
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
    """
    Agrega un nuevo catálogo a una tienda específica.
    ---
    tags:
      - Catalogos
    parameters:
      - name: id_store
        in: path
        type: integer
        required: true
        description: ID de la tienda donde se agrega el catálogo
      - name: body
        in: body
        required: true
        description: Datos del catálogo a agregar
        schema:
          type: object
          properties:
            id_catalog:
              type: integer
              description: ID del catálogo (opcional)
            catalog:
              type: string
              description: Nombre del catálogo
            enabled:
              type: boolean
              description: Estado de habilitación del catálogo (por defecto es `True`)
    responses:
      200:
        description: Catálogo agregado exitosamente
        content:
          application/json:
            schema:
              type: object
              properties:
                catalogo:
                  type: object
                  properties:
                    id_catalog:
                      type: integer
                      description: ID del catálogo
                    catalog:
                      type: string
                      description: Nombre del catálogo
                    id_store:
                      type: integer
                      description: ID de la tienda donde se agregó el catálogo
                    enabled:
                      type: boolean
                      description: Estado de habilitación del catálogo
      400:
        description: Error en la solicitud para agregar un catálogo
      404:
        description: Tienda no encontrada
    """
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()
    
    id_catalog = data.get("id_catalog", 0)
    catalog = data.get("catalog", "")
    enabled = data.get("enabled", True)

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

@endpoints_tiendas_blueprint.route("/stores/<int:id_store>/catalogs/<int:id_catalog>", methods=["PUT"])
def edit_catalog(id_store, id_catalog):
    """
    Edita un catálogo existente en una tienda específica.
    ---
    tags:
      - Catalogos
    parameters:
      - name: id_store
        in: path
        type: integer
        required: true
        description: ID de la tienda donde se encuentra el catálogo
      - name: id_catalog
        in: path
        type: integer
        required: true
        description: ID del catálogo a editar
      - name: body
        in: body
        required: true
        description: Datos del catálogo a actualizar
        schema:
          type: object
          properties:
            catalog:
              type: string
              description: Nombre del catálogo
            enabled:
              type: boolean
              description: Estado de habilitación del catálogo
    responses:
      200:
        description: Catálogo editado exitosamente
        content:
          application/json:
            schema:
              type: object
              properties:
                catalogo:
                  type: object
                  properties:
                    id_catalog:
                      type: integer
                      description: ID del catálogo
                    catalog:
                      type: string
                      description: Nombre del catálogo
                    id_store:
                      type: integer
                      description: ID de la tienda donde se editó el catálogo
                    enabled:
                      type: boolean
                      description: Estado de habilitación del catálogo
      400:
        description: Error en la solicitud para editar el catálogo
      404:
        description: Tienda o catálogo no encontrados
    """
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    data = request.get_json()

    # Obtener datos del catálogo a actualizar
    catalog = data.get("catalog", "")
    enabled = data.get("enabled", True)

    print("Datos recibidos para editar:", data)

    # Llamada al servicio SOAP para actualizar el catálogo
    response = client.service.saveCatalogo(  # Suponiendo que tengas un método `updateCatalogo` en tu servicio SOAP
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
    """
    Agrega un producto a un catálogo específico en una tienda.
    ---
    tags:
      - Catalogos
    parameters:
      - name: id_store
        in: path
        type: integer
        required: true
        description: ID de la tienda donde se agrega el producto
      - name: id_catalog
        in: path
        type: integer
        required: true
        description: ID del catálogo al que se agrega el producto
      - name: id_product
        in: path
        type: integer
        required: true
        description: ID del producto a agregar
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            your_field_name:
              type: string
              description: Descripción del campo
    responses:
      200:
        description: Producto agregado exitosamente al catálogo
        content:
          application/json:
            schema:
              type: object
              properties:
                catalogoProductos:
                  type: object
                  properties:
                    catalogo:
                      type: object
                      properties:
                        id_catalog:
                          type: integer
                          description: ID del catálogo
                        name:
                          type: string
                          description: Nombre del catálogo
                        id_store:
                          type: integer
                          description: ID de la tienda donde se agregó el producto
                    productos:
                      type: array
                      items:
                        type: object
                        properties:
                          id_product:
                            type: integer
                            description: ID del producto
                          productName:
                            type: string
                            description: Nombre del producto
                          productCode:
                            type: string
                            description: Código del producto
                          color:
                            type: string
                            description: Color del producto
                          size:
                            type: string
                            description: Tamaño del producto
                          img:
                            type: string
                            description: URL de la imagen del producto
      400:
        description: ID de catálogo o producto inválido
      500:
        description: Error interno en el servidor
    """
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
    """
    Elimina un producto de un catálogo específico en una tienda.
    ---
    tags:
        - Catalogos
    parameters:
      - name: id_store
        in: path
        type: integer
        required: true
        description: ID de la tienda donde se elimina el producto
      - name: id_catalog
        in: path
        type: integer
        required: true
        description: ID del catálogo del que se elimina el producto
      - name: id_product
        in: path
        type: integer
        required: true
        description: ID del producto a eliminar
    responses:
      200:
        description: Producto eliminado exitosamente del catálogo
        content:
          application/json:
            schema:
              type: object
              properties:
                catalogoProductos:
                  type: object
                  properties:
                    catalogo:
                      type: object
                      properties:
                        id_catalog:
                          type: integer
                          description: ID del catálogo
                        name:
                          type: string
                          description: Nombre del catálogo
                        id_store:
                          type: integer
                          description: ID de la tienda donde se eliminó el producto
                    productos:
                      type: array
                      items:
                        type: object
                        properties:
                          id_product:
                            type: integer
                            description: ID del producto
                          productName:
                            type: string
                            description: Nombre del producto
                          productCode:
                            type: string
                            description: Código del producto
                          color:
                            type: string
                            description: Color del producto
                          size:
                            type: string
                            description: Tamaño del producto
                          img:
                            type: string
                            description: URL de la imagen del producto
      400:
        description: ID de catálogo o producto inválido
      500:
        description: Error interno en el servidor
    """
    wsdl = os.getenv("SOAP_WSDL_CATALOGOS")
    client = Client(wsdl=wsdl)
    
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
    """
    Obtiene la lista de productos para una tienda específica.
    ---
    tags:
      - Catalogos
    parameters:
      - name: id_store
        in: path
        type: integer
        required: true
        description: ID de la tienda para obtener sus productos
    responses:
      200:
        description: Lista de productos obtenida exitosamente
        content:
          application/json:
            schema:
              type: object
              properties:
                productos:
                  type: array
                  items:
                    type: object
                    properties:
                      id_product:
                        type: integer
                        description: ID del producto
                      productName:
                        type: string
                        description: Nombre del producto
                      productCode:
                        type: string
                        description: Código del producto
                      color:
                        type: string
                        description: Color del producto
                      size:
                        type: string
                        description: Tamaño del producto
                      img:
                        type: string
                        description: URL de la imagen del producto
                      stock:
                        type: integer
                        description: Cantidad de stock del producto
                      id_store:
                        type: integer
                        description: ID de la tienda donde se encuentra el producto
      404:
        description: No se encontraron productos para la tienda
      500:
        description: Error interno en el servidor
    """
    wsdl = os.getenv("SOAP_WSDL_PRODUCTOS")
    
    if not wsdl:
        return jsonify({'error': 'WSDL not configured'}), 500
    try:
        client = Client(wsdl=wsdl)
        productos = []
        
        response = client.service.getProductsByStore(id_store=id_store)
        if not response:
            return jsonify({'error': 'No products found for the store'}), 404
        
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

        return jsonify(productos=productos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
