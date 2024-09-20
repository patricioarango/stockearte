package com.stockearte.server.service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;

import com.stockearte.server.entities.User;
import com.stockearte.server.repository.UserRepository;
import com.stockearte.model.UserProto;
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
                .setRole(user.getRole().getRoleName())
                .setIdStore(user.getStore().getIdStore())
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
        userDb = usuarioRepository.save(new User(request.getUsername(),request.getName(),request.getLastname(),request.getPassword(),request.getEnabled()));
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
        .setEnabled(request.getEnabled())
        .build();
        responseObserver.onNext(a);
        responseObserver.onCompleted();
    }

}

