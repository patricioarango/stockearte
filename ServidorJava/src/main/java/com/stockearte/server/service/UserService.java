package com.stockearte.server.service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

import com.stockearte.server.entities.User;
import com.stockearte.server.repository.UserRepository;
import com.stockearte.server.repository.RoleRepository;
import com.stockearte.server.repository.StoreRepository;
import com.stockearte.model.UserProto;
import com.stockearte.model.StoreProto;
import com.stockearte.model.RoleProto;
import com.stockearte.model.UsersServiceGrpc;
import com.google.protobuf.Empty;

import io.grpc.stub.StreamObserver;
import net.devh.boot.grpc.server.service.GrpcService;

@GrpcService
public class UserService extends UsersServiceGrpc.UsersServiceImplBase { 
    AtomicInteger id = new AtomicInteger();


	@Autowired
	@Qualifier("userRepository")
	private UserRepository usuarioRepository;

    @Autowired
	@Qualifier("roleRepository")
	private RoleRepository roleRepository;

    @Autowired
	@Qualifier("storeRepository")
	private StoreRepository storeRepository;
    
    @Override
    public void validateUser(UserProto.User request, StreamObserver<UserProto.User> responseObserver) {

    User user= usuarioRepository.validateUser(request.getUsername(),request.getPassword());
        
    if (user==null) {
        UserProto.User a = UserProto.User.newBuilder()
        .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    } else {
        UserProto.User a = UserProto.User.newBuilder()
        .setIdUser(user.getIdUser())
        .setUsername(user.getUsername())
        .setName(user.getName())
        .setLastname(user.getLastname())
        .setPassword(user.getPassword())
        .setRole(RoleProto.Role.newBuilder().setIdRole(user.getRole().getIdRole())
                                    .setRoleName(user.getRole().getRoleName()).build())
        .setStore(StoreProto.Store.newBuilder().setIdStore(user.getStore().getIdStore())
                                    .setStoreName(user.getStore().getStoreName()).build())
        .setEnabled(user.getEnabled())
        .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
        }
    }

    @Override
    public void getUser(UserProto.User request,StreamObserver<UserProto.User> responseObserver) {

        User user =usuarioRepository.findByIdUser(request.getIdUser());

        UserProto.User a = UserProto.User.newBuilder()
        .setIdUser(user.getIdUser())
        .setUsername(user.getUsername())
        .setName(user.getName())
        .setLastname(user.getLastname())
        .setPassword(user.getPassword())
        .setRole(RoleProto.Role.newBuilder().setIdRole(user.getRole().getIdRole())
                    .setRoleName(user.getRole().getRoleName()).build())
        .setStore(StoreProto.Store.newBuilder().setIdStore(user.getStore().getIdStore())
                    .setStoreName(user.getStore().getStoreName()).build())
        .setEnabled(user.getEnabled())
        .build();

        responseObserver.onNext(a);
        responseObserver.onCompleted();
        
    }

   	@Override
	public void findAll(Empty request, StreamObserver<UserProto.Users> responseObserver) {
        List<UserProto.User> userdb = new ArrayList<>();

        for (User user : usuarioRepository.findAll()) {
            UserProto.User userProto = UserProto.User.newBuilder()
                        .setIdUser(user.getIdUser())
                        .setUsername(user.getUsername())
                        .setName(user.getName())
                        .setLastname(user.getLastname())
                        .setPassword(user.getPassword())
                        .setRole(RoleProto.Role.newBuilder().setIdRole(user.getRole().getIdRole())
                                    .setRoleName(user.getRole().getRoleName()).build())
                        .setStore(StoreProto.Store.newBuilder().setIdStore(user.getStore().getIdStore())
                                    .setStoreName(user.getStore().getStoreName()).build())
                        .setEnabled(user.getEnabled())
                        .build();
            userdb.add(userProto);
        }

        UserProto.Users a = UserProto.Users.newBuilder()
            .addAllUser(userdb)
            .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void addUser(UserProto.User request, StreamObserver<UserProto.User> responseObserver) {
       
        User userDb = new User();

        try {
            if(request.getIdUser() > 0)
            {
                userDb.setIdUser(request.getIdUser());
            }    
            userDb.setUsername(request.getUsername());
            userDb.setName(request.getName());
            userDb.setLastname(request.getLastname());  
            userDb.setPassword(request.getPassword());
            userDb.setRole(roleRepository.findByIdRole(request.getRole().getIdRole()));
            userDb.setStore(storeRepository.findByIdStore(request.getStore().getIdStore()));
            userDb.setEnabled(request.getEnabled());
            userDb = usuarioRepository.save(userDb);
		} catch (Exception e) {
			try {
                throw new Exception("Error: el usuario ya existe");
            } catch (Exception e1) {
                // TODO Auto-generated catch block
                e1.printStackTrace();
            }
		}


        UserProto.User a = UserProto.User.newBuilder()
        .setIdUser(userDb.getIdUser())
        .setUsername(request.getUsername())
        .setName(request.getName())
        .setLastname(request.getLastname())
        .setPassword(request.getPassword())
        .setRole(RoleProto.Role.newBuilder().setIdRole(request.getRole().getIdRole()))
        .setStore(StoreProto.Store.newBuilder().setIdStore(request.getStore().getIdStore()))
        .setEnabled(request.getEnabled())
        .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

    @Override
    public void findByUsernameOrStoreName(UserProto.FindSearch request,StreamObserver<UserProto.Users> responseObserver) {
        List<UserProto.User> usersdb = new ArrayList<>();
        for(User user : usuarioRepository.findByUsernameOrStoreName(request.getSearch())) {
            UserProto.User userProto = UserProto.User.newBuilder()
                        .setIdUser(user.getIdUser())
                        .setUsername(user.getUsername())
                        .setName(user.getName())
                        .setLastname(user.getLastname())
                        .setPassword(user.getPassword())
                        .setRole(RoleProto.Role.newBuilder().setIdRole(user.getRole().getIdRole())
                                    .setRoleName(user.getRole().getRoleName()).build())
                        .setStore(StoreProto.Store.newBuilder().setIdStore(user.getStore().getIdStore())
                                    .setStoreName(user.getStore().getStoreName()).build())
                        .setEnabled(user.getEnabled())
                        .build();
            usersdb.add(userProto);
        }
        UserProto.Users a = UserProto.Users.newBuilder()
                .addAllUser(usersdb)
                .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }    

}

