package src.main.java.com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.DispatchOrder;


public interface DispatchOrderRepository extends JpaRepository<DispatchOrder, Serializable>{

}
