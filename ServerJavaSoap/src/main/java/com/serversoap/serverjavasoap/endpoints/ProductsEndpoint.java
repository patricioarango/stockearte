package com.serversoap.serverjavasoap.endpoints;

import com.serversoap.serverjavasoap.entities.ProductStock;
import com.serversoap.serverjavasoap.repositories.ProductRepository;
import com.serversoap.serverjavasoap.repositories.ProductStockRepository;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import io.spring.guides.product_web_service.*;
import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

@Endpoint
public class ProductsEndpoint {
    private static final String NAMESPACE_URI = "http://spring.io/guides/product-web-service";
    private ProductRepository productRepository;
    private ProductStockRepository productStockRepository;

    @Autowired
    public ProductsEndpoint(ProductRepository productRepository, ProductStockRepository productStockRepository) {
        this.productRepository = productRepository;
        this.productStockRepository = productStockRepository;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getProductsByStoreRequest")
    @ResponsePayload
    public GetProductsByStoreResponse getProductosPorStore(@RequestPayload GetProductsByStoreRequest request) {
        List<ProductStock> productos = productStockRepository.findByStore_IdStore(request.getIdStore());
        List<io.spring.guides.product_web_service.Product> productoStoreResponse = productos.stream().map(product ->
        {
            io.spring.guides.product_web_service.Product productoSimple = new io.spring.guides.product_web_service.Product();
            productoSimple.setIdProduct(product.getProduct().getIdProduct());
            productoSimple.setProduct(product.getProduct().getProductName());
            productoSimple.setCode(product.getProduct().getProductCode());
            productoSimple.setColor(product.getProduct().getColor());
            productoSimple.setSize(product.getProduct().getSize());
            productoSimple.setImg(product.getProduct().getImg());
            productoSimple.setStock(product.getStock());
            productoSimple.setIdStore(product.getStore().getIdStore());
            return productoSimple;
        }).collect(Collectors.toList());

        GetProductsByStoreResponse response = new GetProductsByStoreResponse();
        response.getProducts().addAll(productoStoreResponse);
        return response;
    }
}
