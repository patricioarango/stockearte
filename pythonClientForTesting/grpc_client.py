import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import user_pb2
import user_pb2_grpc

def hello():
    # Connect to the gRPC server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        
        # Create a request
        request = helloworld_pb2.HelloRequest(name="Man")
        
        # Make the call to the gRPC server
        response = stub.SayHello(request)
        
        # Print the response
        print("Greeter client received: " + response.message)

def user():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserStub(channel)
        request = user_pb2.UserRequest(username="World",password="pass")
        response = stub.userLogin(request)
        print(response)

if __name__ == '__main__':
    hello()
