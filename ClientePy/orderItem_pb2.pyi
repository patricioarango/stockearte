from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
import purchaseOrder_pb2 as _purchaseOrder_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderItems(_message.Message):
    __slots__ = ("orderItem",)
    ORDERITEM_FIELD_NUMBER: _ClassVar[int]
    orderItem: _containers.RepeatedCompositeFieldContainer[OrderItem]
    def __init__(self, orderItem: _Optional[_Iterable[_Union[OrderItem, _Mapping]]] = ...) -> None: ...

class OrderItem(_message.Message):
    __slots__ = ("idOrderItem", "productCode", "color", "size", "requestedAmount", "purchaseOrder", "send")
    IDORDERITEM_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUESTEDAMOUNT_FIELD_NUMBER: _ClassVar[int]
    PURCHASEORDER_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    idOrderItem: int
    productCode: str
    color: str
    size: str
    requestedAmount: int
    purchaseOrder: _purchaseOrder_pb2.PurchaseOrder
    send: bool
    def __init__(self, idOrderItem: _Optional[int] = ..., productCode: _Optional[str] = ..., color: _Optional[str] = ..., size: _Optional[str] = ..., requestedAmount: _Optional[int] = ..., purchaseOrder: _Optional[_Union[_purchaseOrder_pb2.PurchaseOrder, _Mapping]] = ..., send: bool = ...) -> None: ...
