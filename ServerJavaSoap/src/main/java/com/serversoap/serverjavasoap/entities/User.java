package com.serversoap.serverjavasoap.entities;

import jakarta.persistence.*;
import lombok.*;


@Entity
@Table(name = "user")
@Getter
@Setter
@Data @NoArgsConstructor
public class User{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idUser;

    @Column(name = "username", nullable = false, length = 255)
    private String username;

    @Column(name = "name", nullable = false, length = 255)
    private String name;

    @Column(name = "lastname", nullable = false, length = 255)
    private String lastname;

    @Column(name = "password", nullable = false, length = 255)
    private String password;

    @ManyToOne
    @JoinColumn(name="id_role", nullable=true)
    private Role role;

    @ManyToOne
    @JoinColumn(name="id_store", nullable=true)
    private Store store;

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}
