# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/torch/tensor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.lib.torch import device_pb2 as proto_dot_lib_dot_torch_dot_device__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/lib/torch/tensor.proto',
  package='syft.lib.torch',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cproto/lib/torch/tensor.proto\x12\x0esyft.lib.torch\x1a\x1cproto/lib/torch/device.proto\"\xe1\x02\n\x0fProtobufContent\x12\r\n\x05shape\x18\x01 \x03(\x03\x12\x16\n\x0e\x63ontents_uint8\x18\x10 \x03(\r\x12\x15\n\rcontents_int8\x18\x11 \x03(\x05\x12\x16\n\x0e\x63ontents_int16\x18\x12 \x03(\x05\x12\x16\n\x0e\x63ontents_int32\x18\x13 \x03(\x05\x12\x16\n\x0e\x63ontents_int64\x18\x14 \x03(\x03\x12\x18\n\x10\x63ontents_float16\x18\x15 \x03(\x02\x12\x18\n\x10\x63ontents_float32\x18\x16 \x03(\x02\x12\x18\n\x10\x63ontents_float64\x18\x17 \x03(\x01\x12\x15\n\rcontents_bool\x18\x18 \x03(\x08\x12\x16\n\x0e\x63ontents_qint8\x18\x19 \x03(\x11\x12\x17\n\x0f\x63ontents_quint8\x18\x1a \x03(\r\x12\x17\n\x0f\x63ontents_qint32\x18\x1b \x03(\x11\x12\x19\n\x11\x63ontents_bfloat16\x18\x1c \x03(\x02\"\x88\x01\n\nTensorData\x12\x14\n\x0cis_quantized\x18\x01 \x01(\x08\x12\r\n\x05scale\x18\x02 \x01(\x02\x12\x12\n\nzero_point\x18\x03 \x01(\x05\x12\x14\n\nproto_data\x18\x04 \x01(\x0cH\x00\x12\x14\n\narrow_data\x18\x05 \x01(\x0cH\x00\x12\r\n\x05\x64type\x18\x06 \x01(\tB\x06\n\x04\x64\x61ta\"j\n\x0bTensorProto\x12\x0e\n\x06tensor\x18\x01 \x01(\x0c\x12\x15\n\rrequires_grad\x18\x02 \x01(\x08\x12\x0c\n\x04grad\x18\x03 \x01(\x0c\x12&\n\x06\x64\x65vice\x18\x04 \x01(\x0b\x32\x16.syft.lib.torch.Deviceb\x06proto3'
  ,
  dependencies=[proto_dot_lib_dot_torch_dot_device__pb2.DESCRIPTOR,])




_PROTOBUFCONTENT = _descriptor.Descriptor(
  name='ProtobufContent',
  full_name='syft.lib.torch.ProtobufContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='syft.lib.torch.ProtobufContent.shape', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_uint8', full_name='syft.lib.torch.ProtobufContent.contents_uint8', index=1,
      number=16, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_int8', full_name='syft.lib.torch.ProtobufContent.contents_int8', index=2,
      number=17, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_int16', full_name='syft.lib.torch.ProtobufContent.contents_int16', index=3,
      number=18, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_int32', full_name='syft.lib.torch.ProtobufContent.contents_int32', index=4,
      number=19, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_int64', full_name='syft.lib.torch.ProtobufContent.contents_int64', index=5,
      number=20, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_float16', full_name='syft.lib.torch.ProtobufContent.contents_float16', index=6,
      number=21, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_float32', full_name='syft.lib.torch.ProtobufContent.contents_float32', index=7,
      number=22, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_float64', full_name='syft.lib.torch.ProtobufContent.contents_float64', index=8,
      number=23, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_bool', full_name='syft.lib.torch.ProtobufContent.contents_bool', index=9,
      number=24, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_qint8', full_name='syft.lib.torch.ProtobufContent.contents_qint8', index=10,
      number=25, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_quint8', full_name='syft.lib.torch.ProtobufContent.contents_quint8', index=11,
      number=26, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_qint32', full_name='syft.lib.torch.ProtobufContent.contents_qint32', index=12,
      number=27, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents_bfloat16', full_name='syft.lib.torch.ProtobufContent.contents_bfloat16', index=13,
      number=28, type=2, cpp_type=6, label=3,
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
  serialized_start=79,
  serialized_end=432,
)


_TENSORDATA = _descriptor.Descriptor(
  name='TensorData',
  full_name='syft.lib.torch.TensorData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_quantized', full_name='syft.lib.torch.TensorData.is_quantized', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scale', full_name='syft.lib.torch.TensorData.scale', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zero_point', full_name='syft.lib.torch.TensorData.zero_point', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proto_data', full_name='syft.lib.torch.TensorData.proto_data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arrow_data', full_name='syft.lib.torch.TensorData.arrow_data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='syft.lib.torch.TensorData.dtype', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='data', full_name='syft.lib.torch.TensorData.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=435,
  serialized_end=571,
)


_TENSORPROTO = _descriptor.Descriptor(
  name='TensorProto',
  full_name='syft.lib.torch.TensorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor', full_name='syft.lib.torch.TensorProto.tensor', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requires_grad', full_name='syft.lib.torch.TensorProto.requires_grad', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grad', full_name='syft.lib.torch.TensorProto.grad', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device', full_name='syft.lib.torch.TensorProto.device', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=573,
  serialized_end=679,
)

_TENSORDATA.oneofs_by_name['data'].fields.append(
  _TENSORDATA.fields_by_name['proto_data'])
_TENSORDATA.fields_by_name['proto_data'].containing_oneof = _TENSORDATA.oneofs_by_name['data']
_TENSORDATA.oneofs_by_name['data'].fields.append(
  _TENSORDATA.fields_by_name['arrow_data'])
_TENSORDATA.fields_by_name['arrow_data'].containing_oneof = _TENSORDATA.oneofs_by_name['data']
_TENSORPROTO.fields_by_name['device'].message_type = proto_dot_lib_dot_torch_dot_device__pb2._DEVICE
DESCRIPTOR.message_types_by_name['ProtobufContent'] = _PROTOBUFCONTENT
DESCRIPTOR.message_types_by_name['TensorData'] = _TENSORDATA
DESCRIPTOR.message_types_by_name['TensorProto'] = _TENSORPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtobufContent = _reflection.GeneratedProtocolMessageType('ProtobufContent', (_message.Message,), {
  'DESCRIPTOR' : _PROTOBUFCONTENT,
  '__module__' : 'proto.lib.torch.tensor_pb2'
  # @@protoc_insertion_point(class_scope:syft.lib.torch.ProtobufContent)
  })
_sym_db.RegisterMessage(ProtobufContent)

TensorData = _reflection.GeneratedProtocolMessageType('TensorData', (_message.Message,), {
  'DESCRIPTOR' : _TENSORDATA,
  '__module__' : 'proto.lib.torch.tensor_pb2'
  # @@protoc_insertion_point(class_scope:syft.lib.torch.TensorData)
  })
_sym_db.RegisterMessage(TensorData)

TensorProto = _reflection.GeneratedProtocolMessageType('TensorProto', (_message.Message,), {
  'DESCRIPTOR' : _TENSORPROTO,
  '__module__' : 'proto.lib.torch.tensor_pb2'
  # @@protoc_insertion_point(class_scope:syft.lib.torch.TensorProto)
  })
_sym_db.RegisterMessage(TensorProto)


# @@protoc_insertion_point(module_scope)
