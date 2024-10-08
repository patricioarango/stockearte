package com.stockearte.server.repository;

import java.io.Serializable;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.stockearte.server.entities.Novelty;

@Repository("noveltyRepository")
public interface NoveltyRepository extends JpaRepository<Novelty, Serializable>{
    public abstract Novelty findByIdNovelty(int id);
    public abstract List<Novelty> findAll();
}
