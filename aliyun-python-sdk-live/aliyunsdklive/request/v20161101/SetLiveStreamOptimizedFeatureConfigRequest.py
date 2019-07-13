# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SetLiveStreamOptimizedFeatureConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'SetLiveStreamOptimizedFeatureConfig','live')

	def get_ConfigStatus(self):
		return self.get_query_params().get('ConfigStatus')

	def set_ConfigStatus(self,ConfigStatus):
		self.add_query_param('ConfigStatus',ConfigStatus)

	def get_ConfigName(self):
		return self.get_query_params().get('ConfigName')

	def set_ConfigName(self,ConfigName):
		self.add_query_param('ConfigName',ConfigName)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_ConfigValue(self):
		return self.get_query_params().get('ConfigValue')

	def set_ConfigValue(self,ConfigValue):
		self.add_query_param('ConfigValue',ConfigValue)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)