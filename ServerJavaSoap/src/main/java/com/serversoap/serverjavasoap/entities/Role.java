package com.serversoap.serverjavasoap.entities;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "role")
@Data
@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class Role {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idRole;

    @Column(name = "role", nullable = false, length = 255)
    private String roleName;

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}