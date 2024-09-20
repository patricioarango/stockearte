
package com.stockearte.server.entities;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@Table(name = "product")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_product")
    private Integer idProduct;

    @Column(name = "product", nullable = false, length = 255)
    private String product;

    @Column(name = "code", nullable = false, length = 10)
    private String code;

    @Column(name = "img", length = 255)
    private String img;

    @Column(name = "enabled", nullable = false)
    private Boolean enabled = true;

    @Column(name = "size", nullable = false, length = 255)
    private String size;

    @Column(name = "color", nullable = false, length = 255)
    private String color;

    public Product(String code, String color, String img, String product, String size) {
        this.code = code;
        this.color = color;
        this.img = img;
        this.product = product;
        this.size = size;
    }

    public Product(String code, String color, String product, String size) {
        this.code = code;
        this.color = color;
        this.product = product;
        this.size = size;
    }
}
