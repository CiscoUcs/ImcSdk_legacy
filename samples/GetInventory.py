#! /usr/bin/python

# Copyright 2013 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script generates the Inventory Report for IMC server.
# With "--html" option, this script will generate the report as an HTML file,
# else it will display the output on your console.
# 
# By Default file_name is ImcInventoryReport_<ImcName>.html , else you can 
# specify it with option "--filename".
#  e.g. ImcInventoryReport_MsftIntRack15.html
#
# By default file will be created in current directory else you can specify
# it with option "--filepath".
#usage: GetInventory.py [options]
# python GetInventory.py -i "IP Address" -u "UserName" -p "Password"
# OR
# python GetInventory.py -i "IP Address" -u "UserName" -p "Password" --html
#
#options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
#  --html=OUTPUTDEST     [Optional] Use for output as an htmlfile
#  --filename=FILENAME   [Optional] name of a file
#  --filepath=FILEPATH   [Optional] Path of a file
#
# Usecase:
# GetInventory.py -i <IP Address> -u <Username> -p <Password>
# GetInventory.py -i <IP Address> -u <Username> -p <Password> --html
# GetInventory.py -i <IP Address> -u <Username> -p <Password> --html --filename Inventory.html

import platform
import getpass
import optparse
import os
import re

from ImcSdk import *

handle_list = []

def get_password(prompt):
    if platform.system() == "Linux":
        return getpass.unix_getpass(prompt=prompt)
    elif platform.system() == "Windows" or platform.system() == "Microsoft":
        return getpass.win_getpass(prompt=prompt)
    else:
        return getpass.getpass(prompt=prompt)

def do_login(ip,user,pwd):
    print "Connecting to IMC Server <%s>...." %(ip)
    handle = ImcHandle()
    if handle.login(ip,user,pwd):
        print "login successful: <%s>\n" %(handle.name)
        handle_list.append(handle)
        return handle

def do_logout():
    for handle in handle_list:
        handle_name = handle.name
        if handle.logout():
            print "\nLogout successful: <%s>" %(handle_name)

def get_molist_by_class_id(handle,class_id):
    return handle.get_imc_managedobject(None, class_id)

def get_molist_by_dn(handle, dn):
    return handle.get_imc_managedobject(params={"Dn":dn})

def get_molist_under_parents(handle,parent_mo_list,class_id=None):
    return handle.get_imc_managedobject(in_mo=parent_mo_list,class_id=class_id)

class RackUnitInventory:
    def __init__(self,rack_unit):
        self.class_id = "Rack Unit"
        self.number_of_cpus = rack_unit.get_attr(ComputeRackUnit.NUM_OF_CPUS)
        self.number_of_cores = rack_unit.get_attr(ComputeRackUnit.NUM_OF_CORES)
        self.available_memory = rack_unit.get_attr(
                                    ComputeRackUnit.AVAILABLE_MEMORY)
        self.number_of_adaptors = rack_unit.get_attr(
                                     ComputeRackUnit.NUM_OF_ADAPTORS)
        self.number_of_eth_interfaces = rack_unit.get_attr(
                                      ComputeRackUnit.NUM_OF_ETH_HOST_IFS)
        self.number_of_fc_interfaces = rack_unit.get_attr(
                                     ComputeRackUnit.NUM_OF_FC_HOST_IFS)
        self.uuid = rack_unit.get_attr(ComputeRackUnit.UUID)
        self.psu_units = []
        self.boot_definitions = []
        self.network_adaptor_units = []
        self.compute_boards = []
        
    def get_rack_health_info(self):
        locator_led_info = get_molist_by_dn(handle,"sys/rack-unit-1/indicator-led-5")
        if locator_led_info is not None:
            if locator_led_info[0].get_attr(
                                 EquipmentIndicatorLed.COLOR) == "green":
                if locator_led_info[0].get_attr(
                                 EquipmentIndicatorLed.OPER_STATE) == "on":
                    self.operation_state = "Good"
                elif locator_led_info[0].get_attr(
                               EquipmentIndicatorLed.OPER_STATE) == "off":
                    self.operation_state = "Good(Memory Test In Progress)"
            if locator_led_info[0].get_attr(
                                 EquipmentIndicatorLed.COLOR) == "amber":
                if locator_led_info[0].get_attr(
                                 EquipmentIndicatorLed.OPER_STATE) == "on":
                    self.operation_state = "Fault"
                elif locator_led_info[0].get_attr(
                               EquipmentIndicatorLed.OPER_STATE) == "off":
                    self.operation_state = "Severe fault"
                elif locator_led_info[0].get_attr(
                               EquipmentIndicatorLed.OPER_STATE) == "blinking":
                    self.operation_state = "Severe fault"

