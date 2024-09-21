from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Products(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, product: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

class Product(_message.Message):
    __slots__ = ("idProduct", "product", "code", "color", "size", "img", "stock", "enabled")
    IDPRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IMG_FIELD_NUMBER: _ClassVar[int]
    STOCK_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    idProduct: int
    product: str
    code: str
    color: str
    size: str
    img: str
    stock: int
    enabled: bool
    def __init__(self, idProduct: _Optional[int] = ..., product: _Optional[str] = ..., code: _Optional[str] = ..., color: _Optional[str] = ..., size: _Optional[str] = ..., img: _Optional[str] = ..., stock: _Optional[int] = ..., enabled: bool = ...) -> None: ...
