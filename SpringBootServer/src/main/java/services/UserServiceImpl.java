package services;

import com.arango.dssdg16.detos.UserDTO;
import com.arango.dssdg16.repositories.IUserRepository;
import com.arango.user.stubs.UserGrpc;
import com.arango.user.stubs.UserReply;
import com.arango.user.stubs.UserRequest;
import io.grpc.stub.StreamObserver;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class UserServiceImpl extends UserGrpc.UserImplBase {
    @Autowired
    IUserService userService;


    @Override
    public void userLogin(UserRequest request, StreamObserver<UserReply> responseObserver) {
        System.out.println("user login");
        System.out.println(request.getUsername());
        //UserDTO user = this.getUser(1);
        //System.out.println(user.toString());
        UserReply userReply = UserReply.newBuilder()
                .setIdUser(1)
                .setName("user.getName()")
                .setLastname("user.getLastname()")
                .setUsername("user.getUsername()")
                .setRole("admin")
                .build();
        responseObserver.onNext(userReply);
        responseObserver.onCompleted();
    }

    private UserDTO getUser(int id)
    {
        return userService.findById(id);
    }
}
