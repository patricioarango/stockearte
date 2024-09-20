package com.stockearte.server.repository;

import com.stockearte.server.entities.Store;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.io.Serializable;
import java.util.List;

@Repository("storeRepository")
public interface StoreRepository extends JpaRepository<Store, Serializable> {
    public abstract List<Store> findAll();
    public abstract Store findByIdStore(int id);

}
