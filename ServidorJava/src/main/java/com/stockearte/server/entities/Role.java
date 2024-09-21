package com.stockearte.server.entities;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

import lombok.Setter;

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
