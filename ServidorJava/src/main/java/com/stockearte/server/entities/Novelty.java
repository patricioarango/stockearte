package com.stockearte.server.entities;

import lombok.*;

import java.util.HashSet;
import java.util.Set;
import javax.persistence.*;

@Entity
@Table(name = "novelty")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Novelty {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int idNovelty;
    
    @Column(name = "date", nullable = false, length = 255)
    private String date;

    @Column(name = "noveltyName", nullable = false, length = 255)
    private String noveltyName;

    @Column(name = "noveltyCode", nullable = false, length = 255)
    private String noveltyCode;

    @Column(name = "color", nullable = false, length = 255)
    private String color;

    @Column(name = "size", nullable = false, length = 255)
    private String size;

    @Column(name = "img", nullable = true, length = 255)
    private String img;

    @Column(name = "saved")
    private Boolean saved;
}
