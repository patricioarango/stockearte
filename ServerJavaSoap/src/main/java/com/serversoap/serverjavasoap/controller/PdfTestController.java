package com.serversoap.serverjavasoap.controller;

import java.util.List;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.serversoap.serverjavasoap.entities.CatalogProducts;
import com.serversoap.serverjavasoap.repositories.CatalogProducsRepository;
import com.serversoap.serverjavasoap.util.PdfGenerator;

@RestController
public class PdfTestController {

    private final PdfGenerator pdfGenerator;
    private final CatalogProducsRepository catalogProductsRepository;

    public PdfTestController(PdfGenerator pdfGenerator, CatalogProducsRepository catalogProductsRepository) {
        this.pdfGenerator = pdfGenerator;
        this.catalogProductsRepository = catalogProductsRepository;
    }

    @GetMapping("/test/pdf")
    @ResponseBody
    public ResponseEntity<byte[]> generatePdf() {
        try {
            int catalogId = 1; 
            List<CatalogProducts> catalogProductsList = catalogProductsRepository.findByCatalog_IdCatalog(catalogId);

            byte[] pdfBytes = pdfGenerator.createCatalogProductsPdf(catalogProductsList);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(org.springframework.http.MediaType.APPLICATION_PDF);
            headers.setContentDispositionFormData("inline", "catalog_products.pdf");

            return new ResponseEntity<>(pdfBytes, headers, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
