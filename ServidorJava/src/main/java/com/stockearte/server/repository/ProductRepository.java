package com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.Product;

@Repository("productRepository")
public interface ProductRepository extends JpaRepository<Product, Serializable> {
    public abstract Product findByIdProduct(int id);
    public abstract List<Product> findAll();
    
    @Query("SELECT ps.product FROM ProductStock ps WHERE ps.store.idStore = :idStore")
    public abstract List<Product> findProductsByStore(@Param("idStore") int idStore);   

    public abstract Product findByProductCode(String productCode);
}

