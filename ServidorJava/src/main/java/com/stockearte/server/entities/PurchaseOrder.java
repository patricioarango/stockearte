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
    private LocalDateTime createdAt;

    @Column(name = "purchase_order_date")
    private LocalDateTime purchaseOrderDate;

    @Column(name = "reception_date")
    private LocalDateTime receptionDate;

    @OneToMany(mappedBy = "purchaseOrder", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<OrderItem> orderItems;

    public enum State {
        RECHAZADA, ACEPTADA, SOLICITADA, RECIBIDA
    }
}
