package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.OrderItem;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.io.Serializable;
import java.util.List;

public interface OrderItemRepository extends JpaRepository<OrderItem, Serializable> {

        @Query(value = """
        SELECT oi.product_code, 
               SUM(CASE WHEN po.state <> 'RECHAZADA' THEN oi.requested_amount ELSE 0 END) AS cantidad_pedida,
               po.id AS purchaseOrderId, 
               po.created_at AS purchaseOrderCreatedAt, 
               po.state AS purchaseOrderState,
               po.id_store AS storeId,
               oi.color, oi.size, oi.send, oi.requested_amount
        FROM order_item oi 
        INNER JOIN purchase_order po ON po.id = oi.purchase_order_id 
        GROUP BY oi.product_code
    """, nativeQuery = true)
        List<Object[]> findAggregatedOrderItems();
}
