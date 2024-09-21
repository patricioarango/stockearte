from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import store_pb2 as _store_pb2
import role_pb2 as _role_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Users(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, user: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("idUser", "username", "name", "lastname", "password", "role", "store", "enabled")
    IDUSER_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    idUser: int
    username: str
    name: str
    lastname: str
    password: str
    role: _role_pb2.Role
    store: _store_pb2.Store
    enabled: bool
    def __init__(self, idUser: _Optional[int] = ..., username: _Optional[str] = ..., name: _Optional[str] = ..., lastname: _Optional[str] = ..., password: _Optional[str] = ..., role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ..., store: _Optional[_Union[_store_pb2.Store, _Mapping]] = ..., enabled: bool = ...) -> None: ...
