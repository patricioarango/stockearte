package com.arango.dssdg16.services.implementations;

import com.arango.dssdg16.detos.UserDTO;
import com.arango.dssdg16.entidades.User;
import com.arango.dssdg16.repositories.IUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import services.IUserService;

import java.util.ArrayList;
import java.util.List;

@Service("userService")
public class UserService implements IUserService {
    @Autowired
    private IUserRepository userRepository;

    public UserDTO findById(int id)
    {
        User user = userRepository.findById(id);
        UserDTO userDTO = this.userToUserDTO(user);
        return userDTO;
    }

    public UserDTO findByUsernameAndPassword(String username, String password){
        User user = userRepository.findByUsernameAndPassword(username,password);
        UserDTO userDTO = this.userToUserDTO(user);
        return userDTO;
    }

    public List<UserDTO> findAll(){
        List<User> users = userRepository.findAll();
        List<UserDTO> userDTOs = new ArrayList<>();
        users.forEach(user -> userDTOs.add(userToUserDTO(user)));
        return userDTOs;
    }

    public List<UserDTO> findAllEnabled(){
        List<User> users = userRepository.findAllByEnabledTrue();
        List<UserDTO> userDTOs = new ArrayList<>();
        users.forEach(user -> userDTOs.add(userToUserDTO(user)));
        return userDTOs;
    }

    private UserDTO userToUserDTO(User user)
    {
        UserDTO userDTO = new UserDTO(user.getId(),user.getName(),user.getLastname(),user.getUsername(),user.getPassword(),user.isEnabled(),user.getCreatedAt(),user.getUpdatedAt(),user.getRole());
        return userDTO;
    }
}
