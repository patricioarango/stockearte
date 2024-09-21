import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import user_pb2
import user_pb2_grpc
import store_pb2
import store_pb2_grpc
import role_pb2
import role_pb2_grpc

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

def roles():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = role_pb2_grpc.RoleServiceStub(channel)
        request = role_pb2.Role()
        response = stub.FindAll(request)
        print(response)        

def product():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        request = product_pb2.Product(idProduct=1)
        response = stub.GetProduct(request)
        print(response)        

def addproduct():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        request = product_pb2.Product(product="producto2",code="code2",color="azul",size="M",img="url_imagen",stock=0,enabled=True)
        response = stub.SaveProduct(request)
        print(response) 

def addstore():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = store_pb2_grpc.StoreServiceStub(channel)
        request = store_pb2.Store(idStore=3,storeName="store2 edit versoin",code="code2",address="address",city="city",state="state",enabled=True)
        response = stub.SaveStore(request)
        print(response)         

def adduser():
    with grpc.insecure_channel('localhost:9090') as channel:
        stub = user_pb2_grpc.UsersServiceStub(channel)
        rolereq = role_pb2.Role(idRole=2);
        storereq = store_pb2.Store(idStore=2);
        request = user_pb2.User(idUser=2,username="user2",name="manager edit",lastname="lastedit",password="pass",role=rolereq,store=storereq,enabled=True)
        response = stub.AddUser(request)
        print(response)

if __name__ == '__main__':
    adduser()
