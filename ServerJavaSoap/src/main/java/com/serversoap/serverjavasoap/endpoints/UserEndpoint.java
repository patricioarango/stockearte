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
import io.spring.guides.user_web_service.GetUserResponse;
import io.spring.guides.user_web_service.AddUserRequest;
import io.spring.guides.user_web_service.AddUserResponse;

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
}
