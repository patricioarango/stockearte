from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Novelties(_message.Message):
    __slots__ = ("novelty",)
    NOVELTY_FIELD_NUMBER: _ClassVar[int]
    novelty: _containers.RepeatedCompositeFieldContainer[Novelty]
    def __init__(self, novelty: _Optional[_Iterable[_Union[Novelty, _Mapping]]] = ...) -> None: ...

class Novelty(_message.Message):
    __slots__ = ("idNovelty", "date", "novelty", "code", "color", "size", "img", "saved")
    IDNOVELTY_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    NOVELTY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IMG_FIELD_NUMBER: _ClassVar[int]
    SAVED_FIELD_NUMBER: _ClassVar[int]
    idNovelty: int
    date: str
    novelty: str
    code: str
    color: str
    size: str
    img: str
    saved: bool
    def __init__(self, idNovelty: _Optional[int] = ..., date: _Optional[str] = ..., novelty: _Optional[str] = ..., code: _Optional[str] = ..., color: _Optional[str] = ..., size: _Optional[str] = ..., img: _Optional[str] = ..., saved: bool = ...) -> None: ...
