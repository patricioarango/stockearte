package com.serversoap.serverjavasoap.util;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.List;

import org.springframework.stereotype.Service;

import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Element;
import com.lowagie.text.Font;
import com.lowagie.text.Image;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
import com.serversoap.serverjavasoap.entities.CatalogProducts;

@Service
public class PdfGenerator {

    public byte[] createCatalogProductsPdf(List<CatalogProducts> catalogProductsList) throws IOException, DocumentException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        Document document = new Document();
        PdfWriter.getInstance(document, baos);
        document.open();

        if (!catalogProductsList.isEmpty() && catalogProductsList.get(0).getCatalog() != null) {
            Paragraph title = new Paragraph("Catálogo " + catalogProductsList.get(0).getCatalog().getCatalog(), new Font(Font.BOLD, 18));
            title.setAlignment(Element.ALIGN_CENTER);
            document.add(title);
            document.add(new Paragraph("\n")); 
        }

        PdfPTable table = new PdfPTable(5);
        table.addCell("Nombre");
        table.addCell("Código");
        table.addCell("Color");
        table.addCell("Tamaño");
        table.addCell("Imagen");

        for (CatalogProducts cp : catalogProductsList) {
            table.addCell(cp.getProduct().getProductName());
            table.addCell(cp.getProduct().getProductCode());
            table.addCell(cp.getProduct().getColor());
            table.addCell(cp.getProduct().getSize());

            String imagePath = cp.getProduct().getImg(); 
            try {
                Image img = Image.getInstance(imagePath);
                img.scaleToFit(50, 50); 

                PdfPCell imageCell = new PdfPCell(img);
                imageCell.setHorizontalAlignment(Element.ALIGN_CENTER); 
                table.addCell(imageCell);
            } catch (Exception e) {
                table.addCell("Imagen no disponible");
            }
        }

        document.add(table);
        document.close();
        return baos.toByteArray();
    }
}
