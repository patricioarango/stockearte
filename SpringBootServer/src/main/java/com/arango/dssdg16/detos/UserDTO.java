package com.arango.dssdg16.detos;

import com.arango.dssdg16.entidades.Role;
import lombok.AllArgsConstructor;
import lombok.Data;

import java.time.LocalDate;

@Data
@AllArgsConstructor
public class UserDTO {
    private int id;
    private String name;
    private String lastname;
    private String username;
    private String password;
    private boolean enabled;
    private LocalDate createdAt;
    private LocalDate updatedAt;
    private Role role;
}
