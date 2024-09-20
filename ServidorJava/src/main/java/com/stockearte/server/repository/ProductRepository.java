package com.stockearte.server.repository;

import com.stockearte.server.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.io.Serializable;
import java.util.List;

@Repository("productRepository")
public interface ProductRepository extends JpaRepository<Product, Serializable> {
    public abstract Product findByIdProduct(int id);
    public abstract List<Product> findAll();
}

