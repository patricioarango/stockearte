from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Stores(_message.Message):
    __slots__ = ("store",)
    STORE_FIELD_NUMBER: _ClassVar[int]
    store: _containers.RepeatedCompositeFieldContainer[Store]
    def __init__(self, store: _Optional[_Iterable[_Union[Store, _Mapping]]] = ...) -> None: ...

class Store(_message.Message):
    __slots__ = ("idStore", "storeName", "code", "address", "city", "state", "enabled")
    IDSTORE_FIELD_NUMBER: _ClassVar[int]
    STORENAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    idStore: int
    storeName: str
    code: str
    address: str
    city: str
    state: str
    enabled: bool
    def __init__(self, idStore: _Optional[int] = ..., storeName: _Optional[str] = ..., code: _Optional[str] = ..., address: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., enabled: bool = ...) -> None: ...
