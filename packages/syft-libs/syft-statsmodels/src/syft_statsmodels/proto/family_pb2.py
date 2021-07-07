# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/family.proto

# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.lib.python import string_pb2 as proto_dot_lib_dot_python_dot_string__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/family.proto",
    package="statsmodels",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n\x12proto/family.proto\x12\x0bstatsmodels\x1a\x1dproto/lib/python/string.proto\"]\n\x0b\x46\x61milyProto\x12'\n\x06\x66\x61mily\x18\x01 \x01(\x0b\x32\x17.syft.lib.python.String\x12%\n\x04link\x18\x02 \x01(\x0b\x32\x17.syft.lib.python.Stringb\x06proto3",
    dependencies=[
        proto_dot_lib_dot_python_dot_string__pb2.DESCRIPTOR,
    ],
)


_FAMILYPROTO = _descriptor.Descriptor(
    name="FamilyProto",
    full_name="statsmodels.FamilyProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="family",
            full_name="statsmodels.FamilyProto.family",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="link",
            full_name="statsmodels.FamilyProto.link",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=66,
    serialized_end=159,
)

_FAMILYPROTO.fields_by_name[
    "family"
].message_type = proto_dot_lib_dot_python_dot_string__pb2._STRING
_FAMILYPROTO.fields_by_name[
    "link"
].message_type = proto_dot_lib_dot_python_dot_string__pb2._STRING
DESCRIPTOR.message_types_by_name["FamilyProto"] = _FAMILYPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FamilyProto = _reflection.GeneratedProtocolMessageType(
    "FamilyProto",
    (_message.Message,),
    {
        "DESCRIPTOR": _FAMILYPROTO,
        "__module__": "proto.family_pb2"
        # @@protoc_insertion_point(class_scope:statsmodels.FamilyProto)
    },
)
_sym_db.RegisterMessage(FamilyProto)


# @@protoc_insertion_point(module_scope)
