package com.serversoap.serverjavasoap.entities;

import jakarta.persistence.*;
import lombok.*;
import java.util.List;

@Entity
@Table(name = "purchase_order")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class PurchaseOrder {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private int id;

    @Column(name = "observation", columnDefinition = "TEXT")
    private String observation;

    @ManyToOne
    @JoinColumn(name="id_store", nullable=true)
    private Store store;

    @Column(name = "state", nullable = false, length = 255)
    private String state;

    @Column(name = "created_at")
    private String createdAt;

    @Column(name = "purchase_order_date")
    private String purchaseOrderDate;

    @Column(name = "reception_date")
    private String receptionDate;

    @Column(name = "id_dispatch_order")
    private int idDispatchOrder;

    @OneToMany(mappedBy = "purchaseOrder", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<OrderItem> orderItems;

}
