# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fulltext_requests.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fulltext_requests.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x66ulltext_requests.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\"=\n\x10\x46ulltextRequests\x12)\n\x08requests\x18\x01 \x03(\x0b\x32\x17.adsmsg.FulltextRequest\"g\n\x0f\x46ulltextRequest\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12\x10\n\x08provider\x18\x02 \x01(\t\x12\x11\n\tft_source\x18\x03 \x01(\t\x12\x1e\n\x06status\x18\x04 \x01(\x0e\x32\x0e.adsmsg.Statusb\x06proto3'
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_FULLTEXTREQUESTS = _descriptor.Descriptor(
  name='FulltextRequests',
  full_name='adsmsg.FulltextRequests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='adsmsg.FulltextRequests.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=49,
  serialized_end=110,
)


_FULLTEXTREQUEST = _descriptor.Descriptor(
  name='FulltextRequest',
  full_name='adsmsg.FulltextRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.FulltextRequest.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='adsmsg.FulltextRequest.provider', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ft_source', full_name='adsmsg.FulltextRequest.ft_source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.FulltextRequest.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=112,
  serialized_end=215,
)

_FULLTEXTREQUESTS.fields_by_name['requests'].message_type = _FULLTEXTREQUEST
_FULLTEXTREQUEST.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['FulltextRequests'] = _FULLTEXTREQUESTS
DESCRIPTOR.message_types_by_name['FulltextRequest'] = _FULLTEXTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FulltextRequests = _reflection.GeneratedProtocolMessageType('FulltextRequests', (_message.Message,), {
  'DESCRIPTOR' : _FULLTEXTREQUESTS,
  '__module__' : 'fulltext_requests_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.FulltextRequests)
  })
_sym_db.RegisterMessage(FulltextRequests)

FulltextRequest = _reflection.GeneratedProtocolMessageType('FulltextRequest', (_message.Message,), {
  'DESCRIPTOR' : _FULLTEXTREQUEST,
  '__module__' : 'fulltext_requests_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.FulltextRequest)
  })
_sym_db.RegisterMessage(FulltextRequest)


# @@protoc_insertion_point(module_scope)
