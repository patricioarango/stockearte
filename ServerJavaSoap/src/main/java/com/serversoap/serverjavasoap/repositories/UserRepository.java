package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;

public interface UserRepository extends JpaRepository<User, Serializable> {
    public abstract User findByIdUser(int idUser);
    public abstract User findByUsername(String username);
}
