from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
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

class PurchaseAndStoreRequest(_message.Message):
    __slots__ = ("idPurchaseOrder", "idStore", "state")
    IDPURCHASEORDER_FIELD_NUMBER: _ClassVar[int]
    IDSTORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    idPurchaseOrder: int
    idStore: int
    state: str
    def __init__(self, idPurchaseOrder: _Optional[int] = ..., idStore: _Optional[int] = ..., state: _Optional[str] = ...) -> None: ...

class PurchaseOrder(_message.Message):
    __slots__ = ("idPurchaseOrder", "observation", "state", "createdAt", "purchaseOrderDate", "receptionDate", "store", "idDispatchOrder")
    IDPURCHASEORDER_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    PURCHASEORDERDATE_FIELD_NUMBER: _ClassVar[int]
    RECEPTIONDATE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    IDDISPATCHORDER_FIELD_NUMBER: _ClassVar[int]
    idPurchaseOrder: int
    observation: str
    state: str
    createdAt: str
    purchaseOrderDate: str
    receptionDate: str
    store: _store_pb2.Store
    idDispatchOrder: int
    def __init__(self, idPurchaseOrder: _Optional[int] = ..., observation: _Optional[str] = ..., state: _Optional[str] = ..., createdAt: _Optional[str] = ..., purchaseOrderDate: _Optional[str] = ..., receptionDate: _Optional[str] = ..., store: _Optional[_Union[_store_pb2.Store, _Mapping]] = ..., idDispatchOrder: _Optional[int] = ...) -> None: ...

class PurchaseOrderWithItem(_message.Message):
    __slots__ = ("idPurchaseOrder", "observation", "state", "createdAt", "purchaseOrderDate", "receptionDate", "store", "items", "idDispatchOrder")
    IDPURCHASEORDER_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    PURCHASEORDERDATE_FIELD_NUMBER: _ClassVar[int]
    RECEPTIONDATE_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    IDDISPATCHORDER_FIELD_NUMBER: _ClassVar[int]
    idPurchaseOrder: int
    observation: str
    state: str
    createdAt: str
    purchaseOrderDate: str
    receptionDate: str
    store: _store_pb2.Store
    items: _containers.RepeatedCompositeFieldContainer[Item]
    idDispatchOrder: int
    def __init__(self, idPurchaseOrder: _Optional[int] = ..., observation: _Optional[str] = ..., state: _Optional[str] = ..., createdAt: _Optional[str] = ..., purchaseOrderDate: _Optional[str] = ..., receptionDate: _Optional[str] = ..., store: _Optional[_Union[_store_pb2.Store, _Mapping]] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., idDispatchOrder: _Optional[int] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("idOrderItem", "productCode", "color", "size", "requestedAmount", "send")
    IDORDERITEM_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUESTEDAMOUNT_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    idOrderItem: int
    productCode: str
    color: str
    size: str
    requestedAmount: int
    send: bool
    def __init__(self, idOrderItem: _Optional[int] = ..., productCode: _Optional[str] = ..., color: _Optional[str] = ..., size: _Optional[str] = ..., requestedAmount: _Optional[int] = ..., send: bool = ...) -> None: ...
