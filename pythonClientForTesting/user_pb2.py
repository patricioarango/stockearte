# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
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
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"1\n\x0bUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"[\n\tUserReply\x12\x0e\n\x06idUser\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08lastname\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t27\n\x04User\x12/\n\tuserLogin\x12\x11.user.UserRequest\x1a\x0f.user.UserReplyB$\n\x15\x63om.arango.user.stubsB\tUserProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.arango.user.stubsB\tUserProtoP\001'
  _globals['_USERREQUEST']._serialized_start=20
  _globals['_USERREQUEST']._serialized_end=69
  _globals['_USERREPLY']._serialized_start=71
  _globals['_USERREPLY']._serialized_end=162
  _globals['_USER']._serialized_start=164
  _globals['_USER']._serialized_end=219
# @@protoc_insertion_point(module_scope)