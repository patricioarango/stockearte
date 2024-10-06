from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
import store_pb2 as _store_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurchaseOrders(_message.Message):
    __slots__ = ("purchaseOrderWithItem",)
    PURCHASEORDERWITHITEM_FIELD_NUMBER: _ClassVar[int]
    purchaseOrderWithItem: _containers.RepeatedCompositeFieldContainer[PurchaseOrderWithItem]
    def __init__(self, purchaseOrderWithItem: _Optional[_Iterable[_Union[PurchaseOrderWithItem, _Mapping]]] = ...) -> None: ...

class PurchaseOrder(_message.Message):
    __slots__ = ("idPurchaseOrder", "observation", "state", "createdAt", "purchaseOrderDate", "receptionDate", "store")
    IDPURCHASEORDER_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    PURCHASEORDERDATE_FIELD_NUMBER: _ClassVar[int]
    RECEPTIONDATE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    idPurchaseOrder: int
    observation: str
    state: str
    createdAt: _timestamp_pb2.Timestamp
    purchaseOrderDate: _timestamp_pb2.Timestamp
    receptionDate: _timestamp_pb2.Timestamp
    store: _store_pb2.Store
    def __init__(self, idPurchaseOrder: _Optional[int] = ..., observation: _Optional[str] = ..., state: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., purchaseOrderDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., receptionDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., store: _Optional[_Union[_store_pb2.Store, _Mapping]] = ...) -> None: ...

class PurchaseOrderWithItem(_message.Message):
    __slots__ = ("idPurchaseOrder", "observation", "state", "createdAt", "purchaseOrderDate", "receptionDate", "store", "items")
    IDPURCHASEORDER_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    PURCHASEORDERDATE_FIELD_NUMBER: _ClassVar[int]
    RECEPTIONDATE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    idPurchaseOrder: int
    observation: str
    state: str
    createdAt: _timestamp_pb2.Timestamp
    purchaseOrderDate: _timestamp_pb2.Timestamp
    receptionDate: _timestamp_pb2.Timestamp
    store: _store_pb2.Store
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, idPurchaseOrder: _Optional[int] = ..., observation: _Optional[str] = ..., state: _Optional[str] = ..., createdAt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., purchaseOrderDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., receptionDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., store: _Optional[_Union[_store_pb2.Store, _Mapping]] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("idOrderItem", "productCode", "color", "size", "requestedAmount")
    IDORDERITEM_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUESTEDAMOUNT_FIELD_NUMBER: _ClassVar[int]
    idOrderItem: int
    productCode: str
    color: str
    size: str
    requestedAmount: int
    def __init__(self, idOrderItem: _Optional[int] = ..., productCode: _Optional[str] = ..., color: _Optional[str] = ..., size: _Optional[str] = ..., requestedAmount: _Optional[int] = ...) -> None: ...
