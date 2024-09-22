package com.stockearte.server.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.ProductStock;

@Repository("productStockRepository")
public interface ProductStockRepository extends JpaRepository<ProductStock, Serializable> {
    public abstract ProductStock findByIdProductStock(int id);
    public abstract ProductStock findByProduct_IdProductAndStore_IdStore(int idProduct, int idStore);
}
