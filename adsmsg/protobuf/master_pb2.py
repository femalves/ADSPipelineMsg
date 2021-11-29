# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: master.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='master.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_pb=_b('\n\x0cmaster.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\";\n\x0eLinkTypeRecord\x12\x0b\n\x03url\x18\x01 \x03(\t\x12\r\n\x05title\x18\x02 \x03(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"\xd0\x04\n\nLinkRecord\x12\r\n\x05\x41RXIV\x18\x01 \x03(\t\x12\x0b\n\x03\x44OI\x18\x02 \x03(\t\x12*\n\x04\x44\x41TA\x18\x03 \x03(\x0b\x32\x1c.adsmsg.LinkRecord.DATAEntry\x12\x30\n\x07\x45SOURCE\x18\x04 \x03(\x0b\x32\x1f.adsmsg.LinkRecord.ESOURCEEntry\x12*\n\nASSOCIATED\x18\x05 \x01(\x0b\x32\x16.adsmsg.LinkTypeRecord\x12\'\n\x07INSPIRE\x18\x06 \x01(\x0b\x32\x16.adsmsg.LinkTypeRecord\x12.\n\x0eLIBRARYCATALOG\x18\x07 \x01(\x0b\x32\x16.adsmsg.LinkTypeRecord\x12,\n\x0cPRESENTATION\x18\x08 \x01(\x0b\x32\x16.adsmsg.LinkTypeRecord\x12\x10\n\x08\x41\x42STRACT\x18\t \x01(\x08\x12\x11\n\tCITATIONS\x18\n \x01(\x08\x12\x10\n\x08GRAPHICS\x18\x0b \x01(\x08\x12\x0f\n\x07METRICS\x18\x0c \x01(\x08\x12\x0f\n\x07OPENURL\x18\r \x01(\x08\x12\x12\n\nREFERENCES\x18\x0e \x01(\x08\x12\x0b\n\x03TOC\x18\x0f \x01(\x08\x12\x0e\n\x06\x43OREAD\x18\x10 \x01(\x08\x1a\x43\n\tDATAEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.adsmsg.LinkTypeRecord:\x02\x38\x01\x1a\x46\n\x0c\x45SOURCEEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.adsmsg.LinkTypeRecord:\x02\x38\x01\"X\n\x0e\x44ocumentRecord\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12\x12\n\nidentifier\x18\x02 \x03(\t\x12!\n\x05links\x18\x03 \x01(\x0b\x32\x12.adsmsg.LinkRecord\"c\n\x0f\x44ocumentRecords\x12\x30\n\x10\x64ocument_records\x18\x01 \x03(\x0b\x32\x16.adsmsg.DocumentRecord\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.adsmsg.Statusb\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_LINKTYPERECORD = _descriptor.Descriptor(
  name='LinkTypeRecord',
  full_name='adsmsg.LinkTypeRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='adsmsg.LinkTypeRecord.url', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='adsmsg.LinkTypeRecord.title', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='adsmsg.LinkTypeRecord.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=97,
)


_LINKRECORD_DATAENTRY = _descriptor.Descriptor(
  name='DATAEntry',
  full_name='adsmsg.LinkRecord.DATAEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adsmsg.LinkRecord.DATAEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='adsmsg.LinkRecord.DATAEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=553,
  serialized_end=620,
)

_LINKRECORD_ESOURCEENTRY = _descriptor.Descriptor(
  name='ESOURCEEntry',
  full_name='adsmsg.LinkRecord.ESOURCEEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adsmsg.LinkRecord.ESOURCEEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='adsmsg.LinkRecord.ESOURCEEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=692,
)

_LINKRECORD = _descriptor.Descriptor(
  name='LinkRecord',
  full_name='adsmsg.LinkRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ARXIV', full_name='adsmsg.LinkRecord.ARXIV', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DOI', full_name='adsmsg.LinkRecord.DOI', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DATA', full_name='adsmsg.LinkRecord.DATA', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ESOURCE', full_name='adsmsg.LinkRecord.ESOURCE', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ASSOCIATED', full_name='adsmsg.LinkRecord.ASSOCIATED', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='INSPIRE', full_name='adsmsg.LinkRecord.INSPIRE', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LIBRARYCATALOG', full_name='adsmsg.LinkRecord.LIBRARYCATALOG', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PRESENTATION', full_name='adsmsg.LinkRecord.PRESENTATION', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ABSTRACT', full_name='adsmsg.LinkRecord.ABSTRACT', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CITATIONS', full_name='adsmsg.LinkRecord.CITATIONS', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GRAPHICS', full_name='adsmsg.LinkRecord.GRAPHICS', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='METRICS', full_name='adsmsg.LinkRecord.METRICS', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OPENURL', full_name='adsmsg.LinkRecord.OPENURL', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='REFERENCES', full_name='adsmsg.LinkRecord.REFERENCES', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TOC', full_name='adsmsg.LinkRecord.TOC', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='COREAD', full_name='adsmsg.LinkRecord.COREAD', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LINKRECORD_DATAENTRY, _LINKRECORD_ESOURCEENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=692,
)


