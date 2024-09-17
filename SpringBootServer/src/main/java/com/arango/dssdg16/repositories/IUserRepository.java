package com.arango.dssdg16.repositories;

import com.arango.dssdg16.entidades.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.Serializable;
import java.util.List;

public interface IUserRepository extends JpaRepository<User, Serializable> {
    public User findById(int id);
    public User findByUsernameAndPassword(String username, String password);
    public List<User> findAll();
    public List<User> findAllByEnabledTrue();
}
