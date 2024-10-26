package com.serversoap.serverjavasoap.endpoints;

import com.serversoap.serverjavasoap.entities.Catalog;
import com.serversoap.serverjavasoap.entities.CatalogProducts;
import com.serversoap.serverjavasoap.entities.Product;
import com.serversoap.serverjavasoap.entities.Store;
import com.serversoap.serverjavasoap.repositories.CatalogProducsRepository;
import com.serversoap.serverjavasoap.repositories.CatalogRepository;
import com.serversoap.serverjavasoap.repositories.ProductRepository;
import com.serversoap.serverjavasoap.repositories.StoreRepository;
import io.spring.guides.catalogos_web_service.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import java.util.List;
import java.util.stream.Collectors;

@Endpoint
public class CatalogEndpoint {
    private static final String NAMESPACE_URI = "http://spring.io/guides/catalogos-web-service";

    private CatalogRepository catalogRepository;
    private CatalogProducsRepository catalogProducsRepository;
    private StoreRepository storeRepository;
    private ProductRepository productRepository;

    @Autowired
    public CatalogEndpoint(CatalogRepository catalogRepository,CatalogProducsRepository catalogProducsRepository,StoreRepository storeRepository, ProductRepository productRepository) {
        this.catalogRepository = catalogRepository;
        this.catalogProducsRepository = catalogProducsRepository;
        this.storeRepository = storeRepository;
        this.productRepository = productRepository;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getCatalogosRequest")
    @ResponsePayload
    public GetCatalogosResponse getCatalogos(@RequestPayload GetCatalogosRequest request) {
        List<Catalog> catalogos = catalogRepository.findAllByStore_IdStore(request.getIdStore());
        List<io.spring.guides.catalogos_web_service.CatalogoSinProductos> catalogoResponse = catalogos.stream().map(catalog ->
        {
            io.spring.guides.catalogos_web_service.CatalogoSinProductos catalogoSimple = new io.spring.guides.catalogos_web_service.CatalogoSinProductos();
            catalogoSimple.setCatalog(catalog.getCatalog());
            catalogoSimple.setIdCatalog(catalog.getIdCatalog());
            catalogoSimple.setIdStore(request.getIdStore());
            catalogoSimple.setEnabled(catalog.getEnabled());
            return catalogoSimple;
        }).collect(Collectors.toList());

        GetCatalogosResponse response = new GetCatalogosResponse();
        response.getCatalogos().addAll(catalogoResponse);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getProductsCatalogoRequest")
    @ResponsePayload
    public GetProductsCatalogoResponse getProductosCatalogos(@RequestPayload GetProductsCatalogoRequest request) {
        Catalog catalogo = catalogRepository.findByIdCatalog(request.getIdCatalog());
        io.spring.guides.catalogos_web_service.Catalogo catalogoSimple = new io.spring.guides.catalogos_web_service.Catalogo();
        catalogoSimple.setCatalog(null);  // Optional: Set catalog to null
        catalogoSimple.setIdCatalog(0);    // Use a default value if applicable
        catalogoSimple.setIdStore(0);
        if(catalogo != null){
            catalogoSimple.setCatalog(catalogo.getCatalog());
            catalogoSimple.setIdCatalog(catalogo.getIdCatalog());
            catalogoSimple.setIdStore(catalogo.getStore().getIdStore());
        }
        List<CatalogProducts> productosCatalogo = catalogProducsRepository.findByCatalog_IdCatalog(request.getIdCatalog());

        List<io.spring.guides.catalogos_web_service.Producto> catalogoResponse = productosCatalogo.stream().map(product ->
        {
            io.spring.guides.catalogos_web_service.Producto productoResponse = new io.spring.guides.catalogos_web_service.Producto();
            productoResponse.setIdProduct(product.getProduct().getIdProduct());
            productoResponse.setProduct(product.getProduct().getProductName());
            productoResponse.setCode(product.getProduct().getProductCode());
            productoResponse.setColor(product.getProduct().getColor());
            productoResponse.setSize(product.getProduct().getSize());
            productoResponse.setImg(product.getProduct().getImg());
            return productoResponse;
        }).collect(Collectors.toList());

        GetProductsCatalogoResponse response = new GetProductsCatalogoResponse();
        response.setCatalogo(catalogoSimple);
        response.getProductos().addAll(catalogoResponse);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "saveCatalogoRequest")
    @ResponsePayload
    public SaveCatalogoResponse saveCatalogo(@RequestPayload SaveCatalogoRequest request) {
        Catalog catalogo = new Catalog();
        Store store = storeRepository.findStoreByIdStore(request.getIdStore());
        if(request.getIdCatalog() > 0)
        {
            catalogo.setIdCatalog(request.getIdCatalog());
        }
        catalogo.setCatalog(request.getCatalog());
        catalogo.setEnabled(request.isEnabled());
        catalogo.setStore(store);
        Catalog nuevoCatalogo = catalogRepository.save(catalogo);
        io.spring.guides.catalogos_web_service.CatalogoSimple catalogoSimple = new io.spring.guides.catalogos_web_service.CatalogoSimple();
        catalogoSimple.setIdCatalog(nuevoCatalogo.getIdCatalog());
        catalogoSimple.setCatalog(nuevoCatalogo.getCatalog());
        catalogoSimple.setIdStore(nuevoCatalogo.getStore().getIdStore());
        catalogoSimple.setEnabled(nuevoCatalogo.getEnabled());
        SaveCatalogoResponse response = new SaveCatalogoResponse();
        response.setCatalogo(catalogoSimple);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "addProductToCatalogRequest")
    @ResponsePayload
    public AddProductToCatalogResponse addProductoACatalogo(@RequestPayload AddProductToCatalogRequest request) {
        Catalog catalogo = catalogRepository.findByIdCatalog(request.getIdCatalog());
        Product producto = productRepository.findByIdProduct(request.getIdProduct());
        CatalogProducts catalogProducts = new CatalogProducts();
        catalogProducts.setCatalog(catalogo);
        catalogProducts.setProduct(producto);
        catalogProducsRepository.save(catalogProducts);

        io.spring.guides.catalogos_web_service.Catalogo catalogoSimple = new io.spring.guides.catalogos_web_service.Catalogo();
        catalogoSimple.setCatalog(null);
        catalogoSimple.setIdCatalog(0);
        catalogoSimple.setIdStore(0);
        if(catalogo != null){
            catalogoSimple.setCatalog(catalogo.getCatalog());
            catalogoSimple.setIdCatalog(catalogo.getIdCatalog());
            catalogoSimple.setIdStore(catalogo.getStore().getIdStore());
        }
        List<CatalogProducts> productosCatalogo = catalogProducsRepository.findByCatalog_IdCatalog(request.getIdCatalog());

        List<io.spring.guides.catalogos_web_service.Producto> catalogoResponse = productosCatalogo.stream().map(product ->
        {
            io.spring.guides.catalogos_web_service.Producto productoResponse = new io.spring.guides.catalogos_web_service.Producto();
            productoResponse.setIdProduct(product.getProduct().getIdProduct());
            productoResponse.setProduct(product.getProduct().getProductName());
            productoResponse.setCode(product.getProduct().getProductCode());
            productoResponse.setColor(product.getProduct().getColor());
            productoResponse.setSize(product.getProduct().getSize());
            productoResponse.setImg(product.getProduct().getImg());
            return productoResponse;
        }).collect(Collectors.toList());

        AddProductToCatalogResponse response = new AddProductToCatalogResponse();
        response.setCatalogo(catalogoSimple);
        response.getProductos().addAll(catalogoResponse);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "removeProductFromCatalogRequest")
    @ResponsePayload
    public RemoveProductFromCatalogResponse removeProductoDeCatalogo(@RequestPayload RemoveProductFromCatalogRequest request) {
        Catalog catalogo = catalogRepository.findByIdCatalog(request.getIdCatalog());

        CatalogProducts catalogProducts = catalogProducsRepository.findByCatalog_IdCatalogAndProduct_IdProduct(request.getIdCatalog(),request.getIdProduct());
        catalogProducsRepository.delete(catalogProducts);

        io.spring.guides.catalogos_web_service.Catalogo catalogoSimple = new io.spring.guides.catalogos_web_service.Catalogo();
        catalogoSimple.setCatalog(null);
        catalogoSimple.setIdCatalog(0);
        catalogoSimple.setIdStore(0);
        if(catalogo != null){
            catalogoSimple.setCatalog(catalogo.getCatalog());
            catalogoSimple.setIdCatalog(catalogo.getIdCatalog());
            catalogoSimple.setIdStore(catalogo.getStore().getIdStore());
        }
        List<CatalogProducts> productosCatalogo = catalogProducsRepository.findByCatalog_IdCatalog(request.getIdCatalog());

        List<io.spring.guides.catalogos_web_service.Producto> catalogoResponse = productosCatalogo.stream().map(product ->
        {
            io.spring.guides.catalogos_web_service.Producto productoResponse = new io.spring.guides.catalogos_web_service.Producto();
            productoResponse.setIdProduct(product.getProduct().getIdProduct());
            productoResponse.setProduct(product.getProduct().getProductName());
            productoResponse.setCode(product.getProduct().getProductCode());
            productoResponse.setColor(product.getProduct().getColor());
            productoResponse.setSize(product.getProduct().getSize());
            productoResponse.setImg(product.getProduct().getImg());
            return productoResponse;
        }).collect(Collectors.toList());

        RemoveProductFromCatalogResponse response = new RemoveProductFromCatalogResponse();
        response.setCatalogo(catalogoSimple);
        response.getProductos().addAll(catalogoResponse);
        return response;
    }
}
