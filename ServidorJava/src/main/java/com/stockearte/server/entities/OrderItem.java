package com.stockearte.server.entities;

import lombok.*;

import javax.persistence.*;

@Entity
@Table(name = "order_item")
@Getter
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
}
