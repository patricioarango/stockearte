package com.serversoap.serverjavasoap.entities;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "catalog")
@Getter
@Setter
@Data @NoArgsConstructor
public class Catalog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idCatalog;

    @Column(name = "catalog", nullable = false, length = 255)
    private String catalog;

    @ManyToOne
    @JoinColumn(name="id_store", nullable=true)
    private Store store;

    @Column(name = "enabled", nullable = false)
    private Boolean enabled;
}
