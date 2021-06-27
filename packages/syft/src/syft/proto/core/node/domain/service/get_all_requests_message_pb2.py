# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/domain/service/get_all_requests_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.node.domain.service import request_message_pb2 as proto_dot_core_dot_node_dot_domain_dot_service_dot_request__message__pb2
from syft.proto.core.common import common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/core/node/domain/service/get_all_requests_message.proto',
  package='syft.core.node.domain.service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=proto/core/node/domain/service/get_all_requests_message.proto\x12\x1dsyft.core.node.domain.service\x1a\x34proto/core/node/domain/service/request_message.proto\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto\"\x8f\x01\n\x15GetAllRequestsMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\"\xaf\x01\n\x1dGetAllRequestsResponseMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12?\n\x08requests\x18\x03 \x03(\x0b\x32-.syft.core.node.domain.service.RequestMessageb\x06proto3'
  ,
  dependencies=[proto_dot_core_dot_node_dot_domain_dot_service_dot_request__message__pb2.DESCRIPTOR,proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,])




_GETALLREQUESTSMESSAGE = _descriptor.Descriptor(
  name='GetAllRequestsMessage',
  full_name='syft.core.node.domain.service.GetAllRequestsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.core.node.domain.service.GetAllRequestsMessage.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.core.node.domain.service.GetAllRequestsMessage.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply_to', full_name='syft.core.node.domain.service.GetAllRequestsMessage.reply_to', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=362,
)


_GETALLREQUESTSRESPONSEMESSAGE = _descriptor.Descriptor(
  name='GetAllRequestsResponseMessage',
  full_name='syft.core.node.domain.service.GetAllRequestsResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.core.node.domain.service.GetAllRequestsResponseMessage.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.core.node.domain.service.GetAllRequestsResponseMessage.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requests', full_name='syft.core.node.domain.service.GetAllRequestsResponseMessage.requests', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=540,
)

_GETALLREQUESTSMESSAGE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETALLREQUESTSMESSAGE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLREQUESTSMESSAGE.fields_by_name['reply_to'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLREQUESTSRESPONSEMESSAGE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETALLREQUESTSRESPONSEMESSAGE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETALLREQUESTSRESPONSEMESSAGE.fields_by_name['requests'].message_type = proto_dot_core_dot_node_dot_domain_dot_service_dot_request__message__pb2._REQUESTMESSAGE
DESCRIPTOR.message_types_by_name['GetAllRequestsMessage'] = _GETALLREQUESTSMESSAGE
DESCRIPTOR.message_types_by_name['GetAllRequestsResponseMessage'] = _GETALLREQUESTSRESPONSEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAllRequestsMessage = _reflection.GeneratedProtocolMessageType('GetAllRequestsMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETALLREQUESTSMESSAGE,
  '__module__' : 'proto.core.node.domain.service.get_all_requests_message_pb2'
  # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.GetAllRequestsMessage)
  })
_sym_db.RegisterMessage(GetAllRequestsMessage)

GetAllRequestsResponseMessage = _reflection.GeneratedProtocolMessageType('GetAllRequestsResponseMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETALLREQUESTSRESPONSEMESSAGE,
  '__module__' : 'proto.core.node.domain.service.get_all_requests_message_pb2'
  # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.GetAllRequestsResponseMessage)
  })
_sym_db.RegisterMessage(GetAllRequestsResponseMessage)


# @@protoc_insertion_point(module_scope)