_DOCUMENTRECORD = _descriptor.Descriptor(
  name='DocumentRecord',
  full_name='adsmsg.DocumentRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.DocumentRecord.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='adsmsg.DocumentRecord.identifier', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='links', full_name='adsmsg.DocumentRecord.links', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=694,
  serialized_end=782,
)


_DOCUMENTRECORDS = _descriptor.Descriptor(
  name='DocumentRecords',
  full_name='adsmsg.DocumentRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='document_records', full_name='adsmsg.DocumentRecords.document_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.DocumentRecords.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=784,
  serialized_end=883,
)

_LINKRECORD_DATAENTRY.fields_by_name['value'].message_type = _LINKTYPERECORD
_LINKRECORD_DATAENTRY.containing_type = _LINKRECORD
_LINKRECORD_ESOURCEENTRY.fields_by_name['value'].message_type = _LINKTYPERECORD
_LINKRECORD_ESOURCEENTRY.containing_type = _LINKRECORD
_LINKRECORD.fields_by_name['DATA'].message_type = _LINKRECORD_DATAENTRY
_LINKRECORD.fields_by_name['ESOURCE'].message_type = _LINKRECORD_ESOURCEENTRY
_LINKRECORD.fields_by_name['ASSOCIATED'].message_type = _LINKTYPERECORD
_LINKRECORD.fields_by_name['INSPIRE'].message_type = _LINKTYPERECORD
_LINKRECORD.fields_by_name['LIBRARYCATALOG'].message_type = _LINKTYPERECORD
_LINKRECORD.fields_by_name['PRESENTATION'].message_type = _LINKTYPERECORD
_DOCUMENTRECORD.fields_by_name['links'].message_type = _LINKRECORD
_DOCUMENTRECORDS.fields_by_name['document_records'].message_type = _DOCUMENTRECORD
_DOCUMENTRECORDS.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['LinkTypeRecord'] = _LINKTYPERECORD
DESCRIPTOR.message_types_by_name['LinkRecord'] = _LINKRECORD
DESCRIPTOR.message_types_by_name['DocumentRecord'] = _DOCUMENTRECORD
DESCRIPTOR.message_types_by_name['DocumentRecords'] = _DOCUMENTRECORDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinkTypeRecord = _reflection.GeneratedProtocolMessageType('LinkTypeRecord', (_message.Message,), dict(
  DESCRIPTOR = _LINKTYPERECORD,
  __module__ = 'master_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.LinkTypeRecord)
  ))
_sym_db.RegisterMessage(LinkTypeRecord)

LinkRecord = _reflection.GeneratedProtocolMessageType('LinkRecord', (_message.Message,), dict(

  DATAEntry = _reflection.GeneratedProtocolMessageType('DATAEntry', (_message.Message,), dict(
    DESCRIPTOR = _LINKRECORD_DATAENTRY,
    __module__ = 'master_pb2'
    # @@protoc_insertion_point(class_scope:adsmsg.LinkRecord.DATAEntry)
    ))
  ,

  ESOURCEEntry = _reflection.GeneratedProtocolMessageType('ESOURCEEntry', (_message.Message,), dict(
    DESCRIPTOR = _LINKRECORD_ESOURCEENTRY,
    __module__ = 'master_pb2'
    # @@protoc_insertion_point(class_scope:adsmsg.LinkRecord.ESOURCEEntry)
    ))
  ,
  DESCRIPTOR = _LINKRECORD,
  __module__ = 'master_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.LinkRecord)
  ))
_sym_db.RegisterMessage(LinkRecord)
_sym_db.RegisterMessage(LinkRecord.DATAEntry)
_sym_db.RegisterMessage(LinkRecord.ESOURCEEntry)

DocumentRecord = _reflection.GeneratedProtocolMessageType('DocumentRecord', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTRECORD,
  __module__ = 'master_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DocumentRecord)
  ))
_sym_db.RegisterMessage(DocumentRecord)

DocumentRecords = _reflection.GeneratedProtocolMessageType('DocumentRecords', (_message.Message,), dict(
  DESCRIPTOR = _DOCUMENTRECORDS,
  __module__ = 'master_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DocumentRecords)
  ))
_sym_db.RegisterMessage(DocumentRecords)


_LINKRECORD_DATAENTRY.has_options = True
_LINKRECORD_DATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_LINKRECORD_ESOURCEENTRY.has_options = True
_LINKRECORD_ESOURCEENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
