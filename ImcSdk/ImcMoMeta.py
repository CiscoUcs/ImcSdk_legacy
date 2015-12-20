"""Copyright 2013 Cisco Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
""" This is an auto-generated module containing ManagedObject Meta information. """

from ImcCoreMeta import MoPropertyMeta, MoMeta, ImcVersion

class _VersionMeta(object):
    """This Class holds the version of all the supported IMC."""
    version_151f = ImcVersion("1.5(1f)")
    version_152 = ImcVersion("1.5(2)")
    version_153 = ImcVersion("1.5(3)")
    version_154 = ImcVersion("1.5(4)")
    version_201a = ImcVersion("2.0(1a)")
    version_202c = ImcVersion("2.0(2c)")
    version_203d = ImcVersion("2.0(3d)")
    version_204c = ImcVersion("2.0(4c)")

_MANAGED_OBJECT_META = {

		"LsbootVirtualMedia": {
			"Access":MoPropertyMeta("Access", "access", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x1L, None, None, None, ["read-only", "read-write"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["1", "2", "3", "4", "5"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["virtual-media"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootVirtualMedia", "lsbootVirtualMedia", "vm-[Access]", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Add", "Get"], ["admin", "read-only", "user"], [u'lsbootDef'])
			},

		"ProcessorEnvStats": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Temperature":MoPropertyMeta("Temperature", "temperature", "float", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"TimeCollected":MoPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("ProcessorEnvStats", "processorEnvStats", "env-stats", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'processorUnit'])
			},

		"BiosVfIOHResource": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpIOHResource":MoPropertyMeta("VpIOHResource", "vpIOHResource", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["IOH0 24k IOH1 40k", "IOH0 32k IOH1 32k", "IOH0 40k IOH1 24k", "IOH0 48k IOH1 16k", "IOH0 56k IOH1 8k", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfIOHResource", "biosVfIOHResource", "ioh-resource", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorFcInterruptProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Mode":MoPropertyMeta("Mode", "mode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["INTx", "MSI", "MSIx"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcInterruptProfile", "adaptorFcInterruptProfile", "fc-int", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"BiosVfSataModeSelect": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpSataModeSelect":MoPropertyMeta("VpSataModeSelect", "vpSataModeSelect", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["AHCI", "Disabled", "LSI SW RAID", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfSataModeSelect", "biosVfSataModeSelect", "Pch-Sata-Mode", _VersionMeta.version_202c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"HuuFirmwareUpdateStatus": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CurrentTime":MoPropertyMeta("CurrentTime", "currentTime", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"HuuImageVersion":MoPropertyMeta("HuuImageVersion", "huuImageVersion", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OverallStatus":MoPropertyMeta("OverallStatus", "overallStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"UpdateEndTime":MoPropertyMeta("UpdateEndTime", "updateEndTime", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"UpdateStartTime":MoPropertyMeta("UpdateStartTime", "updateStartTime", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("HuuFirmwareUpdateStatus", "huuFirmwareUpdateStatus", "updateStatus", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'huuUpdateComponentStatus'], ["Get"], ["admin", "read-only", "user"], [u'huuFirmwareUpdater'])
			},

		"IpBlocking": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Enable":MoPropertyMeta("Enable", "enable", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"FailCount":MoPropertyMeta("FailCount", "failCount", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["3-10"]),
			"FailWindow":MoPropertyMeta("FailWindow", "failWindow", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["60-120"]),
			"PenaltyTime":MoPropertyMeta("PenaltyTime", "penaltyTime", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["300-900"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("IpBlocking", "ipBlocking", "ip-block", _VersionMeta.version_151f, "InputOutput", 0x7fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'mgmtIf'])
			},

		"AdaptorFcPortProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"IoThrottleCount":MoPropertyMeta("IoThrottleCount", "ioThrottleCount", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["1-1024"]),
			"LunsPerTarget":MoPropertyMeta("LunsPerTarget", "lunsPerTarget", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-1024"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcPortProfile", "adaptorFcPortProfile", "fc-port", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"BiosVfOnboardNIC": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpOnboard10GbitLOM":MoPropertyMeta("VpOnboard10GbitLOM", "vpOnboard10GbitLOM", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpOnboardGbitLOM":MoPropertyMeta("VpOnboardGbitLOM", "vpOnboardGbitLOM", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfOnboardNIC", "biosVfOnboardNIC", "Onboard-NIC", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"LsbootSan": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Lun":MoPropertyMeta("Lun", "lun", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x4L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["1-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|MLOM|L1|L2){0,1}""", [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["SAN"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["SAN"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootSan", "lsbootSan", "san-[Name]", _VersionMeta.version_201a, "InputOutput", 0x3ffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"AdaptorFcPortPLogiProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Retries":MoPropertyMeta("Retries", "retries", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["0-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Timeout":MoPropertyMeta("Timeout", "timeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["1000-255000"]),
			"Meta":MoMeta("AdaptorFcPortPLogiProfile", "adaptorFcPortPLogiProfile", "fc-port-plogi", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"BiosVfQPIConfig": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpQPILinkFrequency":MoPropertyMeta("VpQPILinkFrequency", "vpQPILinkFrequency", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["6.4-gt/s", "7.2-gt/s", "8.0-gt/s", "auto", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfQPIConfig", "biosVfQPIConfig", "QPI-Config", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfOutOfBandMgmtPort": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_154, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_154, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_154, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpOutOfBandMgmtPort":MoPropertyMeta("VpOutOfBandMgmtPort", "vpOutOfBandMgmtPort", "string", _VersionMeta.version_154, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfOutOfBandMgmtPort", "biosVfOutOfBandMgmtPort", "OoB-MgmtPort", _VersionMeta.version_154, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"MemoryArray": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CurrCapacity":MoPropertyMeta("CurrCapacity", "currCapacity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"DimmBlackList":MoPropertyMeta("DimmBlackList", "dimmBlackList", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disable", "disabled", "enable", "enabled"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"FailedMemory":MoPropertyMeta("FailedMemory", "failedMemory", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-8"]),
			"IgnoredMemory":MoPropertyMeta("IgnoredMemory", "ignoredMemory", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"MaxDevices":MoPropertyMeta("MaxDevices", "maxDevices", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"MemoryConfiguration":MoPropertyMeta("MemoryConfiguration", "memoryConfiguration", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MemoryRASPossible":MoPropertyMeta("MemoryRASPossible", "memoryRASPossible", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NumOfFailedDimms":MoPropertyMeta("NumOfFailedDimms", "numOfFailedDimms", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NumOfIgnoredDimms":MoPropertyMeta("NumOfIgnoredDimms", "numOfIgnoredDimms", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OverallDIMMStatus":MoPropertyMeta("OverallDIMMStatus", "overallDIMMStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], ["0-4294967295"]),
			"Populated":MoPropertyMeta("Populated", "populated", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"RedundantMemory":MoPropertyMeta("RedundantMemory", "redundantMemory", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("MemoryArray", "memoryArray", "memarray-[Id]", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [u'faultInst', u'memoryUnit'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"AdaptorFcPersistentBindings": {
			"BusId":MoPropertyMeta("BusId", "busId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"HostWwpn":MoPropertyMeta("HostWwpn", "hostWwpn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
			"Index":MoPropertyMeta("Index", "index", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TargetId":MoPropertyMeta("TargetId", "targetId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"TargetWwpn":MoPropertyMeta("TargetWwpn", "targetWwpn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcPersistentBindings", "adaptorFcPersistentBindings", "perbi-[Index]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"EquipmentFanModule": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-8"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Operability":MoPropertyMeta("Operability", "operability", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Power":MoPropertyMeta("Power", "power", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Thermal":MoPropertyMeta("Thermal", "thermal", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Tray":MoPropertyMeta("Tray", "tray", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-1"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Voltage":MoPropertyMeta("Voltage", "voltage", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentFanModule", "equipmentFanModule", "fan-module-[Tray]-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'equipmentFan'], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"AdaptorEthWorkQueueProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Count":MoPropertyMeta("Count", "count", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["1-256"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"RingSize":MoPropertyMeta("RingSize", "ringSize", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["64-4096"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorEthWorkQueueProfile", "adaptorEthWorkQueueProfile", "eth-work-q", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"PidCatalog": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("PidCatalog", "pidCatalog", "pid", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'pidCatalogCpu', u'pidCatalogDimm', u'pidCatalogHdd', u'pidCatalogPCIAdapter'], ["Get"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"ComputeRackUnit": {
			"AdminPower":MoPropertyMeta("AdminPower", "adminPower", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["bmc-reset-default", "bmc-reset-immediate", "cmos-reset-immediate", "cycle-immediate", "diagnostic-interrupt", "down", "hard-reset-immediate", "policy", "soft-shut-down", "up"], ["0-4294967295"]),
			"AvailableMemory":MoPropertyMeta("AvailableMemory", "availableMemory", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ChassisSerial":MoPropertyMeta("ChassisSerial", "chassisSerial", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"MemorySpeed":MoPropertyMeta("MemorySpeed", "memorySpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "unspecified"], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumOfAdaptors":MoPropertyMeta("NumOfAdaptors", "numOfAdaptors", "byte", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumOfCores":MoPropertyMeta("NumOfCores", "numOfCores", "ulong", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumOfCoresEnabled":MoPropertyMeta("NumOfCoresEnabled", "numOfCoresEnabled", "ulong", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumOfCpus":MoPropertyMeta("NumOfCpus", "numOfCpus", "byte", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumOfEthHostIfs":MoPropertyMeta("NumOfEthHostIfs", "numOfEthHostIfs", "ushort", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumOfFcHostIfs":MoPropertyMeta("NumOfFcHostIfs", "numOfFcHostIfs", "ushort", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumOfThreads":MoPropertyMeta("NumOfThreads", "numOfThreads", "ulong", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"OperPower":MoPropertyMeta("OperPower", "operPower", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
			"OriginalUuid":MoPropertyMeta("OriginalUuid", "originalUuid", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ServerId":MoPropertyMeta("ServerId", "serverId", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TotalMemory":MoPropertyMeta("TotalMemory", "totalMemory", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"UsrLbl":MoPropertyMeta("UsrLbl", "usrLbl", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 64, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,64}""", [], ["0-4294967295"]),
			"Uuid":MoPropertyMeta("Uuid", "uuid", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F]){8}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){4}\-([0-9a-fA-F]){12})|0""", [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("ComputeRackUnit", "computeRackUnit", "rack-unit-[ServerId]", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [u'adaptorUnit', u'biosUnit', u'computeBoard', u'equipmentFanModule', u'equipmentIndicatorLed', u'equipmentLocatorLed', u'equipmentPsu', u'equipmentPsuColdRedundancy', u'faultInst', u'lsbootDef', u'lsbootDevPrecision', u'mgmtController', u'networkAdapterUnit', u'oneTimeBootDevice', u'pciEquipSlot', u'powerBudget', u'powerMonitor', u'serverUtilization', u'solIf', u'sysdebugTechSupportExport', u'systemIOController'], ["Get", "Set"], ["admin", "user"], [u'topSystem'])
			},

		"CommSyslog": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"LocalSeverity":MoPropertyMeta("LocalSeverity", "localSeverity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["alert", "critical", "debug", "emergency", "error", "informational", "notice", "warning"], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-65535"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], ["0-4294967295"]),
			"RemoteSeverity":MoPropertyMeta("RemoteSeverity", "remoteSeverity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["alert", "critical", "debug", "emergency", "error", "informational", "notice", "warning"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommSyslog", "commSyslog", "syslog", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [u'commSyslogClient'], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"BiosVfCPUPowerManagement": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCPUPowerManagement":MoPropertyMeta("VpCPUPowerManagement", "vpCPUPowerManagement", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["custom", "disabled", "energy-efficient", "performance", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCPUPowerManagement", "biosVfCPUPowerManagement", "CPU-PowerManagement", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"PidCatalogCpu": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Currentspeed":MoPropertyMeta("Currentspeed", "currentspeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OperState":MoPropertyMeta("OperState", "operState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Pid":MoPropertyMeta("Pid", "pid", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Signature":MoPropertyMeta("Signature", "signature", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Socketdesignation":MoPropertyMeta("Socketdesignation", "socketdesignation", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("PidCatalogCpu", "pidCatalogCpu", "pid-cpu-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'pidCatalog'])
			},

		"StorageOperation": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CurrentLrop":MoPropertyMeta("CurrentLrop", "currentLrop", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"ElapsedSeconds":MoPropertyMeta("ElapsedSeconds", "elapsedSeconds", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"LropInProgress":MoPropertyMeta("LropInProgress", "lropInProgress", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ProgressPercent":MoPropertyMeta("ProgressPercent", "progressPercent", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("StorageOperation", "storageOperation", "storage-operation", _VersionMeta.version_201a, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageLocalDisk', u'storageRaidBattery', u'storageVirtualDrive'])
			},

		"AdaptorIpV4RssHashProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"IpHash":MoPropertyMeta("IpHash", "ipHash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TcpHash":MoPropertyMeta("TcpHash", "tcpHash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorIpV4RssHashProfile", "adaptorIpV4RssHashProfile", "ipv4-rss-hash", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"BiosVfProcessorCState": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpProcessorCState":MoPropertyMeta("VpProcessorCState", "vpProcessorCState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfProcessorCState", "biosVfProcessorCState", "Processor-C-State", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfUSBEmulation": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpUSBEmul6064":MoPropertyMeta("VpUSBEmul6064", "vpUSBEmul6064", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfUSBEmulation", "biosVfUSBEmulation", "USBEmulation-Support", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"EquipmentPsuFan": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_202c, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-8"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Module":MoPropertyMeta("Module", "module", "uint", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-8"]),
			"Operability":MoPropertyMeta("Operability", "operability", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Power":MoPropertyMeta("Power", "power", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Thermal":MoPropertyMeta("Thermal", "thermal", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Tray":MoPropertyMeta("Tray", "tray", "uint", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-8"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Voltage":MoPropertyMeta("Voltage", "voltage", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentPsuFan", "equipmentPsuFan", "fan-[Id]", _VersionMeta.version_202c, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'equipmentPsu'])
			},

		"SolIf": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disable", "enable"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Comport":MoPropertyMeta("Comport", "comport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["com0", "com1"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Speed":MoPropertyMeta("Speed", "speed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["115200", "19200", "38400", "57600", "9600"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("SolIf", "solIf", "sol-if", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"BiosVfIntelVTForDirectedIO": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpIntelVTDATSSupport":MoPropertyMeta("VpIntelVTDATSSupport", "vpIntelVTDATSSupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpIntelVTDCoherencySupport":MoPropertyMeta("VpIntelVTDCoherencySupport", "vpIntelVTDCoherencySupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpIntelVTDInterruptRemapping":MoPropertyMeta("VpIntelVTDInterruptRemapping", "vpIntelVTDInterruptRemapping", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpIntelVTDPassThroughDMASupport":MoPropertyMeta("VpIntelVTDPassThroughDMASupport", "vpIntelVTDPassThroughDMASupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpIntelVTForDirectedIO":MoPropertyMeta("VpIntelVTForDirectedIO", "vpIntelVTForDirectedIO", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfIntelVTForDirectedIO", "biosVfIntelVTForDirectedIO", "Intel-VT-for-directed-IO", _VersionMeta.version_151f, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfPchUsb30Mode": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPchUsb30Mode":MoPropertyMeta("VpPchUsb30Mode", "vpPchUsb30Mode", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPchUsb30Mode", "biosVfPchUsb30Mode", "PchUsb30-Mode", _VersionMeta.version_202c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorConnectorInfo": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_204c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"PartNumber":MoPropertyMeta("PartNumber", "partNumber", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"PartRevision":MoPropertyMeta("PartRevision", "partRevision", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Present":MoPropertyMeta("Present", "present", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Supported":MoPropertyMeta("Supported", "supported", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorConnectorInfo", "adaptorConnectorInfo", "connector-info", _VersionMeta.version_204c, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'adaptorExtEthIf'])
			},

		"FirmwareBootUnit": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"IgnoreCompCheck":MoPropertyMeta("IgnoreCompCheck", "ignoreCompCheck", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
			"Image":MoPropertyMeta("Image", "image", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["backup", "running"], ["0-4294967295"]),
			"OperState":MoPropertyMeta("OperState", "operState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating"], ["0-4294967295"]),
			"ResetOnActivate":MoPropertyMeta("ResetOnActivate", "resetOnActivate", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Version":MoPropertyMeta("Version", "version", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("FirmwareBootUnit", "firmwareBootUnit", "bootunit-[Type]", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'firmwareBootDefinition'])
			},

		"FirmwareBootDefinition": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "fex", "sioc", "storage-controller", "system"], ["0-4294967295"]),
			"Meta":MoMeta("FirmwareBootDefinition", "firmwareBootDefinition", "fw-boot-def", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'firmwareBootUnit'], ["Get"], ["admin", "read-only", "user"], [u'biosUnit', u'mgmtController', u'storageController', u'systemIOController'])
			},

		"StandardPowerProfile": {
			"AllowThrottle":MoPropertyMeta("AllowThrottle", "allowThrottle", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CorrAction":MoPropertyMeta("CorrAction", "corrAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["alert", "alert,shutdown", "none", "shutdown"], ["0-4294967295"]),
			"CorrTime":MoPropertyMeta("CorrTime", "corrTime", "uint", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"HardCap":MoPropertyMeta("HardCap", "hardCap", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"PowerLimit":MoPropertyMeta("PowerLimit", "powerLimit", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], ["0-4294967295"]),
			"ProfileEnabled":MoPropertyMeta("ProfileEnabled", "profileEnabled", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"ProfileType":MoPropertyMeta("ProfileType", "profileType", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"SuspendPeriod":MoPropertyMeta("SuspendPeriod", "suspendPeriod", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x200L, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StandardPowerProfile", "standardPowerProfile", "stdpwrprof", _VersionMeta.version_202c, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'powerBudget'])
			},

		"AdaptorUnit": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["adaptor-reset", "adaptor-reset-default", "policy"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CimcManagementEnabled":MoPropertyMeta("CimcManagementEnabled", "cimcManagementEnabled", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 64, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], ["0-20"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PciAddr":MoPropertyMeta("PciAddr", "pciAddr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PciSlot":MoPropertyMeta("PciSlot", "pciSlot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "missing", "not-supported", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorUnit", "adaptorUnit", "adaptor-[Id]", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [u'adaptorCfgBackup', u'adaptorCfgImporter', u'adaptorExtEthIf', u'adaptorGenProfile', u'adaptorHostEthIf', u'adaptorHostFcIf', u'adaptorVMFexEthIf', u'faultInst', u'mgmtController'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"SysdebugMEpLog": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["backup", "clear", "policy"], ["0-4294967295"]),
			"Capacity":MoPropertyMeta("Capacity", "capacity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["available", "full", "low", "unknown", "very-low"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-8"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x10L, None, None, None, ["OBFL", "SEL", "Syslog"], ["0-4294967295"]),
			"Meta":MoMeta("SysdebugMEpLog", "sysdebugMEpLog", "log-[Type]-[Id]", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [u'faultInst'], ["Get", "Set"], ["admin", "read-only", "user"], [u'mgmtController'])
			},

		"BiosVfPOSTErrorPause": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPOSTErrorPause":MoPropertyMeta("VpPOSTErrorPause", "vpPOSTErrorPause", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPOSTErrorPause", "biosVfPOSTErrorPause", "POST-error-pause", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"LsbootSd": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x2L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["SDCARD"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["SDCARD"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootSd", "lsbootSd", "sd-[Name]", _VersionMeta.version_201a, "InputOutput", 0xffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"CommNtpProvider": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"NtpEnable":MoPropertyMeta("NtpEnable", "ntpEnable", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"NtpServer1":MoPropertyMeta("NtpServer1", "ntpServer1", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"NtpServer2":MoPropertyMeta("NtpServer2", "ntpServer2", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"NtpServer3":MoPropertyMeta("NtpServer3", "ntpServer3", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"NtpServer4":MoPropertyMeta("NtpServer4", "ntpServer4", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommNtpProvider", "commNtpProvider", "ntp-svc", _VersionMeta.version_151f, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"BiosVfLOMPortOptionROM": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpLOMPort0State":MoPropertyMeta("VpLOMPort0State", "vpLOMPort0State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpLOMPort1State":MoPropertyMeta("VpLOMPort1State", "vpLOMPort1State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpLOMPort2State":MoPropertyMeta("VpLOMPort2State", "vpLOMPort2State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpLOMPort3State":MoPropertyMeta("VpLOMPort3State", "vpLOMPort3State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpLOMPortsAllState":MoPropertyMeta("VpLOMPortsAllState", "vpLOMPortsAllState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfLOMPortOptionROM", "biosVfLOMPortOptionROM", "LOMPort-OptionROM", _VersionMeta.version_151f, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfOnboardStorage": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpOnboardSCUStorageSupport":MoPropertyMeta("VpOnboardSCUStorageSupport", "vpOnboardSCUStorageSupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfOnboardStorage", "biosVfOnboardStorage", "Onboard-Storage", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosBOT": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("BiosBOT", "biosBOT", "bdgep", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'biosBootDevGrp', u'biosBootDevPrecision', u'biosBootMode'], ["Get"], ["admin", "read-only", "user"], [u'biosUnit'])
			},

		"BiosVfMirroringMode": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpMirroringMode":MoPropertyMeta("VpMirroringMode", "vpMirroringMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["inter-socket", "intra-socket", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfMirroringMode", "biosVfMirroringMode", "Mirroring-Mode", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorCfgImporter": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Progress":MoPropertyMeta("Progress", "progress", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], ["0-4294967295"]),
			"Pwd":MoPropertyMeta("Pwd", "pwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, None, [], ["0-4294967295"]),
			"RemoteFile":MoPropertyMeta("RemoteFile", "remoteFile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, 0, 256, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorCfgImporter", "adaptorCfgImporter", "import-config", _VersionMeta.version_151f, "InputOutput", 0x1ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorUnit'])
			},

		"StorageControllerSettings": {
			"AutoEnhancedImport":MoPropertyMeta("AutoEnhancedImport", "autoEnhancedImport", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BatteryWarning":MoPropertyMeta("BatteryWarning", "batteryWarning", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CacheFlushInterval":MoPropertyMeta("CacheFlushInterval", "cacheFlushInterval", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ClusterEnable":MoPropertyMeta("ClusterEnable", "clusterEnable", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ConsistencyCheckRate":MoPropertyMeta("ConsistencyCheckRate", "consistencyCheckRate", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"EccBucketLeakRate":MoPropertyMeta("EccBucketLeakRate", "eccBucketLeakRate", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"EnableCopybackOnSmart":MoPropertyMeta("EnableCopybackOnSmart", "enableCopybackOnSmart", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"EnableCopybackToSsdOnSmartError":MoPropertyMeta("EnableCopybackToSsdOnSmartError", "enableCopybackToSsdOnSmartError", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"EnableJbod":MoPropertyMeta("EnableJbod", "enableJbod", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"EnableSsdPatrolRead":MoPropertyMeta("EnableSsdPatrolRead", "enableSsdPatrolRead", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ExposeEnclosureDevices":MoPropertyMeta("ExposeEnclosureDevices", "exposeEnclosureDevices", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MaintainPdFailHistory":MoPropertyMeta("MaintainPdFailHistory", "maintainPdFailHistory", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NcqStatus":MoPropertyMeta("NcqStatus", "ncqStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PatrolReadRate":MoPropertyMeta("PatrolReadRate", "patrolReadRate", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PciSlot":MoPropertyMeta("PciSlot", "pciSlot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysDriveCoercionMode":MoPropertyMeta("PhysDriveCoercionMode", "physDriveCoercionMode", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PredictiveFailPollInterval":MoPropertyMeta("PredictiveFailPollInterval", "predictiveFailPollInterval", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RebuildRate":MoPropertyMeta("RebuildRate", "rebuildRate", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ReconstructionRate":MoPropertyMeta("ReconstructionRate", "reconstructionRate", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"SpinDownUnconfigured":MoPropertyMeta("SpinDownUnconfigured", "spinDownUnconfigured", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SpinupDelay":MoPropertyMeta("SpinupDelay", "spinupDelay", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SpinupDriveCount":MoPropertyMeta("SpinupDriveCount", "spinupDriveCount", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("StorageControllerSettings", "storageControllerSettings", "controller-settings", _VersionMeta.version_201a, "InputOutput", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageController'])
			},

		"BiosVfDemandScrub": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpDemandScrub":MoPropertyMeta("VpDemandScrub", "vpDemandScrub", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfDemandScrub", "biosVfDemandScrub", "Demand-Scrub-Param", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"CommSnmpUser": {
			"Auth":MoPropertyMeta("Auth", "auth", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["", "MD5", "SHA"], ["0-4294967295"]),
			"AuthPwd":MoPropertyMeta("AuthPwd", "authPwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""(.{8,64})?""", [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], ["1-15"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 31, None, [], ["0-4294967295"]),
			"Privacy":MoPropertyMeta("Privacy", "privacy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "AES", "DES"], ["0-4294967295"]),
			"PrivacyPwd":MoPropertyMeta("PrivacyPwd", "privacyPwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""(.{8,64})?""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"SecurityLevel":MoPropertyMeta("SecurityLevel", "securityLevel", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "authnopriv", "authpriv", "noauthnopriv"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommSnmpUser", "commSnmpUser", "snmpv3-user-[Id]", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSnmp'])
			},

		"BiosVfPackageCStateLimit": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPackageCStateLimit":MoPropertyMeta("VpPackageCStateLimit", "vpPackageCStateLimit", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["C0/C1", "C2", "C6 Retention", "C6 non Retention", "c0-state", "c1-state", "c3-state", "c6-state", "no-limit", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPackageCStateLimit", "biosVfPackageCStateLimit", "Package-CState-Limit", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfCPUEnergyPerformance": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCPUEnergyPerformance":MoPropertyMeta("VpCPUEnergyPerformance", "vpCPUEnergyPerformance", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["balanced-energy", "balanced-performance", "energy-efficient", "performance", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCPUEnergyPerformance", "biosVfCPUEnergyPerformance", "CPU-EngPerfBias", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfUSBPortsConfig": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpAllUsbDevices":MoPropertyMeta("VpAllUsbDevices", "vpAllUsbDevices", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpUsbPortFront":MoPropertyMeta("VpUsbPortFront", "vpUsbPortFront", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpUsbPortInternal":MoPropertyMeta("VpUsbPortInternal", "vpUsbPortInternal", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpUsbPortKVM":MoPropertyMeta("VpUsbPortKVM", "vpUsbPortKVM", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpUsbPortRear":MoPropertyMeta("VpUsbPortRear", "vpUsbPortRear", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpUsbPortSDCard":MoPropertyMeta("VpUsbPortSDCard", "vpUsbPortSDCard", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpUsbPortVMedia":MoPropertyMeta("VpUsbPortVMedia", "vpUsbPortVMedia", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfUSBPortsConfig", "biosVfUSBPortsConfig", "USB-Ports-Config", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageRaidBattery": {
			"AbsoluteStateOfCharge":MoPropertyMeta("AbsoluteStateOfCharge", "absoluteStateOfCharge", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["disable-auto-learn", "enable-auto-learn", "start-learn-cycle"], ["0-4294967295"]),
			"BatteryPresent":MoPropertyMeta("BatteryPresent", "batteryPresent", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BatteryStatus":MoPropertyMeta("BatteryStatus", "batteryStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BatteryType":MoPropertyMeta("BatteryType", "batteryType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChargingState":MoPropertyMeta("ChargingState", "chargingState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CompletedChargeCycles":MoPropertyMeta("CompletedChargeCycles", "completedChargeCycles", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Current":MoPropertyMeta("Current", "current", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DateOfManufacture":MoPropertyMeta("DateOfManufacture", "dateOfManufacture", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DesignCapacity":MoPropertyMeta("DesignCapacity", "designCapacity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DesignVoltage":MoPropertyMeta("DesignVoltage", "designVoltage", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"ExpectedMarginOfError":MoPropertyMeta("ExpectedMarginOfError", "expectedMarginOfError", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"FirmwareVersion":MoPropertyMeta("FirmwareVersion", "firmwareVersion", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"FullCapacity":MoPropertyMeta("FullCapacity", "fullCapacity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"LearnCycleRequested":MoPropertyMeta("LearnCycleRequested", "learnCycleRequested", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"LearnCycleStatus":MoPropertyMeta("LearnCycleStatus", "learnCycleStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"LearnMode":MoPropertyMeta("LearnMode", "learnMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Manufacturer":MoPropertyMeta("Manufacturer", "manufacturer", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NextLearnCycle":MoPropertyMeta("NextLearnCycle", "nextLearnCycle", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RelativeStateOfCharge":MoPropertyMeta("RelativeStateOfCharge", "relativeStateOfCharge", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RemainingCapacity":MoPropertyMeta("RemainingCapacity", "remainingCapacity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RetentionTime":MoPropertyMeta("RetentionTime", "retentionTime", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"SerialNumber":MoPropertyMeta("SerialNumber", "serialNumber", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Temperature":MoPropertyMeta("Temperature", "temperature", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"TemperatureHigh":MoPropertyMeta("TemperatureHigh", "temperatureHigh", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Voltage":MoPropertyMeta("Voltage", "voltage", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageRaidBattery", "storageRaidBattery", "raid-battery", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [u'faultInst', u'storageOperation'], ["Get", "Set"], ["admin", "read-only", "user"], [u'storageController'])
			},

		"BiosVfResumeOnACPowerLoss": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Delay":MoPropertyMeta("Delay", "delay", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["0-240"]),
			"DelayType":MoPropertyMeta("DelayType", "delayType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["fixed", "random"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpResumeOnACPowerLoss":MoPropertyMeta("VpResumeOnACPowerLoss", "vpResumeOnACPowerLoss", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["last-state", "platform-default", "reset", "stay-off"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfResumeOnACPowerLoss", "biosVfResumeOnACPowerLoss", "Resume-on-AC-power-loss", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"BiosVfExtendedAPIC": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpExtendedAPIC":MoPropertyMeta("VpExtendedAPIC", "vpExtendedAPIC", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "X2APIC", "XAPIC", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfExtendedAPIC", "biosVfExtendedAPIC", "Extended-APIC", _VersionMeta.version_201a, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorFcErrorRecoveryProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"ErrorDetectTimeout":MoPropertyMeta("ErrorDetectTimeout", "errorDetectTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["1000-100000"]),
			"FcpErrorRecovery":MoPropertyMeta("FcpErrorRecovery", "fcpErrorRecovery", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"LinkDownTimeout":MoPropertyMeta("LinkDownTimeout", "linkDownTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["0-240000"]),
			"PortDownIoRetryCount":MoPropertyMeta("PortDownIoRetryCount", "portDownIoRetryCount", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["0-255"]),
			"PortDownTimeout":MoPropertyMeta("PortDownTimeout", "portDownTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["0-240000"]),
			"ResourceAllocationTimeout":MoPropertyMeta("ResourceAllocationTimeout", "resourceAllocationTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], ["5000-100000"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcErrorRecoveryProfile", "adaptorFcErrorRecoveryProfile", "fc-err-rec", _VersionMeta.version_151f, "InputOutput", 0x1ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"CommVMediaMap": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"DriveType":MoPropertyMeta("DriveType", "driveType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cd", "floppy"], ["0-4294967295"]),
			"Map":MoPropertyMeta("Map", "map", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["cifs", "nfs", "www"], ["0-4294967295"]),
			"MappingStatus":MoPropertyMeta("MappingStatus", "mappingStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"MountOptions":MoPropertyMeta("MountOptions", "mountOptions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 1, 248, None, [], ["0-4294967295"]),
			"Password":MoPropertyMeta("Password", "password", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["0-4294967295"]),
			"RemoteFile":MoPropertyMeta("RemoteFile", "remoteFile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], ["0-4294967295"]),
			"RemoteShare":MoPropertyMeta("RemoteShare", "remoteShare", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Username":MoPropertyMeta("Username", "username", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, [], ["0-4294967295"]),
			"VolumeName":MoPropertyMeta("VolumeName", "volumeName", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x200L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,47}""", [], ["0-4294967295"]),
			"Meta":MoMeta("CommVMediaMap", "commVMediaMap", "vmmap-[VolumeName]", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], ["Add", "Get"], ["admin", "read-only", "user"], [u'commVMedia'])
			},

		"LsbootPchStorage": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Lun":MoPropertyMeta("Lun", "lun", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x4L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["1-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["PCHSTORAGE"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootPchStorage", "lsbootPchStorage", "pchstorage-[Name]", _VersionMeta.version_201a, "InputOutput", 0xffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"BiosVfCDNEnable": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCDNEnable":MoPropertyMeta("VpCDNEnable", "vpCDNEnable", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCDNEnable", "biosVfCDNEnable", "CDN-Enable", _VersionMeta.version_204c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"CommKvm": {
			"ActiveSessions":MoPropertyMeta("ActiveSessions", "activeSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"EncryptionState":MoPropertyMeta("EncryptionState", "encryptionState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"LocalVideoState":MoPropertyMeta("LocalVideoState", "localVideoState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["1-65535"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TotalSessions":MoPropertyMeta("TotalSessions", "totalSessions", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], ["1-4"]),
			"Meta":MoMeta("CommKvm", "commKvm", "kvm-svc", _VersionMeta.version_151f, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"LsbootDef": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Purpose":MoPropertyMeta("Purpose", "purpose", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], ["0-4294967295"]),
			"RebootOnUpdate":MoPropertyMeta("RebootOnUpdate", "rebootOnUpdate", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootDef", "lsbootDef", "boot-policy", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [u'lsbootBootSecurity', u'lsbootEfi', u'lsbootLan', u'lsbootStorage', u'lsbootVirtualMedia'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"AdaptorEthRecvQueueProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Count":MoPropertyMeta("Count", "count", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["1-256"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"RingSize":MoPropertyMeta("RingSize", "ringSize", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["64-4096"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorEthRecvQueueProfile", "adaptorEthRecvQueueProfile", "eth-rcv-q", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"AdaptorEthOffloadProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"LargeReceive":MoPropertyMeta("LargeReceive", "largeReceive", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TcpRxChecksum":MoPropertyMeta("TcpRxChecksum", "tcpRxChecksum", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TcpSegment":MoPropertyMeta("TcpSegment", "tcpSegment", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TcpTxChecksum":MoPropertyMeta("TcpTxChecksum", "tcpTxChecksum", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorEthOffloadProfile", "adaptorEthOffloadProfile", "eth-offload", _VersionMeta.version_151f, "InputOutput", 0x7fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"LsbootHdd": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x2L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|M|HBA|SAS){0,1}""", [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["LOCALHDD"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["LOCALHDD"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootHdd", "lsbootHdd", "hdd-[Name]", _VersionMeta.version_201a, "InputOutput", 0x1ffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"PidCatalogDimm": {
			"Capacity":MoPropertyMeta("Capacity", "capacity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Datawidth":MoPropertyMeta("Datawidth", "datawidth", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Manufacturer":MoPropertyMeta("Manufacturer", "manufacturer", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Mfgid":MoPropertyMeta("Mfgid", "mfgid", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Operability":MoPropertyMeta("Operability", "operability", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Pid":MoPropertyMeta("Pid", "pid", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serialnumber":MoPropertyMeta("Serialnumber", "serialnumber", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Speed":MoPropertyMeta("Speed", "speed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("PidCatalogDimm", "pidCatalogDimm", "pid-dimm-[Name]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'pidCatalog'])
			},

		"BiosVfCPUPerformance": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCPUPerformance":MoPropertyMeta("VpCPUPerformance", "vpCPUPerformance", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["custom", "enterprise", "high-throughput", "hpc", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCPUPerformance", "biosVfCPUPerformance", "CPU-Performance", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorFcRecvQueueProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"RingSize":MoPropertyMeta("RingSize", "ringSize", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["64-128"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcRecvQueueProfile", "adaptorFcRecvQueueProfile", "fc-rcv-q", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"AdaptorEthInterruptProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CoalescingTime":MoPropertyMeta("CoalescingTime", "coalescingTime", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["0-65535"]),
			"CoalescingType":MoPropertyMeta("CoalescingType", "coalescingType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["IDLE", "MIN"], ["0-4294967295"]),
			"Count":MoPropertyMeta("Count", "count", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-514"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Mode":MoPropertyMeta("Mode", "mode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["INTx", "MSI", "MSIx"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorEthInterruptProfile", "adaptorEthInterruptProfile", "eth-int", _VersionMeta.version_151f, "InputOutput", 0x7fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"AaaLdapRoleGroup": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["clear"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Domain":MoPropertyMeta("Domain", "domain", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 1, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], ["1-28"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 127, r"""([^+\-][a-zA-Z0-9=!#$%()*+,-.:;@ _{|}~?&]*){0,127}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"Role":MoPropertyMeta("Role", "role", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "admin", "read-only", "user"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AaaLdapRoleGroup", "aaaLdapRoleGroup", "rolegroup-[Id]", _VersionMeta.version_151f, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'aaaLdap'])
			},

		"AdaptorLinkTraining": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_204c, MoPropertyMeta.INTERNAL, 0x1L, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"LinkTraining":MoPropertyMeta("LinkTraining", "linkTraining", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["off", "on"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorLinkTraining", "adaptorLinkTraining", "link-training", _VersionMeta.version_204c, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "user"], [u'adaptorExtEthIf'])
			},

		"StorageFlexFlashController": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["configure-cards", "configure-firmware-mode", "reset-flexflash-controller", "reset-partition-default", "sync-card-configuration"], ["0-4294967295"]),
			"AutoSync":MoPropertyMeta("AutoSync", "autoSync", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"CardSlot":MoPropertyMeta("CardSlot", "cardSlot", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, 0, 510, None, ["none", "slot-1", "slot-2"], ["0-4294967295"]),
			"CardsManageable":MoPropertyMeta("CardsManageable", "cardsManageable", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ConfiguredMode":MoPropertyMeta("ConfiguredMode", "configuredMode", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, 0x8L, None, None, None, ["mirror", "util"], ["0-4294967295"]),
			"ControllerStatus":MoPropertyMeta("ControllerStatus", "controllerStatus", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"FwVersion":MoPropertyMeta("FwVersion", "fwVersion", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_202c, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"InternalState":MoPropertyMeta("InternalState", "internalState", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NonUtilPartitionName":MoPropertyMeta("NonUtilPartitionName", "nonUtilPartitionName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, [], ["0-4294967295"]),
			"PartitionName":MoPropertyMeta("PartitionName", "partitionName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], ["0-4294967295"]),
			"ProductName":MoPropertyMeta("ProductName", "productName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"RunningFwVersion":MoPropertyMeta("RunningFwVersion", "runningFwVersion", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"StartupFwVersion":MoPropertyMeta("StartupFwVersion", "startupFwVersion", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageFlexFlashController", "storageFlexFlashController", "storage-flexflash-[Id]", _VersionMeta.version_202c, "InputOutput", 0x1ffL, [], [u'faultInst', u'storageFlexFlashControllerProps', u'storageFlexFlashOperationalProfile', u'storageFlexFlashPhysicalDrive', u'storageFlexFlashVirtualDrive', u'storageFlexFlashVirtualDriveImageMap'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"BiosVfCoreMultiProcessing": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCoreMultiProcessing":MoPropertyMeta("VpCoreMultiProcessing", "vpCoreMultiProcessing", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["1", "10", "11", "12", "13", "14", "2", "3", "4", "5", "6", "7", "8", "9", "all", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCoreMultiProcessing", "biosVfCoreMultiProcessing", "Core-MultiProcessing", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorCfgBackup": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Progress":MoPropertyMeta("Progress", "progress", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], ["0-4294967295"]),
			"Pwd":MoPropertyMeta("Pwd", "pwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, None, [], ["0-4294967295"]),
			"RemoteFile":MoPropertyMeta("RemoteFile", "remoteFile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, 0, 256, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorCfgBackup", "adaptorCfgBackup", "export-config", _VersionMeta.version_151f, "InputOutput", 0x1ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorUnit'])
			},

		"StorageVirtualDriveWithDriveGroupSpace": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"MaxAvailableSpace":MoPropertyMeta("MaxAvailableSpace", "maxAvailableSpace", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RaidLevel":MoPropertyMeta("RaidLevel", "raidLevel", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"UsedPhysicalDriveIds":MoPropertyMeta("UsedPhysicalDriveIds", "usedPhysicalDriveIds", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VdStatus":MoPropertyMeta("VdStatus", "vdStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageVirtualDriveWithDriveGroupSpace", "storageVirtualDriveWithDriveGroupSpace", "vd-[Id]", _VersionMeta.version_201a, "InputOutput", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageVirtualDriveCreatorUsingVirtualDriveGroup'])
			},

		"EquipmentTpm": {
			"ActiveStatus":MoPropertyMeta("ActiveStatus", "activeStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activated", "deactivated", "unknown"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"EnabledStatus":MoPropertyMeta("EnabledStatus", "enabledStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["disabled", "enabled", "unknown"], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Ownership":MoPropertyMeta("Ownership", "ownership", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["owned", "unknown", "unowned"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"TpmRevision":MoPropertyMeta("TpmRevision", "tpmRevision", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Version":MoPropertyMeta("Version", "version", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentTpm", "equipmentTpm", "tpm", _VersionMeta.version_201a, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"], [u'computeBoard'])
			},

		"AdaptorFcBootTable": {
			"BootLun":MoPropertyMeta("BootLun", "bootLun", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["0-255"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Index":MoPropertyMeta("Index", "index", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], ["0-3"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TargetWwpn":MoPropertyMeta("TargetWwpn", "targetWwpn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcBootTable", "adaptorFcBootTable", "fcboot-[Index]", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Add", "Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"BiosVfIntelHyperThreadingTech": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpIntelHyperThreadingTech":MoPropertyMeta("VpIntelHyperThreadingTech", "vpIntelHyperThreadingTech", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfIntelHyperThreadingTech", "biosVfIntelHyperThreadingTech", "Intel-HyperThreading-Tech", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfMemoryMappedIOAbove4GB": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpMemoryMappedIOAbove4GB":MoPropertyMeta("VpMemoryMappedIOAbove4GB", "vpMemoryMappedIOAbove4GB", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfMemoryMappedIOAbove4GB", "biosVfMemoryMappedIOAbove4GB", "Memory-mapped-IO-above-4GB", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfEnhancedIntelSpeedStepTech": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpEnhancedIntelSpeedStepTech":MoPropertyMeta("VpEnhancedIntelSpeedStepTech", "vpEnhancedIntelSpeedStepTech", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfEnhancedIntelSpeedStepTech", "biosVfEnhancedIntelSpeedStepTech", "Enhanced-Intel-SpeedStep-Tech", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorHostFcIf": {
			"AdminPersistentBindings":MoPropertyMeta("AdminPersistentBindings", "adminPersistentBindings", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["policy", "rebuild"], ["0-4294967295"]),
			"ChannelNumber":MoPropertyMeta("ChannelNumber", "channelNumber", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["1-1000"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"IfType":MoPropertyMeta("IfType", "ifType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x8L, None, None, r"""[a-zA-Z0-9\-\._:]{1,31}""", [], ["0-4294967295"]),
			"PortProfile":MoPropertyMeta("PortProfile", "portProfile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[a-zA-Z0-9_\-]{0,80}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"SanBoot":MoPropertyMeta("SanBoot", "sanBoot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"UplinkPort":MoPropertyMeta("UplinkPort", "uplinkPort", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["0", "1"], ["0-4294967295"]),
			"Wwnn":MoPropertyMeta("Wwnn", "wwnn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["AUTO"], ["0-4294967295"]),
			"Wwpn":MoPropertyMeta("Wwpn", "wwpn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", ["AUTO"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorHostFcIf", "adaptorHostFcIf", "host-fc-[Name]", _VersionMeta.version_151f, "InputOutput", 0x7ffL, [], [u'adaptorFcBootTable', u'adaptorFcCdbWorkQueueProfile', u'adaptorFcErrorRecoveryProfile', u'adaptorFcGenProfile', u'adaptorFcInterruptProfile', u'adaptorFcPersistentBindings', u'adaptorFcPortFLogiProfile', u'adaptorFcPortPLogiProfile', u'adaptorFcPortProfile', u'adaptorFcRecvQueueProfile', u'adaptorFcWorkQueueProfile'], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'adaptorUnit'])
			},

		"IodSnapshotCancel": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_152, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TimeOut":MoPropertyMeta("TimeOut", "timeOut", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["30-240"]),
			"Meta":MoMeta("IodSnapshotCancel", "iodSnapshotCancel", "snapshotCancel", _VersionMeta.version_152, "InputOutput", 0x1fL, [], [], [None], ["admin"], [u'iodController'])
			},

		"AdaptorHostEthIf": {
			"Cdn":MoPropertyMeta("Cdn", "cdn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, None, None, r"""[a-zA-Z0-9\-\._:]{0,32}""", [], ["0-4294967295"]),
			"ChannelNumber":MoPropertyMeta("ChannelNumber", "channelNumber", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["1-1000"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ClassOfService":MoPropertyMeta("ClassOfService", "classOfService", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[0-6]""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"IfType":MoPropertyMeta("IfType", "ifType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], ["0-4294967295"]),
			"IscsiBoot":MoPropertyMeta("IscsiBoot", "iscsiBoot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Mac":MoPropertyMeta("Mac", "mac", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["AUTO"], ["0-4294967295"]),
			"Mtu":MoPropertyMeta("Mtu", "mtu", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["1500-9000"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x40L, None, None, r"""[a-zA-Z0-9\-\._:]{1,31}""", [], ["0-4294967295"]),
			"PortProfile":MoPropertyMeta("PortProfile", "portProfile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""[a-zA-Z0-9_\-]{0,80}""", [], ["0-4294967295"]),
			"PxeBoot":MoPropertyMeta("PxeBoot", "pxeBoot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"UplinkPort":MoPropertyMeta("UplinkPort", "uplinkPort", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["0", "1"], ["0-4294967295"]),
			"UsnicCount":MoPropertyMeta("UsnicCount", "usnicCount", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-225"]),
			"Meta":MoMeta("AdaptorHostEthIf", "adaptorHostEthIf", "host-eth-[Name]", _VersionMeta.version_151f, "InputOutput", 0xfffL, [], [u'adaptorEthCompQueueProfile', u'adaptorEthGenProfile', u'adaptorEthISCSIProfile', u'adaptorEthInterruptProfile', u'adaptorEthOffloadProfile', u'adaptorEthRecvQueueProfile', u'adaptorEthUSNICProfile', u'adaptorEthWorkQueueProfile', u'adaptorExtIpV6RssHashProfile', u'adaptorIpV4RssHashProfile', u'adaptorIpV6RssHashProfile', u'adaptorRssProfile'], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'adaptorUnit'])
			},

		"AdaptorEthISCSIProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"DhcpISCSI":MoPropertyMeta("DhcpISCSI", "dhcpISCSI", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"DhcpId":MoPropertyMeta("DhcpId", "dhcpId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 64, None, [], ["0-4294967295"]),
			"DhcpNetworkSettings":MoPropertyMeta("DhcpNetworkSettings", "dhcpNetworkSettings", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"DhcpTimeout":MoPropertyMeta("DhcpTimeout", "dhcpTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["60-300"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"InitiatorChapName":MoPropertyMeta("InitiatorChapName", "initiatorChapName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[a-zA-Z0-9]{0,50}""", [], ["0-4294967295"]),
			"InitiatorChapSecret":MoPropertyMeta("InitiatorChapSecret", "initiatorChapSecret", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,50}""", [], ["0-4294967295"]),
			"InitiatorGateway":MoPropertyMeta("InitiatorGateway", "initiatorGateway", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"InitiatorIPAddress":MoPropertyMeta("InitiatorIPAddress", "initiatorIPAddress", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"InitiatorName":MoPropertyMeta("InitiatorName", "initiatorName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""[0-9a-zA-Z\.:-]{0,223}""", [], ["0-4294967295"]),
			"InitiatorPrimaryDns":MoPropertyMeta("InitiatorPrimaryDns", "initiatorPrimaryDns", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"InitiatorSecondaryDns":MoPropertyMeta("InitiatorSecondaryDns", "initiatorSecondaryDns", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x800L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"InitiatorSubnetMask":MoPropertyMeta("InitiatorSubnetMask", "initiatorSubnetMask", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"InitiatorTCPTimeout":MoPropertyMeta("InitiatorTCPTimeout", "initiatorTCPTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, [], ["0-255"]),
			"IpVer":MoPropertyMeta("IpVer", "ipVer", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"LinkBusyRetryCount":MoPropertyMeta("LinkBusyRetryCount", "linkBusyRetryCount", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, [], ["0-255"]),
			"LinkupTimeout":MoPropertyMeta("LinkupTimeout", "linkupTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, [], ["0-255"]),
			"PrimaryTargetBootLun":MoPropertyMeta("PrimaryTargetBootLun", "primaryTargetBootLun", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, None, [], ["0-65535"]),
			"PrimaryTargetChapName":MoPropertyMeta("PrimaryTargetChapName", "primaryTargetChapName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, r"""[a-zA-Z0-9]{0,50}""", [], ["0-4294967295"]),
			"PrimaryTargetChapSecret":MoPropertyMeta("PrimaryTargetChapSecret", "primaryTargetChapSecret", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,50}""", [], ["0-4294967295"]),
			"PrimaryTargetIPAddress":MoPropertyMeta("PrimaryTargetIPAddress", "primaryTargetIPAddress", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80000L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"PrimaryTargetName":MoPropertyMeta("PrimaryTargetName", "primaryTargetName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100000L, None, None, r"""[0-9a-zA-Z\.:-]{0,223}""", [], ["0-4294967295"]),
			"PrimaryTargetPort":MoPropertyMeta("PrimaryTargetPort", "primaryTargetPort", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200000L, 0, 255, None, [], ["0-4294967295"]),
			"SecondaryTargetBootLun":MoPropertyMeta("SecondaryTargetBootLun", "secondaryTargetBootLun", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400000L, None, None, None, [], ["0-65535"]),
			"SecondaryTargetChapName":MoPropertyMeta("SecondaryTargetChapName", "secondaryTargetChapName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x800000L, None, None, r"""[a-zA-Z0-9]{0,50}""", [], ["0-4294967295"]),
			"SecondaryTargetChapSecret":MoPropertyMeta("SecondaryTargetChapSecret", "secondaryTargetChapSecret", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1000000L, None, None, r"""[!""#%&'\(\)\*\+,\-\./:;<>@\[\\\]\^_`\{\|\}~a-zA-Z0-9]{0,50}""", [], ["0-4294967295"]),
			"SecondaryTargetIPAddress":MoPropertyMeta("SecondaryTargetIPAddress", "secondaryTargetIPAddress", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2000000L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"SecondaryTargetName":MoPropertyMeta("SecondaryTargetName", "secondaryTargetName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4000000L, None, None, r"""[0-9a-zA-Z\.:-]{0,223}""", [], ["0-4294967295"]),
			"SecondaryTargetPort":MoPropertyMeta("SecondaryTargetPort", "secondaryTargetPort", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8000000L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorEthISCSIProfile", "adaptorEthISCSIProfile", "ethiscsi", _VersionMeta.version_151f, "InputOutput", 0xfffffffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"LsbootEfi": {
			"Access":MoPropertyMeta("Access", "access", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["read-only"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["1", "2", "3", "4", "5"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["efi"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootEfi", "lsbootEfi", "efi-read-only", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDef'])
			},

		"BiosVfPCISlotOptionROMEnable": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpSlot10LinkSpeed":MoPropertyMeta("VpSlot10LinkSpeed", "vpSlot10LinkSpeed", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot10State":MoPropertyMeta("VpSlot10State", "vpSlot10State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot1LinkSpeed":MoPropertyMeta("VpSlot1LinkSpeed", "vpSlot1LinkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot1State":MoPropertyMeta("VpSlot1State", "vpSlot1State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot2LinkSpeed":MoPropertyMeta("VpSlot2LinkSpeed", "vpSlot2LinkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot2State":MoPropertyMeta("VpSlot2State", "vpSlot2State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot3LinkSpeed":MoPropertyMeta("VpSlot3LinkSpeed", "vpSlot3LinkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot3State":MoPropertyMeta("VpSlot3State", "vpSlot3State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot4LinkSpeed":MoPropertyMeta("VpSlot4LinkSpeed", "vpSlot4LinkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot4State":MoPropertyMeta("VpSlot4State", "vpSlot4State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot5LinkSpeed":MoPropertyMeta("VpSlot5LinkSpeed", "vpSlot5LinkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot5State":MoPropertyMeta("VpSlot5State", "vpSlot5State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot6LinkSpeed":MoPropertyMeta("VpSlot6LinkSpeed", "vpSlot6LinkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot6State":MoPropertyMeta("VpSlot6State", "vpSlot6State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot7LinkSpeed":MoPropertyMeta("VpSlot7LinkSpeed", "vpSlot7LinkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20000L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot7State":MoPropertyMeta("VpSlot7State", "vpSlot7State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot8LinkSpeed":MoPropertyMeta("VpSlot8LinkSpeed", "vpSlot8LinkSpeed", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80000L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot8State":MoPropertyMeta("VpSlot8State", "vpSlot8State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlot9LinkSpeed":MoPropertyMeta("VpSlot9LinkSpeed", "vpSlot9LinkSpeed", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200000L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlot9State":MoPropertyMeta("VpSlot9State", "vpSlot9State", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlotHBALinkSpeed":MoPropertyMeta("VpSlotHBALinkSpeed", "vpSlotHBALinkSpeed", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x800000L, None, None, None, ["Auto", "Disabled", "GEN1", "GEN2", "GEN3", "platform-default"], ["0-4294967295"]),
			"VpSlotHBAState":MoPropertyMeta("VpSlotHBAState", "vpSlotHBAState", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1000000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlotMLOMState":MoPropertyMeta("VpSlotMLOMState", "vpSlotMLOMState", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2000000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlotMezzState":MoPropertyMeta("VpSlotMezzState", "vpSlotMezzState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4000000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlotN1State":MoPropertyMeta("VpSlotN1State", "vpSlotN1State", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8000000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlotN2State":MoPropertyMeta("VpSlotN2State", "vpSlotN2State", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10000000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpSlotSASState":MoPropertyMeta("VpSlotSASState", "vpSlotSASState", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20000000L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPCISlotOptionROMEnable", "biosVfPCISlotOptionROMEnable", "PCI-Slot-OptionROM-Enable", _VersionMeta.version_151f, "InputOutput", 0x3fffffffL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfProcessorC3Report": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpProcessorC3Report":MoPropertyMeta("VpProcessorC3Report", "vpProcessorC3Report", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfProcessorC3Report", "biosVfProcessorC3Report", "Processor-C3-Report", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorEthCompQueueProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Count":MoPropertyMeta("Count", "count", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["1-512"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"RingSize":MoPropertyMeta("RingSize", "ringSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-1"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorEthCompQueueProfile", "adaptorEthCompQueueProfile", "eth-comp-q", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"HuuFirmwareCatalogComponent": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ComponentName":MoPropertyMeta("ComponentName", "componentName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("HuuFirmwareCatalogComponent", "huuFirmwareCatalogComponent", "id-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'huuFirmwareCatalog'])
			},

		"BiosVfCPUFrequencyFloor": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCPUFrequencyFloor":MoPropertyMeta("VpCPUFrequencyFloor", "vpCPUFrequencyFloor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCPUFrequencyFloor", "biosVfCPUFrequencyFloor", "CPU-FreqFloor", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"EquipmentIndicatorLed": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Color":MoPropertyMeta("Color", "color", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,25}""", [], ["0-4294967295"]),
			"OperState":MoPropertyMeta("OperState", "operState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentIndicatorLed", "equipmentIndicatorLed", "indicator-led-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"BiosVfAltitude": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpAltitude":MoPropertyMeta("VpAltitude", "vpAltitude", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["1500-m", "300-m", "3000-m", "900-m", "auto", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfAltitude", "biosVfAltitude", "Altitude-Param", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"LsbootStorage": {
			"Access":MoPropertyMeta("Access", "access", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["read-write"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["1", "2", "3", "4", "5"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["storage"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootStorage", "lsbootStorage", "storage-read-write", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [u'lsbootLocalStorage'], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDef'])
			},

		"LsbootUsb": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x2L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "usb-cd", "usb-fdd", "usb-hdd"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["USB"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootUsb", "lsbootUsb", "usb-[Name]", _VersionMeta.version_201a, "InputOutput", 0xffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"ComputeMbPowerStats": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ConsumedPower":MoPropertyMeta("ConsumedPower", "consumedPower", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"InputCurrent":MoPropertyMeta("InputCurrent", "inputCurrent", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"InputVoltage":MoPropertyMeta("InputVoltage", "inputVoltage", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TimeCollected":MoPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("ComputeMbPowerStats", "computeMbPowerStats", "power-stats", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"BiosVfIntelTurboBoostTech": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpIntelTurboBoostTech":MoPropertyMeta("VpIntelTurboBoostTech", "vpIntelTurboBoostTech", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfIntelTurboBoostTech", "biosVfIntelTurboBoostTech", "Intel-Turbo-Boost-Tech", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"CommSvcEp": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("CommSvcEp", "commSvcEp", "svc-ext", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'commHttp', u'commHttps', u'commIpmiLan', u'commKvm', u'commNtpProvider', u'commSnmp', u'commSsh', u'commSyslog', u'commVMedia'], ["Get"], ["admin", "read-only", "user"], [u'topSystem'])
			},

		"AaaUser": {
			"AccountStatus":MoPropertyMeta("AccountStatus", "accountStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["active", "inactive"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x4L, None, None, None, [], ["1-15"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[a-zA-Z0-9\._\+\-]{0,16}""", [], ["0-4294967295"]),
			"Priv":MoPropertyMeta("Priv", "priv", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "admin", "read-only", "user"], ["0-4294967295"]),
			"Pwd":MoPropertyMeta("Pwd", "pwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[\S+]{0,20}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AaaUser", "aaaUser", "user-[Id]", _VersionMeta.version_151f, "InputOutput", 0xffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'aaaUserEp'])
			},

		"StorageVirtualDrive": {
			"AccessPolicy":MoPropertyMeta("AccessPolicy", "accessPolicy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["", "blocked", "hidden", "read-only", "read-write"], ["0-4294967295"]),
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 510, None, ["cancel-initialization", "reconstruct-virtual-drive", "set-boot-drive", "start-fast-initialization", "start-full-initialization"], ["0-4294967295"]),
			"AllowBackgroundInit":MoPropertyMeta("AllowBackgroundInit", "allowBackgroundInit", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"AutoDeleteOldest":MoPropertyMeta("AutoDeleteOldest", "autoDeleteOldest", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"AutoSnapshot":MoPropertyMeta("AutoSnapshot", "autoSnapshot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BootDrive":MoPropertyMeta("BootDrive", "bootDrive", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CachePolicy":MoPropertyMeta("CachePolicy", "cachePolicy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "cached-io", "direct-io"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CurrentWriteCachePolicy":MoPropertyMeta("CurrentWriteCachePolicy", "currentWriteCachePolicy", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DiskCachePolicy":MoPropertyMeta("DiskCachePolicy", "diskCachePolicy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "disabled", "enabled", "unchanged"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"DriveState":MoPropertyMeta("DriveState", "driveState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DrivesPerSpan":MoPropertyMeta("DrivesPerSpan", "drivesPerSpan", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x20L, 0, 510, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysicalDrivesList":MoPropertyMeta("PhysicalDrivesList", "physicalDrivesList", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, 1, 510, r"""(\d+(,\d+)*)""", [], ["0-4294967295"]),
			"RaidLevel":MoPropertyMeta("RaidLevel", "raidLevel", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 510, None, ["0", "1", "5", "6"], ["0-4294967295"]),
			"ReadPolicy":MoPropertyMeta("ReadPolicy", "readPolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "always-read-ahead", "no-read-ahead"], ["0-4294967295"]),
			"RequestedWriteCachePolicy":MoPropertyMeta("RequestedWriteCachePolicy", "requestedWriteCachePolicy", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200L, 0, 510, None, ["Always Write Back", "Write Back Good BBU", "Write Through", "always-write-back", "write-back-good-bbu", "write-through"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, 0, 255, None, [], ["0-4294967295"]),
			"Size":MoPropertyMeta("Size", "size", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SpanDepth":MoPropertyMeta("SpanDepth", "spanDepth", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"StripSize":MoPropertyMeta("StripSize", "stripSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k"], ["0-4294967295"]),
			"TargetId":MoPropertyMeta("TargetId", "targetId", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VdStatus":MoPropertyMeta("VdStatus", "vdStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"WriteCachePolicy":MoPropertyMeta("WriteCachePolicy", "writeCachePolicy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageVirtualDrive", "storageVirtualDrive", "vd-[Id]", _VersionMeta.version_151f, "InputOutput", 0xfffL, [], [u'faultInst', u'storageLocalDiskUsage', u'storageOperation'], ["Get", "Set"], ["admin", "read-only", "user"], [u'storageController'])
			},

		"AdaptorExtEthIf": {
			"AdminSpeed":MoPropertyMeta("AdminSpeed", "adminSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["-", "10Gbps", "1Gbps", "40Gbps", "4x10Gbps", "Auto"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"IfType":MoPropertyMeta("IfType", "ifType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["aggregation", "physical", "unknown", "virtual"], ["0-4294967295"]),
			"LinkState":MoPropertyMeta("LinkState", "linkState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["admin-down", "down", "error", "unallocated", "unavailable", "unknown", "up"], ["0-4294967295"]),
			"Mac":MoPropertyMeta("Mac", "mac", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], ["0-4294967295"]),
			"OperSpeed":MoPropertyMeta("OperSpeed", "operSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["-", "10Gbps", "1Gbps", "40Gbps", "4x10Gbps", "Auto"], ["0-4294967295"]),
			"PortId":MoPropertyMeta("PortId", "portId", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x4L, None, None, None, ["0", "1"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Transport":MoPropertyMeta("Transport", "transport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorExtEthIf", "adaptorExtEthIf", "ext-eth-[PortId]", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [u'adaptorConnectorInfo', u'adaptorLinkTraining', u'adaptorPortProfiles'], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorUnit'])
			},

		"BiosBootDev": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, ["1", "10", "11", "12", "13", "14", "15", "2", "3", "4", "5", "6", "7", "8", "9"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("BiosBootDev", "biosBootDev", "bdv-[Order]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'biosBootDevGrp'])
			},

		"HuuController": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("HuuController", "huuController", "huu", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'huuFirmwareCatalog', u'huuFirmwareRunning', u'huuFirmwareUpdateCancel', u'huuFirmwareUpdater'], ["Get"], ["admin", "read-only", "user"], [u'topSystem'])
			},

		"LsbootPxe": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x2L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-255"]),
			"Port":MoPropertyMeta("Port", "port", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|L|MLOM|L1|L2){0,1}""", [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["PXE"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["PXE"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootPxe", "lsbootPxe", "pxe-[Name]", _VersionMeta.version_201a, "InputOutput", 0x3ffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"BiosVfProcessorC6Report": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpProcessorC6Report":MoPropertyMeta("VpProcessorC6Report", "vpProcessorC6Report", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfProcessorC6Report", "biosVfProcessorC6Report", "Processor-C6-Report", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfDCUPrefetch": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpIPPrefetch":MoPropertyMeta("VpIPPrefetch", "vpIPPrefetch", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpStreamerPrefetch":MoPropertyMeta("VpStreamerPrefetch", "vpStreamerPrefetch", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfDCUPrefetch", "biosVfDCUPrefetch", "DCU-Prefetch", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfFRB2Enable": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpFRB2Enable":MoPropertyMeta("VpFRB2Enable", "vpFRB2Enable", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfFRB2Enable", "biosVfFRB2Enable", "FRB2-Enable", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorFcPortFLogiProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Retries":MoPropertyMeta("Retries", "retries", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["INFINITE"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Timeout":MoPropertyMeta("Timeout", "timeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["1000-255000"]),
			"Meta":MoMeta("AdaptorFcPortFLogiProfile", "adaptorFcPortFLogiProfile", "fc-port-flogi", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"StorageVirtualDriveCreatorUsingUnusedPhysicalDrive": {
			"AccessPolicy":MoPropertyMeta("AccessPolicy", "accessPolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["", "blocked", "hidden", "read-only", "read-write"], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"CachePolicy":MoPropertyMeta("CachePolicy", "cachePolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "cached-io", "direct-io"], ["0-4294967295"]),
			"CreatedVirtualDriveDn":MoPropertyMeta("CreatedVirtualDriveDn", "createdVirtualDriveDn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DiskCachePolicy":MoPropertyMeta("DiskCachePolicy", "diskCachePolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "disabled", "enabled", "unchanged"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"DriveGroup":MoPropertyMeta("DriveGroup", "driveGroup", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, 1, 510, r"""((\[\d+(,\d+)*\])(\[\d+(,\d+)*\])*)""", [], ["0-4294967295"]),
			"MinRequiredPhysicalDrives":MoPropertyMeta("MinRequiredPhysicalDrives", "minRequiredPhysicalDrives", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OperStatus":MoPropertyMeta("OperStatus", "operStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RaidLevel":MoPropertyMeta("RaidLevel", "raidLevel", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "0", "1", "10", "5", "50", "6", "60"], ["0-4294967295"]),
			"ReadPolicy":MoPropertyMeta("ReadPolicy", "readPolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "always-read-ahead", "no-read-ahead"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, 0, 255, None, [], ["0-4294967295"]),
			"Size":MoPropertyMeta("Size", "size", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200L, 1, 510, r"""(\d+\s?([MGT]B)?)""", [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"StripSize":MoPropertyMeta("StripSize", "stripSize", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["", "1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k"], ["0-4294967295"]),
			"VirtualDriveName":MoPropertyMeta("VirtualDriveName", "virtualDriveName", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 15, None, [], ["0-4294967295"]),
			"WritePolicy":MoPropertyMeta("WritePolicy", "writePolicy", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["", "Always Write Back", "Write Back Good BBU", "Write Through", "always-write-back", "write-back-good-bbu", "write-through"], ["0-4294967295"]),
			"Meta":MoMeta("StorageVirtualDriveCreatorUsingUnusedPhysicalDrive", "storageVirtualDriveCreatorUsingUnusedPhysicalDrive", "virtual-drive-create", _VersionMeta.version_201a, "InputOutput", 0x3fffL, [], [u'storageUnusedLocalDisk'], ["Get", "Set"], ["admin"], [u'storageController'])
			},

		"LsbootDevPrecision": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ConfiguredBootMode":MoPropertyMeta("ConfiguredBootMode", "configuredBootMode", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Legacy", "None", "Uefi"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"LastConfiguredBootOrderSource":MoPropertyMeta("LastConfiguredBootOrderSource", "lastConfiguredBootOrderSource", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["BIOS", "CIMC", "UNKNOWN"], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Purpose":MoPropertyMeta("Purpose", "purpose", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], ["0-4294967295"]),
			"Reapply":MoPropertyMeta("Reapply", "reapply", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"RebootOnUpdate":MoPropertyMeta("RebootOnUpdate", "rebootOnUpdate", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootDevPrecision", "lsbootDevPrecision", "boot-precision", _VersionMeta.version_201a, "InputOutput", 0x3fL, [], [u'lsbootHdd', u'lsbootIscsi', u'lsbootPchStorage', u'lsbootPxe', u'lsbootSan', u'lsbootSd', u'lsbootUefiShell', u'lsbootUsb', u'lsbootVMedia'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"BiosVfNUMAOptimized": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpNUMAOptimized":MoPropertyMeta("VpNUMAOptimized", "vpNUMAOptimized", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfNUMAOptimized", "biosVfNUMAOptimized", "NUMA-optimized", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"CommSsh": {
			"ActiveSessions":MoPropertyMeta("ActiveSessions", "activeSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"MaximumSessions":MoPropertyMeta("MaximumSessions", "maximumSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["0-65535", "1-65535"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"SessionTimeout":MoPropertyMeta("SessionTimeout", "sessionTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["60-10800"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommSsh", "commSsh", "ssh-svc", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"BiosVfLvDIMMSupport": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpLvDDRMode":MoPropertyMeta("VpLvDDRMode", "vpLvDDRMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["auto", "performance-mode", "platform-default", "power-saving-mode"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfLvDIMMSupport", "biosVfLvDIMMSupport", "LvDIMM-Support", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfProcessorC1E": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpProcessorC1E":MoPropertyMeta("VpProcessorC1E", "vpProcessorC1E", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfProcessorC1E", "biosVfProcessorC1E", "Processor-C1E", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfCDNSupport": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCDNSupport":MoPropertyMeta("VpCDNSupport", "vpCDNSupport", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "LOMs Only", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCDNSupport", "biosVfCDNSupport", "CDN-Support", _VersionMeta.version_201a, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"CommVMedia": {
			"ActiveSessions":MoPropertyMeta("ActiveSessions", "activeSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"EncryptionState":MoPropertyMeta("EncryptionState", "encryptionState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommVMedia", "commVMedia", "vmedia-svc", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [u'commVMediaMap'], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"BiosVfPwrPerfTuning": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPwrPerfTuning":MoPropertyMeta("VpPwrPerfTuning", "vpPwrPerfTuning", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["bios", "os", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPwrPerfTuning", "biosVfPwrPerfTuning", "Pwr-Perf-Tuning", _VersionMeta.version_204c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"NetworkAdapterUnit": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NumIntf":MoPropertyMeta("NumIntf", "numIntf", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("NetworkAdapterUnit", "networkAdapterUnit", "network-adapter-[Slot]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'networkAdapterEthIf'], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"AdaptorFcCdbWorkQueueProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Count":MoPropertyMeta("Count", "count", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, [], ["1-8"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"RingSize":MoPropertyMeta("RingSize", "ringSize", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["64-512"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcCdbWorkQueueProfile", "adaptorFcCdbWorkQueueProfile", "fc-cdb-work-q", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"StorageFlexFlashControllerProps": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"AutoSync":MoPropertyMeta("AutoSync", "autoSync", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CardSlot":MoPropertyMeta("CardSlot", "cardSlot", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CardsManageable":MoPropertyMeta("CardsManageable", "cardsManageable", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ConfiguredMode":MoPropertyMeta("ConfiguredMode", "configuredMode", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ControllerName":MoPropertyMeta("ControllerName", "controllerName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ControllerStatus":MoPropertyMeta("ControllerStatus", "controllerStatus", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"FwVersion":MoPropertyMeta("FwVersion", "fwVersion", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"InternalState":MoPropertyMeta("InternalState", "internalState", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NonUtilPartitionName":MoPropertyMeta("NonUtilPartitionName", "nonUtilPartitionName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OperatingMode":MoPropertyMeta("OperatingMode", "operatingMode", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PartitionName":MoPropertyMeta("PartitionName", "partitionName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysicalDriveCount":MoPropertyMeta("PhysicalDriveCount", "physicalDriveCount", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ProductName":MoPropertyMeta("ProductName", "productName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"RunningFwVersion":MoPropertyMeta("RunningFwVersion", "runningFwVersion", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"StartupFwVersion":MoPropertyMeta("StartupFwVersion", "startupFwVersion", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VirtualDriveCount":MoPropertyMeta("VirtualDriveCount", "virtualDriveCount", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageFlexFlashControllerProps", "storageFlexFlashControllerProps", "flexflashcontroller-props", _VersionMeta.version_202c, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageFlexFlashController'])
			},

		"AaaLdap": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Attribute":MoPropertyMeta("Attribute", "attribute", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 63, r"""[a-zA-Z0-9][a-zA-Z0-9\-\.]*[a-zA-Z0-9\-]""", [], ["0-4294967295"]),
			"Basedn":MoPropertyMeta("Basedn", "basedn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 254, None, [], ["0-4294967295"]),
			"BindDn":MoPropertyMeta("BindDn", "bindDn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8L, 0, 254, None, [], ["0-4294967295"]),
			"BindMethod":MoPropertyMeta("BindMethod", "bindMethod", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["anonymous", "configured-credentials", "login-credentials"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"DnsDomainSource":MoPropertyMeta("DnsDomainSource", "dnsDomainSource", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["configured-domain", "extracted-configured-domain", "extracted-domain"], ["0-4294967295"]),
			"DnsSearchDomain":MoPropertyMeta("DnsSearchDomain", "dnsSearchDomain", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x80L, 0, 64, r"""[a-zA-Z][a-zA-Z0-9\.\-]*[a-zA-Z0-9]""", [], ["0-4294967295"]),
			"DnsSearchForest":MoPropertyMeta("DnsSearchForest", "dnsSearchForest", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x100L, 0, 64, r"""[a-zA-Z][a-zA-Z0-9\.\-]*[a-zA-Z0-9]""", [], ["0-4294967295"]),
			"Domain":MoPropertyMeta("Domain", "domain", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x200L, 1, 255, None, [], ["0-4294967295"]),
			"Encryption":MoPropertyMeta("Encryption", "encryption", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Filter":MoPropertyMeta("Filter", "filter", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x800L, 0, 20, r"""([a-zA-Z0-9][a-zA-Z0-9_#@$%&\-\^]*[a-zA-Z0-9\-]){0,20}""", [], ["0-4294967295"]),
			"GroupAttribute":MoPropertyMeta("GroupAttribute", "groupAttribute", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 254, r"""[a-zA-Z0-9][a-zA-Z0-9_#@$%&\-\^]*[a-zA-Z0-9\-]""", [], ["0-4294967295"]),
			"GroupAuth":MoPropertyMeta("GroupAuth", "groupAuth", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"GroupNestedSearch":MoPropertyMeta("GroupNestedSearch", "groupNestedSearch", "uint", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, [], ["1-128"]),
			"LdapServer1":MoPropertyMeta("LdapServer1", "ldapServer1", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8000L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"LdapServer2":MoPropertyMeta("LdapServer2", "ldapServer2", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x10000L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"LdapServer3":MoPropertyMeta("LdapServer3", "ldapServer3", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x20000L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"LdapServer4":MoPropertyMeta("LdapServer4", "ldapServer4", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x40000L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"LdapServer5":MoPropertyMeta("LdapServer5", "ldapServer5", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x80000L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"LdapServer6":MoPropertyMeta("LdapServer6", "ldapServer6", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x100000L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [""], ["0-4294967295"]),
			"LdapServerPort1":MoPropertyMeta("LdapServerPort1", "ldapServerPort1", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x200000L, None, None, None, [], ["1-65535"]),
			"LdapServerPort2":MoPropertyMeta("LdapServerPort2", "ldapServerPort2", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x400000L, None, None, None, [], ["1-65535"]),
			"LdapServerPort3":MoPropertyMeta("LdapServerPort3", "ldapServerPort3", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x800000L, None, None, None, [], ["1-65535"]),
			"LdapServerPort4":MoPropertyMeta("LdapServerPort4", "ldapServerPort4", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1000000L, None, None, None, [], ["1-65535"]),
			"LdapServerPort5":MoPropertyMeta("LdapServerPort5", "ldapServerPort5", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2000000L, None, None, None, [], ["1-65535"]),
			"LdapServerPort6":MoPropertyMeta("LdapServerPort6", "ldapServerPort6", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4000000L, None, None, None, [], ["1-65535"]),
			"LocateDirectoryUsingDNS":MoPropertyMeta("LocateDirectoryUsingDNS", "locateDirectoryUsingDNS", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8000000L, None, None, None, ["no", "yes"], ["0-4294967295"]),
			"Password":MoPropertyMeta("Password", "password", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x10000000L, None, None, r"""[\S+]{0,254}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20000000L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40000000L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Timeout":MoPropertyMeta("Timeout", "timeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80000000L, None, None, None, [], ["0-180", "0-1800"]),
			"Meta":MoMeta("AaaLdap", "aaaLdap", "ldap-ext", _VersionMeta.version_151f, "InputOutput", 0xffffffffL, [], [u'aaaLdapRoleGroup'], ["Get", "Set"], ["admin", "read-only", "user"], [u'topSystem'])
			},

		"BiosVfOSBootWatchdogTimerTimeout": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_152, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpOSBootWatchdogTimerTimeout":MoPropertyMeta("VpOSBootWatchdogTimerTimeout", "vpOSBootWatchdogTimerTimeout", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["10-minutes", "15-minutes", "20-minutes", "5-minutes", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfOSBootWatchdogTimerTimeout", "biosVfOSBootWatchdogTimerTimeout", "OS-Boot-Watchdog-Timer-Time-Out", _VersionMeta.version_152, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorFcWorkQueueProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"RingSize":MoPropertyMeta("RingSize", "ringSize", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["64-128"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorFcWorkQueueProfile", "adaptorFcWorkQueueProfile", "fc-work-q", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"BiosVfAssertNMIOnSERR": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpAssertNMIOnSERR":MoPropertyMeta("VpAssertNMIOnSERR", "vpAssertNMIOnSERR", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfAssertNMIOnSERR", "biosVfAssertNMIOnSERR", "Assert-NMI-on-SERR", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageControllerProps": {
			"BackendPortCount":MoPropertyMeta("BackendPortCount", "backendPortCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BatteryStatus":MoPropertyMeta("BatteryStatus", "batteryStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BbuPresent":MoPropertyMeta("BbuPresent", "bbuPresent", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BootBlockVersion":MoPropertyMeta("BootBlockVersion", "bootBlockVersion", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BootDrive":MoPropertyMeta("BootDrive", "bootDrive", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BootDriveIsPhysicalDrive":MoPropertyMeta("BootDriveIsPhysicalDrive", "bootDriveIsPhysicalDrive", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BootVersion":MoPropertyMeta("BootVersion", "bootVersion", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CacheMemorySize":MoPropertyMeta("CacheMemorySize", "cacheMemorySize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ControllerStatus":MoPropertyMeta("ControllerStatus", "controllerStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CriticalPhysicalDriveCount":MoPropertyMeta("CriticalPhysicalDriveCount", "criticalPhysicalDriveCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DateOfManufacture":MoPropertyMeta("DateOfManufacture", "dateOfManufacture", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DegradedVirtualDriveCount":MoPropertyMeta("DegradedVirtualDriveCount", "degradedVirtualDriveCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"FailedPhysicalDriveCount":MoPropertyMeta("FailedPhysicalDriveCount", "failedPhysicalDriveCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"FirmwarePackageBuild":MoPropertyMeta("FirmwarePackageBuild", "firmwarePackageBuild", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"FlashPresent":MoPropertyMeta("FlashPresent", "flashPresent", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MemoryCorrectableErrors":MoPropertyMeta("MemoryCorrectableErrors", "memoryCorrectableErrors", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MemoryPresent":MoPropertyMeta("MemoryPresent", "memoryPresent", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MemorySize":MoPropertyMeta("MemorySize", "memorySize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MemoryUncorrectableErrors":MoPropertyMeta("MemoryUncorrectableErrors", "memoryUncorrectableErrors", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NvdataVersion":MoPropertyMeta("NvdataVersion", "nvdataVersion", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NvramPresent":MoPropertyMeta("NvramPresent", "nvramPresent", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OfflineVirtualDriveCount":MoPropertyMeta("OfflineVirtualDriveCount", "offlineVirtualDriveCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PciSlot":MoPropertyMeta("PciSlot", "pciSlot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysicalDriveCount":MoPropertyMeta("PhysicalDriveCount", "physicalDriveCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PrebootCliVersion":MoPropertyMeta("PrebootCliVersion", "prebootCliVersion", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RaidChipTempCentigrade":MoPropertyMeta("RaidChipTempCentigrade", "raidChipTempCentigrade", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Revision":MoPropertyMeta("Revision", "revision", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"SasAddress0":MoPropertyMeta("SasAddress0", "sasAddress0", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress1":MoPropertyMeta("SasAddress1", "sasAddress1", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress2":MoPropertyMeta("SasAddress2", "sasAddress2", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress3":MoPropertyMeta("SasAddress3", "sasAddress3", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress4":MoPropertyMeta("SasAddress4", "sasAddress4", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress5":MoPropertyMeta("SasAddress5", "sasAddress5", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress6":MoPropertyMeta("SasAddress6", "sasAddress6", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress7":MoPropertyMeta("SasAddress7", "sasAddress7", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SerialDebuggerPresent":MoPropertyMeta("SerialDebuggerPresent", "serialDebuggerPresent", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"SupportsRaid0":MoPropertyMeta("SupportsRaid0", "supportsRaid0", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid00":MoPropertyMeta("SupportsRaid00", "supportsRaid00", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid1":MoPropertyMeta("SupportsRaid1", "supportsRaid1", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid10":MoPropertyMeta("SupportsRaid10", "supportsRaid10", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid1e":MoPropertyMeta("SupportsRaid1e", "supportsRaid1e", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid1e0rlq0":MoPropertyMeta("SupportsRaid1e0rlq0", "supportsRaid1e0rlq0", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid1erlq0":MoPropertyMeta("SupportsRaid1erlq0", "supportsRaid1erlq0", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid5":MoPropertyMeta("SupportsRaid5", "supportsRaid5", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid50":MoPropertyMeta("SupportsRaid50", "supportsRaid50", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid6":MoPropertyMeta("SupportsRaid6", "supportsRaid6", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaid60":MoPropertyMeta("SupportsRaid60", "supportsRaid60", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SupportsRaidsrl03":MoPropertyMeta("SupportsRaidsrl03", "supportsRaidsrl03", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"TtyLogStatus":MoPropertyMeta("TtyLogStatus", "ttyLogStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VirtualDriveCount":MoPropertyMeta("VirtualDriveCount", "virtualDriveCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"WebBiosVersion":MoPropertyMeta("WebBiosVersion", "webBiosVersion", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageControllerProps", "storageControllerProps", "controller-props", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageController'])
			},

		"LsbootIscsi": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x2L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-255"]),
			"Port":MoPropertyMeta("Port", "port", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]|L|MLOM|L1|L2){0,1}""", [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["ISCSI"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["ISCSI"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootIscsi", "lsbootIscsi", "iscsi-[Name]", _VersionMeta.version_201a, "InputOutput", 0x3ffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"PowerBudget": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["reset-power-profile-default", "start-power-char"], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"MaxCpuPower":MoPropertyMeta("MaxCpuPower", "maxCpuPower", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MaxMemoryPower":MoPropertyMeta("MaxMemoryPower", "maxMemoryPower", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MaxPower":MoPropertyMeta("MaxPower", "maxPower", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MinCpuPower":MoPropertyMeta("MinCpuPower", "minCpuPower", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MinMemoryPower":MoPropertyMeta("MinMemoryPower", "minMemoryPower", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MinPower":MoPropertyMeta("MinPower", "minPower", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PowerCharStatus":MoPropertyMeta("PowerCharStatus", "powerCharStatus", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"RunPowCharAtBoot":MoPropertyMeta("RunPowCharAtBoot", "runPowCharAtBoot", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("PowerBudget", "powerBudget", "budget", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [u'advancedPowerProfile', u'faultInst', u'standardPowerProfile'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"CommHttps": {
			"ActiveSessions":MoPropertyMeta("ActiveSessions", "activeSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"MaximumSessions":MoPropertyMeta("MaximumSessions", "maximumSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-65535"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"SessionTimeout":MoPropertyMeta("SessionTimeout", "sessionTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["60-10800"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommHttps", "commHttps", "https-svc", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"MgmtController": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Subject":MoPropertyMeta("Subject", "subject", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade", "board-controller", "system", "unknown"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("MgmtController", "mgmtController", "mgmt", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'firmwareBootDefinition', u'firmwareRunning', u'firmwareUpdatable', u'mgmtIf', u'sysdebugMEpLog'], ["Get"], ["admin", "read-only", "user"], [u'adaptorUnit', u'computeRackUnit'])
			},

		"BiosVfLegacyUSBSupport": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpLegacyUSBSupport":MoPropertyMeta("VpLegacyUSBSupport", "vpLegacyUSBSupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Auto", "Disabled", "Enabled", "auto", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfLegacyUSBSupport", "biosVfLegacyUSBSupport", "LegacyUSB-Support", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfCkeLowPolicy": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpCkeLowPolicy":MoPropertyMeta("VpCkeLowPolicy", "vpCkeLowPolicy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["auto", "disabled", "fast", "platform-default", "slow"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfCkeLowPolicy", "biosVfCkeLowPolicy", "Cke-Low-Policy", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"CommHttp": {
			"ActiveSessions":MoPropertyMeta("ActiveSessions", "activeSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"MaximumSessions":MoPropertyMeta("MaximumSessions", "maximumSessions", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-65535"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], ["0-4294967295"]),
			"RedirectState":MoPropertyMeta("RedirectState", "redirectState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"SessionTimeout":MoPropertyMeta("SessionTimeout", "sessionTimeout", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["60-10800"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommHttp", "commHttp", "http-svc", _VersionMeta.version_151f, "InputOutput", 0x7fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"BiosVfOnboardStorageSWStack": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpOnboardSCUStorageSWStack":MoPropertyMeta("VpOnboardSCUStorageSWStack", "vpOnboardSCUStorageSWStack", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Intel RSTe", "LSI SW RAID", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfOnboardStorageSWStack", "biosVfOnboardStorageSWStack", "Onboard-SCU-Storage-SWStack", _VersionMeta.version_152, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorGenProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ConfigurationPending":MoPropertyMeta("ConfigurationPending", "configurationPending", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"FipMode":MoPropertyMeta("FipMode", "fipMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"IscsiBootSupported":MoPropertyMeta("IscsiBootSupported", "iscsiBootSupported", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NumOfVMFexIfs":MoPropertyMeta("NumOfVMFexIfs", "numOfVMFexIfs", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["0-112"]),
			"PciSlot":MoPropertyMeta("PciSlot", "pciSlot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ProductName":MoPropertyMeta("ProductName", "productName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Revision":MoPropertyMeta("Revision", "revision", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"UsnicSupported":MoPropertyMeta("UsnicSupported", "usnicSupported", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VendorId":MoPropertyMeta("VendorId", "vendorId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"VntagMode":MoPropertyMeta("VntagMode", "vntagMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorGenProfile", "adaptorGenProfile", "general", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorUnit'])
			},

		"StorageVirtualDriveCreatorUsingVirtualDriveGroup": {
			"AccessPolicy":MoPropertyMeta("AccessPolicy", "accessPolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["", "blocked", "hidden", "read-only", "read-write"], ["0-4294967295"]),
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"CachePolicy":MoPropertyMeta("CachePolicy", "cachePolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "cached-io", "direct-io"], ["0-4294967295"]),
			"CreatedVirtualDriveDn":MoPropertyMeta("CreatedVirtualDriveDn", "createdVirtualDriveDn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DiskCachePolicy":MoPropertyMeta("DiskCachePolicy", "diskCachePolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "disabled", "enabled", "unchanged"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"OperStatus":MoPropertyMeta("OperStatus", "operStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ReadPolicy":MoPropertyMeta("ReadPolicy", "readPolicy", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "always-read-ahead", "no-read-ahead"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"SharedVirtualDriveId":MoPropertyMeta("SharedVirtualDriveId", "sharedVirtualDriveId", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [""], ["0-4294967295"]),
			"Size":MoPropertyMeta("Size", "size", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, 1, 510, r"""(\d+\s?([MGT]B)?)""", [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"StripSize":MoPropertyMeta("StripSize", "stripSize", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["", "1024k", "128k", "16k", "256k", "32k", "512k", "64k", "8k"], ["0-4294967295"]),
			"VirtualDriveName":MoPropertyMeta("VirtualDriveName", "virtualDriveName", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x800L, 0, 15, None, [], ["0-4294967295"]),
			"WritePolicy":MoPropertyMeta("WritePolicy", "writePolicy", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, ["", "Always Write Back", "Write Back Good BBU", "Write Through", "always-write-back", "write-back-good-bbu", "write-through"], ["0-4294967295"]),
			"Meta":MoMeta("StorageVirtualDriveCreatorUsingVirtualDriveGroup", "storageVirtualDriveCreatorUsingVirtualDriveGroup", "virtual-drive-carve", _VersionMeta.version_201a, "InputOutput", 0x1fffL, [], [u'storageVirtualDriveWithDriveGroupSpace'], ["Get", "Set"], ["admin"], [u'storageController'])
			},

		"EquipmentPsuColdRedundancy": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Enabled":MoPropertyMeta("Enabled", "enabled", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentPsuColdRedundancy", "equipmentPsuColdRedundancy", "psu-cold-redundancy", _VersionMeta.version_204c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'computeRackUnit'])
			},

		"PciEquipSlot": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ControllerReported":MoPropertyMeta("ControllerReported", "controllerReported", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"SmbiosId":MoPropertyMeta("SmbiosId", "smbiosId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Version":MoPropertyMeta("Version", "version", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("PciEquipSlot", "pciEquipSlot", "equipped-slot-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'faultInst'], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"CommSyslogClient": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x8L, None, None, None, ["primary", "secondary", "tertiary"], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["1-65535"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommSyslogClient", "commSyslogClient", "client-[Name]", _VersionMeta.version_151f, "InputOutput", 0x7fL, [], [], ["Get"], ["admin", "read-only", "user"], [u'commSyslog'])
			},

		"CommSnmpTrap": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Community":MoPropertyMeta("Community", "community", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[!#$%\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{1,32}""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x8L, None, None, None, [], ["1-15"]),
			"NotificationType":MoPropertyMeta("NotificationType", "notificationType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["informs", "traps"], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["1-65535"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, 0, 31, None, [], ["0-4294967295"]),
			"Version":MoPropertyMeta("Version", "version", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["v1", "v2c", "v3"], ["0-4294967295"]),
			"Meta":MoMeta("CommSnmpTrap", "commSnmpTrap", "snmp-trap-[Id]", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSnmp'])
			},

		"StorageLocalDiskUsage": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"NumberOfBlocks":MoPropertyMeta("NumberOfBlocks", "numberOfBlocks", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysicalDrive":MoPropertyMeta("PhysicalDrive", "physicalDrive", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Span":MoPropertyMeta("Span", "span", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"StartingBlock":MoPropertyMeta("StartingBlock", "startingBlock", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VirtualDrive":MoPropertyMeta("VirtualDrive", "virtualDrive", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageLocalDiskUsage", "storageLocalDiskUsage", "pd-[PhysicalDrive]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageVirtualDrive'])
			},

		"AdaptorIpV6RssHashProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"IpHash":MoPropertyMeta("IpHash", "ipHash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TcpHash":MoPropertyMeta("TcpHash", "tcpHash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorIpV6RssHashProfile", "adaptorIpV6RssHashProfile", "ipv6-rss-hash", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"BiosBootDevPrecision": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Lun":MoPropertyMeta("Lun", "lun", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-255"]),
			"Port":MoPropertyMeta("Port", "port", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cimc-mapped-dvd", "cimc-mapped-hdd", "kvm-mapped-dvd", "kvm-mapped-fdd", "kvm-mapped-hdd", "usb-cd", "usb-fdd", "usb-hdd"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["EFI", "HDD", "ISCSI", "PCHSTORAGE", "PXE", "SAN", "SDCARD", "USB", "VMEDIA"], ["0-4294967295"]),
			"Meta":MoMeta("BiosBootDevPrecision", "biosBootDevPrecision", "bdvp-[Order]", _VersionMeta.version_201a, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'biosBOT'])
			},

		"LsbootLan": {
			"Access":MoPropertyMeta("Access", "access", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["read-only"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["1", "2", "3", "4", "5"], ["0-4294967295"]),
			"Prot":MoPropertyMeta("Prot", "prot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["gpxe", "iSCSI", "pxe"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["lan"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootLan", "lsbootLan", "lan-read-only", _VersionMeta.version_151f, "InputOutput", 0x7fL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDef'])
			},

		"LsbootUefiShell": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x2L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["1-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["UEFISHELL"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootUefiShell", "lsbootUefiShell", "uefishell-[Name]", _VersionMeta.version_201a, "InputOutput", 0x7fL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"AdaptorEthUSNICProfile": {
			"ClassOfService":MoPropertyMeta("ClassOfService", "classOfService", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1L, None, None, r"""[0-6]""", [], ["0-4294967295"]),
			"CoalescingTime":MoPropertyMeta("CoalescingTime", "coalescingTime", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], ["0-65535"]),
			"CoalescingType":MoPropertyMeta("CoalescingType", "coalescingType", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["IDLE", "MIN"], ["0-4294967295"]),
			"CompletionQueueCount":MoPropertyMeta("CompletionQueueCount", "completionQueueCount", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["1-512"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"InterruptCount":MoPropertyMeta("InterruptCount", "interruptCount", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["1-514"]),
			"LargeReceive":MoPropertyMeta("LargeReceive", "largeReceive", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ReceiveQueueCount":MoPropertyMeta("ReceiveQueueCount", "receiveQueueCount", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, [], ["1-256"]),
			"ReceiveQueueRingSize":MoPropertyMeta("ReceiveQueueRingSize", "receiveQueueRingSize", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, [], ["64-4096"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x200L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TcpRxChecksum":MoPropertyMeta("TcpRxChecksum", "tcpRxChecksum", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TcpSegment":MoPropertyMeta("TcpSegment", "tcpSegment", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TcpTxChecksum":MoPropertyMeta("TcpTxChecksum", "tcpTxChecksum", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TransmitQueueCount":MoPropertyMeta("TransmitQueueCount", "transmitQueueCount", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, [], ["1-256"]),
			"TransmitQueueRingSize":MoPropertyMeta("TransmitQueueRingSize", "transmitQueueRingSize", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, [], ["64-4096"]),
			"UsnicCount":MoPropertyMeta("UsnicCount", "usnicCount", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, None, [], ["1-225"]),
			"Meta":MoMeta("AdaptorEthUSNICProfile", "adaptorEthUSNICProfile", "ethusnic", _VersionMeta.version_152, "InputOutput", 0x1ffffL, [], [], ["Get", "Remove", "Set"], ["admin"], [u'adaptorHostEthIf'])
			},

		"LsbootLocalStorage": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootLocalStorage", "lsbootLocalStorage", "local-storage", _VersionMeta.version_151f, "InputOutput", 0x7L, [], [], ["Get"], ["admin", "read-only", "user"], [u'lsbootStorage'])
			},

		"EquipmentLocatorLed": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["inactive", "off", "on"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Color":MoPropertyMeta("Color", "color", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["amber", "blue", "green", "red", "unknown"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 512, None, [], ["0-4294967295"]),
			"OperState":MoPropertyMeta("OperState", "operState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["blinking", "eth", "fc", "off", "on", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentLocatorLed", "equipmentLocatorLed", "locator-led", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"HuuFirmwareUpdater": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CimcSecureBoot":MoPropertyMeta("CimcSecureBoot", "cimcSecureBoot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"MapType":MoPropertyMeta("MapType", "mapType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["cifs", "nfs", "www"], ["0-4294967295"]),
			"Password":MoPropertyMeta("Password", "password", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["0-4294967295"]),
			"RemoteIp":MoPropertyMeta("RemoteIp", "remoteIp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"RemoteShare":MoPropertyMeta("RemoteShare", "remoteShare", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], ["0-4294967295"]),
			"RemoteShareFile":MoPropertyMeta("RemoteShareFile", "remoteShareFile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RemoteSharePath":MoPropertyMeta("RemoteSharePath", "remoteSharePath", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"StopOnError":MoPropertyMeta("StopOnError", "stopOnError", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"TimeOut":MoPropertyMeta("TimeOut", "timeOut", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], ["30-240"]),
			"UpdateComponent":MoPropertyMeta("UpdateComponent", "updateComponent", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], ["0-4294967295"]),
			"Username":MoPropertyMeta("Username", "username", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, [], ["0-4294967295"]),
			"VerifyUpdate":MoPropertyMeta("VerifyUpdate", "verifyUpdate", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Meta":MoMeta("HuuFirmwareUpdater", "huuFirmwareUpdater", "firmwareUpdater", _VersionMeta.version_151f, "InputOutput", 0x3fffL, [], [u'huuFirmwareUpdateStatus'], ["Get"], ["admin", "read-only", "user"], [u'huuController'])
			},

		"BiosVfAssertNMIOnPERR": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpAssertNMIOnPERR":MoPropertyMeta("VpAssertNMIOnPERR", "vpAssertNMIOnPERR", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfAssertNMIOnPERR", "biosVfAssertNMIOnPERR", "Assert-NMI-on-PERR", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"FirmwareRunning": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Deployment":MoPropertyMeta("Deployment", "deployment", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, ["boot-loader", "kernel", "system", "unspecified"], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["adaptor", "blade-bios", "blade-controller", "sioc", "storage-controller", "system", "unspecified"], ["0-4294967295"]),
			"Version":MoPropertyMeta("Version", "version", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("FirmwareRunning", "firmwareRunning", "fw-[Deployment]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'biosUnit', u'mgmtController', u'storageController', u'systemIOController'])
			},

		"PidCatalogHdd": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Controller":MoPropertyMeta("Controller", "controller", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Disk":MoPropertyMeta("Disk", "disk", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Pid":MoPropertyMeta("Pid", "pid", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serialnumber":MoPropertyMeta("Serialnumber", "serialnumber", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("PidCatalogHdd", "pidCatalogHdd", "pid-hdd-[Disk]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'pidCatalog'])
			},

		"BiosVfASPMSupport": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpASPMSupport":MoPropertyMeta("VpASPMSupport", "vpASPMSupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Auto", "Disabled", "Force L0s", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfASPMSupport", "biosVfASPMSupport", "ASPM-Support", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AdaptorVMFexEthIf": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ClassOfService":MoPropertyMeta("ClassOfService", "classOfService", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[0-6]""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"IfType":MoPropertyMeta("IfType", "ifType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["virtual"], ["0-4294967295"]),
			"Mtu":MoPropertyMeta("Mtu", "mtu", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1500-9000"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, r"""[a-zA-Z0-9\-\._:]{1,32}""", [], ["0-4294967295"]),
			"PxeBoot":MoPropertyMeta("PxeBoot", "pxeBoot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"UplinkFailbackTimeout":MoPropertyMeta("UplinkFailbackTimeout", "uplinkFailbackTimeout", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"UplinkFailover":MoPropertyMeta("UplinkFailover", "uplinkFailover", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"UplinkPort":MoPropertyMeta("UplinkPort", "uplinkPort", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["0", "1"], ["0-4294967295"]),
			"Vlan":MoPropertyMeta("Vlan", "vlan", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"VlanMode":MoPropertyMeta("VlanMode", "vlanMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorVMFexEthIf", "adaptorVMFexEthIf", "vmfex-eth-[Name]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'adaptorVMFexEthProfile'], ["Get"], ["admin", "read-only", "user"], [u'adaptorUnit'])
			},

		"AdaptorExtIpV6RssHashProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"IpHash":MoPropertyMeta("IpHash", "ipHash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TcpHash":MoPropertyMeta("TcpHash", "tcpHash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorExtIpV6RssHashProfile", "adaptorExtIpV6RssHashProfile", "ext-ipv6-rss-hash", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"BiosVfMemoryInterleave": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpChannelInterLeave":MoPropertyMeta("VpChannelInterLeave", "vpChannelInterLeave", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["1-way", "2-way", "3-way", "4-way", "auto", "platform-default"], ["0-4294967295"]),
			"VpMemoryInterLeave":MoPropertyMeta("VpMemoryInterLeave", "vpMemoryInterLeave", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["1 Way Node Interleave", "2 Way Node Interleave", "4 Way Node Interleave", "8 Way Node Interleave", "Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpRankInterLeave":MoPropertyMeta("VpRankInterLeave", "vpRankInterLeave", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["1-way", "2-way", "4-way", "8-way", "auto", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfMemoryInterleave", "biosVfMemoryInterleave", "Memory-Interleave", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfConsoleRedirection": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpBaudRate":MoPropertyMeta("VpBaudRate", "vpBaudRate", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["115200", "19200", "38400", "57600", "9600", "platform-default"], ["0-4294967295"]),
			"VpConsoleRedirection":MoPropertyMeta("VpConsoleRedirection", "vpConsoleRedirection", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["com-0", "com-1", "disabled", "enabled", "platform-default", "serial-port-a"], ["0-4294967295"]),
			"VpFlowControl":MoPropertyMeta("VpFlowControl", "vpFlowControl", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["none", "platform-default", "rts-cts"], ["0-4294967295"]),
			"VpLegacyOSRedirection":MoPropertyMeta("VpLegacyOSRedirection", "vpLegacyOSRedirection", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"VpPuttyKeyPad":MoPropertyMeta("VpPuttyKeyPad", "vpPuttyKeyPad", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["ESCN", "LINUX", "SCO", "VT100", "VT400", "XTERMR6", "platform-default"], ["0-4294967295"]),
			"VpRedirectionAfterPOST":MoPropertyMeta("VpRedirectionAfterPOST", "vpRedirectionAfterPOST", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["Always Enable", "Bootloader", "platform-default"], ["0-4294967295"]),
			"VpTerminalType":MoPropertyMeta("VpTerminalType", "vpTerminalType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["pc-ansi", "platform-default", "vt-utf8", "vt100", "vt100-plus"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfConsoleRedirection", "biosVfConsoleRedirection", "Console-redirection", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"HuuFirmwareRunning": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CurrentTime":MoPropertyMeta("CurrentTime", "currentTime", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"LastQueriedTimeStamp":MoPropertyMeta("LastQueriedTimeStamp", "lastQueriedTimeStamp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("HuuFirmwareRunning", "huuFirmwareRunning", "currentFirmware", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'huuFirmwareComponent'], ["Get"], ["admin", "read-only", "user"], [u'huuController'])
			},

		"StorageFlexFlashVirtualDrive": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["disable-vd", "enable-vd", "erase-vd", "sync-vd", "update-vd"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"DriveScope":MoPropertyMeta("DriveScope", "driveScope", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DriveStatus":MoPropertyMeta("DriveStatus", "driveStatus", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DriveType":MoPropertyMeta("DriveType", "driveType", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"HostAccessible":MoPropertyMeta("HostAccessible", "hostAccessible", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"LastOperationStatus":MoPropertyMeta("LastOperationStatus", "lastOperationStatus", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OperationInProgress":MoPropertyMeta("OperationInProgress", "operationInProgress", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PartitionId":MoPropertyMeta("PartitionId", "partitionId", "string", _VersionMeta.version_202c, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Size":MoPropertyMeta("Size", "size", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VirtualDrive":MoPropertyMeta("VirtualDrive", "virtualDrive", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageFlexFlashVirtualDrive", "storageFlexFlashVirtualDrive", "vd-[PartitionId]", _VersionMeta.version_202c, "InputOutput", 0xfL, [], [u'faultInst'], ["Get", "Set"], ["admin", "read-only", "user"], [u'storageFlexFlashController'])
			},

		"BiosPlatformDefaults": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_152, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("BiosPlatformDefaults", "biosPlatformDefaults", "bios-defaults", _VersionMeta.version_152, "OutputOnly", 0x0L, [], [u'biosVfASPMSupport', u'biosVfAdjacentCacheLinePrefetch', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfBootOptionRetry', u'biosVfCDNEnable', u'biosVfCDNSupport', u'biosVfCPUEnergyPerformance', u'biosVfCPUFrequencyFloor', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfCkeLowPolicy', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDCUPrefetch', u'biosVfDRAMClockThrottling', u'biosVfDemandScrub', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfExecuteDisableBit', u'biosVfExtendedAPIC', u'biosVfFRB2Enable', u'biosVfHardwarePrefetch', u'biosVfIOHResource', u'biosVfIntelHyperThreadingTech', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfLOMPortOptionROM', u'biosVfLegacyUSBSupport', u'biosVfLvDIMMSupport', u'biosVfMMCFGBase', u'biosVfMemoryInterleave', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardNIC', u'biosVfOnboardStorage', u'biosVfOnboardStorageSWStack', u'biosVfOutOfBandMgmtPort', u'biosVfPCIOptionROMs', u'biosVfPCISlotOptionROMEnable', u'biosVfPOSTErrorPause', u'biosVfPStateCoordType', u'biosVfPackageCStateLimit', u'biosVfPatrolScrub', u'biosVfPatrolScrubDuration', u'biosVfPchUsb30Mode', u'biosVfPciRomClp', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorCState', u'biosVfPwrPerfTuning', u'biosVfQPIConfig', u'biosVfQpiSnoopMode', u'biosVfSataModeSelect', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSparingMode', u'biosVfSrIov', u'biosVfTPMSupport', u'biosVfUCSMBootOrderRuleControl', u'biosVfUSBBootConfig', u'biosVfUSBEmulation', u'biosVfUSBPortsConfig', u'biosVfVgaPriority', u'biosVfWorkLoadConfig'], ["Get"], ["admin", "read-only", "user"], [u'biosUnit'])
			},

		"AdaptorVMFexEthProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CoalescingTime":MoPropertyMeta("CoalescingTime", "coalescingTime", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"CoalescingType":MoPropertyMeta("CoalescingType", "coalescingType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"CompletionQueueCount":MoPropertyMeta("CompletionQueueCount", "completionQueueCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"CompletionQueueRingSize":MoPropertyMeta("CompletionQueueRingSize", "completionQueueRingSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"InterruptCount":MoPropertyMeta("InterruptCount", "interruptCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"InterruptMode":MoPropertyMeta("InterruptMode", "interruptMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"LargeReceive":MoPropertyMeta("LargeReceive", "largeReceive", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[a-zA-Z0-9\-\._:]{1,32}""", [], ["0-4294967295"]),
			"PciOrder":MoPropertyMeta("PciOrder", "pciOrder", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ReceiveQueueCount":MoPropertyMeta("ReceiveQueueCount", "receiveQueueCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ReceiveQueueRingSize":MoPropertyMeta("ReceiveQueueRingSize", "receiveQueueRingSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ReceiveSideScaling":MoPropertyMeta("ReceiveSideScaling", "receiveSideScaling", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ReceiveSideScalingExtIpV6Hash":MoPropertyMeta("ReceiveSideScalingExtIpV6Hash", "receiveSideScalingExtIpV6Hash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ReceiveSideScalingExtTCPIpV6Hash":MoPropertyMeta("ReceiveSideScalingExtTCPIpV6Hash", "receiveSideScalingExtTCPIpV6Hash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ReceiveSideScalingIpV4Hash":MoPropertyMeta("ReceiveSideScalingIpV4Hash", "receiveSideScalingIpV4Hash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ReceiveSideScalingIpV6Hash":MoPropertyMeta("ReceiveSideScalingIpV6Hash", "receiveSideScalingIpV6Hash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ReceiveSideScalingTCPIpV4Hash":MoPropertyMeta("ReceiveSideScalingTCPIpV4Hash", "receiveSideScalingTCPIpV4Hash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ReceiveSideScalingTCPIpV6Hash":MoPropertyMeta("ReceiveSideScalingTCPIpV6Hash", "receiveSideScalingTCPIpV6Hash", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TcpRxChecksum":MoPropertyMeta("TcpRxChecksum", "tcpRxChecksum", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TcpSegment":MoPropertyMeta("TcpSegment", "tcpSegment", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TcpTxChecksum":MoPropertyMeta("TcpTxChecksum", "tcpTxChecksum", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"TransmitQueueCount":MoPropertyMeta("TransmitQueueCount", "transmitQueueCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"TransmitQueueRingSize":MoPropertyMeta("TransmitQueueRingSize", "transmitQueueRingSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"TrustedClassOfService":MoPropertyMeta("TrustedClassOfService", "trustedClassOfService", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorVMFexEthProfile", "adaptorVMFexEthProfile", "vmfexprofile", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'adaptorVMFexEthIf'])
			},

		"BiosVfSparingMode": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpSparingMode":MoPropertyMeta("VpSparingMode", "vpSparingMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["dimm-sparing", "platform-default", "rank-sparing"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfSparingMode", "biosVfSparingMode", "Sparing-Mode", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfDRAMClockThrottling": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpDRAMClockThrottling":MoPropertyMeta("VpDRAMClockThrottling", "vpDRAMClockThrottling", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Auto", "Balanced", "Energy Efficient", "Performance", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfDRAMClockThrottling", "biosVfDRAMClockThrottling", "DRAM-Clock-Throttling", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfIntelVirtualizationTechnology": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpIntelVirtualizationTechnology":MoPropertyMeta("VpIntelVirtualizationTechnology", "vpIntelVirtualizationTechnology", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfIntelVirtualizationTechnology", "biosVfIntelVirtualizationTechnology", "Intel-Virtualization-Technology", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"EquipmentPsu": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"FwVersion":MoPropertyMeta("FwVersion", "fwVersion", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-4"]),
			"Input":MoPropertyMeta("Input", "input", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MaxOutput":MoPropertyMeta("MaxOutput", "maxOutput", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Operability":MoPropertyMeta("Operability", "operability", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Power":MoPropertyMeta("Power", "power", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Thermal":MoPropertyMeta("Thermal", "thermal", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Voltage":MoPropertyMeta("Voltage", "voltage", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentPsu", "equipmentPsu", "psu-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'equipmentPsuFan', u'faultInst'], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"PidCatalogPCIAdapter": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Device":MoPropertyMeta("Device", "device", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Pid":MoPropertyMeta("Pid", "pid", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Subdevice":MoPropertyMeta("Subdevice", "subdevice", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Subvendor":MoPropertyMeta("Subvendor", "subvendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("PidCatalogPCIAdapter", "pidCatalogPCIAdapter", "pid-pciadapter-[Slot]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'pidCatalog'])
			},

		"StorageLocalDiskProps": {
			"BlockCount":MoPropertyMeta("BlockCount", "blockCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BlockSize":MoPropertyMeta("BlockSize", "blockSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"BootDrive":MoPropertyMeta("BootDrive", "bootDrive", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CoercedSize":MoPropertyMeta("CoercedSize", "coercedSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DeviceId":MoPropertyMeta("DeviceId", "deviceId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"EnclosureDeviceId":MoPropertyMeta("EnclosureDeviceId", "enclosureDeviceId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"InterfaceType":MoPropertyMeta("InterfaceType", "interfaceType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"LinkSpeed":MoPropertyMeta("LinkSpeed", "linkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MediaErrorCount":MoPropertyMeta("MediaErrorCount", "mediaErrorCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MediaType":MoPropertyMeta("MediaType", "mediaType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NonCoercedSize":MoPropertyMeta("NonCoercedSize", "nonCoercedSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OtherErrorCount":MoPropertyMeta("OtherErrorCount", "otherErrorCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PdStatus":MoPropertyMeta("PdStatus", "pdStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysicalDrive":MoPropertyMeta("PhysicalDrive", "physicalDrive", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PowerState":MoPropertyMeta("PowerState", "powerState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PredictiveFailureCount":MoPropertyMeta("PredictiveFailureCount", "predictiveFailureCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RawSize":MoPropertyMeta("RawSize", "rawSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"SasAddress0":MoPropertyMeta("SasAddress0", "sasAddress0", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SasAddress1":MoPropertyMeta("SasAddress1", "sasAddress1", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SequenceNumber":MoPropertyMeta("SequenceNumber", "sequenceNumber", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("StorageLocalDiskProps", "storageLocalDiskProps", "general-props", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageController', u'storageLocalDisk'])
			},

		"BiosVfUSBBootConfig": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpMakeDeviceNonBootable":MoPropertyMeta("VpMakeDeviceNonBootable", "vpMakeDeviceNonBootable", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfUSBBootConfig", "biosVfUSBBootConfig", "USB-Boot-Config", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"ProcessorUnit": {
			"Arch":MoPropertyMeta("Arch", "arch", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Dual-Core_Opteron", "Intel_P4_C", "Opteron", "Pentium_4", "Turion_64", "Xeon", "Xeon_MP", "any"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Cores":MoPropertyMeta("Cores", "cores", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-65535"]),
			"CoresEnabled":MoPropertyMeta("CoresEnabled", "coresEnabled", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-65535"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OperState":MoPropertyMeta("OperState", "operState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"SocketDesignation":MoPropertyMeta("SocketDesignation", "socketDesignation", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Speed":MoPropertyMeta("Speed", "speed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Stepping":MoPropertyMeta("Stepping", "stepping", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"Threads":MoPropertyMeta("Threads", "threads", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-65535"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("ProcessorUnit", "processorUnit", "cpu-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'faultInst', u'processorEnvStats'], ["Get"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"PowerMonitor": {
			"Average":MoPropertyMeta("Average", "average", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Current":MoPropertyMeta("Current", "current", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Domain":MoPropertyMeta("Domain", "domain", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["CPU", "Memory", "Platform"], ["0-4294967295"]),
			"Maximum":MoPropertyMeta("Maximum", "maximum", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Minimum":MoPropertyMeta("Minimum", "minimum", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("PowerMonitor", "powerMonitor", "pwrmonitor-", _VersionMeta.version_202c, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"CommIpmiLan": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Key":MoPropertyMeta("Key", "key", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[a-fA-F0-9]{40}""", [], ["0-4294967295"]),
			"Priv":MoPropertyMeta("Priv", "priv", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["admin", "read-only", "user"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("CommIpmiLan", "commIpmiLan", "ipmi-lan-svc", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"Error": {
			"Cookie":MoPropertyMeta("Cookie", "cookie", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ErrorCode":MoPropertyMeta("ErrorCode", "errorCode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ErrorDescr":MoPropertyMeta("ErrorDescr", "errorDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"InvocationResult":MoPropertyMeta("InvocationResult", "invocationResult", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Response":MoPropertyMeta("Response", "response", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Meta":MoMeta("Error", "error", "", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], [None], [""], [])
			},

		"BiosVfWorkLoadConfig": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpWorkLoadConfig":MoPropertyMeta("VpWorkLoadConfig", "vpWorkLoadConfig", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Balanced", "I/O Sensitive", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfWorkLoadConfig", "biosVfWorkLoadConfig", "work-load-config", _VersionMeta.version_204c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfOSBootWatchdogTimerPolicy": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpOSBootWatchdogTimerPolicy":MoPropertyMeta("VpOSBootWatchdogTimerPolicy", "vpOSBootWatchdogTimerPolicy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["do-nothing", "platform-default", "power-off", "reset"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfOSBootWatchdogTimerPolicy", "biosVfOSBootWatchdogTimerPolicy", "OS-Boot-Watchdog-Timer-Policy", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosSettings": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("BiosSettings", "biosSettings", "bios-settings", _VersionMeta.version_151f, "InputOutput", 0x7L, [], [u'biosVfASPMSupport', u'biosVfAdjacentCacheLinePrefetch', u'biosVfAltitude', u'biosVfAssertNMIOnPERR', u'biosVfAssertNMIOnSERR', u'biosVfBootOptionRetry', u'biosVfCDNEnable', u'biosVfCDNSupport', u'biosVfCPUEnergyPerformance', u'biosVfCPUFrequencyFloor', u'biosVfCPUPerformance', u'biosVfCPUPowerManagement', u'biosVfCkeLowPolicy', u'biosVfConsoleRedirection', u'biosVfCoreMultiProcessing', u'biosVfDCUPrefetch', u'biosVfDRAMClockThrottling', u'biosVfDemandScrub', u'biosVfDirectCacheAccess', u'biosVfDramRefreshRate', u'biosVfEnhancedIntelSpeedStepTech', u'biosVfExecuteDisableBit', u'biosVfExtendedAPIC', u'biosVfFRB2Enable', u'biosVfHardwarePrefetch', u'biosVfIOHResource', u'biosVfIntelHyperThreadingTech', u'biosVfIntelTurboBoostTech', u'biosVfIntelVTForDirectedIO', u'biosVfIntelVirtualizationTechnology', u'biosVfLOMPortOptionROM', u'biosVfLegacyUSBSupport', u'biosVfLvDIMMSupport', u'biosVfMMCFGBase', u'biosVfMemoryInterleave', u'biosVfMemoryMappedIOAbove4GB', u'biosVfMirroringMode', u'biosVfNUMAOptimized', u'biosVfOSBootWatchdogTimer', u'biosVfOSBootWatchdogTimerPolicy', u'biosVfOSBootWatchdogTimerTimeout', u'biosVfOnboardNIC', u'biosVfOnboardStorage', u'biosVfOnboardStorageSWStack', u'biosVfOutOfBandMgmtPort', u'biosVfPCIOptionROMs', u'biosVfPCISlotOptionROMEnable', u'biosVfPOSTErrorPause', u'biosVfPStateCoordType', u'biosVfPackageCStateLimit', u'biosVfPatrolScrub', u'biosVfPatrolScrubDuration', u'biosVfPchUsb30Mode', u'biosVfPciRomClp', u'biosVfProcessorC1E', u'biosVfProcessorC3Report', u'biosVfProcessorC6Report', u'biosVfProcessorCState', u'biosVfPwrPerfTuning', u'biosVfQPIConfig', u'biosVfQpiSnoopMode', u'biosVfSataModeSelect', u'biosVfSelectMemoryRASConfiguration', u'biosVfSerialPortAEnable', u'biosVfSparingMode', u'biosVfSrIov', u'biosVfTPMSupport', u'biosVfUCSMBootOrderRuleControl', u'biosVfUSBBootConfig', u'biosVfUSBEmulation', u'biosVfUSBPortsConfig', u'biosVfVgaPriority', u'biosVfWorkLoadConfig'], ["Get"], ["admin", "read-only", "user"], [u'biosUnit'])
			},

		"StorageUnusedLocalDisk": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CoercedSize":MoPropertyMeta("CoercedSize", "coercedSize", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"MediaType":MoPropertyMeta("MediaType", "mediaType", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PdStatus":MoPropertyMeta("PdStatus", "pdStatus", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageUnusedLocalDisk", "storageUnusedLocalDisk", "pd-[Id]", _VersionMeta.version_201a, "InputOutput", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'storageVirtualDriveCreatorUsingUnusedPhysicalDrive'])
			},

		"HuuFirmwareUpdateCancel": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_152, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("HuuFirmwareUpdateCancel", "huuFirmwareUpdateCancel", "firmwareUpdateCancel", _VersionMeta.version_152, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'huuController'])
			},

		"FaultInst": {
			"Ack":MoPropertyMeta("Ack", "ack", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], ["0-4294967295"]),
			"AffectedDN":MoPropertyMeta("AffectedDN", "affectedDN", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Cause":MoPropertyMeta("Cause", "cause", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ChangeSet":MoPropertyMeta("ChangeSet", "changeSet", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 512, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Code":MoPropertyMeta("Code", "code", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Created":MoPropertyMeta("Created", "created", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 384, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"HighestSeverity":MoPropertyMeta("HighestSeverity", "highestSeverity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "ulong", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"LastTransition":MoPropertyMeta("LastTransition", "lastTransition", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Lc":MoPropertyMeta("Lc", "lc", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|none|flapping|soaking-clear),){0,3}(defaultValue|none|flapping|soaking-clear){0,1}""", [], ["0-4294967295"]),
			"Occur":MoPropertyMeta("Occur", "occur", "ushort", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"OrigSeverity":MoPropertyMeta("OrigSeverity", "origSeverity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], ["0-4294967295"]),
			"PrevSeverity":MoPropertyMeta("PrevSeverity", "prevSeverity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rule":MoPropertyMeta("Rule", "rule", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Severity":MoPropertyMeta("Severity", "severity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cleared", "condition", "critical", "info", "major", "minor", "warning"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Tags":MoPropertyMeta("Tags", "tags", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|generic|server|network|storage|pod|security|operations|fsmstagefail|fsmstageretry|fsmstageremoteinv),){0,10}(defaultValue|generic|server|network|storage|pod|security|operations|fsmstagefail|fsmstageretry|fsmstageremoteinv){0,1}""", [], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["configuration", "connectivity", "environmental", "equipment", "fsm", "generic", "management", "network", "operational", "server", "sysdebug"], ["0-4294967295"]),
			"Meta":MoMeta("FaultInst", "faultInst", "fault-[Code]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'adaptorUnit', u'computeBoard', u'computeRackUnit', u'equipmentFan', u'equipmentPsu', u'memoryArray', u'memoryUnit', u'pciEquipSlot', u'powerBudget', u'processorUnit', u'storageController', u'storageFlexFlashController', u'storageFlexFlashPhysicalDrive', u'storageFlexFlashVirtualDrive', u'storageLocalDisk', u'storageRaidBattery', u'storageVirtualDrive', u'sysdebugMEpLog'])
			},

		"BiosVfPciRomClp": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPciRomClp":MoPropertyMeta("VpPciRomClp", "vpPciRomClp", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPciRomClp", "biosVfPciRomClp", "pci-rom-clp", _VersionMeta.version_204c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageFlexFlashOperationalProfile": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["clear-errors"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Controller":MoPropertyMeta("Controller", "controller", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"IoReadErrorThreshold":MoPropertyMeta("IoReadErrorThreshold", "ioReadErrorThreshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"IoWriteErrorThreshold":MoPropertyMeta("IoWriteErrorThreshold", "ioWriteErrorThreshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"OperatingMode":MoPropertyMeta("OperatingMode", "operatingMode", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RaidPrimaryMember":MoPropertyMeta("RaidPrimaryMember", "raidPrimaryMember", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10L, 0, 510, None, ["slot-1", "slot-2"], ["0-4294967295"]),
			"RaidSecondaryRole":MoPropertyMeta("RaidSecondaryRole", "raidSecondaryRole", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, None, ["active", "initializing"], ["0-4294967295"]),
			"RdErrCountSlot1Threshold":MoPropertyMeta("RdErrCountSlot1Threshold", "rdErrCountSlot1Threshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"RdErrCountSlot2Threshold":MoPropertyMeta("RdErrCountSlot2Threshold", "rdErrCountSlot2Threshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x80L, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x100L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VirtualDrivesEnabled":MoPropertyMeta("VirtualDrivesEnabled", "virtualDrivesEnabled", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x400L, 0, 30, None, [], ["0-4294967295"]),
			"WrErrCountSlot1Threshold":MoPropertyMeta("WrErrCountSlot1Threshold", "wrErrCountSlot1Threshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x800L, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"WrErrCountSlot2Threshold":MoPropertyMeta("WrErrCountSlot2Threshold", "wrErrCountSlot2Threshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 510, r"""([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("StorageFlexFlashOperationalProfile", "storageFlexFlashOperationalProfile", "oper-profile", _VersionMeta.version_202c, "InputOutput", 0x1fffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'storageFlexFlashController'])
			},

		"AdaptorRssProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"ReceiveSideScaling":MoPropertyMeta("ReceiveSideScaling", "receiveSideScaling", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorRssProfile", "adaptorRssProfile", "rss", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"AdvancedPowerProfile": {
			"AllowThrottle":MoPropertyMeta("AllowThrottle", "allowThrottle", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CorrAction":MoPropertyMeta("CorrAction", "corrAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["alert", "alert,shutdown", "none", "shutdown"], ["0-4294967295"]),
			"CorrTime":MoPropertyMeta("CorrTime", "corrTime", "uint", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, 0, 510, None, [], ["0-4294967295"]),
			"CpuPowerLimit":MoPropertyMeta("CpuPowerLimit", "cpuPowerLimit", "uint", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, 0, 510, None, [], ["0-4294967295"]),
			"CpuSafeThrotLvl":MoPropertyMeta("CpuSafeThrotLvl", "cpuSafeThrotLvl", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10L, 0, 510, None, [], ["0-100"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"HardCap":MoPropertyMeta("HardCap", "hardCap", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"MemSafeThrotLvl":MoPropertyMeta("MemSafeThrotLvl", "memSafeThrotLvl", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x80L, 0, 510, None, [], ["0-100"]),
			"MemoryPowerLimit":MoPropertyMeta("MemoryPowerLimit", "memoryPowerLimit", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x100L, 0, 510, None, [], ["0-4294967295"]),
			"MissRdgTimeout":MoPropertyMeta("MissRdgTimeout", "missRdgTimeout", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x200L, 0, 510, None, [], ["0-4294967295"]),
			"PlatSafeThrotLvl":MoPropertyMeta("PlatSafeThrotLvl", "platSafeThrotLvl", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x400L, 0, 510, None, [], ["0-100"]),
			"PlatformThermal":MoPropertyMeta("PlatformThermal", "platformThermal", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x800L, 0, 510, None, [], ["0-4294967295"]),
			"PowerLimit":MoPropertyMeta("PowerLimit", "powerLimit", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 510, None, [], ["0-4294967295"]),
			"ProfileEnabled":MoPropertyMeta("ProfileEnabled", "profileEnabled", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"ProfileType":MoPropertyMeta("ProfileType", "profileType", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4000L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"SuspendPeriod":MoPropertyMeta("SuspendPeriod", "suspendPeriod", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10000L, 0, 510, None, [], ["0-4294967295"]),
			"ThermalPowLimit":MoPropertyMeta("ThermalPowLimit", "thermalPowLimit", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x20000L, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AdvancedPowerProfile", "advancedPowerProfile", "advpwrprof", _VersionMeta.version_202c, "InputOutput", 0x3ffffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'powerBudget'])
			},

		"CommSnmp": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Com2Sec":MoPropertyMeta("Com2Sec", "com2Sec", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["None", "disabled", "full", "limited"], ["0-4294967295"]),
			"Community":MoPropertyMeta("Community", "community", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[!#$%\(\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,18}""", [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Port":MoPropertyMeta("Port", "port", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, [], ["1-65535"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["all", "none", "tcp", "udp"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"SysContact":MoPropertyMeta("SysContact", "sysContact", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 64, None, [], ["0-4294967295"]),
			"SysLocation":MoPropertyMeta("SysLocation", "sysLocation", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, 0, 64, None, [], ["0-4294967295"]),
			"TrapCommunity":MoPropertyMeta("TrapCommunity", "trapCommunity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""[!#$%\(\)\*\+,\-\./:<=\[\]\^_\{\}~a-zA-Z0-9]{0,18}""", [], ["0-4294967295"]),
			"Meta":MoMeta("CommSnmp", "commSnmp", "snmp-svc", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [u'commSnmpTrap', u'commSnmpUser'], ["Get", "Set"], ["admin", "read-only", "user"], [u'commSvcEp'])
			},

		"HuuUpdateComponentStatus": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CntrlId":MoPropertyMeta("CntrlId", "cntrlId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Component":MoPropertyMeta("Component", "component", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DeviceId":MoPropertyMeta("DeviceId", "deviceId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"ErrorDescription":MoPropertyMeta("ErrorDescription", "errorDescription", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_154, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"MacAddr":MoPropertyMeta("MacAddr", "macAddr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"NewVersion":MoPropertyMeta("NewVersion", "newVersion", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"RunningVersion":MoPropertyMeta("RunningVersion", "runningVersion", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"SubDeviceId":MoPropertyMeta("SubDeviceId", "subDeviceId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SubVendorId":MoPropertyMeta("SubVendorId", "subVendorId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"UpdateStatus":MoPropertyMeta("UpdateStatus", "updateStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VendorId":MoPropertyMeta("VendorId", "vendorId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VerifyStatus":MoPropertyMeta("VerifyStatus", "verifyStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("HuuUpdateComponentStatus", "huuUpdateComponentStatus", "component-[Component]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'huuFirmwareUpdateStatus'])
			},

		"BiosPassword": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", None, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Password":MoPropertyMeta("Password", "password", "string", None, MoPropertyMeta.READ_WRITE, 0x2L, None, None, r"""[\S+]{0,20}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", None, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("BiosPassword", "biosPassword", "bios-pw", None, "InputOutput", 0xfL, [], [], [None], ["admin"], [])
			},

		"BiosBootDevGrp": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Descr":MoPropertyMeta("Descr", "descr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["bev-order", "cd-order", "fdd-order", "hdd-order", "internal-efi-shell", "network-device-order", "system-boot-order"], ["0-4294967295"]),
			"Meta":MoMeta("BiosBootDevGrp", "biosBootDevGrp", "bdg-[Order]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'biosBootDev'], ["Get"], ["admin", "read-only", "user"], [u'biosBOT'])
			},

		"SystemIOController": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_202c, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-999"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("SystemIOController", "systemIOController", "sioc-[Id]", _VersionMeta.version_202c, "OutputOnly", 0x0L, [], [u'firmwareBootDefinition', u'firmwareRunning', u'firmwareUpdatable'], ["Get"], ["read-only"], [u'computeRackUnit'])
			},

		"BiosVfMMCFGBase": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpMMCFGBase":MoPropertyMeta("VpMMCFGBase", "vpMMCFGBase", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["1 GB", "2 GB", "2.5 GB", "3 GB", "Auto", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfMMCFGBase", "biosVfMMCFGBase", "MMCFG-Base", _VersionMeta.version_201a, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"AaaUserEp": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("AaaUserEp", "aaaUserEp", "user-ext", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'aaaSession', u'aaaUser'], ["Get"], ["admin", "read-only", "user"], [u'topSystem'])
			},

		"NetworkAdapterEthIf": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Mac":MoPropertyMeta("Mac", "mac", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("NetworkAdapterEthIf", "networkAdapterEthIf", "eth-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'networkAdapterUnit'])
			},

		"FirmwareUpdatable": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Deployment":MoPropertyMeta("Deployment", "deployment", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["backup", "primary"], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"OperState":MoPropertyMeta("OperState", "operState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["activating", "bad-image", "failed", "pending-next-boot", "ready", "rebooting", "scheduled", "set-startup", "throttled", "updating", "upgrading"], ["0-4294967295"]),
			"Progress":MoPropertyMeta("Progress", "progress", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Protocol":MoPropertyMeta("Protocol", "protocol", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], ["0-4294967295"]),
			"Pwd":MoPropertyMeta("Pwd", "pwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 256, None, [], ["0-4294967295"]),
			"RemotePath":MoPropertyMeta("RemotePath", "remotePath", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{0,128}""", [], ["0-4294967295"]),
			"RemoteServer":MoPropertyMeta("RemoteServer", "remoteServer", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"SecureBoot":MoPropertyMeta("SecureBoot", "secureBoot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["disable", "disabled", "enable", "enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["adaptor", "blade-bios", "blade-controller", "sioc"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, 0, 256, None, [], ["0-4294967295"]),
			"Version":MoPropertyMeta("Version", "version", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("FirmwareUpdatable", "firmwareUpdatable", "fw-updatable", _VersionMeta.version_151f, "InputOutput", 0x7ffL, [], [], ["Get"], ["admin", "read-only", "user"], [u'biosUnit', u'mgmtController', u'systemIOController'])
			},

		"BiosVfSelectMemoryRASConfiguration": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpSelectMemoryRASConfiguration":MoPropertyMeta("VpSelectMemoryRASConfiguration", "vpSelectMemoryRASConfiguration", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["lockstep", "maximum-performance", "mirroring", "platform-default", "sparing"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfSelectMemoryRASConfiguration", "biosVfSelectMemoryRASConfiguration", "SelectMemory-RAS-configuration", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"IodSnapshotStart": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["trigger", "triggered"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_152, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"IsoShare":MoPropertyMeta("IsoShare", "isoShare", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, 0x4L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,255}""", [], ["0-4294967295"]),
			"IsoShareFile":MoPropertyMeta("IsoShareFile", "isoShareFile", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"IsoShareIp":MoPropertyMeta("IsoShareIp", "isoShareIp", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"IsoSharePath":MoPropertyMeta("IsoSharePath", "isoSharePath", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"IsoShareType":MoPropertyMeta("IsoShareType", "isoShareType", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["cifs", "nfs", "sd", "www"], ["0-4294967295"]),
			"Password":MoPropertyMeta("Password", "password", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, [], ["0-4294967295"]),
			"RemoteShareFile":MoPropertyMeta("RemoteShareFile", "remoteShareFile", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, None, [], ["0-4294967295"]),
			"RemoteShareIp":MoPropertyMeta("RemoteShareIp", "remoteShareIp", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, r"""(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])""", [], ["0-4294967295"]),
			"RemoteSharePassword":MoPropertyMeta("RemoteSharePassword", "remoteSharePassword", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, [], ["0-4294967295"]),
			"RemoteSharePath":MoPropertyMeta("RemoteSharePath", "remoteSharePath", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x200L, 0, 510, None, [], ["0-4294967295"]),
			"RemoteShareType":MoPropertyMeta("RemoteShareType", "remoteShareType", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["scp", "sftp", "tftp"], ["0-4294967295"]),
			"RemoteShareUsername":MoPropertyMeta("RemoteShareUsername", "remoteShareUsername", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x1000L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TimeOut":MoPropertyMeta("TimeOut", "timeOut", "uint", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, [], ["30-240"]),
			"Username":MoPropertyMeta("Username", "username", "string", _VersionMeta.version_152, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, [], ["0-4294967295"]),
			"Meta":MoMeta("IodSnapshotStart", "iodSnapshotStart", "snapshotStart", _VersionMeta.version_152, "InputOutput", 0xffffL, [], [], [None], ["admin"], [u'iodController'])
			},

		"SysdebugTechSupportExport": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"FsmProgr":MoPropertyMeta("FsmProgr", "fsmProgr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-100"]),
			"FsmStageDescr":MoPropertyMeta("FsmStageDescr", "fsmStageDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"FsmStatus":MoPropertyMeta("FsmStatus", "fsmStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Protocol":MoPropertyMeta("Protocol", "protocol", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["ftp", "http", "scp", "sftp", "tftp"], ["0-4294967295"]),
			"Pwd":MoPropertyMeta("Pwd", "pwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, None, [], ["0-4294967295"]),
			"RemoteFile":MoPropertyMeta("RemoteFile", "remoteFile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, 0, 256, None, [], ["0-4294967295"]),
			"Meta":MoMeta("SysdebugTechSupportExport", "sysdebugTechSupportExport", "tech-support", _VersionMeta.version_151f, "InputOutput", 0x1ffL, [], [], [None], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"EquipmentFan": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["1-8"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Module":MoPropertyMeta("Module", "module", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-8"]),
			"Operability":MoPropertyMeta("Operability", "operability", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Power":MoPropertyMeta("Power", "power", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Thermal":MoPropertyMeta("Thermal", "thermal", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Tray":MoPropertyMeta("Tray", "tray", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["1-8"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Voltage":MoPropertyMeta("Voltage", "voltage", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Meta":MoMeta("EquipmentFan", "equipmentFan", "fan-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'faultInst'], ["Get"], ["admin", "read-only", "user"], [u'equipmentFanModule'])
			},

		"BiosVfVgaPriority": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpVgaPriority":MoPropertyMeta("VpVgaPriority", "vpVgaPriority", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Offboard", "Onboard", "Onboard VGA Disabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfVgaPriority", "biosVfVgaPriority", "VgaPriority", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"MgmtImporter": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"FsmDescr":MoPropertyMeta("FsmDescr", "fsmDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"FsmRmtInvErrCode":MoPropertyMeta("FsmRmtInvErrCode", "fsmRmtInvErrCode", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, ["", "Aborted", "Error collecting configuration data", "Error importing configuration", "Partially Imported", "TFTP Error", "Unknown error", "none"], ["0-4294967295"]),
			"FsmRmtInvErrDescr":MoPropertyMeta("FsmRmtInvErrDescr", "fsmRmtInvErrDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], ["0-4294967295"]),
			"FsmStageDescr":MoPropertyMeta("FsmStageDescr", "fsmStageDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Passphrase":MoPropertyMeta("Passphrase", "passphrase", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, 0, 256, None, [], ["0-4294967295"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], ["0-4294967295"]),
			"Pwd":MoPropertyMeta("Pwd", "pwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 256, None, [], ["0-4294967295"]),
			"RemoteFile":MoPropertyMeta("RemoteFile", "remoteFile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 128, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, 0, 256, None, [], ["0-4294967295"]),
			"Meta":MoMeta("MgmtImporter", "mgmtImporter", "import-config", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], [None], ["admin", "read-only", "user"], [u'topSystem'])
			},

		"LsbootVMedia": {
			"Access":MoPropertyMeta("Access", "access", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["", "read-only-local", "read-only-remote", "read-write-drive", "read-write-local", "read-write-remote"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_201a, MoPropertyMeta.NAMING, 0x4L, None, None, r"""(([a-zA-Z0-9]{1})|([a-zA-Z0-9]{1}[a-zA-Z0-9_\-]{0,28}[a-zA-Z0-9]{1})|([a-zA-Z0-9]{2}))""", [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["1-255"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"State":MoPropertyMeta("State", "state", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subtype":MoPropertyMeta("Subtype", "subtype", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["", "cimc-mapped-dvd", "cimc-mapped-hdd", "kvm-mapped-dvd", "kvm-mapped-fdd", "kvm-mapped-hdd"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["VMEDIA"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootVMedia", "lsbootVMedia", "vm-[Name]", _VersionMeta.version_201a, "InputOutput", 0x1ffL, [], [], ["Add", "Get", "Remove", "Set"], ["admin", "read-only", "user"], [u'lsbootDevPrecision'])
			},

		"BiosVfOSBootWatchdogTimer": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpOSBootWatchdogTimer":MoPropertyMeta("VpOSBootWatchdogTimer", "vpOSBootWatchdogTimer", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfOSBootWatchdogTimer", "biosVfOSBootWatchdogTimer", "OS-Boot-Watchdog-Timer-Param", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfAdjacentCacheLinePrefetch": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpAdjacentCacheLinePrefetch":MoPropertyMeta("VpAdjacentCacheLinePrefetch", "vpAdjacentCacheLinePrefetch", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfAdjacentCacheLinePrefetch", "biosVfAdjacentCacheLinePrefetch", "Adjacent-Cache-Line-Prefetch", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"MgmtIf": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"DdnsDomain":MoPropertyMeta("DdnsDomain", "ddnsDomain", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"DdnsEnable":MoPropertyMeta("DdnsEnable", "ddnsEnable", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"DhcpEnable":MoPropertyMeta("DhcpEnable", "dhcpEnable", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"DnsAlternate":MoPropertyMeta("DnsAlternate", "dnsAlternate", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"DnsPreferred":MoPropertyMeta("DnsPreferred", "dnsPreferred", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"DnsUsingDhcp":MoPropertyMeta("DnsUsingDhcp", "dnsUsingDhcp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"ExtEnabled":MoPropertyMeta("ExtEnabled", "extEnabled", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"ExtGw":MoPropertyMeta("ExtGw", "extGw", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"ExtIp":MoPropertyMeta("ExtIp", "extIp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"ExtMask":MoPropertyMeta("ExtMask", "extMask", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, 0, 63, r"""(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])""", [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"IfType":MoPropertyMeta("IfType", "ifType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["physical"], ["0-4294967295"]),
			"Mac":MoPropertyMeta("Mac", "mac", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"NicMode":MoPropertyMeta("NicMode", "nicMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["cisco_card", "dedicated", "shared_lom", "shared_lom_10g", "shared_lom_ext", "shipping"], ["0-4294967295"]),
			"NicRedundancy":MoPropertyMeta("NicRedundancy", "nicRedundancy", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, ["active-active", "active-standby", "none"], ["0-4294967295"]),
			"PortProfile":MoPropertyMeta("PortProfile", "portProfile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, r"""[a-zA-Z0-9_\-]{0,80}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4000L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8000L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Subject":MoPropertyMeta("Subject", "subject", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"V6SlaacIp":MoPropertyMeta("V6SlaacIp", "v6SlaacIp", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], ["0-4294967295"]),
			"V6dhcpEnable":MoPropertyMeta("V6dhcpEnable", "v6dhcpEnable", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x10000L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"V6dnsAlternate":MoPropertyMeta("V6dnsAlternate", "v6dnsAlternate", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x20000L, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], ["0-4294967295"]),
			"V6dnsPreferred":MoPropertyMeta("V6dnsPreferred", "v6dnsPreferred", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x40000L, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], ["0-4294967295"]),
			"V6dnsUsingDhcp":MoPropertyMeta("V6dnsUsingDhcp", "v6dnsUsingDhcp", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x80000L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"V6extEnabled":MoPropertyMeta("V6extEnabled", "v6extEnabled", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x100000L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"V6extGw":MoPropertyMeta("V6extGw", "v6extGw", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x200000L, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], ["0-4294967295"]),
			"V6extIp":MoPropertyMeta("V6extIp", "v6extIp", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x400000L, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], ["0-4294967295"]),
			"V6linkLocal":MoPropertyMeta("V6linkLocal", "v6linkLocal", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, r"""([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:""", [], ["0-4294967295"]),
			"V6prefix":MoPropertyMeta("V6prefix", "v6prefix", "uint", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x800000L, None, None, None, [], ["1-128"]),
			"VicSlot":MoPropertyMeta("VicSlot", "vicSlot", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1000000L, None, None, None, ["0", "1", "10", "2", "4", "5", "9", "flex-lom", "riser1", "riser2"], ["0-4294967295"]),
			"VlanEnable":MoPropertyMeta("VlanEnable", "vlanEnable", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2000000L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"VlanId":MoPropertyMeta("VlanId", "vlanId", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4000000L, None, None, None, [], ["1-4094"]),
			"VlanPriority":MoPropertyMeta("VlanPriority", "vlanPriority", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8000000L, None, None, None, [], ["0-7"]),
			"Meta":MoMeta("MgmtIf", "mgmtIf", "if-1", _VersionMeta.version_151f, "InputOutput", 0xfffffffL, [], [u'ipBlocking'], ["Get", "Set"], ["admin", "read-only", "user"], [u'mgmtController'])
			},

		"AdaptorFcGenProfile": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"ClassOfService":MoPropertyMeta("ClassOfService", "classOfService", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, r"""[0-6]""", [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Mac":MoPropertyMeta("Mac", "mac", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", ["AUTO"], ["0-4294967295"]),
			"MaxDataFieldSize":MoPropertyMeta("MaxDataFieldSize", "maxDataFieldSize", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, [], ["256-2112"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[0-9]|1[0-7]""", ["ANY"], ["0-4294967295"]),
			"PersistentLunBind":MoPropertyMeta("PersistentLunBind", "persistentLunBind", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"RateLimit":MoPropertyMeta("RateLimit", "rateLimit", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["OFF"], ["1-10000"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Vlan":MoPropertyMeta("Vlan", "vlan", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["NONE"], ["1-4094"]),
			"Meta":MoMeta("AdaptorFcGenProfile", "adaptorFcGenProfile", "general", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostFcIf'])
			},

		"MgmtBackup": {
			"AdminState":MoPropertyMeta("AdminState", "adminState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"FsmDescr":MoPropertyMeta("FsmDescr", "fsmDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"FsmRmtInvErrCode":MoPropertyMeta("FsmRmtInvErrCode", "fsmRmtInvErrCode", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, ["", "Aborted", "Error collecting configuration data", "Error importing configuration", "Partially Imported", "TFTP Error", "Unknown error", "none"], ["0-4294967295"]),
			"FsmRmtInvErrDescr":MoPropertyMeta("FsmRmtInvErrDescr", "fsmRmtInvErrDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, 0, 510, None, [], ["0-4294967295"]),
			"FsmStageDescr":MoPropertyMeta("FsmStageDescr", "fsmStageDescr", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Hostname":MoPropertyMeta("Hostname", "hostname", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, r"""(([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:([0-9A-Fa-f]{1,4}:[0-9A-Fa-f]{0,4}|:[0-9A-Fa-f]{1,4})?|(:[0-9A-Fa-f]{1,4}){0,2})|(:[0-9A-Fa-f]{1,4}){0,3})|(:[0-9A-Fa-f]{1,4}){0,4})|:(:[0-9A-Fa-f]{1,4}){0,5})((:[0-9A-Fa-f]{1,4}){2}|:(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])(\.(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])){3})|(([0-9A-Fa-f]{1,4}:){1,6}|:):[0-9A-Fa-f]{0,4}|([0-9A-Fa-f]{1,4}:){7}:) |((([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})|(([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+)|([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))""", [], ["0-4294967295"]),
			"Passphrase":MoPropertyMeta("Passphrase", "passphrase", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, 0, 256, None, [], ["0-4294967295"]),
			"Proto":MoPropertyMeta("Proto", "proto", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["ftp", "http", "none", "scp", "sftp", "tftp"], ["0-4294967295"]),
			"Pwd":MoPropertyMeta("Pwd", "pwd", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, 0, 256, None, [], ["0-4294967295"]),
			"RemoteFile":MoPropertyMeta("RemoteFile", "remoteFile", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, 0, 128, r"""[^\(\)~`'\?\\"";<>\|&\*\^$%]{1,128}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, 0, 256, None, [], ["0-4294967295"]),
			"Meta":MoMeta("MgmtBackup", "mgmtBackup", "export-config", _VersionMeta.version_151f, "InputOutput", 0x3ffL, [], [], [None], ["admin", "read-only", "user"], [u'topSystem'])
			},

		"BiosVfExecuteDisableBit": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpExecuteDisableBit":MoPropertyMeta("VpExecuteDisableBit", "vpExecuteDisableBit", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfExecuteDisableBit", "biosVfExecuteDisableBit", "Execute-Disable-Bit", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"LsbootBootSecurity": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"SecureBoot":MoPropertyMeta("SecureBoot", "secureBoot", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["disable", "disabled", "enable", "enabled"], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("LsbootBootSecurity", "lsbootBootSecurity", "boot-security", _VersionMeta.version_201a, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "user"], [u'lsbootDef'])
			},

		"HuuFirmwareCatalog": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"NumOfComponents":MoPropertyMeta("NumOfComponents", "numOfComponents", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("HuuFirmwareCatalog", "huuFirmwareCatalog", "firmwareCatalog", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'huuFirmwareCatalogComponent'], ["Get"], ["admin", "read-only", "user"], [u'huuController'])
			},

		"TopRoot": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("TopRoot", "topRoot", "", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'topSystem'], ["Get"], ["admin", "read-only", "user"], [])
			},

		"BiosVfSrIov": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpSrIov":MoPropertyMeta("VpSrIov", "vpSrIov", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfSrIov", "biosVfSrIov", "sr-iov", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageFlexFlashVirtualDriveImageMap": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["map", "unmap"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Map":MoPropertyMeta("Map", "map", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x4L, 0, 510, None, ["cifs", "nfs"], ["0-4294967295"]),
			"MountOptions":MoPropertyMeta("MountOptions", "mountOptions", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, 1, 510, None, [], ["0-4294967295"]),
			"Password":MoPropertyMeta("Password", "password", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x10L, 0, 510, None, [], ["0-4294967295"]),
			"RemoteFile":MoPropertyMeta("RemoteFile", "remoteFile", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x20L, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], ["0-4294967295"]),
			"RemoteShare":MoPropertyMeta("RemoteShare", "remoteShare", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x40L, 0, 510, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{1,235}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x80L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"ToEnableMapping":MoPropertyMeta("ToEnableMapping", "toEnableMapping", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, 0x200L, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"Username":MoPropertyMeta("Username", "username", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x400L, 0, 510, None, [], ["0-4294967295"]),
			"VirtualDrive":MoPropertyMeta("VirtualDrive", "virtualDrive", "string", _VersionMeta.version_202c, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageFlexFlashVirtualDriveImageMap", "storageFlexFlashVirtualDriveImageMap", "vdrive-map-[VirtualDrive]", _VersionMeta.version_202c, "InputOutput", 0x7ffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'storageFlexFlashController'])
			},

		"ComputeRackUnitMbTempStats": {
			"AmbientTemp":MoPropertyMeta("AmbientTemp", "ambientTemp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"FrontTemp":MoPropertyMeta("FrontTemp", "frontTemp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
			"Ioh1Temp":MoPropertyMeta("Ioh1Temp", "ioh1Temp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
			"Ioh2Temp":MoPropertyMeta("Ioh2Temp", "ioh2Temp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
			"RearTemp":MoPropertyMeta("RearTemp", "rearTemp", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [""], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TimeCollected":MoPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("ComputeRackUnitMbTempStats", "computeRackUnitMbTempStats", "temp-stats", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"AdaptorPortProfiles": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"PortProfilesCount":MoPropertyMeta("PortProfilesCount", "portProfilesCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"PortProfilesName":MoPropertyMeta("PortProfilesName", "portProfilesName", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorPortProfiles", "adaptorPortProfiles", "port-profiles", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'adaptorExtEthIf'])
			},

		"ServerUtilization": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CpuUtilization":MoPropertyMeta("CpuUtilization", "cpuUtilization", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"IoUtilization":MoPropertyMeta("IoUtilization", "ioUtilization", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MemoryUtilization":MoPropertyMeta("MemoryUtilization", "memoryUtilization", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OverallUtilization":MoPropertyMeta("OverallUtilization", "overallUtilization", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("ServerUtilization", "serverUtilization", "utilization", _VersionMeta.version_202c, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"AaaSession": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Host":MoPropertyMeta("Host", "host", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 1, 32, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Ui":MoPropertyMeta("Ui", "ui", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["ep", "none", "shell", "vMedia", "web"], ["0-4294967295"]),
			"User":MoPropertyMeta("User", "user", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Meta":MoMeta("AaaSession", "aaaSession", "term-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'aaaUserEp'])
			},

		"BiosBootMode": {
			"ActualBootMode":MoPropertyMeta("ActualBootMode", "actualBootMode", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Legacy", "Uefi", "Unknown"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_201a, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("BiosBootMode", "biosBootMode", "boot-mode", _VersionMeta.version_201a, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "user"], [u'biosBOT'])
			},

		"BiosVfTPMSupport": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpTPMSupport":MoPropertyMeta("VpTPMSupport", "vpTPMSupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfTPMSupport", "biosVfTPMSupport", "TPM-Support", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageFlexFlashPhysicalDrive": {
			"BlockSize":MoPropertyMeta("BlockSize", "blockSize", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Capacity":MoPropertyMeta("Capacity", "capacity", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CardMode":MoPropertyMeta("CardMode", "cardMode", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CardStatus":MoPropertyMeta("CardStatus", "cardStatus", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CardType":MoPropertyMeta("CardType", "cardType", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_202c, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Controller":MoPropertyMeta("Controller", "controller", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"DrivesEnabled":MoPropertyMeta("DrivesEnabled", "drivesEnabled", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ManufacturerDate":MoPropertyMeta("ManufacturerDate", "manufacturerDate", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ManufacturerId":MoPropertyMeta("ManufacturerId", "manufacturerId", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OemId":MoPropertyMeta("OemId", "oemId", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PartitionCount":MoPropertyMeta("PartitionCount", "partitionCount", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PasswordProtected":MoPropertyMeta("PasswordProtected", "passwordProtected", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PdStatus":MoPropertyMeta("PdStatus", "pdStatus", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysicalDrive":MoPropertyMeta("PhysicalDrive", "physicalDrive", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PhysicalDriveId":MoPropertyMeta("PhysicalDriveId", "physicalDriveId", "string", _VersionMeta.version_202c, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"ProductName":MoPropertyMeta("ProductName", "productName", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ProductRevision":MoPropertyMeta("ProductRevision", "productRevision", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RaidRole":MoPropertyMeta("RaidRole", "raidRole", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ReadErrorCount":MoPropertyMeta("ReadErrorCount", "readErrorCount", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ReadErrorThreshold":MoPropertyMeta("ReadErrorThreshold", "readErrorThreshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"SerialNumber":MoPropertyMeta("SerialNumber", "serialNumber", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Signature":MoPropertyMeta("Signature", "signature", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SlotNumber":MoPropertyMeta("SlotNumber", "slotNumber", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"SyncMode":MoPropertyMeta("SyncMode", "syncMode", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"WriteEnabled":MoPropertyMeta("WriteEnabled", "writeEnabled", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"WriteErrorCount":MoPropertyMeta("WriteErrorCount", "writeErrorCount", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"WriteErrorThreshold":MoPropertyMeta("WriteErrorThreshold", "writeErrorThreshold", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageFlexFlashPhysicalDrive", "storageFlexFlashPhysicalDrive", "card-[PhysicalDriveId]", _VersionMeta.version_202c, "OutputOnly", 0x0L, [], [u'faultInst'], ["Get"], ["admin", "read-only", "user"], [u'storageFlexFlashController'])
			},

		"BiosVfQpiSnoopMode": {
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpQpiSnoopMode":MoPropertyMeta("VpQpiSnoopMode", "vpQpiSnoopMode", "string", _VersionMeta.version_204c, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["cluster-on-die", "early-snoop", "home-snoop", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfQpiSnoopMode", "biosVfQpiSnoopMode", "QPI-Snoop-Mode", _VersionMeta.version_204c, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"OneTimeBootDevice": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Device":MoPropertyMeta("Device", "device", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["huu", "hv", "none", "scu"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("OneTimeBootDevice", "oneTimeBootDevice", "boot-one-time", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"BiosVfPatrolScrubDuration": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPatrolScrubDuration":MoPropertyMeta("VpPatrolScrubDuration", "vpPatrolScrubDuration", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["platform-default"], ["5-23"]),
			"Meta":MoMeta("BiosVfPatrolScrubDuration", "biosVfPatrolScrubDuration", "Patrol-Scrub-Duration", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfPCIOptionROMs": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPCIOptionROMs":MoPropertyMeta("VpPCIOptionROMs", "vpPCIOptionROMs", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "Legacy Only", "UEFI Only", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPCIOptionROMs", "biosVfPCIOptionROMs", "PCI-OptionROMs", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageLocalDisk": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["locator-led-off", "locator-led-on", "make-dedicated-hot-spare", "make-global-hot-spare", "make-jbod", "make-unconfigured-good", "prepare-for-removal", "remove-hot-spare", "set-boot-drive", "undo-prepare-for-removal"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CoercedSize":MoPropertyMeta("CoercedSize", "coercedSize", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DedicatedHotSpareForVDId":MoPropertyMeta("DedicatedHotSpareForVDId", "dedicatedHotSpareForVDId", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [""], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"DriveFirmware":MoPropertyMeta("DriveFirmware", "driveFirmware", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DriveSerialNumber":MoPropertyMeta("DriveSerialNumber", "driveSerialNumber", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DriveState":MoPropertyMeta("DriveState", "driveState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Health":MoPropertyMeta("Health", "health", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x8L, 0, 510, None, [], ["0-256"]),
			"InterfaceType":MoPropertyMeta("InterfaceType", "interfaceType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"LinkSpeed":MoPropertyMeta("LinkSpeed", "linkSpeed", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MediaType":MoPropertyMeta("MediaType", "mediaType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Online":MoPropertyMeta("Online", "online", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PdStatus":MoPropertyMeta("PdStatus", "pdStatus", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PredictiveFailureCount":MoPropertyMeta("PredictiveFailureCount", "predictiveFailureCount", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"ProductId":MoPropertyMeta("ProductId", "productId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageLocalDisk", "storageLocalDisk", "pd-[Id]", _VersionMeta.version_151f, "InputOutput", 0x3fL, [], [u'faultInst', u'storageLocalDiskProps', u'storageOperation'], ["Get", "Set"], ["admin", "read-only", "user"], [u'storageController'])
			},

		"BiosUnit": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["enter-bios-setup"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("BiosUnit", "biosUnit", "bios", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [u'biosBOT', u'biosPlatformDefaults', u'biosSettings', u'firmwareBootDefinition', u'firmwareRunning', u'firmwareUpdatable'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"BiosVfPStateCoordType": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPStateCoordType":MoPropertyMeta("VpPStateCoordType", "vpPStateCoordType", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["HW ALL", "SW ALL", "SW ANY", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPStateCoordType", "biosVfPStateCoordType", "p-state-coord", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"IodController": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_152, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("IodController", "iodController", "iod", _VersionMeta.version_152, "OutputOnly", 0x0L, [], [u'iodSnapshotCancel', u'iodSnapshotStart', u'iodSnapshotStatus'], ["Get"], ["read-only"], [u'topSystem'])
			},

		"BiosVfDirectCacheAccess": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpDirectCacheAccess":MoPropertyMeta("VpDirectCacheAccess", "vpDirectCacheAccess", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Auto", "Disabled", "Enabled", "auto", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfDirectCacheAccess", "biosVfDirectCacheAccess", "Direct-Cache-Access", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageController": {
			"AdminAction":MoPropertyMeta("AdminAction", "adminAction", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_WRITE, 0x1L, 0, 510, None, ["clear-boot-drive", "clear-foreign-config", "delete-all-vds-reset-pds", "disable-jbod", "enable-jbod", "get-tty-log", "import-foreign-config"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, 0x4L, None, None, r"""[a-zA-Z0-9_\-]{1,30}""", [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"PciSlot":MoPropertyMeta("PciSlot", "pciSlot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"RaidSupport":MoPropertyMeta("RaidSupport", "raidSupport", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("StorageController", "storageController", "storage-[Type]-[Id]", _VersionMeta.version_151f, "InputOutput", 0x1fL, [], [u'faultInst', u'firmwareBootDefinition', u'firmwareRunning', u'storageControllerProps', u'storageControllerSettings', u'storageLocalDisk', u'storageLocalDiskProps', u'storageRaidBattery', u'storageVirtualDrive', u'storageVirtualDriveCreatorUsingUnusedPhysicalDrive', u'storageVirtualDriveCreatorUsingVirtualDriveGroup'], ["Get", "Set"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"MemoryUnit": {
			"Array":MoPropertyMeta("Array", "array", "ushort", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"BankLocator":MoPropertyMeta("BankLocator", "bankLocator", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Capacity":MoPropertyMeta("Capacity", "capacity", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Clock":MoPropertyMeta("Clock", "clock", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"FormFactor":MoPropertyMeta("FormFactor", "formFactor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["DIMM", "FB-DIMM", "Other", "RIMM", "SIMM", "SODIMM", "SRIMM", "TSOP", "Unknown", "undiscovered"], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Location":MoPropertyMeta("Location", "location", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"MemoryTypeDetail":MoPropertyMeta("MemoryTypeDetail", "memoryTypeDetail", "string", _VersionMeta.version_201a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OperState":MoPropertyMeta("OperState", "operState", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Operability":MoPropertyMeta("Operability", "operability", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Type":MoPropertyMeta("Type", "type", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["3DRAM", "CDRAM", "DDR", "DDR2", "DDR2 FB-DIMM", "DDR3", "DRAM", "EDRAM", "EEPROM", "EPROM", "FBD2", "FEPROM", "FLASH", "Other", "RAM", "RDRAM", "ROM", "SDRAM", "SGRAM", "SRAM", "Unknown", "VRAM", "undiscovered"], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Visibility":MoPropertyMeta("Visibility", "visibility", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "unknown", "yes"], ["0-4294967295"]),
			"Width":MoPropertyMeta("Width", "width", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["unspecified"], ["0-4294967295"]),
			"Meta":MoMeta("MemoryUnit", "memoryUnit", "mem-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'faultInst', u'memoryUnitEnvStats'], ["Get"], ["admin", "read-only", "user"], [u'memoryArray'])
			},

		"BiosVfPatrolScrub": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpPatrolScrub":MoPropertyMeta("VpPatrolScrub", "vpPatrolScrub", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfPatrolScrub", "biosVfPatrolScrub", "Patrol-Scrub-Param", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"MemoryUnitEnvStats": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Temperature":MoPropertyMeta("Temperature", "temperature", "float", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"TimeCollected":MoPropertyMeta("TimeCollected", "timeCollected", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("MemoryUnitEnvStats", "memoryUnitEnvStats", "dimm-env-stats", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'memoryUnit'])
			},

		"AdaptorEthGenProfile": {
			"Arfs":MoPropertyMeta("Arfs", "arfs", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Order":MoPropertyMeta("Order", "order", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[0-9]|1[0-7]""", ["ANY"], ["0-4294967295"]),
			"RateLimit":MoPropertyMeta("RateLimit", "rateLimit", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["OFF"], ["1-10000"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x10L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TrustedClassOfService":MoPropertyMeta("TrustedClassOfService", "trustedClassOfService", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"UplinkFailbackTimeout":MoPropertyMeta("UplinkFailbackTimeout", "uplinkFailbackTimeout", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""(0{0,2}[0-9]|0?[1-9][0-9]|[1-5][0-9][0-9]|600)""", [], ["0-4294967295"]),
			"UplinkFailover":MoPropertyMeta("UplinkFailover", "uplinkFailover", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Vlan":MoPropertyMeta("Vlan", "vlan", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x200L, None, None, None, ["NONE"], ["1-4094"]),
			"VlanMode":MoPropertyMeta("VlanMode", "vlanMode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, ["ACCESS", "TRUNK"], ["0-4294967295"]),
			"Vmq":MoPropertyMeta("Vmq", "vmq", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], ["0-4294967295"]),
			"Meta":MoMeta("AdaptorEthGenProfile", "adaptorEthGenProfile", "general", _VersionMeta.version_151f, "InputOutput", 0xfffL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'adaptorHostEthIf'])
			},

		"BiosVfUCSMBootOrderRuleControl": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpUCSMBootOrderRule":MoPropertyMeta("VpUCSMBootOrderRule", "vpUCSMBootOrderRule", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Loose", "Strict", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfUCSMBootOrderRuleControl", "biosVfUCSMBootOrderRuleControl", "Boot-Order-Rules", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"StorageLocalDiskSlotEp": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, None, None, None, [], ["0-4294967295"]),
			"Operability":MoPropertyMeta("Operability", "operability", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["accessibility-problem", "auto-upgrade", "bios-post-timeout", "chassis-limit-exceeded", "config", "decomissioning", "degraded", "disabled", "discovery", "discovery-failed", "equipment-problem", "fabric-conn-problem", "fabric-unsupported-conn", "identify", "identity-unestablishable", "inoperable", "malformed-fru", "not-supported", "operable", "peer-comm-problem", "performance-problem", "post-failure", "power-problem", "powered-off", "removed", "thermal-problem", "unknown", "upgrade-problem", "voltage-problem"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Meta":MoMeta("StorageLocalDiskSlotEp", "storageLocalDiskSlotEp", "disk-[Id]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'computeBoard'])
			},

		"ComputeBoard": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Model":MoPropertyMeta("Model", "model", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"OperPower":MoPropertyMeta("OperPower", "operPower", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
			"Perf":MoPropertyMeta("Perf", "perf", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["lower-critical", "lower-non-critical", "lower-non-recoverable", "not-supported", "ok", "unknown", "upper-critical", "upper-non-critical", "upper-non-recoverable"], ["0-4294967295"]),
			"Power":MoPropertyMeta("Power", "power", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["degraded", "error", "not-supported", "off", "offduty", "offline", "on", "online", "power-save", "test", "unknown"], ["0-4294967295"]),
			"Presence":MoPropertyMeta("Presence", "presence", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["empty", "equipped", "equipped-identity-unestablishable", "equipped-not-primary", "equipped-with-malformed-fru", "inaccessible", "mismatch", "mismatch-identity-unestablishable", "missing", "not-supported", "unauthorized", "unknown"], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Serial":MoPropertyMeta("Serial", "serial", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], ["0-4294967295"]),
			"Vendor":MoPropertyMeta("Vendor", "vendor", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("ComputeBoard", "computeBoard", "board", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [u'biosVfResumeOnACPowerLoss', u'computeMbPowerStats', u'computeRackUnitMbTempStats', u'equipmentTpm', u'faultInst', u'memoryArray', u'pidCatalog', u'processorUnit', u'storageController', u'storageFlexFlashController', u'storageLocalDiskSlotEp'], ["Get"], ["admin", "read-only", "user"], [u'computeRackUnit'])
			},

		"HuuFirmwareComponent": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CntrlId":MoPropertyMeta("CntrlId", "cntrlId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Component":MoPropertyMeta("Component", "component", "string", _VersionMeta.version_151f, MoPropertyMeta.NAMING, None, 0, 510, None, [], ["0-4294967295"]),
			"Description":MoPropertyMeta("Description", "description", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"DeviceId":MoPropertyMeta("DeviceId", "deviceId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"Id":MoPropertyMeta("Id", "id", "uint", _VersionMeta.version_154, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"MacAddr":MoPropertyMeta("MacAddr", "macAddr", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"RunningVersion":MoPropertyMeta("RunningVersion", "runningVersion", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Slot":MoPropertyMeta("Slot", "slot", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"SubDeviceId":MoPropertyMeta("SubDeviceId", "subDeviceId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SubVendorId":MoPropertyMeta("SubVendorId", "subVendorId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"VendorId":MoPropertyMeta("VendorId", "vendorId", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Meta":MoMeta("HuuFirmwareComponent", "huuFirmwareComponent", "component-[Component]", _VersionMeta.version_151f, "OutputOnly", 0x0L, [], [], ["Get"], ["admin", "read-only", "user"], [u'huuFirmwareRunning'])
			},

		"IodSnapshotStatus": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_152, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CurrentStatus":MoPropertyMeta("CurrentStatus", "currentStatus", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"CurrentTime":MoPropertyMeta("CurrentTime", "currentTime", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"IodImageVersion":MoPropertyMeta("IodImageVersion", "iodImageVersion", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RemoteShareFile":MoPropertyMeta("RemoteShareFile", "remoteShareFile", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RemoteShareIp":MoPropertyMeta("RemoteShareIp", "remoteShareIp", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"RemoteSharePath":MoPropertyMeta("RemoteSharePath", "remoteSharePath", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 255, None, [], ["0-4294967295"]),
			"RunningTime":MoPropertyMeta("RunningTime", "runningTime", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"SnapshotCancelOp":MoPropertyMeta("SnapshotCancelOp", "snapshotCancelOp", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"SnapshotReport":MoPropertyMeta("SnapshotReport", "snapshotReport", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], ["0-4294967295"]),
			"StartTime":MoPropertyMeta("StartTime", "startTime", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_152, MoPropertyMeta.READ_ONLY, None, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"Meta":MoMeta("IodSnapshotStatus", "iodSnapshotStatus", "snapshotStatus", _VersionMeta.version_152, "OutputOnly", 0x0L, [], [], ["Get"], ["read-only"], [u'iodController'])
			},

		"TopSystem": {
			"Address":MoPropertyMeta("Address", "address", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)""", [], ["0-4294967295"]),
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"CurrentTime":MoPropertyMeta("CurrentTime", "currentTime", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"LocalTime":MoPropertyMeta("LocalTime", "localTime", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Mode":MoPropertyMeta("Mode", "mode", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["cluster", "stand-alone", "unspecified"], ["0-4294967295"]),
			"Name":MoPropertyMeta("Name", "name", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"TimeZone":MoPropertyMeta("TimeZone", "timeZone", "string", _VersionMeta.version_202c, MoPropertyMeta.READ_WRITE, 0x8L, 0, 510, None, ["Africa/Abidjan", "Africa/Accra", "Africa/Addis Ababa", "Africa/Algiers", "Africa/Asmara", "Africa/Bamako", "Africa/Bangui", "Africa/Banjul", "Africa/Bissau", "Africa/Blantyre", "Africa/Brazzaville", "Africa/Bujumbura", "Africa/Cairo", "Africa/Casablanca", "Africa/Ceuta", "Africa/Conakry", "Africa/Dakar", "Africa/Dar es Salaam", "Africa/Djibouti", "Africa/Douala", "Africa/El Aaiun", "Africa/Freetown", "Africa/Gaborone", "Africa/Harare", "Africa/Johannesburg", "Africa/Juba", "Africa/Kampala", "Africa/Khartoum", "Africa/Kigali", "Africa/Kinshasa", "Africa/Lagos", "Africa/Libreville", "Africa/Lome", "Africa/Luanda", "Africa/Lubumbashi", "Africa/Lusaka", "Africa/Malabo", "Africa/Maputo", "Africa/Maseru", "Africa/Mbabane", "Africa/Mogadishu", "Africa/Monrovia", "Africa/Nairobi", "Africa/Ndjamena", "Africa/Niamey", "Africa/Nouakchott", "Africa/Ouagadougou", "Africa/Porto-Novo", "Africa/Sao Tome", "Africa/Tripoli", "Africa/Tunis", "Africa/Windhoek", "America/Adak", "America/Anchorage", "America/Anguilla", "America/Antigua", "America/Araguaina", "America/Argentina/Buenos Aires", "America/Argentina/Catamarca", "America/Argentina/Cordoba", "America/Argentina/Jujuy", "America/Argentina/La Rioja", "America/Argentina/Mendoza", "America/Argentina/Rio Gallegos", "America/Argentina/Salta", "America/Argentina/San Juan", "America/Argentina/San Luis", "America/Argentina/Tucuman", "America/Argentina/Ushuaia", "America/Aruba", "America/Asuncion", "America/Atikokan", "America/Bahia", "America/Bahia Banderas", "America/Barbados", "America/Belem", "America/Belize", "America/Blanc-Sablon", "America/Boa Vista", "America/Bogota", "America/Boise", "America/Cambridge Bay", "America/Campo Grande", "America/Cancun", "America/Caracas", "America/Cayenne", "America/Cayman", "America/Chicago", "America/Chihuahua", "America/Costa Rica", "America/Creston", "America/Cuiaba", "America/Curacao", "America/Danmarkshavn", "America/Dawson", "America/Dawson Creek", "America/Denver", "America/Detroit", "America/Dominica", "America/Edmonton", "America/Eirunepe", "America/El Salvador", "America/Fortaleza", "America/Glace Bay", "America/Godthab", "America/Goose Bay", "America/Grand Turk", "America/Grenada", "America/Guadeloupe", "America/Guatemala", "America/Guayaquil", "America/Guyana", "America/Halifax", "America/Havana", "America/Hermosillo", "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Tell City", "America/Indiana/Vevay", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Inuvik", "America/Iqaluit", "America/Jamaica", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Kralendijk", "America/La Paz", "America/Lima", "America/Los Angeles", "America/Lower Princes", "America/Maceio", "America/Managua", "America/Manaus", "America/Marigot", "America/Martinique", "America/Matamoros", "America/Mazatlan", "America/Menominee", "America/Merida", "America/Metlakatla", "America/Mexico City", "America/Miquelon", "America/Moncton", "America/Monterrey", "America/Montevideo", "America/Montreal", "America/Montserrat", "America/Nassau", "America/New York", "America/Nipigon", "America/Nome", "America/Noronha", "America/North Dakota/Beulah", "America/North Dakota/Center", "America/North Dakota/New Salem", "America/Ojinaga", "America/Panama", "America/Pangnirtung", "America/Paramaribo", "America/Phoenix", "America/Port of Spain", "America/Port-au-Prince", "America/Porto Velho", "America/Puerto Rico", "America/Rainy River", "America/Rankin Inlet", "America/Recife", "America/Regina", "America/Resolute", "America/Rio Branco", "America/Santa Isabel", "America/Santarem", "America/Santiago", "America/Santo Domingo", "America/Sao Paulo", "America/Scoresbysund", "America/Shiprock", "America/Sitka", "America/St Barthelemy", "America/St Johns", "America/St Kitts", "America/St Lucia", "America/St Thomas", "America/St Vincent", "America/Swift Current", "America/Tegucigalpa", "America/Thule", "America/Thunder Bay", "America/Tijuana", "America/Toronto", "America/Tortola", "America/Vancouver", "America/Whitehorse", "America/Winnipeg", "America/Yakutat", "America/Yellowknife", "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Macquarie", "Antarctica/Mawson", "Antarctica/McMurdo", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/South Pole", "Antarctica/Syowa", "Antarctica/Troll", "Antarctica/Vostok", "Arctic/Longyearbyen", "Asia/Aden", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Baghdad", "Asia/Bahrain", "Asia/Baku", "Asia/Bangkok", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei", "Asia/Choibalsan", "Asia/Chongqing", "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe", "Asia/Gaza", "Asia/Harbin", "Asia/Hebron", "Asia/Ho Chi Minh", "Asia/Hong Kong", "Asia/Hovd", "Asia/Irkutsk", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem", "Asia/Kabul", "Asia/Kamchatka", "Asia/Karachi", "Asia/Kashgar", "Asia/Kathmandu", "Asia/Khandyga", "Asia/Kolkata", "Asia/Krasnoyarsk", "Asia/Kuala Lumpur", "Asia/Kuching", "Asia/Kuwait", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novokuznetsk", "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral", "Asia/Phnom Penh", "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qyzylorda", "Asia/Rangoon", "Asia/Riyadh", "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran", "Asia/Thimphu", "Asia/Tokyo", "Asia/Ulaanbaatar", "Asia/Urumqi", "Asia/Ust-Nera", "Asia/Vientiane", "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yekaterinburg", "Asia/Yerevan", "Atlantic/Azores", "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape Verde", "Atlantic/Faroe", "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South Georgia", "Atlantic/St Helena", "Atlantic/Stanley", "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken Hill", "Australia/Currie", "Australia/Darwin", "Australia/Eucla", "Australia/Hobart", "Australia/Lindeman", "Australia/Lord Howe", "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "Europe/Amsterdam", "Europe/Andorra", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest", "Europe/Busingen", "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar", "Europe/Guernsey", "Europe/Helsinki", "Europe/Isle of Man", "Europe/Istanbul", "Europe/Jersey", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Lisbon", "Europe/Ljubljana", "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Mariehamn", "Europe/Minsk", "Europe/Monaco", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Podgorica", "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Samara", "Europe/San Marino", "Europe/Sarajevo", "Europe/Simferopol", "Europe/Skopje", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Tirane", "Europe/Uzhgorod", "Europe/Vaduz", "Europe/Vatican", "Europe/Vienna", "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zagreb", "Europe/Zaporozhye", "Europe/Zurich", "Indian/Antananarivo", "Indian/Chagos", "Indian/Christmas", "Indian/Cocos", "Indian/Comoro", "Indian/Kerguelen", "Indian/Mahe", "Indian/Maldives", "Indian/Mauritius", "Indian/Mayotte", "Indian/Reunion", "Pacific/Apia", "Pacific/Auckland", "Pacific/Chatham", "Pacific/Chuuk", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal", "Pacific/Guam", "Pacific/Honolulu", "Pacific/Johnston", "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein", "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Midway", "Pacific/Nauru", "Pacific/Niue", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pago Pago", "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Pohnpei", "Pacific/Port Moresby", "Pacific/Rarotonga", "Pacific/Saipan", "Pacific/Tahiti", "Pacific/Tarawa", "Pacific/Tongatapu", "Pacific/Wake", "Pacific/Wallis", "UTC"], ["0-4294967295"]),
			"Meta":MoMeta("TopSystem", "topSystem", "sys", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [u'aaaLdap', u'aaaUserEp', u'commSvcEp', u'computeRackUnit', u'huuController', u'iodController', u'mgmtBackup', u'mgmtImporter'], ["Get", "Set"], ["admin", "read-only", "user"], [u'topRoot'])
			},

		"BiosVfBootOptionRetry": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpBootOptionRetry":MoPropertyMeta("VpBootOptionRetry", "vpBootOptionRetry", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfBootOptionRetry", "biosVfBootOptionRetry", "Boot-option-retry", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfDramRefreshRate": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpDramRefreshRate":MoPropertyMeta("VpDramRefreshRate", "vpDramRefreshRate", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["1x", "2x", "3x", "4x", "Auto", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfDramRefreshRate", "biosVfDramRefreshRate", "dram-refresh-rate", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfHardwarePrefetch": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpHardwarePrefetch":MoPropertyMeta("VpHardwarePrefetch", "vpHardwarePrefetch", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfHardwarePrefetch", "biosVfHardwarePrefetch", "Hardware-Prefetch", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin"], [u'biosPlatformDefaults', u'biosSettings'])
			},

		"BiosVfSerialPortAEnable": {
			"ChildAction":MoPropertyMeta("ChildAction", "childAction", "string", _VersionMeta.version_151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], ["0-4294967295"]),
			"Dn":MoPropertyMeta("Dn", "dn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x1L, 0, 255, None, [], ["0-4294967295"]),
			"Rn":MoPropertyMeta("Rn", "rn", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x2L, 0, 255, None, [], ["0-4294967295"]),
			"Status":MoPropertyMeta("Status", "status", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, ["", "created", "deleted", "modified", "removed"], ["0-4294967295"]),
			"VpSerialPortAEnable":MoPropertyMeta("VpSerialPortAEnable", "vpSerialPortAEnable", "string", _VersionMeta.version_151f, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], ["0-4294967295"]),
			"Meta":MoMeta("BiosVfSerialPortAEnable", "biosVfSerialPortAEnable", "Serial-port-A-enable", _VersionMeta.version_151f, "InputOutput", 0xfL, [], [], ["Get", "Set"], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'])
			},

	}

