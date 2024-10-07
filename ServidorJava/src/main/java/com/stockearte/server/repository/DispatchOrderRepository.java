package src.main.java.com.stockearte.server.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;

import src.main.java.com.stockearte.server.entities.DispatchOrder;


public interface DispatchOrderRepository extends JpaRepository<DispatchOrder, Serializable>{

}
