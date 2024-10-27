package com.serversoap.serverjavasoap.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

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
    private Integer idStore;

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}