class NetworkAdaptorUnitInventory:
    def __init__(self,network_adaptor_unit):
        self.class_id = "Network Adaptor Unit"
        self.model = network_adaptor_unit.get_attr(NetworkAdapterUnit.MODEL)
        self.num_int_f = network_adaptor_unit.get_attr(NetworkAdapterUnit.NUM_INTF)
        self.slot = network_adaptor_unit.get_attr(NetworkAdapterUnit.SLOT)


class ComputeBoardInventory:
    def __init__(self,compute_board):
        self.class_id = "Compute Board"
        self.id = compute_board.get_attr(ComputeBoard.ID)
        self.model = compute_board.get_attr(ComputeBoard.MODEL)
        self.oper_power = compute_board.get_attr(ComputeBoard.OPER_POWER)
        self.perf = compute_board.get_attr(ComputeBoard.PERF)
        self.power = compute_board.get_attr(ComputeBoard.POWER)
        self.presence = compute_board.get_attr(ComputeBoard.PRESENCE)
        self.serial = compute_board.get_attr(ComputeBoard.SERIAL)
        self.processor_units = []
        self.memory_arrays = []
        self.storage_controllers = []
        self.pid_catalog_dimms = []
        self.pid_catalog_pci_adapters = []
        self.bios_units = []
        self.temp_stats = []
        self.power_stats = []

class ProcessorUnitInventory:
    def __init__(self,processorUnit):
        self.class_id = "Processor Unit"
        self.id = processorUnit.get_attr(ProcessorUnit.ID)
        self.arch = processorUnit.get_attr(ProcessorUnit.ARCH)
        self.cores = processorUnit.get_attr(ProcessorUnit.CORES)
        self.cores_enabled = processorUnit.get_attr(
                                          ProcessorUnit.CORES_ENABLED)
        self.model = processorUnit.get_attr(ProcessorUnit.MODEL)
        self.socket_designation = processorUnit.get_attr(
                                           ProcessorUnit.SOCKET_DESIGNATION)
        self.speed = processorUnit.get_attr(ProcessorUnit.SPEED)
        self.stepping = processorUnit.get_attr(ProcessorUnit.STEPPING)
        self.threads = processorUnit.get_attr(ProcessorUnit.THREADS)
        self.vendor = processorUnit.get_attr(ProcessorUnit.VENDOR)
        self.sensor_description=None
        self.temperature=None
        
class MemoryArrayInventory:
    def __init__(self,memory_array):
        self.class_id = "Memory Array"
        self.id = memory_array.get_attr(MemoryArray.ID)
        self.curr_capacity = memory_array.get_attr(MemoryArray.CURR_CAPACITY)
        self.max_capacity = memory_array.get_attr(MemoryArray.MAX_DEVICES)
        self.populated = memory_array.get_attr(MemoryArray.POPULATED)
        self.memory_units = []
        
class MemoryUnitInventory:
    def __init__(self,memory_unit):
        self.class_id = "Memory Unit"
        self.id = memory_unit.get_attr(MemoryUnit.ID)
        self.capacity = memory_unit.get_attr(MemoryUnit.CAPACITY)
        self.clock = memory_unit.get_attr(MemoryUnit.CLOCK)
        self.form_factor = memory_unit.get_attr(MemoryUnit.FORM_FACTOR)
        self.location = memory_unit.get_attr(MemoryUnit.LOCATION)
        self.model = memory_unit.get_attr(MemoryUnit.MODEL)
        self.oper_state = memory_unit.get_attr(MemoryUnit.OPER_STATE)
        self.operability =memory_unit.get_attr(MemoryUnit.OPERABILITY)
        self.presence = memory_unit.get_attr(MemoryUnit.PRESENCE)
        self.serial = memory_unit.get_attr(MemoryUnit.SERIAL)
        self.type = memory_unit.get_attr(MemoryUnit.TYPE)
        self.vendor = memory_unit.get_attr(MemoryUnit.VENDOR)
        self.Visibility = memory_unit.get_attr(MemoryUnit.VISIBILITY)
        
