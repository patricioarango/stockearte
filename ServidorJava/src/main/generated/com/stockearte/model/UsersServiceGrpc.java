package com.stockearte.model;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.57.2)",
    comments = "Source: user.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class UsersServiceGrpc {

  private UsersServiceGrpc() {}

  public static final java.lang.String SERVICE_NAME = "model.UsersService";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User,
      com.stockearte.model.UserProto.User> getValidateUserMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ValidateUser",
      requestType = com.stockearte.model.UserProto.User.class,
      responseType = com.stockearte.model.UserProto.User.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User,
      com.stockearte.model.UserProto.User> getValidateUserMethod() {
    io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User, com.stockearte.model.UserProto.User> getValidateUserMethod;
    if ((getValidateUserMethod = UsersServiceGrpc.getValidateUserMethod) == null) {
      synchronized (UsersServiceGrpc.class) {
        if ((getValidateUserMethod = UsersServiceGrpc.getValidateUserMethod) == null) {
          UsersServiceGrpc.getValidateUserMethod = getValidateUserMethod =
              io.grpc.MethodDescriptor.<com.stockearte.model.UserProto.User, com.stockearte.model.UserProto.User>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ValidateUser"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.stockearte.model.UserProto.User.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.stockearte.model.UserProto.User.getDefaultInstance()))
              .setSchemaDescriptor(new UsersServiceMethodDescriptorSupplier("ValidateUser"))
              .build();
        }
      }
    }
    return getValidateUserMethod;
  }

  private static volatile io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User,
      com.stockearte.model.UserProto.User> getGetUserMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GetUser",
      requestType = com.stockearte.model.UserProto.User.class,
      responseType = com.stockearte.model.UserProto.User.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User,
      com.stockearte.model.UserProto.User> getGetUserMethod() {
    io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User, com.stockearte.model.UserProto.User> getGetUserMethod;
    if ((getGetUserMethod = UsersServiceGrpc.getGetUserMethod) == null) {
      synchronized (UsersServiceGrpc.class) {
        if ((getGetUserMethod = UsersServiceGrpc.getGetUserMethod) == null) {
          UsersServiceGrpc.getGetUserMethod = getGetUserMethod =
              io.grpc.MethodDescriptor.<com.stockearte.model.UserProto.User, com.stockearte.model.UserProto.User>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "GetUser"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.stockearte.model.UserProto.User.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.stockearte.model.UserProto.User.getDefaultInstance()))
              .setSchemaDescriptor(new UsersServiceMethodDescriptorSupplier("GetUser"))
              .build();
        }
      }
    }
    return getGetUserMethod;
  }

  private static volatile io.grpc.MethodDescriptor<com.google.protobuf.Empty,
      com.stockearte.model.UserProto.Users> getFindAllMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "FindAll",
      requestType = com.google.protobuf.Empty.class,
      responseType = com.stockearte.model.UserProto.Users.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<com.google.protobuf.Empty,
      com.stockearte.model.UserProto.Users> getFindAllMethod() {
    io.grpc.MethodDescriptor<com.google.protobuf.Empty, com.stockearte.model.UserProto.Users> getFindAllMethod;
    if ((getFindAllMethod = UsersServiceGrpc.getFindAllMethod) == null) {
      synchronized (UsersServiceGrpc.class) {
        if ((getFindAllMethod = UsersServiceGrpc.getFindAllMethod) == null) {
          UsersServiceGrpc.getFindAllMethod = getFindAllMethod =
              io.grpc.MethodDescriptor.<com.google.protobuf.Empty, com.stockearte.model.UserProto.Users>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "FindAll"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.google.protobuf.Empty.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.stockearte.model.UserProto.Users.getDefaultInstance()))
              .setSchemaDescriptor(new UsersServiceMethodDescriptorSupplier("FindAll"))
              .build();
        }
      }
    }
    return getFindAllMethod;
  }

  private static volatile io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User,
      com.stockearte.model.UserProto.User> getAddUserMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "AddUser",
      requestType = com.stockearte.model.UserProto.User.class,
      responseType = com.stockearte.model.UserProto.User.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User,
      com.stockearte.model.UserProto.User> getAddUserMethod() {
    io.grpc.MethodDescriptor<com.stockearte.model.UserProto.User, com.stockearte.model.UserProto.User> getAddUserMethod;
    if ((getAddUserMethod = UsersServiceGrpc.getAddUserMethod) == null) {
      synchronized (UsersServiceGrpc.class) {
        if ((getAddUserMethod = UsersServiceGrpc.getAddUserMethod) == null) {
          UsersServiceGrpc.getAddUserMethod = getAddUserMethod =
              io.grpc.MethodDescriptor.<com.stockearte.model.UserProto.User, com.stockearte.model.UserProto.User>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "AddUser"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.stockearte.model.UserProto.User.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  com.stockearte.model.UserProto.User.getDefaultInstance()))
              .setSchemaDescriptor(new UsersServiceMethodDescriptorSupplier("AddUser"))
              .build();
        }
      }
    }
    return getAddUserMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static UsersServiceStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<UsersServiceStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<UsersServiceStub>() {
        @java.lang.Override
        public UsersServiceStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new UsersServiceStub(channel, callOptions);
        }
      };
    return UsersServiceStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static UsersServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<UsersServiceBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<UsersServiceBlockingStub>() {
        @java.lang.Override
        public UsersServiceBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new UsersServiceBlockingStub(channel, callOptions);
        }
      };
    return UsersServiceBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static UsersServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<UsersServiceFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<UsersServiceFutureStub>() {
        @java.lang.Override
        public UsersServiceFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new UsersServiceFutureStub(channel, callOptions);
        }
      };
    return UsersServiceFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void validateUser(com.stockearte.model.UserProto.User request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getValidateUserMethod(), responseObserver);
    }

    /**
     */
    default void getUser(com.stockearte.model.UserProto.User request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getGetUserMethod(), responseObserver);
    }

    /**
     */
    default void findAll(com.google.protobuf.Empty request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.Users> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getFindAllMethod(), responseObserver);
    }

    /**
     */
    default void addUser(com.stockearte.model.UserProto.User request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAddUserMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service UsersService.
   */
  public static abstract class UsersServiceImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return UsersServiceGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service UsersService.
   */
  public static final class UsersServiceStub
      extends io.grpc.stub.AbstractAsyncStub<UsersServiceStub> {
    private UsersServiceStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected UsersServiceStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new UsersServiceStub(channel, callOptions);
    }

    /**
     */
    public void validateUser(com.stockearte.model.UserProto.User request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getValidateUserMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void getUser(com.stockearte.model.UserProto.User request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getGetUserMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void findAll(com.google.protobuf.Empty request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.Users> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getFindAllMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void addUser(com.stockearte.model.UserProto.User request,
        io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAddUserMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service UsersService.
   */
  public static final class UsersServiceBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<UsersServiceBlockingStub> {
    private UsersServiceBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected UsersServiceBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new UsersServiceBlockingStub(channel, callOptions);
    }

    /**
     */
    public com.stockearte.model.UserProto.User validateUser(com.stockearte.model.UserProto.User request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getValidateUserMethod(), getCallOptions(), request);
    }

    /**
     */
    public com.stockearte.model.UserProto.User getUser(com.stockearte.model.UserProto.User request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getGetUserMethod(), getCallOptions(), request);
    }

    /**
     */
    public com.stockearte.model.UserProto.Users findAll(com.google.protobuf.Empty request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getFindAllMethod(), getCallOptions(), request);
    }

    /**
     */
    public com.stockearte.model.UserProto.User addUser(com.stockearte.model.UserProto.User request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAddUserMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service UsersService.
   */
  public static final class UsersServiceFutureStub
      extends io.grpc.stub.AbstractFutureStub<UsersServiceFutureStub> {
    private UsersServiceFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected UsersServiceFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new UsersServiceFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.stockearte.model.UserProto.User> validateUser(
        com.stockearte.model.UserProto.User request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getValidateUserMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.stockearte.model.UserProto.User> getUser(
        com.stockearte.model.UserProto.User request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getGetUserMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.stockearte.model.UserProto.Users> findAll(
        com.google.protobuf.Empty request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getFindAllMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.stockearte.model.UserProto.User> addUser(
        com.stockearte.model.UserProto.User request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAddUserMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_VALIDATE_USER = 0;
  private static final int METHODID_GET_USER = 1;
  private static final int METHODID_FIND_ALL = 2;
  private static final int METHODID_ADD_USER = 3;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AsyncService serviceImpl;
    private final int methodId;

    MethodHandlers(AsyncService serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_VALIDATE_USER:
          serviceImpl.validateUser((com.stockearte.model.UserProto.User) request,
              (io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User>) responseObserver);
          break;
        case METHODID_GET_USER:
          serviceImpl.getUser((com.stockearte.model.UserProto.User) request,
              (io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User>) responseObserver);
          break;
        case METHODID_FIND_ALL:
          serviceImpl.findAll((com.google.protobuf.Empty) request,
              (io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.Users>) responseObserver);
          break;
        case METHODID_ADD_USER:
          serviceImpl.addUser((com.stockearte.model.UserProto.User) request,
              (io.grpc.stub.StreamObserver<com.stockearte.model.UserProto.User>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  public static final io.grpc.ServerServiceDefinition bindService(AsyncService service) {
    return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
        .addMethod(
          getValidateUserMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              com.stockearte.model.UserProto.User,
              com.stockearte.model.UserProto.User>(
                service, METHODID_VALIDATE_USER)))
        .addMethod(
          getGetUserMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              com.stockearte.model.UserProto.User,
              com.stockearte.model.UserProto.User>(
                service, METHODID_GET_USER)))
        .addMethod(
          getFindAllMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              com.google.protobuf.Empty,
              com.stockearte.model.UserProto.Users>(
                service, METHODID_FIND_ALL)))
        .addMethod(
          getAddUserMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              com.stockearte.model.UserProto.User,
              com.stockearte.model.UserProto.User>(
                service, METHODID_ADD_USER)))
        .build();
  }

  private static abstract class UsersServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    UsersServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return com.stockearte.model.UserProto.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("UsersService");
    }
  }

  private static final class UsersServiceFileDescriptorSupplier
      extends UsersServiceBaseDescriptorSupplier {
    UsersServiceFileDescriptorSupplier() {}
  }

  private static final class UsersServiceMethodDescriptorSupplier
      extends UsersServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final java.lang.String methodName;

    UsersServiceMethodDescriptorSupplier(java.lang.String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (UsersServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new UsersServiceFileDescriptorSupplier())
              .addMethod(getValidateUserMethod())
              .addMethod(getGetUserMethod())
              .addMethod(getFindAllMethod())
              .addMethod(getAddUserMethod())
              .build();
        }
      }
    }
    return result;
  }
}
