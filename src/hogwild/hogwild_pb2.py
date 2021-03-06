# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hogwild.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hogwild.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rhogwild.proto\"\x07\n\x05\x45mpty\"B\n\x0bNetworkInfo\x12\x1b\n\x13\x63oordinator_address\x18\x01 \x01(\t\x12\x16\n\x0enode_addresses\x18\x02 \x03(\t\"\xb7\x01\n\x07\x44\x61taSet\x12&\n\ndatapoints\x18\x01 \x03(\x0b\x32\x12.DataSet.DataPoint\x1a\x83\x01\n\tDataPoint\x12\x34\n\tdatapoint\x18\x01 \x03(\x0b\x32!.DataSet.DataPoint.DatapointEntry\x12\x0e\n\x06target\x18\x02 \x01(\x05\x1a\x30\n\x0e\x44\x61tapointEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"]\n\x0cStartMessage\x12\x15\n\rlearning_rate\x18\x01 \x01(\x02\x12\x12\n\nlambda_reg\x18\x02 \x01(\x02\x12\x0e\n\x06\x65pochs\x18\x03 \x01(\x05\x12\x12\n\nbatch_size\x18\x04 \x01(\x05\"i\n\x0cWeightUpdate\x12*\n\x07\x64\x65lta_w\x18\x01 \x03(\x0b\x32\x19.WeightUpdate.DeltaWEntry\x1a-\n\x0b\x44\x65ltaWEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\x0b\n\tReadyToGo\"\x0c\n\nEpochsDone2\xf1\x01\n\x07Hogwild\x12%\n\x0bGetNodeInfo\x12\x0c.NetworkInfo\x1a\x06.Empty\"\x00\x12 \n\nGetDataSet\x12\x08.DataSet\x1a\x06.Empty\"\x00\x12#\n\x08StartSGD\x12\r.StartMessage\x1a\x06.Empty\"\x00\x12*\n\x0fGetWeightUpdate\x12\r.WeightUpdate\x1a\x06.Empty\"\x00\x12$\n\x0cGetReadyToGo\x12\n.ReadyToGo\x1a\x06.Empty\"\x00\x12&\n\rGetEpochsDone\x12\x0b.EpochsDone\x1a\x06.Empty\"\x00\x62\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=17,
  serialized_end=24,
)


_NETWORKINFO = _descriptor.Descriptor(
  name='NetworkInfo',
  full_name='NetworkInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coordinator_address', full_name='NetworkInfo.coordinator_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_addresses', full_name='NetworkInfo.node_addresses', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=26,
  serialized_end=92,
)


_DATASET_DATAPOINT_DATAPOINTENTRY = _descriptor.Descriptor(
  name='DatapointEntry',
  full_name='DataSet.DataPoint.DatapointEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataSet.DataPoint.DatapointEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataSet.DataPoint.DatapointEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=230,
  serialized_end=278,
)

_DATASET_DATAPOINT = _descriptor.Descriptor(
  name='DataPoint',
  full_name='DataSet.DataPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datapoint', full_name='DataSet.DataPoint.datapoint', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='DataSet.DataPoint.target', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATASET_DATAPOINT_DATAPOINTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=278,
)

_DATASET = _descriptor.Descriptor(
  name='DataSet',
  full_name='DataSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datapoints', full_name='DataSet.datapoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATASET_DATAPOINT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=278,
)


_STARTMESSAGE = _descriptor.Descriptor(
  name='StartMessage',
  full_name='StartMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='StartMessage.learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lambda_reg', full_name='StartMessage.lambda_reg', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epochs', full_name='StartMessage.epochs', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='StartMessage.batch_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=280,
  serialized_end=373,
)


_WEIGHTUPDATE_DELTAWENTRY = _descriptor.Descriptor(
  name='DeltaWEntry',
  full_name='WeightUpdate.DeltaWEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='WeightUpdate.DeltaWEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='WeightUpdate.DeltaWEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=435,
  serialized_end=480,
)

_WEIGHTUPDATE = _descriptor.Descriptor(
  name='WeightUpdate',
  full_name='WeightUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delta_w', full_name='WeightUpdate.delta_w', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WEIGHTUPDATE_DELTAWENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=480,
)


_READYTOGO = _descriptor.Descriptor(
  name='ReadyToGo',
  full_name='ReadyToGo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=482,
  serialized_end=493,
)


_EPOCHSDONE = _descriptor.Descriptor(
  name='EpochsDone',
  full_name='EpochsDone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=495,
  serialized_end=507,
)

_DATASET_DATAPOINT_DATAPOINTENTRY.containing_type = _DATASET_DATAPOINT
_DATASET_DATAPOINT.fields_by_name['datapoint'].message_type = _DATASET_DATAPOINT_DATAPOINTENTRY
_DATASET_DATAPOINT.containing_type = _DATASET
_DATASET.fields_by_name['datapoints'].message_type = _DATASET_DATAPOINT
_WEIGHTUPDATE_DELTAWENTRY.containing_type = _WEIGHTUPDATE
_WEIGHTUPDATE.fields_by_name['delta_w'].message_type = _WEIGHTUPDATE_DELTAWENTRY
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['NetworkInfo'] = _NETWORKINFO
DESCRIPTOR.message_types_by_name['DataSet'] = _DATASET
DESCRIPTOR.message_types_by_name['StartMessage'] = _STARTMESSAGE
DESCRIPTOR.message_types_by_name['WeightUpdate'] = _WEIGHTUPDATE
DESCRIPTOR.message_types_by_name['ReadyToGo'] = _READYTOGO
DESCRIPTOR.message_types_by_name['EpochsDone'] = _EPOCHSDONE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'hogwild_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)

