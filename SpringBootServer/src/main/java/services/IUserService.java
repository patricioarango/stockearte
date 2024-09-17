package services;

import com.arango.dssdg16.detos.UserDTO;

import java.util.List;

public interface IUserService {

    public UserDTO findById(int id);
    public UserDTO findByUsernameAndPassword(String username, String password);
    public List<UserDTO> findAll();
    public List<UserDTO> findAllEnabled();
}
