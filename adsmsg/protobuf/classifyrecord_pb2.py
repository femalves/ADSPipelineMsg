# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: classifyrecord.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='classifyrecord.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x63lassifyrecord.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\"\x89\x02\n\x15\x43lassifyRequestRecord\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12\x0f\n\x07scix_id\x18\x02 \x01(\t\x12\x1e\n\x06status\x18\x03 \x01(\x0e\x32\x0e.adsmsg.Status\x12\r\n\x05title\x18\x04 \x01(\t\x12\x10\n\x08\x61\x62stract\x18\x05 \x01(\t\x12\x16\n\x0eoperation_step\x18\x06 \x01(\t\x12\x0e\n\x06run_id\x18\x07 \x01(\x04\x12\x10\n\x08override\x18\x08 \x03(\t\x12\x13\n\x0boutput_path\x18\t \x01(\t\x12\x0e\n\x06scores\x18\n \x03(\x01\x12\x13\n\x0b\x63ollections\x18\x0b \x03(\t\x12\x19\n\x11\x63ollection_scores\x18\x0c \x03(\x01\"u\n\x19\x43lassifyRequestRecordList\x12\x38\n\x11\x63lassify_requests\x18\x01 \x03(\x0b\x32\x1d.adsmsg.ClassifyRequestRecord\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.adsmsg.Status\"o\n\x16\x43lassifyResponseRecord\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12\x0f\n\x07scix_id\x18\x02 \x01(\t\x12\x1e\n\x06status\x18\x03 \x01(\x0e\x32\x0e.adsmsg.Status\x12\x13\n\x0b\x63ollections\x18\x04 \x03(\t\"x\n\x1a\x43lassifyResponseRecordList\x12:\n\x12\x63lassify_responses\x18\x01 \x03(\x0b\x32\x1e.adsmsg.ClassifyResponseRecord\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.adsmsg.Statusb\x06proto3'
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_CLASSIFYREQUESTRECORD = _descriptor.Descriptor(
  name='ClassifyRequestRecord',
  full_name='adsmsg.ClassifyRequestRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.ClassifyRequestRecord.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scix_id', full_name='adsmsg.ClassifyRequestRecord.scix_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.ClassifyRequestRecord.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='adsmsg.ClassifyRequestRecord.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='abstract', full_name='adsmsg.ClassifyRequestRecord.abstract', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation_step', full_name='adsmsg.ClassifyRequestRecord.operation_step', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='run_id', full_name='adsmsg.ClassifyRequestRecord.run_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='override', full_name='adsmsg.ClassifyRequestRecord.override', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_path', full_name='adsmsg.ClassifyRequestRecord.output_path', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scores', full_name='adsmsg.ClassifyRequestRecord.scores', index=9,
      number=10, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collections', full_name='adsmsg.ClassifyRequestRecord.collections', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collection_scores', full_name='adsmsg.ClassifyRequestRecord.collection_scores', index=11,
      number=12, type=1, cpp_type=5, label=3,
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
  serialized_start=47,
  serialized_end=312,
)


_CLASSIFYREQUESTRECORDLIST = _descriptor.Descriptor(
  name='ClassifyRequestRecordList',
  full_name='adsmsg.ClassifyRequestRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classify_requests', full_name='adsmsg.ClassifyRequestRecordList.classify_requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.ClassifyRequestRecordList.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=314,
  serialized_end=431,
)


_CLASSIFYRESPONSERECORD = _descriptor.Descriptor(
  name='ClassifyResponseRecord',
  full_name='adsmsg.ClassifyResponseRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.ClassifyResponseRecord.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scix_id', full_name='adsmsg.ClassifyResponseRecord.scix_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.ClassifyResponseRecord.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='collections', full_name='adsmsg.ClassifyResponseRecord.collections', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=433,
  serialized_end=544,
)


_CLASSIFYRESPONSERECORDLIST = _descriptor.Descriptor(
  name='ClassifyResponseRecordList',
  full_name='adsmsg.ClassifyResponseRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='classify_responses', full_name='adsmsg.ClassifyResponseRecordList.classify_responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.ClassifyResponseRecordList.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=546,
  serialized_end=666,
)

_CLASSIFYREQUESTRECORD.fields_by_name['status'].enum_type = status__pb2._STATUS
_CLASSIFYREQUESTRECORDLIST.fields_by_name['classify_requests'].message_type = _CLASSIFYREQUESTRECORD
_CLASSIFYREQUESTRECORDLIST.fields_by_name['status'].enum_type = status__pb2._STATUS
_CLASSIFYRESPONSERECORD.fields_by_name['status'].enum_type = status__pb2._STATUS
_CLASSIFYRESPONSERECORDLIST.fields_by_name['classify_responses'].message_type = _CLASSIFYRESPONSERECORD
_CLASSIFYRESPONSERECORDLIST.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['ClassifyRequestRecord'] = _CLASSIFYREQUESTRECORD
DESCRIPTOR.message_types_by_name['ClassifyRequestRecordList'] = _CLASSIFYREQUESTRECORDLIST
DESCRIPTOR.message_types_by_name['ClassifyResponseRecord'] = _CLASSIFYRESPONSERECORD
DESCRIPTOR.message_types_by_name['ClassifyResponseRecordList'] = _CLASSIFYRESPONSERECORDLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifyRequestRecord = _reflection.GeneratedProtocolMessageType('ClassifyRequestRecord', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYREQUESTRECORD,
  '__module__' : 'classifyrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.ClassifyRequestRecord)
  })
_sym_db.RegisterMessage(ClassifyRequestRecord)

ClassifyRequestRecordList = _reflection.GeneratedProtocolMessageType('ClassifyRequestRecordList', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYREQUESTRECORDLIST,
  '__module__' : 'classifyrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.ClassifyRequestRecordList)
  })
_sym_db.RegisterMessage(ClassifyRequestRecordList)

ClassifyResponseRecord = _reflection.GeneratedProtocolMessageType('ClassifyResponseRecord', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYRESPONSERECORD,
  '__module__' : 'classifyrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.ClassifyResponseRecord)
  })
_sym_db.RegisterMessage(ClassifyResponseRecord)

ClassifyResponseRecordList = _reflection.GeneratedProtocolMessageType('ClassifyResponseRecordList', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYRESPONSERECORDLIST,
  '__module__' : 'classifyrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.ClassifyResponseRecordList)
  })
_sym_db.RegisterMessage(ClassifyResponseRecordList)


# @@protoc_insertion_point(module_scope)