NetworkInfo = _reflection.GeneratedProtocolMessageType('NetworkInfo', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKINFO,
  __module__ = 'hogwild_pb2'
  # @@protoc_insertion_point(class_scope:NetworkInfo)
  ))
_sym_db.RegisterMessage(NetworkInfo)

DataSet = _reflection.GeneratedProtocolMessageType('DataSet', (_message.Message,), dict(

  DataPoint = _reflection.GeneratedProtocolMessageType('DataPoint', (_message.Message,), dict(

    DatapointEntry = _reflection.GeneratedProtocolMessageType('DatapointEntry', (_message.Message,), dict(
      DESCRIPTOR = _DATASET_DATAPOINT_DATAPOINTENTRY,
      __module__ = 'hogwild_pb2'
      # @@protoc_insertion_point(class_scope:DataSet.DataPoint.DatapointEntry)
      ))
    ,
    DESCRIPTOR = _DATASET_DATAPOINT,
    __module__ = 'hogwild_pb2'
    # @@protoc_insertion_point(class_scope:DataSet.DataPoint)
    ))
  ,
  DESCRIPTOR = _DATASET,
  __module__ = 'hogwild_pb2'
  # @@protoc_insertion_point(class_scope:DataSet)
  ))
_sym_db.RegisterMessage(DataSet)
_sym_db.RegisterMessage(DataSet.DataPoint)
_sym_db.RegisterMessage(DataSet.DataPoint.DatapointEntry)

StartMessage = _reflection.GeneratedProtocolMessageType('StartMessage', (_message.Message,), dict(
  DESCRIPTOR = _STARTMESSAGE,
  __module__ = 'hogwild_pb2'
  # @@protoc_insertion_point(class_scope:StartMessage)
  ))
_sym_db.RegisterMessage(StartMessage)

WeightUpdate = _reflection.GeneratedProtocolMessageType('WeightUpdate', (_message.Message,), dict(

  DeltaWEntry = _reflection.GeneratedProtocolMessageType('DeltaWEntry', (_message.Message,), dict(
    DESCRIPTOR = _WEIGHTUPDATE_DELTAWENTRY,
    __module__ = 'hogwild_pb2'
    # @@protoc_insertion_point(class_scope:WeightUpdate.DeltaWEntry)
    ))
  ,
  DESCRIPTOR = _WEIGHTUPDATE,
  __module__ = 'hogwild_pb2'
  # @@protoc_insertion_point(class_scope:WeightUpdate)
  ))
_sym_db.RegisterMessage(WeightUpdate)
_sym_db.RegisterMessage(WeightUpdate.DeltaWEntry)

ReadyToGo = _reflection.GeneratedProtocolMessageType('ReadyToGo', (_message.Message,), dict(
  DESCRIPTOR = _READYTOGO,
  __module__ = 'hogwild_pb2'
  # @@protoc_insertion_point(class_scope:ReadyToGo)
  ))
_sym_db.RegisterMessage(ReadyToGo)

EpochsDone = _reflection.GeneratedProtocolMessageType('EpochsDone', (_message.Message,), dict(
  DESCRIPTOR = _EPOCHSDONE,
  __module__ = 'hogwild_pb2'
  # @@protoc_insertion_point(class_scope:EpochsDone)
  ))
_sym_db.RegisterMessage(EpochsDone)


_DATASET_DATAPOINT_DATAPOINTENTRY.has_options = True
_DATASET_DATAPOINT_DATAPOINTENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_WEIGHTUPDATE_DELTAWENTRY.has_options = True
_WEIGHTUPDATE_DELTAWENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_HOGWILD = _descriptor.ServiceDescriptor(
  name='Hogwild',
  full_name='Hogwild',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=510,
  serialized_end=751,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetNodeInfo',
    full_name='Hogwild.GetNodeInfo',
    index=0,
    containing_service=None,
    input_type=_NETWORKINFO,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataSet',
    full_name='Hogwild.GetDataSet',
    index=1,
    containing_service=None,
    input_type=_DATASET,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartSGD',
    full_name='Hogwild.StartSGD',
    index=2,
    containing_service=None,
    input_type=_STARTMESSAGE,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWeightUpdate',
    full_name='Hogwild.GetWeightUpdate',
    index=3,
    containing_service=None,
    input_type=_WEIGHTUPDATE,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetReadyToGo',
    full_name='Hogwild.GetReadyToGo',
    index=4,
    containing_service=None,
    input_type=_READYTOGO,
    output_type=_EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetEpochsDone',
    full_name='Hogwild.GetEpochsDone',
    index=5,
    containing_service=None,
    input_type=_EPOCHSDONE,
    output_type=_EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HOGWILD)

DESCRIPTOR.services_by_name['Hogwild'] = _HOGWILD

# @@protoc_insertion_point(module_scope)
