// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.
package org.apache.cloudstack.engine.cloud.entity.dao;

import java.util.Date;
import java.util.List;
import java.util.Map;

import org.apache.cloudstack.engine.cloud.entity.VMEntityVO;

import com.cloud.utils.Pair;
import com.cloud.utils.db.GenericDao;
import com.cloud.utils.fsm.StateDao;
import com.cloud.vm.VMInstanceVO;
import com.cloud.vm.VirtualMachine;
import com.cloud.vm.VirtualMachine.State;
import com.cloud.vm.VirtualMachine.Type;


/*
 * Data Access Object for vm_instance table
 */
public interface VMEntityDao extends GenericDao<VMEntityVO, Long> {
  
    void loadVmReservation(VMEntityVO vm);
    
}