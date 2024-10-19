package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.Store;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;

public interface StoreRepository extends JpaRepository<Store, Serializable>{
    public abstract Store findStoreByStoreCodeAndEnabledTrue(String code);
    public abstract Store findStoreByIdStore(int idStore);
}
