package com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.User;

@Repository("userRepository")
public interface UserRepository extends JpaRepository<User, Serializable> {

	@Query("SELECT u FROM User u WHERE u.username LIKE :username AND u.password LIKE :password")
	public abstract User validateUser(@Param("username") String username, @Param("password") String password);
	
	public abstract User findByIdUser(int idUser);
	public abstract List<User> findAll();
}