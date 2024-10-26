package com.serversoap.serverjavasoap.endpoints;

import com.serversoap.serverjavasoap.entities.Store;
import com.serversoap.serverjavasoap.entities.User;
import com.serversoap.serverjavasoap.repositories.RoleRepository;
import com.serversoap.serverjavasoap.repositories.StoreRepository;
import com.serversoap.serverjavasoap.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;
import io.spring.guides.user_web_service.GetUserRequest;
import io.spring.guides.user_web_service.GetAllUsersRequest;
import io.spring.guides.user_web_service.GetAllUsersResponse;
import io.spring.guides.user_web_service.GetUserResponse;
import io.spring.guides.user_web_service.AddUserRequest;
import io.spring.guides.user_web_service.AddUserResponse;
import io.spring.guides.user_web_service.UserLoginRequest;
import io.spring.guides.user_web_service.UserLoginResponse;

import java.util.List;
import java.util.stream.Collectors;

@Endpoint
public class UserEndpoint {
    private static final String NAMESPACE_URI = "http://spring.io/guides/user-web-service";

    private UserRepository userRepository;
    private StoreRepository storeRepository;
    private RoleRepository roleRepository;

    @Autowired
    public UserEndpoint(UserRepository userRepository, StoreRepository storeRepository,RoleRepository roleRepository) {
        this.userRepository = userRepository;
        this.storeRepository = storeRepository;
        this.roleRepository = roleRepository;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getUserRequest")
    @ResponsePayload
    public GetUserResponse getUser(@RequestPayload GetUserRequest request) {
        GetUserResponse response = new GetUserResponse();
        User userEntity = userRepository.findByIdUser(request.getIdUser());
        io.spring.guides.user_web_service.User user = new io.spring.guides.user_web_service.User();
        user.setIdUser(userEntity.getIdUser());
        user.setName(userEntity.getName());
        user.setLastname(userEntity.getLastname());
        user.setUsername(userEntity.getUsername());
        user.setPassword(userEntity.getPassword());
        user.setIdRole(userEntity.getRole().getIdRole());
        user.setIdStore(userEntity.getStore().getIdStore());
        response.setUser(user);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "addUserRequest")
    @ResponsePayload
    public AddUserResponse addUser(@RequestPayload AddUserRequest request) {
        AddUserResponse response = new AddUserResponse();
        boolean puede_insertar = true;

        //el username ya existe
        User existe = userRepository.findByUsername(request.getUser().getUsername());
        if (existe != null) {
            response.setStatus("el usuario ya existe");
            puede_insertar = false;
        }
        //el codigo de la tienda no existe o la tienda esta deshabilitada
        Store store = storeRepository.findStoreByStoreCodeAndEnabledTrue(request.getUser().getStoreCode());
        if(store == null) {
            response.setStatus("el codigo de la tienda no existe o la tienda esta deshabilitada");
            puede_insertar = false;
        }
        if(puede_insertar) {
            User userEntity = new User();
            userEntity.setUsername(request.getUser().getUsername());
            userEntity.setPassword(request.getUser().getPassword());
            userEntity.setName(request.getUser().getName());
            userEntity.setLastname(request.getUser().getLastname());
            userEntity.setRole(roleRepository.findByIdRole(1));
            userEntity.setStore(store);
            userEntity.setEnabled(true);
            User nuevoUser = userRepository.save(userEntity);

            io.spring.guides.user_web_service.User userReponse = new io.spring.guides.user_web_service.User();
            userReponse.setIdUser(nuevoUser.getIdUser());
            userReponse.setName(nuevoUser.getName());
            userReponse.setLastname(nuevoUser.getLastname());
            userReponse.setUsername(nuevoUser.getUsername());
            userReponse.setPassword(nuevoUser.getPassword());
            userReponse.setIdRole(nuevoUser.getRole().getIdRole());
            userReponse.setIdStore(nuevoUser.getStore().getIdStore());
            response.setStatus("ok");
            response.setUser(userReponse);
        }
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "getAllUsersRequest")
    @ResponsePayload
    public GetAllUsersResponse getAllUsers(@RequestPayload GetAllUsersRequest request) {
        List<User> usuarios = userRepository.findAllByEnabledTrue();
        List<io.spring.guides.user_web_service.UserFull> usersResponse = usuarios.stream().map(userEntity -> {
            io.spring.guides.user_web_service.UserFull userReponse = new io.spring.guides.user_web_service.UserFull();
            io.spring.guides.user_web_service.Role roleResponse = new io.spring.guides.user_web_service.Role();

            roleResponse.setIdRole(userEntity.getRole().getIdRole());
            roleResponse.setRole(userEntity.getRole().getRoleName());
            userReponse.setRole(roleResponse);

            io.spring.guides.user_web_service.Store storeResponse = new io.spring.guides.user_web_service.Store();
            storeResponse.setIdStore(userEntity.getStore().getIdStore());
            storeResponse.setAddress(userEntity.getStore().getAddress());
            storeResponse.setCity(userEntity.getStore().getCity());
            storeResponse.setState(userEntity.getStore().getState());
            storeResponse.setCode(userEntity.getStore().getStoreCode());
            storeResponse.setStore(userEntity.getStore().getStoreName());
            storeResponse.setState(userEntity.getStore().getState());
            userReponse.setStore(storeResponse);

            userReponse.setIdUser(userEntity.getIdUser());
            userReponse.setName(userEntity.getName());
            userReponse.setLastname(userEntity.getLastname());
            userReponse.setUsername(userEntity.getUsername());
            userReponse.setPassword(userEntity.getPassword());
            userReponse.setStore(storeResponse);
            return userReponse;
        }).collect(Collectors.toList());
        GetAllUsersResponse response = new GetAllUsersResponse();
        response.getUsers().addAll(usersResponse);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "userLoginRequest")
    @ResponsePayload
    public UserLoginResponse loginUser(@RequestPayload UserLoginRequest request) {
        UserLoginResponse response = new UserLoginResponse();
        User userEntity = userRepository.validateUser(request.getUsername(), request.getPassword());
        response.setStatus("login error");
        if(userEntity != null) {
            response.setStatus("ok");
            io.spring.guides.user_web_service.UserFull userReponse = new io.spring.guides.user_web_service.UserFull();
            io.spring.guides.user_web_service.Role roleResponse = new io.spring.guides.user_web_service.Role();

            roleResponse.setIdRole(userEntity.getRole().getIdRole());
            roleResponse.setRole(userEntity.getRole().getRoleName());
            userReponse.setRole(roleResponse);

            io.spring.guides.user_web_service.Store storeResponse = new io.spring.guides.user_web_service.Store();
            storeResponse.setIdStore(userEntity.getStore().getIdStore());
            System.out.println(userEntity.getStore().getIdStore());
            storeResponse.setAddress(userEntity.getStore().getAddress());
            storeResponse.setCity(userEntity.getStore().getCity());
            storeResponse.setState(userEntity.getStore().getState());
            storeResponse.setCode(userEntity.getStore().getStoreCode());
            storeResponse.setStore(userEntity.getStore().getStoreName());
            userReponse.setStore(storeResponse);
            userReponse.setIdUser(userEntity.getIdUser());
            userReponse.setName(userEntity.getName());
            userReponse.setLastname(userEntity.getLastname());
            userReponse.setUsername(userEntity.getUsername());
            userReponse.setPassword(userEntity.getPassword());
            response.setUser(userReponse);
        }
        return response;
    }
}