class StorageControllerInventory:
    def __init__(self,storage_controller):
        self.class_id = "Storage Controller"
        self.id = storage_controller.get_attr(StorageController.ID)
        self.model = storage_controller.get_attr(StorageController.MODEL)
        self.type = storage_controller.get_attr(StorageController.TYPE)
        self.vendor = storage_controller.get_attr(StorageController.VENDOR)
        self.serial = storage_controller.get_attr(StorageController.SERIAL)
        self.pci_slot = storage_controller.get_attr(StorageController.PCI_SLOT)
        self.presence = storage_controller.get_attr(StorageController.PRESENCE)
        self.storage_local_disks = []
        self.storage_virtual_drives = []
        self.firmware_deployment = None
        self.firmware_version = None
        
class StorageLocalDiskInventory:
    def __init__(self,storage_local_disk):
        self.class_id = "Storage Local Disk"
        self.id = storage_local_disk.get_attr(StorageLocalDisk.ID)
        self.interface_type = storage_local_disk.get_attr(
                                StorageLocalDisk.INTERFACE_TYPE)
        self.drive_state = storage_local_disk.get_attr(
                                StorageLocalDisk.DRIVE_STATE)
        self.drive_serial_number = storage_local_disk.get_attr(
                                StorageLocalDisk.DRIVE_SERIAL_NUMBER)
        self.vendor = storage_local_disk.get_attr(StorageLocalDisk.VENDOR)
        self.product_id = storage_local_disk.get_attr(
                                  StorageLocalDisk.PRODUCT_ID)
        self.health = storage_local_disk.get_attr(StorageLocalDisk.HEALTH)
        self.pd_status = storage_local_disk.get_attr(StorageLocalDisk.PD_STATUS)
        self.link_speed = storage_local_disk.get_attr(
                                              StorageLocalDisk.LINK_SPEED)
        
class StorageVirtualDriveInventory:
    def __init__(self,storageVirtualDrive):
        self.class_id = "Storage Virtual Drive"
        self.id = storageVirtualDrive.get_attr(StorageVirtualDrive.ID)
        self.name = storageVirtualDrive.get_attr(StorageVirtualDrive.NAME)
        self.raid_level = storageVirtualDrive.get_attr(
                                             StorageVirtualDrive.RAID_LEVEL)
        self.access_policy = storageVirtualDrive.get_attr(
                                        StorageVirtualDrive.ACCESS_POLICY)
        self.allow_background_init = storageVirtualDrive.get_attr(
                               StorageVirtualDrive.ALLOW_BACKGROUND_INIT)
        self.auto_delete_oldest = storageVirtualDrive.get_attr(
                                    StorageVirtualDrive.AUTO_DELETE_OLDEST)
        self.auto_snapshot = storageVirtualDrive.get_attr(
                                    StorageVirtualDrive.AUTO_SNAPSHOT)
        self.cache_policy = storageVirtualDrive.get_attr(
                                   StorageVirtualDrive.CACHE_POLICY)
        self.disk_cache_policy = storageVirtualDrive.get_attr(
                                   StorageVirtualDrive.DISK_CACHE_POLICY)
        self.drive_state = storageVirtualDrive.get_attr(
                                          StorageVirtualDrive.DRIVE_STATE)
        self.drives_per_span = storageVirtualDrive.get_attr(
                                     StorageVirtualDrive.DRIVES_PER_SPAN)
        self.health = storageVirtualDrive.get_attr(
                                          StorageVirtualDrive.HEALTH)
        self.size = storageVirtualDrive.get_attr(StorageVirtualDrive.SIZE)
        self.strip_size = storageVirtualDrive.get_attr(
                                         StorageVirtualDrive.STRIP_SIZE)
        self.vd_status = storageVirtualDrive.get_attr(
                                            StorageVirtualDrive.VD_STATUS)     

