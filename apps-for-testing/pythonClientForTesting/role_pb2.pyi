from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Roles(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: _containers.RepeatedCompositeFieldContainer[Role]
    def __init__(self, role: _Optional[_Iterable[_Union[Role, _Mapping]]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("idRole", "roleName")
    IDROLE_FIELD_NUMBER: _ClassVar[int]
    ROLENAME_FIELD_NUMBER: _ClassVar[int]
    idRole: int
    roleName: str
    def __init__(self, idRole: _Optional[int] = ..., roleName: _Optional[str] = ...) -> None: ...
