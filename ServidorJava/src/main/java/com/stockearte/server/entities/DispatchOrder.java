package src.main.java.com.stockearte.server.entities;

import lombok.*;

import java.util.HashSet;
import java.util.Set;
import java.util.List;

import javax.persistence.*;

@Entity
@Table(name = "dispatch_order")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class DispatchOrder {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false)
    private int id;

    @ManyToOne
    @JoinColumn(name = "purchase_order_id", nullable = false)
    private PurchaseOrder purchaseOrder;

    @Column(name = "estimated_shipping_date")
    private String estimatedShippingDate;
}
