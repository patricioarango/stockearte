package com.arango.dssdg16.repositories;

import com.arango.dssdg16.detos.RoleDTO;
import com.arango.dssdg16.entidades.Role;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.io.Serializable;

public interface IRoleRepository extends JpaRepository<Role, Serializable> {
    @Query(value = "SELECT new com.arango.springbootserver.dtos.RolDTO(r.id_rol,r.rol,r.created_at,r.updated_at,r.enabled) FROM rol r WHERE r.id_rol=:idRol", nativeQuery = true)
    RoleDTO findByIdRol(@Param("idRol") int id);
}
