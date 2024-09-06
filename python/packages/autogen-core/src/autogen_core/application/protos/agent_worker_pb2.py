# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent_worker.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61gent_worker.proto\x12\x06\x61gents\"$\n\x07\x41gentId\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"E\n\x07Payload\x12\x11\n\tdata_type\x18\x01 \x01(\t\x12\x19\n\x11\x64\x61ta_content_type\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xf9\x01\n\nRpcRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x1f\n\x06source\x18\x02 \x01(\x0b\x32\x0f.agents.AgentId\x12\x1f\n\x06target\x18\x03 \x01(\x0b\x32\x0f.agents.AgentId\x12\x0e\n\x06method\x18\x04 \x01(\t\x12 \n\x07payload\x18\x05 \x01(\x0b\x32\x0f.agents.Payload\x12\x32\n\x08metadata\x18\x06 \x03(\x0b\x32 .agents.RpcRequest.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb8\x01\n\x0bRpcResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12 \n\x07payload\x18\x02 \x01(\x0b\x32\x0f.agents.Payload\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x08metadata\x18\x04 \x03(\x0b\x32!.agents.RpcResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb3\x01\n\x05\x45vent\x12\x12\n\ntopic_type\x18\x01 \x01(\t\x12\x14\n\x0ctopic_source\x18\x02 \x01(\t\x12 \n\x07payload\x18\x03 \x01(\x0b\x32\x0f.agents.Payload\x12-\n\x08metadata\x18\x04 \x03(\x0b\x32\x1b.agents.Event.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"!\n\x11RegisterAgentType\x12\x0c\n\x04type\x18\x01 \x01(\t\":\n\x10TypeSubscription\x12\x12\n\ntopic_type\x18\x01 \x01(\t\x12\x12\n\nagent_type\x18\x02 \x01(\t\"T\n\x0cSubscription\x12\x34\n\x10typeSubscription\x18\x01 \x01(\x0b\x32\x18.agents.TypeSubscriptionH\x00\x42\x0e\n\x0csubscription\"=\n\x0f\x41\x64\x64Subscription\x12*\n\x0csubscription\x18\x01 \x01(\x0b\x32\x14.agents.Subscription\"\xf0\x01\n\x07Message\x12%\n\x07request\x18\x01 \x01(\x0b\x32\x12.agents.RpcRequestH\x00\x12\'\n\x08response\x18\x02 \x01(\x0b\x32\x13.agents.RpcResponseH\x00\x12\x1e\n\x05\x65vent\x18\x03 \x01(\x0b\x32\r.agents.EventH\x00\x12\x36\n\x11registerAgentType\x18\x04 \x01(\x0b\x32\x19.agents.RegisterAgentTypeH\x00\x12\x32\n\x0f\x61\x64\x64Subscription\x18\x05 \x01(\x0b\x32\x17.agents.AddSubscriptionH\x00\x42\t\n\x07message2?\n\x08\x41gentRpc\x12\x33\n\x0bOpenChannel\x12\x0f.agents.Message\x1a\x0f.agents.Message(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_worker_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RPCREQUEST_METADATAENTRY']._options = None
  _globals['_RPCREQUEST_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_RPCRESPONSE_METADATAENTRY']._options = None
  _globals['_RPCRESPONSE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_EVENT_METADATAENTRY']._options = None
  _globals['_EVENT_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_AGENTID']._serialized_start=30
  _globals['_AGENTID']._serialized_end=66
  _globals['_PAYLOAD']._serialized_start=68
  _globals['_PAYLOAD']._serialized_end=137
  _globals['_RPCREQUEST']._serialized_start=140
  _globals['_RPCREQUEST']._serialized_end=389
  _globals['_RPCREQUEST_METADATAENTRY']._serialized_start=342
  _globals['_RPCREQUEST_METADATAENTRY']._serialized_end=389
  _globals['_RPCRESPONSE']._serialized_start=392
  _globals['_RPCRESPONSE']._serialized_end=576
  _globals['_RPCRESPONSE_METADATAENTRY']._serialized_start=342
  _globals['_RPCRESPONSE_METADATAENTRY']._serialized_end=389
  _globals['_EVENT']._serialized_start=579
  _globals['_EVENT']._serialized_end=758
  _globals['_EVENT_METADATAENTRY']._serialized_start=342
  _globals['_EVENT_METADATAENTRY']._serialized_end=389
  _globals['_REGISTERAGENTTYPE']._serialized_start=760
  _globals['_REGISTERAGENTTYPE']._serialized_end=793
  _globals['_TYPESUBSCRIPTION']._serialized_start=795
  _globals['_TYPESUBSCRIPTION']._serialized_end=853
  _globals['_SUBSCRIPTION']._serialized_start=855
  _globals['_SUBSCRIPTION']._serialized_end=939
  _globals['_ADDSUBSCRIPTION']._serialized_start=941
  _globals['_ADDSUBSCRIPTION']._serialized_end=1002
  _globals['_MESSAGE']._serialized_start=1005
  _globals['_MESSAGE']._serialized_end=1245
  _globals['_AGENTRPC']._serialized_start=1247
  _globals['_AGENTRPC']._serialized_end=1310
# @@protoc_insertion_point(module_scope)
