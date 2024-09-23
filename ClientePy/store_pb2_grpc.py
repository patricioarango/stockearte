# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import store_pb2 as store__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in store_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StoreServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStore = channel.unary_unary(
                '/model.StoreService/GetStore',
                request_serializer=store__pb2.Store.SerializeToString,
                response_deserializer=store__pb2.Store.FromString,
                _registered_method=True)
        self.FindAll = channel.unary_unary(
                '/model.StoreService/FindAll',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=store__pb2.Stores.FromString,
                _registered_method=True)
        self.SaveStore = channel.unary_unary(
                '/model.StoreService/SaveStore',
                request_serializer=store__pb2.Store.SerializeToString,
                response_deserializer=store__pb2.Store.FromString,
                _registered_method=True)


class StoreServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveStore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StoreServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStore': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStore,
                    request_deserializer=store__pb2.Store.FromString,
                    response_serializer=store__pb2.Store.SerializeToString,
            ),
            'FindAll': grpc.unary_unary_rpc_method_handler(
                    servicer.FindAll,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=store__pb2.Stores.SerializeToString,
            ),
            'SaveStore': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveStore,
                    request_deserializer=store__pb2.Store.FromString,
                    response_serializer=store__pb2.Store.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'model.StoreService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('model.StoreService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StoreService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model.StoreService/GetStore',
            store__pb2.Store.SerializeToString,
            store__pb2.Store.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def FindAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model.StoreService/FindAll',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            store__pb2.Stores.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SaveStore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/model.StoreService/SaveStore',
            store__pb2.Store.SerializeToString,
            store__pb2.Store.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)