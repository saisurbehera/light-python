# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proximity_sensors.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proximity_sensors.proto',
  package='ltpb',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17proximity_sensors.proto\x12\x04ltpb\"l\n\x10ProximitySensors\x12\x10\n\x08sensor_1\x18\x01 \x02(\x08\x12\x10\n\x08sensor_2\x18\x02 \x02(\x08\x12\x10\n\x08sensor_3\x18\x03 \x02(\x08\x12\x10\n\x08sensor_4\x18\x04 \x02(\x08\x12\x10\n\x08sensor_5\x18\x05 \x02(\x08'
)




_PROXIMITYSENSORS = _descriptor.Descriptor(
  name='ProximitySensors',
  full_name='ltpb.ProximitySensors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_1', full_name='ltpb.ProximitySensors.sensor_1', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor_2', full_name='ltpb.ProximitySensors.sensor_2', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor_3', full_name='ltpb.ProximitySensors.sensor_3', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor_4', full_name='ltpb.ProximitySensors.sensor_4', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor_5', full_name='ltpb.ProximitySensors.sensor_5', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['ProximitySensors'] = _PROXIMITYSENSORS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProximitySensors = _reflection.GeneratedProtocolMessageType('ProximitySensors', (_message.Message,), {
  'DESCRIPTOR' : _PROXIMITYSENSORS,
  '__module__' : 'proximity_sensors_pb2'
  # @@protoc_insertion_point(class_scope:ltpb.ProximitySensors)
  })
_sym_db.RegisterMessage(ProximitySensors)


# @@protoc_insertion_point(module_scope)
