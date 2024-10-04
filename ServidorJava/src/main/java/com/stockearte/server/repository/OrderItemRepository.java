
package com.stockearte.server.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.OrderItem;

@Repository("orderItemRepository")
public interface OrderItemRepository extends JpaRepository<OrderItem, Serializable>{

}
