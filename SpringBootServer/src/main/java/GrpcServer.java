import io.grpc.Server;
import io.grpc.ServerBuilder;
import services.GreeterServiceImpl;

public class GrpcServer {

    public static void main(String[] args) throws Exception {
        // Build and start the gRPC server
        Server server = ServerBuilder.forPort(50051)  // gRPC server listens on port 50051
                .addService(new GreeterServiceImpl())
                .build();

        // Start the server
        server.start();
        System.out.println("gRPC server started on port 50051");

        // Keep the server running
        server.awaitTermination();
    }
}
