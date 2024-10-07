package com.stockearte.server.entities;

import java.time.LocalDateTime;
import java.util.List;

import lombok.*;

import javax.persistence.*;
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

    @Enumerated(EnumType.STRING)
    @Column(name = "state", columnDefinition = "ENUM('RECHAZADA', 'ACEPTADA', 'SOLICITADA', 'RECIBIDA') DEFAULT 'SOLICITADA'")
    private State state = State.SOLICITADA;

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

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("PurchaseOrder{");
        sb.append("id=").append(id);
        sb.append(", observation=").append(observation);
        sb.append(", store=").append(store);
        sb.append(", state=").append(state);
        sb.append(", createdAt=").append(createdAt);
        sb.append(", purchaseOrderDate=").append(purchaseOrderDate);
        sb.append(", receptionDate=").append(receptionDate);
        sb.append(", orderItems=").append(orderItems);
        sb.append('}');
        return sb.toString();
    }

    public enum State {
        RECHAZADA, ACEPTADA, SOLICITADA, RECIBIDA
    }

    
}
