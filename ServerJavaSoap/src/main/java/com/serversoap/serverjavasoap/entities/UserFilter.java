package com.serversoap.serverjavasoap.entities;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "user_filters")
@Getter
@Setter
@Data @NoArgsConstructor
public class UserFilter {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idUserFilter;

    @Column(name = "filter", nullable = false, length = 255)
    private String filter;

    @ManyToOne
    @JoinColumn(name="id_user", nullable=false)
    private User user;

    @Column(name = "cod_prod", nullable = true, length = 255)
    private String codProd;

    @Column(name = "date_from", nullable = true, length = 255)
    private String dateFrom;

    @Column(name = "date_to", nullable = true, length = 255)
    private String dateTo;

    @Column(name = "state", nullable = true, length = 255)
    private String state;

    @Column(name = "id_store", nullable = true)
    private int id_store;

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}
