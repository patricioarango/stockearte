package com.stockearte.server.dto;

import com.stockearte.server.entities.Store;

public class StoreDTO {
    private int idStore;
    private String storeName;
    private String storeCode;

    public StoreDTO(Store store) {
        this.idStore = store.getIdStore();
        this.storeName = store.getStoreName(); 
        this.storeCode = store.getStoreCode();
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

    public String getStoreCode() {
        return storeCode;
    }

    public void setStoreCode(String storeCode) {
        this.storeCode = storeCode;
    }

}