class PidCatalogDimmInventory:
    def __init__(self,pid_catalog_dimm):
        self.class_id = "DIMM"
        self.name = pid_catalog_dimm.get_attr(PidCatalogDimm.NAME)
        self.model = pid_catalog_dimm.get_attr(PidCatalogDimm.MODEL)
        self.manufacturer = pid_catalog_dimm.get_attr(
                                           PidCatalogDimm.MANUFACTURER)
        self.operability = pid_catalog_dimm.get_attr(
                                          PidCatalogDimm.OPERABILITY)
        self.capacity = pid_catalog_dimm.get_attr(PidCatalogDimm.CAPACITY)
        self.data_width = pid_catalog_dimm.get_attr(PidCatalogDimm.DATAWIDTH)
        self.serial_number = pid_catalog_dimm.get_attr(
                                           PidCatalogDimm.SERIALNUMBER)
        self.description = pid_catalog_dimm.get_attr(
                                          PidCatalogDimm.DESCRIPTION)

class PidCatalogPciAdapterInventory:
    def __init__(self,pciAdapter):
        self.class_id = "PCI Adapter"
        self.Pid = pciAdapter.get_attr(PidCatalogPCIAdapter.PID)
        self.slot = pciAdapter.get_attr(PidCatalogPCIAdapter.SLOT)
        self.description = pciAdapter.get_attr(
                                      PidCatalogPCIAdapter.DESCRIPTION)
        self.vendor = pciAdapter.get_attr(PidCatalogPCIAdapter.VENDOR)
        
class BiosUnitInventory:
    def __init__(self,bios_unit):
        self.class_id = "Bios Unit"
        self.model = bios_unit.get_attr(BiosUnit.MODEL)
        self.vendor = bios_unit.get_attr(BiosUnit.VENDOR)
        self.firmware_deployment = None
        self.firmware_version = None

class BootDefinitionInventory:
    def __init__(self,boot_definition):
        self.class_id = "Boot Definition"
        self.name = boot_definition.get_attr(LsbootDef.NAME)
        self.purpose = boot_definition.get_attr(LsbootDef.PURPOSE)
        self.reboot_on_update = boot_definition.get_attr(
                                                 LsbootDef.REBOOT_ON_UPDATE)

class PsuUnitInventory:
    def __init__(self,psu_unit):
        self.class_id = "Power Supply Unit"
        self.name = psu_unit.get_attr(EquipmentPsu.ID)
        self.model = psu_unit.get_attr(EquipmentPsu.MODEL)
        self.vendor = psu_unit.get_attr(EquipmentPsu.VENDOR)
        self.serial = psu_unit.get_attr(EquipmentPsu.SERIAL)
        self.power = psu_unit.get_attr(EquipmentPsu.POWER)
        self.thermal = psu_unit.get_attr(EquipmentPsu.THERMAL)
        self.operability = psu_unit.get_attr(EquipmentPsu.OPERABILITY)
        self.presence = psu_unit.get_attr(EquipmentPsu.PRESENCE)

class TempStatInventory:
    def __init__(self,temp_stat):
        self.class_id = "Temperature Statistic"
        self.ambient_temp = temp_stat.get_attr(
                                    ComputeRackUnitMbTempStats.AMBIENT_TEMP)
        self.front_temp = temp_stat.get_attr(
                                  ComputeRackUnitMbTempStats.FRONT_TEMP)
        self.ioh1_temp = temp_stat.get_attr(
                                 ComputeRackUnitMbTempStats.IOH1_TEMP)
        self.ioh2_temp = temp_stat.get_attr(
                                 ComputeRackUnitMbTempStats.IOH2_TEMP)
        self.rear_temp = temp_stat.get_attr(
                                 ComputeRackUnitMbTempStats.REAR_TEMP)
        self.time_collected = temp_stat.get_attr(
                                  ComputeRackUnitMbTempStats.TIME_COLLECTED)
        
