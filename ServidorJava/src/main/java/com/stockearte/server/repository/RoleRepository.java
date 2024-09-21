package com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.Role;

@Repository("roleRepository")
public interface  RoleRepository extends JpaRepository<Role,Serializable>{
    public abstract List<Role> findAll();
    public abstract Role findByIdRole(int id);
}
