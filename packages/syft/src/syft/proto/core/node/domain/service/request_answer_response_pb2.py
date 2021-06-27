# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/domain/service/request_answer_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/core/node/domain/service/request_answer_response.proto',
  package='syft.core.node.domain.service',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n<proto/core/node/domain/service/request_answer_response.proto\x12\x1dsyft.core.node.domain.service\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto\"z\n\x15RequestAnswerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\nrequest_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3'
  ,
  dependencies=[proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,])




_REQUESTANSWERRESPONSE = _descriptor.Descriptor(
  name='RequestAnswerResponse',
  full_name='syft.core.node.domain.service.RequestAnswerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='syft.core.node.domain.service.RequestAnswerResponse.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='syft.core.node.domain.service.RequestAnswerResponse.request_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.core.node.domain.service.RequestAnswerResponse.address', index=2,
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
  serialized_start=163,
  serialized_end=285,
)

_REQUESTANSWERRESPONSE.fields_by_name['request_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_REQUESTANSWERRESPONSE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name['RequestAnswerResponse'] = _REQUESTANSWERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestAnswerResponse = _reflection.GeneratedProtocolMessageType('RequestAnswerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTANSWERRESPONSE,
  '__module__' : 'proto.core.node.domain.service.request_answer_response_pb2'
  # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.RequestAnswerResponse)
  })
_sym_db.RegisterMessage(RequestAnswerResponse)


# @@protoc_insertion_point(module_scope)