class PowerStatInventory:
    def __init__(self,power_stat):
        self.class_id = "Power Statistic"
        self.ConsumedPower = power_stat.get_attr(
                                       ComputeMbPowerStats.CONSUMED_POWER)
        self.InputCurrent = power_stat.get_attr(
                                      ComputeMbPowerStats.INPUT_CURRENT)
        self.InputVoltage = power_stat.get_attr(
                                      ComputeMbPowerStats.INPUT_VOLTAGE)
        self.time_collected = power_stat.get_attr(
                                       ComputeMbPowerStats.TIME_COLLECTED)

def get_rack_unit_inventory(handle):
    rack_unit = get_molist_by_class_id(handle,ComputeRackUnit.class_id())
    rack_unit_obj = RackUnitInventory(rack_unit[0])
    rack_unit_obj.get_rack_health_info()
    rack_unit_obj.psu_units = get_psu_unit_inventory(handle,rack_unit)
    rack_unit_obj.boot_definitions = get_boot_definition_inventory(handle,rack_unit)
    rack_unit_obj.network_adaptor_units = get_network_adaptor_unit_inventory(
                                                         handle,rack_unit)
    rack_unit_obj.compute_boards = get_compute_board_inventory(handle,rack_unit)
    
    return rack_unit_obj

def get_psu_unit_inventory(handle, rack_unit):
    psu_unit_inventory = []
    psu_units = get_molist_under_parents(handle,rack_unit,EquipmentPsu.class_id())
    if psu_units:
        for psu_unit in psu_units:
            psu_unit_obj = PsuUnitInventory(psu_unit)
            psu_unit_inventory.append(psu_unit_obj)
            
    return psu_unit_inventory

def get_boot_definition_inventory(handle, rack_unit):
    boot_definition_inventory = []
    boot_definitions = get_molist_under_parents(handle, rack_unit,LsbootDef.class_id())
    if boot_definitions:
        for boot_definition in boot_definitions:
            boot_definition_obj = BootDefinitionInventory(boot_definition)
            boot_definition_inventory.append(boot_definition_obj)
            
    return boot_definition_inventory
    
def get_network_adaptor_unit_inventory(handle,rack_unit):
    network_adaptor_unit_inventory = []
    network_adaptor_units = get_molist_under_parents(handle,rack_unit,
                                           NetworkAdapterUnit.class_id())
    if network_adaptor_units:
        for network_adaptor_unit in network_adaptor_units:
            network_adaptor_unit_obj = NetworkAdaptorUnitInventory(
                                                        network_adaptor_unit)
            
            adaptorEthIfInfo = get_molist_under_parents(handle,
                                                [network_adaptor_unit],
                                            NetworkAdapterEthIf.class_id())
            if adaptorEthIfInfo:
                for eachadaptorEthIf in adaptorEthIfInfo:
                    network_adaptor_unit_obj.__dict__["MacAddressOf <%s>"%(
                            eachadaptorEthIf.Rn)] = eachadaptorEthIf.Mac
                    #network_adaptor_unit_obj.setattr("MacAddressOf <%s>"%(eachadaptorEthIf.Rn),eachadaptorEthIf.Mac)
                    
            network_adaptor_unit_inventory.append(network_adaptor_unit_obj)
            
    return network_adaptor_unit_inventory

def get_compute_board_inventory(handle,rack_unit):
    compute_board_inventory = []
    compute_boards = get_molist_under_parents(handle,rack_unit,ComputeBoard.class_id())
    if compute_boards:
        for compute_board in compute_boards:
            compute_board_obj = ComputeBoardInventory(compute_board)
            compute_board_obj.processor_units = get_processor_unit_inventory(
                                                       handle,compute_board)
            compute_board_obj.memory_arrays = get_memory_array_inventory(
                                                       handle,compute_board)
            compute_board_obj.storage_controllers = get_storage_controller_inventory(
                                                       handle,compute_board)
            compute_board_obj.pid_catalog_dimms = get_pid_catalog_dimm_inventory(
                                                         handle,compute_board)
            compute_board_obj.pid_catalog_pci_adapters = \
                get_pid_catalog_pci_adapter_inventory(handle,compute_board)
            compute_board_obj.bios_units = get_bios_unit_inventory(
                                                         handle,compute_board)
            compute_board_obj.temp_stats = get_temp_stat_inventory(
                                                         handle,compute_board)
            compute_board_obj.power_stats = get_power_stat_inventory(
                                                       handle,compute_board)
            
            compute_board_inventory.append(compute_board_obj)
            
    return compute_board_inventory

