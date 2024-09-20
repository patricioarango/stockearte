package com.stockearte.server.entities;

import lombok.*;

import javax.persistence.*;
import java.util.Set;

@Entity
@Table(name = "store")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Store {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idStore;

    @Column(name = "store", nullable = false, length = 255)
    private String storeName;

    @Column(name = "code", nullable = false, length = 255)
    private String storeCode;

    @Column(name = "address", nullable = false, length = 255)
    private String address;

    @Column(name = "city", nullable = false, length = 255)
    private String city;

    @Column(name = "state", nullable = false, length = 255)
    private String state;

    @ManyToMany
    @JoinTable(name = "product_store",
            joinColumns = @JoinColumn(name = "id_store"),
            inverseJoinColumns = @JoinColumn(name = "id_product"))
    private Set<Product> products;

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}
