package com.stockearte.server.dto;

import com.stockearte.server.entities.OrderItem;

public class OrderItemDTO {
    private int idOrderItem;
    private String productCode;
    private String color;
    private String size;
    private int requestedAmount;

    public OrderItemDTO(OrderItem orderItem) {
        this.idOrderItem = orderItem.getId();
        this.productCode = orderItem.getProductCode();
        this.color = orderItem.getColor();
        this.size = orderItem.getSize();
        this.requestedAmount = orderItem.getRequestedAmount();
    }

    public int getIdOrderItem() {
        return idOrderItem;
    }

    public void setIdOrderItem(int idOrderItem) {
        this.idOrderItem = idOrderItem;
    }

    public String getProductCode() {
        return productCode;
    }

    public void setProductCode(String productCode) {
        this.productCode = productCode;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public int getRequestedAmount() {
        return requestedAmount;
    }

    public void setRequestedAmount(int requestedAmount) {
        this.requestedAmount = requestedAmount;
    }
}
