package com.stockearte.server.entities;

import java.util.Objects;

import javax.persistence.*;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

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


	public User(int idUser, String username, String name, String lastname, String password, Boolean enabled) {
		this.idUser = idUser;
		this.username = username;
		this.name = name;
		this.lastname = lastname;
		this.password = password;
		this.enabled = enabled;
	}

	public User(String username, String name, String lastname, String password, Boolean enabled) {
		this.username = username;
		this.name = name;
		this.lastname = lastname;
		this.password = password;
		this.enabled = enabled;
	}

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 97 * hash + Objects.hashCode(this.username);
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final User other = (User) obj;
        return Objects.equals(this.username, other.username);
    }

}