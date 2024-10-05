
package com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.PurchaseOrder;


@Repository("purchaseOrderRepository")
public interface PurchaseOrderRepository  extends JpaRepository<PurchaseOrder, Serializable>{

    public abstract PurchaseOrder findById(int id);
    public abstract List<PurchaseOrder> findAll();   
    public abstract List<PurchaseOrder> findByStore_IdStore(int idStore); 

}
