package com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.Store;

@Repository("storeRepository")
public interface StoreRepository extends JpaRepository<Store, Serializable> {
    public abstract List<Store> findAll();
    public abstract Store findByIdStore(int id);

    @Query("SELECT s FROM Store s WHERE (:code IS NULL OR s.storeCode LIKE %:code%) AND (:enabled IS NULL OR s.enabled = :enabled)")
    public abstract List<Store> findByCodeAndEnabled(@Param("code") String code, @Param("enabled") Boolean enabled);

    public abstract List<Store> findByStoreCode(String storeCode);
    public abstract List<Store> findByEnabled(Boolean enabled);

    public abstract Store findFirstByStoreCode(String storeCode);

}
