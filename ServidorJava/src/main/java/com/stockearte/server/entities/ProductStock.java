package com.stockearte.server.entities;
import lombok.*;

import java.util.HashSet;
import java.util.Set;
import javax.persistence.*;

@Entity
@Table(name = "product_stock")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ProductStock {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idProductStock;

    @Column(name = "stock", nullable = false, length = 11)
    private int stock;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_product", nullable = false)
    private Product product;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "id_store", nullable = false)
    private Store store;
}
