package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.Role;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;

public interface RoleRepository extends JpaRepository<Role, Serializable>{
    public abstract Role findByIdRole(int id);
}