def get_processor_unit_inventory(handle,compute_board):
    processor_unit_inventory=[]
    processorUnits = get_molist_under_parents(
                                      handle,
                                      [compute_board],
                                      ProcessorUnit.class_id())
    if processorUnits:
        for processorUnit in processorUnits:
            processorUnitObj = ProcessorUnitInventory(processorUnit)
            
            env_stats = get_molist_under_parents(handle,
                                        [processorUnit],
                                        ProcessorEnvStats.class_id())
            if env_stats:
                for envStat in env_stats:
                    processorUnitObj.sensor_description=envStat.get_attr(
                                           ProcessorEnvStats.DESCRIPTION)
                    processorUnitObj.temperature=envStat.get_attr(
                                             ProcessorEnvStats.TEMPERATURE)
            
            processor_unit_inventory.append(processorUnitObj)
            
    return processor_unit_inventory
        
def get_memory_array_inventory(handle,compute_board):
    memory_array_inventory = []
    memory_arrays = get_molist_under_parents(handle,[compute_board],
                                    MemoryArray.class_id())
    if memory_arrays:
        for memory_array in memory_arrays:
            memory_array_obj = MemoryArrayInventory(memory_array)
            memory_array_obj.memory_units=get_memory_unit_inventory(handle,
                                                              memory_array)
            
            memory_array_inventory.append(memory_array_obj)
        
    return memory_array_inventory
    
def get_memory_unit_inventory(handle,memory_array):
    memory_unit_inventory = []
    memory_units = get_molist_under_parents(handle,[memory_array],
                                   MemoryUnit.class_id())
    if memory_units:
        for memory_unit in memory_units:
            memory_unit_obj = MemoryUnitInventory(memory_unit)
            
            env_stats = get_molist_under_parents(handle,[memory_unit],
                                        MemoryUnitEnvStats.class_id())
            if env_stats:
                for envStat in env_stats:
                    memory_unit_obj.sensor_description=envStat.get_attr(
                                        MemoryUnitEnvStats.DESCRIPTION)
                    memory_unit_obj.temperature=envStat.get_attr(
                                          MemoryUnitEnvStats.TEMPERATURE)
            
            memory_unit_inventory.append(memory_unit_obj)
        
    return memory_unit_inventory

def get_storage_controller_inventory(handle,compute_board):
    storage_controller_inventory = []
    storage_controllers = get_molist_under_parents(handle,
                                          [compute_board],
                                          StorageController.class_id())
    if storage_controllers:
        for storage_controller in storage_controllers:
            storageControllerObj = StorageControllerInventory(
                                                      storage_controller)
            
            firmwareRunningInfo = get_molist_under_parents(handle,
                                                   [storage_controller],
                                                   FirmwareRunning.class_id())
            if firmwareRunningInfo:
                for eachFR in firmwareRunningInfo:
                    storageControllerObj.firmware_deployment=eachFR.get_attr(
                                               FirmwareRunning.DEPLOYMENT)
                    storageControllerObj.firmware_version=eachFR.get_attr(
                                                FirmwareRunning.VERSION)
                
            storageControllerObj.storage_local_disks= \
                get_storage_local_disk_inventory(handle,storage_controller)
            storageControllerObj.storage_virtual_drives= \
                get_storage_virtual_drive_inventory(handle,storage_controller)
            
            storage_controller_inventory.append(storageControllerObj)
        
    return storage_controller_inventory

