package services;

import com.arango.user.stubs.UserGrpc;
import com.arango.user.stubs.UserReply;
import com.arango.user.stubs.UserRequest;
import io.grpc.stub.StreamObserver;

public class UserServiceImpl extends UserGrpc.UserImplBase {

    @Override
    public void userLogin(UserRequest request, StreamObserver<UserReply> responseObserver) {
        System.out.println("user login");
        System.out.println(request.getUsername());
        UserReply userReply = UserReply.newBuilder()
                .setIdUser(1)
                .setName("patricio")
                .setLastname("arango")
                .setUsername("patricioarango")
                .setRole("admin")
                .build();
        responseObserver.onNext(userReply);
        responseObserver.onCompleted();
    }
}
