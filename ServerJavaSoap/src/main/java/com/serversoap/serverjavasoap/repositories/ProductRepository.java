package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;

public interface ProductRepository extends JpaRepository<Product, Serializable> {
    public abstract Product findByIdProduct(int id);
}
