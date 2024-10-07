# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: purchaseOrder.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'purchaseOrder.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import store_pb2 as store__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13purchaseOrder.proto\x12\x05model\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0bstore.proto\"M\n\x0ePurchaseOrders\x12;\n\x15purchaseOrderWithItem\x18\x01 \x03(\x0b\x32\x1c.model.PurchaseOrderWithItem\"C\n\x17PurchaseAndStoreRequest\x12\x17\n\x0fidPurchaseOrder\x18\x01 \x01(\x05\x12\x0f\n\x07idStore\x18\x02 \x01(\x05\"\xae\x01\n\rPurchaseOrder\x12\x17\n\x0fidPurchaseOrder\x18\x01 \x01(\x05\x12\x13\n\x0bobservation\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x11\n\tcreatedAt\x18\x04 \x01(\t\x12\x19\n\x11purchaseOrderDate\x18\x05 \x01(\t\x12\x15\n\rreceptionDate\x18\x06 \x01(\t\x12\x1b\n\x05store\x18\x08 \x01(\x0b\x32\x0c.model.Store\"\xd2\x01\n\x15PurchaseOrderWithItem\x12\x17\n\x0fidPurchaseOrder\x18\x01 \x01(\x05\x12\x13\n\x0bobservation\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x11\n\tcreatedAt\x18\x04 \x01(\t\x12\x19\n\x11purchaseOrderDate\x18\x05 \x01(\t\x12\x15\n\rreceptionDate\x18\x06 \x01(\t\x12\x1b\n\x05store\x18\x08 \x01(\x0b\x32\x0c.model.Store\x12\x1a\n\x05items\x18\t \x03(\x0b\x32\x0b.model.Item\"f\n\x04Item\x12\x13\n\x0bidOrderItem\x18\x01 \x01(\x05\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\t\x12\x17\n\x0frequestedAmount\x18\x05 \x01(\x05\x32\xa9\x02\n\x14PurchaseOrderService\x12H\n\x10GetPurchaseOrder\x12\x14.model.PurchaseOrder\x1a\x1c.model.PurchaseOrderWithItem\"\x00\x12:\n\x07\x46indAll\x12\x16.google.protobuf.Empty\x1a\x15.model.PurchaseOrders\"\x00\x12@\n\x10\x41\x64\x64PurchaseOrder\x12\x14.model.PurchaseOrder\x1a\x14.model.PurchaseOrder\"\x00\x12I\n\x0e\x46indAllByStore\x12\x1e.model.PurchaseAndStoreRequest\x1a\x15.model.PurchaseOrders\"\x00\x42*\n\x14\x63om.stockearte.modelB\x12PurchaseOrderProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'purchaseOrder_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.stockearte.modelB\022PurchaseOrderProto'
  _globals['_PURCHASEORDERS']._serialized_start=104
  _globals['_PURCHASEORDERS']._serialized_end=181
  _globals['_PURCHASEANDSTOREREQUEST']._serialized_start=183
  _globals['_PURCHASEANDSTOREREQUEST']._serialized_end=250
  _globals['_PURCHASEORDER']._serialized_start=253
  _globals['_PURCHASEORDER']._serialized_end=427
  _globals['_PURCHASEORDERWITHITEM']._serialized_start=430
  _globals['_PURCHASEORDERWITHITEM']._serialized_end=640
  _globals['_ITEM']._serialized_start=642
  _globals['_ITEM']._serialized_end=744
  _globals['_PURCHASEORDERSERVICE']._serialized_start=747
  _globals['_PURCHASEORDERSERVICE']._serialized_end=1044
# @@protoc_insertion_point(module_scope)