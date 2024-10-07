package com.stockearte.server.dto;

import com.stockearte.server.entities.Store;

public class StoreDTO {
    private int idStore;
    private String storeName;

    public StoreDTO(Store store) {
        this.idStore = store.getIdStore();
        this.storeName = store.getStoreName(); 
    }

    public int getIdStore() {
        return idStore;
    }

    public void setIdStore(int idStore) {
        this.idStore = idStore;
    }

    public String getStoreName() {
        return storeName;
    }

    public void setStoreName(String storeName) {
        this.storeName = storeName;
    }
}
