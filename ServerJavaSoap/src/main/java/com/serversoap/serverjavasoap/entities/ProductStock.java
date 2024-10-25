package com.serversoap.serverjavasoap.entities;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "product_stock")
@Getter
@Setter
@Data
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
