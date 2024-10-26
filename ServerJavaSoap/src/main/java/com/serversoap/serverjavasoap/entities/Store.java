package com.serversoap.serverjavasoap.entities;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "store")
@Setter
@Getter
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

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}