def get_storage_local_disk_inventory(handle,storage_controller):
    storage_local_disk_inventory = []
    storage_local_disks = get_molist_under_parents(handle,[storage_controller],
                                         StorageLocalDisk.class_id())
    if storage_local_disks:
        for storage_local_disk in storage_local_disks:
            storage_local_disk_obj = StorageLocalDiskInventory(
                                                            storage_local_disk)
            
            storage_local_disk_inventory.append(storage_local_disk_obj)
        
    return storage_local_disk_inventory

def get_storage_virtual_drive_inventory(handle,storage_controller):
    storage_virtual_drive_inventory = []
    storageVirtualDrives = get_molist_under_parents(handle,[storage_controller],
                                            StorageVirtualDrive.class_id())
    if storageVirtualDrives:
        for storageVirtualDrive in storageVirtualDrives:
            storageVirtualDriveObj = StorageVirtualDriveInventory(
                                                      storageVirtualDrive)
            
            storage_virtual_drive_inventory.append(storageVirtualDriveObj)
        
    return storage_virtual_drive_inventory

def get_pid_catalog_dimm_inventory(handle,compute_board):
    pid_catalog_dimm_inventory = []
    pid_catalog_dimms = get_molist_under_parents(handle,[compute_board],class_id = 
                                       PidCatalogDimm.class_id())
    if pid_catalog_dimms:
        for pid_catalog_dimm in pid_catalog_dimms:
            pid_catalog_dimm_obj = PidCatalogDimmInventory(pid_catalog_dimm)
            
            pid_catalog_dimm_inventory.append(pid_catalog_dimm_obj)
        
    return pid_catalog_dimm_inventory

def get_pid_catalog_pci_adapter_inventory(handle,compute_board):
    pid_catalog_pci_adapter_inventory = []
    pid_catalog_pci_adapters = get_molist_under_parents(handle,
                                             [compute_board],
                                 class_id = PidCatalogPCIAdapter.class_id())
    if pid_catalog_pci_adapters:
        for pid_catalog_pci_adapter in pid_catalog_pci_adapters:
            pid_catalog_pci_adapter_obj = PidCatalogPciAdapterInventory(
                                                    pid_catalog_pci_adapter)
            
            pid_catalog_pci_adapter_inventory.append(pid_catalog_pci_adapter_obj)
        
    return pid_catalog_pci_adapter_inventory


def get_bios_unit_inventory(handle,compute_board):
    bios_unit_inventory = []
    bios_units = get_molist_under_parents(handle,[compute_board],BiosUnit.class_id())
    if bios_units:
        for bios_unit in bios_units:
            bios_unit_obj = BiosUnitInventory(bios_unit)
            
            firmwareRunningInfo = get_molist_under_parents(handle,
                                                   [bios_unit],
                                                   FirmwareRunning.class_id())
            if firmwareRunningInfo:
                for eachFR in firmwareRunningInfo:
                    bios_unit_obj.firmware_deployment=eachFR.get_attr(
                                              FirmwareRunning.DEPLOYMENT)
                    bios_unit_obj.firmware_version=eachFR.get_attr(
                                               FirmwareRunning.VERSION)
                
            bios_unit_inventory.append(bios_unit_obj)
        
    return bios_unit_inventory

def get_temp_stat_inventory(handle,compute_board):
    temp_stat_inventory = []
    temp_stats = get_molist_under_parents(handle,[compute_board],
                                 ComputeRackUnitMbTempStats.class_id())
    if temp_stats:
        for temp_stat in temp_stats:
            temp_stat_obj = TempStatInventory(temp_stat)
               
            temp_stat_inventory.append(temp_stat_obj)
        
    return temp_stat_inventory
    
def get_power_stat_inventory(handle,compute_board):
    power_stat_inventory = []
    power_stats = get_molist_under_parents(handle,[compute_board],
                                  ComputeMbPowerStats.class_id())
    if power_stats:
        for power_stat in power_stats:
            power_stat_obj = PowerStatInventory(power_stat)
               
            power_stat_inventory.append(power_stat_obj)
        
    return power_stat_inventory

