package com.serversoap.serverjavasoap.repositories;
import org.springframework.data.jpa.repository.JpaRepository;
import com.serversoap.serverjavasoap.entities.Catalog;

import java.io.Serializable;
import java.util.List;

public interface CatalogRepository extends JpaRepository<Catalog, Serializable>{
    public abstract Catalog findByIdCatalog(int idCatalog);
    public abstract List<Catalog> findAllByStore_IdStore(int idStore);
}
