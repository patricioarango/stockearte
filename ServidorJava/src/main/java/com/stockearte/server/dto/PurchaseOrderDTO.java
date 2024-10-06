package com.stockearte.server.dto;

import com.stockearte.server.entities.PurchaseOrder;
import com.stockearte.server.entities.Store;

import java.util.List;
import java.util.stream.Collectors;

public class PurchaseOrderDTO {
    private int idPurchaseOrder;
    private String observation;
    private String createdAt; 
    private String purchaseOrderDate; 
    private String receptionDate;    
    private String state;              
    private StoreDTO store;            
    private List<OrderItemDTO> orderItems; 

    public PurchaseOrderDTO(PurchaseOrder purchaseOrder) {
        this.idPurchaseOrder = purchaseOrder.getId();
        this.observation = purchaseOrder.getObservation();
        this.createdAt = purchaseOrder.getCreatedAt();
        this.purchaseOrderDate = purchaseOrder.getPurchaseOrderDate(); 
        this.receptionDate = purchaseOrder.getReceptionDate(); 
        this.state = purchaseOrder.getState().name();

        if (purchaseOrder.getStore() != null) {
            this.store = new StoreDTO(purchaseOrder.getStore());
        }

        if (purchaseOrder.getOrderItems() != null) {
            this.orderItems = purchaseOrder.getOrderItems().stream()
                    .map(OrderItemDTO::new)
                    .collect(Collectors.toList());
        }
    }

    public int getIdPurchaseOrder() {
        return idPurchaseOrder;
    }

    public void setIdPurchaseOrder(int idPurchaseOrder) {
        this.idPurchaseOrder = idPurchaseOrder;
    }

    public String getObservation() {
        return observation;
    }

    public void setObservation(String observation) {
        this.observation = observation;
    }
    
    public String getPurchaseOrderDate() {
        return purchaseOrderDate;
    }

    public void setPurchaseOrderDate(String purchaseOrderDate) {
        this.purchaseOrderDate = purchaseOrderDate;
    }

    public String getReceptionDate() {
        return receptionDate;
    }

    public void setReceptionDate(String receptionDate) {
        this.receptionDate = receptionDate;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public StoreDTO getStore() {
        return store;
    }

    public void setStore(StoreDTO store) {
        this.store = store;
    }

    public List<OrderItemDTO> getOrderItems() {
        return orderItems;
    }

    public void setOrderItems(List<OrderItemDTO> orderItems) {
        this.orderItems = orderItems;
    }

    public String getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
    }
}
