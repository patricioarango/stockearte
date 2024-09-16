package services;
import com.arango.helloworld.stubs.GreeterGrpc;
import com.arango.helloworld.stubs.HelloReply;
import com.arango.helloworld.stubs.HelloRequest;
import io.grpc.stub.StreamObserver;

// Greeter service implementation
public class GreeterServiceImpl extends GreeterGrpc.GreeterImplBase {

    @Override
    public void sayHello(HelloRequest request, StreamObserver<HelloReply> responseObserver) {
        // Create a response
        HelloReply reply = HelloReply.newBuilder()
                .setMessage("Hello, " + request.getName())
                .build();

        // Send the response
        responseObserver.onNext(reply);
        responseObserver.onCompleted();
    }
}