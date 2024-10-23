package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.io.Serializable;
import java.util.List;

public interface UserRepository extends JpaRepository<User, Serializable> {
    public abstract User findByIdUser(int idUser);
    public abstract User findByUsername(String username);
    public abstract List<User> findAllByEnabledTrue();
    @Query("SELECT u FROM User u WHERE u.username LIKE :username AND u.password LIKE :password")
    public abstract User validateUser(@Param("username") String username, @Param("password") String password);
}
