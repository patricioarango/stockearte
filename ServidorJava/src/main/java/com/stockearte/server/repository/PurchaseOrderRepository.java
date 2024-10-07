
package com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.PurchaseOrder;


@Repository("purchaseOrderRepository")
public interface PurchaseOrderRepository  extends JpaRepository<PurchaseOrder, Serializable>{

    public abstract PurchaseOrder findById(int id);
    public abstract List<PurchaseOrder> findAll();   
    public abstract List<PurchaseOrder> findByStore_IdStore(int idStore); 
    
    @Query("SELECT p FROM PurchaseOrder p WHERE p.store.idStore = :idStore AND (p.observation IS NULL OR p.observation = '') AND (p.receptionDate IS NULL OR p.receptionDate = '') AND p.state = :state AND p.idDispatchOrder IS NOT NULL AND p.idDispatchOrder != 0")
    List<PurchaseOrder> findByStoreAndState(@Param("idStore") int idStore, @Param("state") PurchaseOrder.State state);
    
}
