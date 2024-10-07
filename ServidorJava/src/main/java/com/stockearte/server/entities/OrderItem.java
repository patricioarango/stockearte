package com.stockearte.server.entities;

import lombok.*;

import javax.persistence.*;

@Entity
@Table(name = "order_item")
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class OrderItem {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private int id;

    @Column(name = "product_code", nullable = false, length = 255)
    private String productCode;

    @Column(name = "color", nullable = false, length = 255)
    private String color;

    @Column(name = "size", nullable = false, length = 255)
    private String size;

    @Column(name = "requested_amount", nullable = false, length = 11)
    private int requestedAmount;

    @ManyToOne
    @JoinColumn(name = "purchase_order_id", nullable = false)
    private PurchaseOrder purchaseOrder;

    @Column(name = "send")
    private Boolean send;

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("OrderItem{");
        sb.append("id=").append(id);
        sb.append(", productCode=").append(productCode);
        sb.append(", color=").append(color);
        sb.append(", size=").append(size);
        sb.append(", requestedAmount=").append(requestedAmount);
        sb.append('}');
        return sb.toString();
    }

    public int getId() {
        return id;
    }

    public String getProductCode() {
        return productCode;
    }

    public String getColor() {
        return color;
    }

    public String getSize() {
        return size;
    }

    public int getRequestedAmount() {
        return requestedAmount;
    }

    public PurchaseOrder getPurchaseOrder() {
        return purchaseOrder;
    }

    public Boolean getSend() {
        return send;
    }

}
