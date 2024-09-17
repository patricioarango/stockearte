package com.arango.dssdg16.detos;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.time.LocalDate;

@Data
@AllArgsConstructor
public class RoleDTO {
    private int id;
    private String rolName;
    private LocalDate createdAt;
    private LocalDate updatedAt;
    private boolean enabled;
}
