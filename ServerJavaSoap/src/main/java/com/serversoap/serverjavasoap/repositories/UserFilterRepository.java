package com.serversoap.serverjavasoap.repositories;

import com.serversoap.serverjavasoap.entities.UserFilter;
import org.springframework.data.jpa.repository.JpaRepository;
import java.io.Serializable;
import java.util.List;

public interface UserFilterRepository extends JpaRepository<UserFilter, Serializable>{
    List<UserFilter> findAllByUser_IdUser(int userId);
}
