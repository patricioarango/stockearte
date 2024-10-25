package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.ProductStock;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;
import java.util.List;

public interface ProductStockRepository extends JpaRepository<ProductStock, Serializable> {
    public abstract List<ProductStock> findByStore_IdStore(int idStore);
}
