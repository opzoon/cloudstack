# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from marvin.base import CloudStackEntity
from marvin.cloudstackAPI import createNetwork
from marvin.cloudstackAPI import listNetworks
from marvin.cloudstackAPI import updateNetwork
from marvin.cloudstackAPI import restartNetwork
from marvin.cloudstackAPI import deleteNetwork

class Network(CloudStackEntity.CloudStackEntity):


    def __init__(self, items):
        self.__dict__.update(items)


    @classmethod
    def create(cls, apiclient, factory, **kwargs):
        cmd = createNetwork.createNetworkCmd()
        [setattr(cmd, factoryKey, factoryValue) for factoryKey, factoryValue in factory.__dict__.iteritems()]
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        network = apiclient.createNetwork(cmd)
        return Network(network.__dict__)


    @classmethod
    def list(self, apiclient, **kwargs):
        cmd = listNetworks.listNetworksCmd()
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        network = apiclient.listNetworks(cmd)
        return map(lambda e: Network(e.__dict__), network)


    def update(self, apiclient, **kwargs):
        cmd = updateNetwork.updateNetworkCmd()
        cmd.id = self.id
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        network = apiclient.updateNetwork(cmd)
        return network


    def restart(self, apiclient, **kwargs):
        cmd = restartNetwork.restartNetworkCmd()
        cmd.id = self.id
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        network = apiclient.restartNetwork(cmd)
        return network


    def delete(self, apiclient, **kwargs):
        cmd = deleteNetwork.deleteNetworkCmd()
        cmd.id = self.id
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        network = apiclient.deleteNetwork(cmd)
        return network
