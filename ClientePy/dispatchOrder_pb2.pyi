from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DispatchOrder(_message.Message):
    __slots__ = ("idDispatchOrder", "idPurchaseOrder", "estimatedShippingDate")
    IDDISPATCHORDER_FIELD_NUMBER: _ClassVar[int]
    IDPURCHASEORDER_FIELD_NUMBER: _ClassVar[int]
    ESTIMATEDSHIPPINGDATE_FIELD_NUMBER: _ClassVar[int]
    idDispatchOrder: int
    idPurchaseOrder: int
    estimatedShippingDate: str
    def __init__(self, idDispatchOrder: _Optional[int] = ..., idPurchaseOrder: _Optional[int] = ..., estimatedShippingDate: _Optional[str] = ...) -> None: ...
