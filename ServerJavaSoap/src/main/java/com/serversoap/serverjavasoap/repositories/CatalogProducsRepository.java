package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.CatalogProducts;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;
import java.util.List;

public interface CatalogProducsRepository extends JpaRepository<CatalogProducts, Serializable> {
    public abstract List<CatalogProducts> findByCatalog_IdCatalog(int idCatalog);
}