def display_object(obj):
    tabsize = 8
    outstr = "\n"
    child_list=[]
    
    outstr += "Managed Object\t\t\t: " + str(obj.class_id) + "\n"
    outstr += "-"*len("Managed Object") + "\n"
    
    for key in obj.__dict__.keys():
        if key == "class_id":
            continue
        
        val = obj.__dict__[key]
        if (isinstance(val, list) == True):
            child_list.append(key)
            continue
        
        outstr += str(key).ljust(tabsize*4) + ': ' + str(val) + "\n"
    
    for child in child_list:
        for child_obj in obj.__dict__[child]:
            outstr += display_object(child_obj)
        
    outstr += "\n"
    return outstr

def generate_html_table(obj):
    table_str = ""
    child_list=[]
    
    table_str += "<TR>"
    table_str += '<TH colspan="2" bgcolor="teal">'
    table_str += '<font color="white"/>'
    table_str += str(obj.class_id)
    table_str += "</TH>" 
    table_str += "</TR>"
    
    for key in obj.__dict__.keys():
        if key == "class_id":
            continue
        
        val = obj.__dict__[key]
        if (isinstance(val, list) == True):
            child_list.append(key)
            continue
        table_str += "<TR>"
        table_str += "<TD>"
        table_str += str(key)
        table_str += "</TD>"
        table_str += "<TD>"
        if str(val) == "":
            table_str += "---"
        else:
            table_str += str(val)
        table_str += "</TD>"
        table_str += "</TR>"
        
    for child in child_list:
        for child_obj in obj.__dict__[child]:
            table_str += generate_html_table(child_obj)
    
    return table_str

def generate_html_file(obj,file_name,imc_name):
    imc = imc_name
    myFile= open(file_name,"w")
    myFile.write("<html>")
    myFile.write("<head>")
    myFile.write("<title>Inventory Report for IMC &lt"+imc+"&gt </title>")
    myFile.write("</head>")
    myFile.write("<body>")
    myFile.write("<h2>Inventory Report for IMC &lt"+imc+"&gt </h2>")
    myFile.write('<TABLE border="2">')
    myFile.write(generate_html_table(obj))
    myFile.write("</TABLE>")
    myFile.write("</body>")
    myFile.write("</html>")
    myFile.close()

if __name__ == '__main__':
    try:
        parser = optparse.OptionParser()
        parser.add_option('-i', '--ip',dest="ip",
                          help="[Mandatory] IMC IP Address")
        parser.add_option('-u', '--username',dest="username",
                          help="[Mandatory] Account Username for IMC login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC login")
        parser.add_option('--html',dest="is_html",
                          action="store_true",
                          help="[Optional] Use for output as an htmlfile")
        parser.add_option('--filename',dest="file_name",
                          help="[Optional] name of a file")
        parser.add_option('--filepath',dest="file_path",
                          help="[Optional] Path of a file")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Provide IMC IP Address")
        if not options.username:
            parser.error("Provide IMC UserName")
            parser.print_help()
        if not options.password:
            options.password=get_password("IMC Password:")
        
        if options.is_html:
            if options.file_name is not None:
                matchObj = re.match(r".*\.html$",options.file_name)
                if not matchObj:
                    raise Exception("Should be a .html file")
                
            if options.file_path is not None:
                if not os.path.exists(options.file_path):
                    raise Exception("Invalid Path")
        
        handle=do_login(options.ip,options.username,options.password)
        print "Generating Report for IMC <"+ handle.imc + ">...."
        print "It will take few minutes....\n"
        rack_unit = get_rack_unit_inventory(handle)
        
        if options.is_html:
            if options.file_name is None:
                html_file_name="ImcInventoryReport_" + handle.imc + ".html"
            else:   
                html_file_name=options.file_name
            
            if options.file_path is not None:
                html_file_name = os.path.join(options.file_path, html_file_name)
            else:
                html_file_name = os.path.join(os.getcwd(), html_file_name)
            
            print "Preparing HTML File <" + html_file_name + ">...."
            generate_html_file(rack_unit,html_file_name,handle.imc)
        else:
            print display_object(rack_unit)
            
        print "Report generation completed successfully."
                
        do_logout()
        
    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60