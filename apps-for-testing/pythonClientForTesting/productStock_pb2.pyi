from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import store_pb2 as _store_pb2
import product_pb2 as _product_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductsStock(_message.Message):
    __slots__ = ("productStock",)
    PRODUCTSTOCK_FIELD_NUMBER: _ClassVar[int]
    productStock: _containers.RepeatedCompositeFieldContainer[ProductStock]
    def __init__(self, productStock: _Optional[_Iterable[_Union[ProductStock, _Mapping]]] = ...) -> None: ...

class ProductAndStoreRequest(_message.Message):
    __slots__ = ("idProduct", "idStore")
    IDPRODUCT_FIELD_NUMBER: _ClassVar[int]
    IDSTORE_FIELD_NUMBER: _ClassVar[int]
    idProduct: int
    idStore: int
    def __init__(self, idProduct: _Optional[int] = ..., idStore: _Optional[int] = ...) -> None: ...

class ProductStock(_message.Message):
    __slots__ = ("idProductStock", "stock", "product", "store")
    IDPRODUCTSTOCK_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    idProductStock: int
    stock: int
    product: _product_pb2.Product
    store: _store_pb2.Store
    def __init__(self, idProductStock: _Optional[int] = ..., stock: _Optional[int] = ..., product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ..., store: _Optional[_Union[_store_pb2.Store, _Mapping]] = ...) -> None: ...
