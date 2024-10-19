package com.serversoap.serverjavasoap.endpoints;

import com.serversoap.serverjavasoap.entities.Catalog;
import com.serversoap.serverjavasoap.repositories.CatalogRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;
import io.spring.guides.catalogos_web_service.GetCatalogosResponse;
import io.spring.guides.catalogos_web_service.GetCatalogosRequest;

import java.util.List;
import java.util.stream.Collectors;

@Endpoint
public class CatalogEndpoint {
    private static final String NAMESPACE_URI = "http://spring.io/guides/catalogos-web-service";

    private CatalogRepository catalogRepository;

    @Autowired
    public CatalogEndpoint(CatalogRepository catalogRepository) {
        this.catalogRepository = catalogRepository;
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
            return catalogoSimple;
        }).collect(Collectors.toList());

        GetCatalogosResponse response = new GetCatalogosResponse();
        response.getCatalogos().addAll(catalogoResponse);
        return response;
    }
}
