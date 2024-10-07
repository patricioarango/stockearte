package com.stockearte.server.entities;

import lombok.*;

import javax.persistence.*;

import java.util.Set;
import java.util.HashSet;

@Entity
@Table(name = "store")
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
    
    @OneToMany(mappedBy = "store", cascade = CascadeType.ALL, orphanRemoval = true)
    private Set<ProductStock> productStock = new HashSet<>();

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Store{");
        sb.append("idStore=").append(idStore);
        sb.append(", storeName=").append(storeName);
        sb.append(", storeCode=").append(storeCode);
        sb.append(", address=").append(address);
        sb.append(", city=").append(city);
        sb.append(", state=").append(state);
        sb.append(", enabled=").append(enabled);
        sb.append('}');
        return sb.toString();
    }

    public int getIdStore() {
        return idStore;
    }

    public String getStoreName() {
        return storeName;
    }

    public String getStoreCode() {
        return storeCode;
    }

    public String getAddress() {
        return address;
    }

    public String getCity() {
        return city;
    }

    public String getState() {
        return state;
    }

    public Set<ProductStock> getProductStock() {
        return productStock;
    }

    public Boolean getEnabled() {
        return enabled;
    }


}
