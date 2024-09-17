package com.arango.dssdg16.entidades;

import java.time.LocalDate;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Data
@NoArgsConstructor @AllArgsConstructor
@Setter
@Getter
@Table(name="rol")
public class Role {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id_rol")
    private int id;

    @Column(name="rol", nullable=false)
    private String rolName;

    @CreationTimestamp
    @Column(name="created_at", nullable=false)
    private LocalDate createdAt;

    @UpdateTimestamp
    @Column(name="updated_at", nullable=false)
    private LocalDate updatedAt;

    @Column(name="enabled", nullable=false)
    private boolean enabled;

}
