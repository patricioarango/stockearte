package com.arango.dssdg16.entidades;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDate;

@Entity
@Data
@NoArgsConstructor @AllArgsConstructor
@Setter
@Getter
@Table(name="user")

public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="id_user")
    private int id;

    @Column(name="name", nullable=false)
    private String name;

    @Column(name="lastname", nullable=false)
    private String lastname;

    @Column(name="username", nullable=false)
    private String username;

    @Column(name="password", nullable=false)
    private String password;

    @Column(name="enabled", nullable=false)
    private boolean enabled;

    @CreationTimestamp
    @Column(name="created_at", nullable=false)
    private LocalDate createdAt;

    @UpdateTimestamp
    @Column(name="updated_at", nullable=false)
    private LocalDate updatedAt;

    @ManyToOne
    @JoinColumn(name="id_role", nullable=false)
    private Role role;
}
