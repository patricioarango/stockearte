package com.serversoap.serverjavasoap.entities;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "catalog_products")
@Getter
@Setter
@Data @NoArgsConstructor
public class CatalogProducts {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idCatalogProducts;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_product", nullable = false)
    private Product product;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_catalog", nullable = false)
    private Catalog catalog;
}
