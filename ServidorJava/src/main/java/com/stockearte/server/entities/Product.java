package com.stockearte.server.entities;

import lombok.*;

import java.util.HashSet;
import java.util.Set;
import javax.persistence.*;

@Entity
@Table(name = "product")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idProduct;

    @Column(name = "product", nullable = false, length = 255)
    private String productName;

    @Column(name = "code", nullable = false, length = 255)
    private String productCode;

    @Column(name = "color", nullable = false, length = 255)
    private String color;

    @Column(name = "size", nullable = false, length = 255)
    private String size;

    @Column(name = "img", nullable = false, length = 255)
    private String img;

    @OneToMany(mappedBy = "product", cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<ProductStock> productStock = new HashSet<>();

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}
