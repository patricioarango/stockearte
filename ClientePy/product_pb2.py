# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: product.proto
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
    'product.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproduct.proto\x12\x05model\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\"#\n\x11\x46indProductSearch\x12\x0e\n\x06search\x18\x01 \x01(\t\"\"\n\x12ProductCodeRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"\x1f\n\x0cStoreRequest\x12\x0f\n\x07idStore\x18\x01 \x01(\x05\"+\n\x08Products\x12\x1f\n\x07product\x18\x01 \x03(\x0b\x32\x0e.model.Product\"v\n\x07Product\x12\x11\n\tidProduct\x18\x01 \x01(\x05\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\t\x12\x0b\n\x03img\x18\x06 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x07 \x01(\x08\x32\xe9\x02\n\x0eProductService\x12.\n\nGetProduct\x12\x0e.model.Product\x1a\x0e.model.Product\"\x00\x12\x34\n\x07\x46indAll\x12\x16.google.protobuf.Empty\x1a\x0f.model.Products\"\x00\x12/\n\x0bSaveProduct\x12\x0e.model.Product\x1a\x0e.model.Product\"\x00\x12=\n\x13\x46indProductsByStore\x12\x13.model.StoreRequest\x1a\x0f.model.Products\"\x00\x12@\n\x11\x46indProductByCode\x12\x19.model.ProductCodeRequest\x1a\x0e.model.Product\"\x00\x12?\n\x10\x66indByAttributes\x12\x18.model.FindProductSearch\x1a\x0f.model.Products\"\x00\x42$\n\x14\x63om.stockearte.modelB\x0cProductProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.stockearte.modelB\014ProductProto'
  _globals['_FINDPRODUCTSEARCH']._serialized_start=85
  _globals['_FINDPRODUCTSEARCH']._serialized_end=120
  _globals['_PRODUCTCODEREQUEST']._serialized_start=122
  _globals['_PRODUCTCODEREQUEST']._serialized_end=156
  _globals['_STOREREQUEST']._serialized_start=158
  _globals['_STOREREQUEST']._serialized_end=189
  _globals['_PRODUCTS']._serialized_start=191
  _globals['_PRODUCTS']._serialized_end=234
  _globals['_PRODUCT']._serialized_start=236
  _globals['_PRODUCT']._serialized_end=354
  _globals['_PRODUCTSERVICE']._serialized_start=357
  _globals['_PRODUCTSERVICE']._serialized_end=718
# @@protoc_insertion_point(module_scope)
