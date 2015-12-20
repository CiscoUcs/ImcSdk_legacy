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
"""
This is an auto-generated module.
It contains independent classes for all Managed Objects and its respective attributes.
"""

from ImcCore import ManagedObject

class LsbootVirtualMedia(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootVirtualMedia")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootVirtualMedia"

    ACCESS = "Access"
    DN = "Dn"
    ORDER = "Order"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"

    CONST_ACCESS_READ_ONLY = "read-only"
    CONST_ACCESS_READ_WRITE = "read-write"
    CONST_TYPE_VIRTUAL_MEDIA = "virtual-media"

class ProcessorEnvStats(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "ProcessorEnvStats")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "processorEnvStats"

    DESCRIPTION = "Description"
    DN = "Dn"
    ID = "Id"
    RN = "Rn"
    STATUS = "Status"
    TEMPERATURE = "Temperature"
    TIME_COLLECTED = "TimeCollected"


class BiosVfIOHResource(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfIOHResource")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfIOHResource"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_IOHRESOURCE = "VpIOHResource"

    CONST_VP_IOHRESOURCE_IOH0__24K_IOH1__40K = "IOH0 24k IOH1 40k"
    CONST_VP_IOHRESOURCE_IOH0__32K_IOH1__32K = "IOH0 32k IOH1 32k"
    CONST_VP_IOHRESOURCE_IOH0__40K_IOH1__24K = "IOH0 40k IOH1 24k"
    CONST_VP_IOHRESOURCE_IOH0__48K_IOH1__16K = "IOH0 48k IOH1 16k"
    CONST_VP_IOHRESOURCE_IOH0__56K_IOH1__8K = "IOH0 56k IOH1 8k"
    CONST_VP_IOHRESOURCE_PLATFORM_DEFAULT = "platform-default"

class AdaptorFcInterruptProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcInterruptProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcInterruptProfile"

    DN = "Dn"
    MODE = "Mode"
    RN = "Rn"
    STATUS = "Status"

    CONST_MODE_INTX = "INTx"
    CONST_MODE_MSI = "MSI"
    CONST_MODE_MSIX = "MSIx"

class BiosVfSataModeSelect(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfSataModeSelect")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfSataModeSelect"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_SATA_MODE_SELECT = "VpSataModeSelect"

    CONST_VP_SATA_MODE_SELECT_AHCI = "AHCI"
    CONST_VP_SATA_MODE_SELECT_DISABLED = "Disabled"
    CONST_VP_SATA_MODE_SELECT_LSI_SW_RAID = "LSI SW RAID"
    CONST_VP_SATA_MODE_SELECT_PLATFORM_DEFAULT = "platform-default"

class HuuFirmwareUpdateStatus(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuFirmwareUpdateStatus")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuFirmwareUpdateStatus"

    CURRENT_TIME = "CurrentTime"
    DN = "Dn"
    HUU_IMAGE_VERSION = "HuuImageVersion"
    OVERALL_STATUS = "OverallStatus"
    RN = "Rn"
    STATUS = "Status"
    UPDATE_END_TIME = "UpdateEndTime"
    UPDATE_START_TIME = "UpdateStartTime"


class IpBlocking(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "IpBlocking")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "ipBlocking"

    DESCRIPTION = "Description"
    DN = "Dn"
    ENABLE = "Enable"
    FAIL_COUNT = "FailCount"
    FAIL_WINDOW = "FailWindow"
    PENALTY_TIME = "PenaltyTime"
    RN = "Rn"
    STATUS = "Status"


class AdaptorFcPortProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcPortProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcPortProfile"

    DN = "Dn"
    IO_THROTTLE_COUNT = "IoThrottleCount"
    LUNS_PER_TARGET = "LunsPerTarget"
    RN = "Rn"
    STATUS = "Status"


class BiosVfOnboardNIC(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfOnboardNIC")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfOnboardNIC"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ONBOARD10_GBIT_LOM = "VpOnboard10GbitLOM"
    VP_ONBOARD_GBIT_LOM = "VpOnboardGbitLOM"

    CONST_VP_ONBOARD10_GBIT_LOM_DISABLED = "Disabled"
    CONST_VP_ONBOARD10_GBIT_LOM_ENABLED = "Enabled"
    CONST__VP_ONBOARD10_GBIT_LOM_DISABLED = "disabled"
    CONST__VP_ONBOARD10_GBIT_LOM_ENABLED = "enabled"
    CONST_VP_ONBOARD10_GBIT_LOM_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_ONBOARD_GBIT_LOM_DISABLED = "Disabled"
    CONST_VP_ONBOARD_GBIT_LOM_ENABLED = "Enabled"
    CONST__VP_ONBOARD_GBIT_LOM_DISABLED = "disabled"
    CONST__VP_ONBOARD_GBIT_LOM_ENABLED = "enabled"
    CONST_VP_ONBOARD_GBIT_LOM_PLATFORM_DEFAULT = "platform-default"

class LsbootSan(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootSan")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootSan"

    DN = "Dn"
    LUN = "Lun"
    NAME = "Name"
    ORDER = "Order"
    RN = "Rn"
    SLOT = "Slot"
    STATE = "State"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_SUBTYPE_SAN = "SAN"
    CONST_TYPE_SAN = "SAN"

class AdaptorFcPortPLogiProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcPortPLogiProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcPortPLogiProfile"

    DN = "Dn"
    RETRIES = "Retries"
    RN = "Rn"
    STATUS = "Status"
    TIMEOUT = "Timeout"


class BiosVfQPIConfig(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfQPIConfig")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfQPIConfig"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_QPILINK_FREQUENCY = "VpQPILinkFrequency"

    CONST_VP_QPILINK_FREQUENCY_6_4_GT_S = "6.4-gt/s"
    CONST_VP_QPILINK_FREQUENCY_7_2_GT_S = "7.2-gt/s"
    CONST_VP_QPILINK_FREQUENCY_8_0_GT_S = "8.0-gt/s"
    CONST_VP_QPILINK_FREQUENCY_AUTO = "auto"
    CONST_VP_QPILINK_FREQUENCY_PLATFORM_DEFAULT = "platform-default"

class BiosVfOutOfBandMgmtPort(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfOutOfBandMgmtPort")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfOutOfBandMgmtPort"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_OUT_OF_BAND_MGMT_PORT = "VpOutOfBandMgmtPort"

    CONST_VP_OUT_OF_BAND_MGMT_PORT_DISABLED = "Disabled"
    CONST_VP_OUT_OF_BAND_MGMT_PORT_ENABLED = "Enabled"
    CONST__VP_OUT_OF_BAND_MGMT_PORT_DISABLED = "disabled"
    CONST__VP_OUT_OF_BAND_MGMT_PORT_ENABLED = "enabled"
    CONST_VP_OUT_OF_BAND_MGMT_PORT_PLATFORM_DEFAULT = "platform-default"

class MemoryArray(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "MemoryArray")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "memoryArray"

    CURR_CAPACITY = "CurrCapacity"
    DIMM_BLACK_LIST = "DimmBlackList"
    DN = "Dn"
    FAILED_MEMORY = "FailedMemory"
    ID = "Id"
    IGNORED_MEMORY = "IgnoredMemory"
    MAX_DEVICES = "MaxDevices"
    MEMORY_CONFIGURATION = "MemoryConfiguration"
    MEMORY_RASPOSSIBLE = "MemoryRASPossible"
    NUM_OF_FAILED_DIMMS = "NumOfFailedDimms"
    NUM_OF_IGNORED_DIMMS = "NumOfIgnoredDimms"
    OVERALL_DIMMSTATUS = "OverallDIMMStatus"
    POPULATED = "Populated"
    PRESENCE = "Presence"
    REDUNDANT_MEMORY = "RedundantMemory"
    RN = "Rn"
    STATUS = "Status"

    CONST_CURR_CAPACITY_UNSPECIFIED = "unspecified"
    CONST_DIMM_BLACK_LIST_DISABLE = "disable"
    CONST_DIMM_BLACK_LIST_DISABLED = "disabled"
    CONST_DIMM_BLACK_LIST_ENABLE = "enable"
    CONST_DIMM_BLACK_LIST_ENABLED = "enabled"
    CONST_FAILED_MEMORY_UNSPECIFIED = "unspecified"
    CONST_IGNORED_MEMORY_UNSPECIFIED = "unspecified"
    CONST_MAX_DEVICES_UNSPECIFIED = "unspecified"
    CONST_OVERALL_DIMMSTATUS_AMBER = "amber"
    CONST_OVERALL_DIMMSTATUS_BLUE = "blue"
    CONST_OVERALL_DIMMSTATUS_GREEN = "green"
    CONST_OVERALL_DIMMSTATUS_RED = "red"
    CONST_OVERALL_DIMMSTATUS_UNKNOWN = "unknown"
    CONST_POPULATED_UNSPECIFIED = "unspecified"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"
    CONST_REDUNDANT_MEMORY_UNSPECIFIED = "unspecified"

class AdaptorFcPersistentBindings(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcPersistentBindings")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcPersistentBindings"

    BUS_ID = "BusId"
    DN = "Dn"
    HOST_WWPN = "HostWwpn"
    INDEX = "Index"
    RN = "Rn"
    STATUS = "Status"
    TARGET_ID = "TargetId"
    TARGET_WWPN = "TargetWwpn"


class EquipmentFanModule(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentFanModule")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentFanModule"

    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    OPERABILITY = "Operability"
    POWER = "Power"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    THERMAL = "Thermal"
    TRAY = "Tray"
    VENDOR = "Vendor"
    VOLTAGE = "Voltage"

    CONST_OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPERABILITY_CONFIG = "config"
    CONST_OPERABILITY_DECOMISSIONING = "decomissioning"
    CONST_OPERABILITY_DEGRADED = "degraded"
    CONST_OPERABILITY_DISABLED = "disabled"
    CONST_OPERABILITY_DISCOVERY = "discovery"
    CONST_OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPERABILITY_IDENTIFY = "identify"
    CONST_OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPERABILITY_INOPERABLE = "inoperable"
    CONST_OPERABILITY_MALFORMED_FRU = "malformed-fru"
    CONST_OPERABILITY_NOT_SUPPORTED = "not-supported"
    CONST_OPERABILITY_OPERABLE = "operable"
    CONST_OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPERABILITY_POST_FAILURE = "post-failure"
    CONST_OPERABILITY_POWER_PROBLEM = "power-problem"
    CONST_OPERABILITY_POWERED_OFF = "powered-off"
    CONST_OPERABILITY_REMOVED = "removed"
    CONST_OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPERABILITY_UNKNOWN = "unknown"
    CONST_OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_POWER_DEGRADED = "degraded"
    CONST_POWER_ERROR = "error"
    CONST_POWER_NOT_SUPPORTED = "not-supported"
    CONST_POWER_OFF = "off"
    CONST_POWER_OFFDUTY = "offduty"
    CONST_POWER_OFFLINE = "offline"
    CONST_POWER_ON = "on"
    CONST_POWER_ONLINE = "online"
    CONST_POWER_POWER_SAVE = "power-save"
    CONST_POWER_TEST = "test"
    CONST_POWER_UNKNOWN = "unknown"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"
    CONST_THERMAL_LOWER_CRITICAL = "lower-critical"
    CONST_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_THERMAL_NOT_SUPPORTED = "not-supported"
    CONST_THERMAL_OK = "ok"
    CONST_THERMAL_UNKNOWN = "unknown"
    CONST_THERMAL_UPPER_CRITICAL = "upper-critical"
    CONST_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    CONST_VOLTAGE_LOWER_CRITICAL = "lower-critical"
    CONST_VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_VOLTAGE_NOT_SUPPORTED = "not-supported"
    CONST_VOLTAGE_OK = "ok"
    CONST_VOLTAGE_UNKNOWN = "unknown"
    CONST_VOLTAGE_UPPER_CRITICAL = "upper-critical"
    CONST_VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"

class AdaptorEthWorkQueueProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthWorkQueueProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthWorkQueueProfile"

    COUNT = "Count"
    DN = "Dn"
    RING_SIZE = "RingSize"
    RN = "Rn"
    STATUS = "Status"


class PidCatalog(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PidCatalog")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "pidCatalog"

    DN = "Dn"
    NAME = "Name"
    RN = "Rn"
    STATUS = "Status"


class ComputeRackUnit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "ComputeRackUnit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "computeRackUnit"

    ADMIN_POWER = "AdminPower"
    AVAILABLE_MEMORY = "AvailableMemory"
    CHASSIS_SERIAL = "ChassisSerial"
    DN = "Dn"
    MEMORY_SPEED = "MemorySpeed"
    MODEL = "Model"
    NAME = "Name"
    NUM_OF_ADAPTORS = "NumOfAdaptors"
    NUM_OF_CORES = "NumOfCores"
    NUM_OF_CORES_ENABLED = "NumOfCoresEnabled"
    NUM_OF_CPUS = "NumOfCpus"
    NUM_OF_ETH_HOST_IFS = "NumOfEthHostIfs"
    NUM_OF_FC_HOST_IFS = "NumOfFcHostIfs"
    NUM_OF_THREADS = "NumOfThreads"
    OPER_POWER = "OperPower"
    ORIGINAL_UUID = "OriginalUuid"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    SERVER_ID = "ServerId"
    STATUS = "Status"
    TOTAL_MEMORY = "TotalMemory"
    USR_LBL = "UsrLbl"
    UUID = "Uuid"
    VENDOR = "Vendor"

    CONST_ADMIN_POWER_BMC_RESET_DEFAULT = "bmc-reset-default"
    CONST_ADMIN_POWER_BMC_RESET_IMMEDIATE = "bmc-reset-immediate"
    CONST_ADMIN_POWER_CMOS_RESET_IMMEDIATE = "cmos-reset-immediate"
    CONST_ADMIN_POWER_CYCLE_IMMEDIATE = "cycle-immediate"
    CONST_ADMIN_POWER_DIAGNOSTIC_INTERRUPT = "diagnostic-interrupt"
    CONST_ADMIN_POWER_DOWN = "down"
    CONST_ADMIN_POWER_HARD_RESET_IMMEDIATE = "hard-reset-immediate"
    CONST_ADMIN_POWER_POLICY = "policy"
    CONST_ADMIN_POWER_SOFT_SHUT_DOWN = "soft-shut-down"
    CONST_ADMIN_POWER_UP = "up"
    CONST_MEMORY_SPEED_ = ""
    CONST_MEMORY_SPEED_UNSPECIFIED = "unspecified"
    CONST_OPER_POWER_DEGRADED = "degraded"
    CONST_OPER_POWER_ERROR = "error"
    CONST_OPER_POWER_NOT_SUPPORTED = "not-supported"
    CONST_OPER_POWER_OFF = "off"
    CONST_OPER_POWER_OFFDUTY = "offduty"
    CONST_OPER_POWER_OFFLINE = "offline"
    CONST_OPER_POWER_ON = "on"
    CONST_OPER_POWER_ONLINE = "online"
    CONST_OPER_POWER_POWER_SAVE = "power-save"
    CONST_OPER_POWER_TEST = "test"
    CONST_OPER_POWER_UNKNOWN = "unknown"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"

class CommSyslog(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommSyslog")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commSyslog"

    ADMIN_STATE = "AdminState"
    DESCR = "Descr"
    DN = "Dn"
    LOCAL_SEVERITY = "LocalSeverity"
    NAME = "Name"
    PORT = "Port"
    PROTO = "Proto"
    REMOTE_SEVERITY = "RemoteSeverity"
    RN = "Rn"
    STATUS = "Status"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_LOCAL_SEVERITY_ALERT = "alert"
    CONST_LOCAL_SEVERITY_CRITICAL = "critical"
    CONST_LOCAL_SEVERITY_DEBUG = "debug"
    CONST_LOCAL_SEVERITY_EMERGENCY = "emergency"
    CONST_LOCAL_SEVERITY_ERROR = "error"
    CONST_LOCAL_SEVERITY_INFORMATIONAL = "informational"
    CONST_LOCAL_SEVERITY_NOTICE = "notice"
    CONST_LOCAL_SEVERITY_WARNING = "warning"
    CONST_PROTO_ALL = "all"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_TCP = "tcp"
    CONST_PROTO_UDP = "udp"
    CONST_REMOTE_SEVERITY_ALERT = "alert"
    CONST_REMOTE_SEVERITY_CRITICAL = "critical"
    CONST_REMOTE_SEVERITY_DEBUG = "debug"
    CONST_REMOTE_SEVERITY_EMERGENCY = "emergency"
    CONST_REMOTE_SEVERITY_ERROR = "error"
    CONST_REMOTE_SEVERITY_INFORMATIONAL = "informational"
    CONST_REMOTE_SEVERITY_NOTICE = "notice"
    CONST_REMOTE_SEVERITY_WARNING = "warning"

class BiosVfCPUPowerManagement(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCPUPowerManagement")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCPUPowerManagement"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CPUPOWER_MANAGEMENT = "VpCPUPowerManagement"

    CONST_VP_CPUPOWER_MANAGEMENT_CUSTOM = "custom"
    CONST_VP_CPUPOWER_MANAGEMENT_DISABLED = "disabled"
    CONST_VP_CPUPOWER_MANAGEMENT_ENERGY_EFFICIENT = "energy-efficient"
    CONST_VP_CPUPOWER_MANAGEMENT_PERFORMANCE = "performance"
    CONST_VP_CPUPOWER_MANAGEMENT_PLATFORM_DEFAULT = "platform-default"

class PidCatalogCpu(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PidCatalogCpu")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "pidCatalogCpu"

    CURRENTSPEED = "Currentspeed"
    DESCRIPTION = "Description"
    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    OPER_STATE = "OperState"
    PID = "Pid"
    RN = "Rn"
    SIGNATURE = "Signature"
    SOCKETDESIGNATION = "Socketdesignation"
    STATUS = "Status"


class StorageOperation(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageOperation")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageOperation"

    CURRENT_LROP = "CurrentLrop"
    DN = "Dn"
    ELAPSED_SECONDS = "ElapsedSeconds"
    LROP_IN_PROGRESS = "LropInProgress"
    PROGRESS_PERCENT = "ProgressPercent"
    RN = "Rn"
    STATUS = "Status"


class AdaptorIpV4RssHashProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorIpV4RssHashProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorIpV4RssHashProfile"

    DN = "Dn"
    IP_HASH = "IpHash"
    RN = "Rn"
    STATUS = "Status"
    TCP_HASH = "TcpHash"


class BiosVfProcessorCState(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfProcessorCState")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfProcessorCState"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PROCESSOR_CSTATE = "VpProcessorCState"

    CONST_VP_PROCESSOR_CSTATE_DISABLED = "Disabled"
    CONST_VP_PROCESSOR_CSTATE_ENABLED = "Enabled"
    CONST__VP_PROCESSOR_CSTATE_DISABLED = "disabled"
    CONST__VP_PROCESSOR_CSTATE_ENABLED = "enabled"
    CONST_VP_PROCESSOR_CSTATE_PLATFORM_DEFAULT = "platform-default"

class BiosVfUSBEmulation(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfUSBEmulation")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfUSBEmulation"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_USBEMUL6064 = "VpUSBEmul6064"

    CONST_VP_USBEMUL6064_DISABLED = "Disabled"
    CONST_VP_USBEMUL6064_ENABLED = "Enabled"
    CONST__VP_USBEMUL6064_DISABLED = "disabled"
    CONST__VP_USBEMUL6064_ENABLED = "enabled"
    CONST_VP_USBEMUL6064_PLATFORM_DEFAULT = "platform-default"

class EquipmentPsuFan(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentPsuFan")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentPsuFan"

    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    MODULE = "Module"
    OPERABILITY = "Operability"
    POWER = "Power"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    THERMAL = "Thermal"
    TRAY = "Tray"
    VENDOR = "Vendor"
    VOLTAGE = "Voltage"

    CONST_OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPERABILITY_CONFIG = "config"
    CONST_OPERABILITY_DECOMISSIONING = "decomissioning"
    CONST_OPERABILITY_DEGRADED = "degraded"
    CONST_OPERABILITY_DISABLED = "disabled"
    CONST_OPERABILITY_DISCOVERY = "discovery"
    CONST_OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPERABILITY_IDENTIFY = "identify"
    CONST_OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPERABILITY_INOPERABLE = "inoperable"
    CONST_OPERABILITY_MALFORMED_FRU = "malformed-fru"
    CONST_OPERABILITY_NOT_SUPPORTED = "not-supported"
    CONST_OPERABILITY_OPERABLE = "operable"
    CONST_OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPERABILITY_POST_FAILURE = "post-failure"
    CONST_OPERABILITY_POWER_PROBLEM = "power-problem"
    CONST_OPERABILITY_POWERED_OFF = "powered-off"
    CONST_OPERABILITY_REMOVED = "removed"
    CONST_OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPERABILITY_UNKNOWN = "unknown"
    CONST_OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_POWER_DEGRADED = "degraded"
    CONST_POWER_ERROR = "error"
    CONST_POWER_NOT_SUPPORTED = "not-supported"
    CONST_POWER_OFF = "off"
    CONST_POWER_OFFDUTY = "offduty"
    CONST_POWER_OFFLINE = "offline"
    CONST_POWER_ON = "on"
    CONST_POWER_ONLINE = "online"
    CONST_POWER_POWER_SAVE = "power-save"
    CONST_POWER_TEST = "test"
    CONST_POWER_UNKNOWN = "unknown"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"
    CONST_THERMAL_LOWER_CRITICAL = "lower-critical"
    CONST_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_THERMAL_NOT_SUPPORTED = "not-supported"
    CONST_THERMAL_OK = "ok"
    CONST_THERMAL_UNKNOWN = "unknown"
    CONST_THERMAL_UPPER_CRITICAL = "upper-critical"
    CONST_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    CONST_VOLTAGE_LOWER_CRITICAL = "lower-critical"
    CONST_VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_VOLTAGE_NOT_SUPPORTED = "not-supported"
    CONST_VOLTAGE_OK = "ok"
    CONST_VOLTAGE_UNKNOWN = "unknown"
    CONST_VOLTAGE_UPPER_CRITICAL = "upper-critical"
    CONST_VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"

class SolIf(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "SolIf")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "solIf"

    ADMIN_STATE = "AdminState"
    COMPORT = "Comport"
    DN = "Dn"
    NAME = "Name"
    RN = "Rn"
    SPEED = "Speed"
    STATUS = "Status"

    CONST_ADMIN_STATE_DISABLE = "disable"
    CONST_ADMIN_STATE_ENABLE = "enable"
    CONST_COMPORT_COM0 = "com0"
    CONST_COMPORT_COM1 = "com1"
    CONST_SPEED_115200 = "115200"
    CONST_SPEED_19200 = "19200"
    CONST_SPEED_38400 = "38400"
    CONST_SPEED_57600 = "57600"
    CONST_SPEED_9600 = "9600"

class BiosVfIntelVTForDirectedIO(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfIntelVTForDirectedIO")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfIntelVTForDirectedIO"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_INTEL_VTDATSSUPPORT = "VpIntelVTDATSSupport"
    VP_INTEL_VTDCOHERENCY_SUPPORT = "VpIntelVTDCoherencySupport"
    VP_INTEL_VTDINTERRUPT_REMAPPING = "VpIntelVTDInterruptRemapping"
    VP_INTEL_VTDPASS_THROUGH_DMASUPPORT = "VpIntelVTDPassThroughDMASupport"
    VP_INTEL_VTFOR_DIRECTED_IO = "VpIntelVTForDirectedIO"

    CONST_VP_INTEL_VTDATSSUPPORT_DISABLED = "Disabled"
    CONST_VP_INTEL_VTDATSSUPPORT_ENABLED = "Enabled"
    CONST__VP_INTEL_VTDATSSUPPORT_DISABLED = "disabled"
    CONST__VP_INTEL_VTDATSSUPPORT_ENABLED = "enabled"
    CONST_VP_INTEL_VTDATSSUPPORT_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_INTEL_VTDCOHERENCY_SUPPORT_DISABLED = "Disabled"
    CONST_VP_INTEL_VTDCOHERENCY_SUPPORT_ENABLED = "Enabled"
    CONST__VP_INTEL_VTDCOHERENCY_SUPPORT_DISABLED = "disabled"
    CONST__VP_INTEL_VTDCOHERENCY_SUPPORT_ENABLED = "enabled"
    CONST_VP_INTEL_VTDCOHERENCY_SUPPORT_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_INTEL_VTDINTERRUPT_REMAPPING_DISABLED = "Disabled"
    CONST_VP_INTEL_VTDINTERRUPT_REMAPPING_ENABLED = "Enabled"
    CONST__VP_INTEL_VTDINTERRUPT_REMAPPING_DISABLED = "disabled"
    CONST__VP_INTEL_VTDINTERRUPT_REMAPPING_ENABLED = "enabled"
    CONST_VP_INTEL_VTDINTERRUPT_REMAPPING_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_DISABLED = "Disabled"
    CONST_VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_ENABLED = "Enabled"
    CONST__VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_DISABLED = "disabled"
    CONST__VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_ENABLED = "enabled"
    CONST_VP_INTEL_VTDPASS_THROUGH_DMASUPPORT_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_INTEL_VTFOR_DIRECTED_IO_DISABLED = "Disabled"
    CONST_VP_INTEL_VTFOR_DIRECTED_IO_ENABLED = "Enabled"
    CONST__VP_INTEL_VTFOR_DIRECTED_IO_DISABLED = "disabled"
    CONST__VP_INTEL_VTFOR_DIRECTED_IO_ENABLED = "enabled"
    CONST_VP_INTEL_VTFOR_DIRECTED_IO_PLATFORM_DEFAULT = "platform-default"

class BiosVfPchUsb30Mode(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPchUsb30Mode")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPchUsb30Mode"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PCH_USB30_MODE = "VpPchUsb30Mode"

    CONST_VP_PCH_USB30_MODE_DISABLED = "Disabled"
    CONST_VP_PCH_USB30_MODE_ENABLED = "Enabled"
    CONST__VP_PCH_USB30_MODE_DISABLED = "disabled"
    CONST__VP_PCH_USB30_MODE_ENABLED = "enabled"
    CONST_VP_PCH_USB30_MODE_PLATFORM_DEFAULT = "platform-default"

class AdaptorConnectorInfo(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorConnectorInfo")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorConnectorInfo"

    DN = "Dn"
    PART_NUMBER = "PartNumber"
    PART_REVISION = "PartRevision"
    PRESENT = "Present"
    RN = "Rn"
    STATUS = "Status"
    SUPPORTED = "Supported"
    TYPE = "Type"
    VENDOR = "Vendor"


class FirmwareBootUnit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "FirmwareBootUnit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "firmwareBootUnit"

    ADMIN_STATE = "AdminState"
    DESCRIPTION = "Description"
    DN = "Dn"
    IGNORE_COMP_CHECK = "IgnoreCompCheck"
    IMAGE = "Image"
    OPER_STATE = "OperState"
    RESET_ON_ACTIVATE = "ResetOnActivate"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"
    VERSION = "Version"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_IGNORE_COMP_CHECK_FALSE = "false"
    CONST_IGNORE_COMP_CHECK_NO = "no"
    CONST_IGNORE_COMP_CHECK_TRUE = "true"
    CONST_IGNORE_COMP_CHECK_YES = "yes"
    CONST_IMAGE_BACKUP = "backup"
    CONST_IMAGE_RUNNING = "running"
    CONST_OPER_STATE_ACTIVATING = "activating"
    CONST_OPER_STATE_BAD_IMAGE = "bad-image"
    CONST_OPER_STATE_FAILED = "failed"
    CONST_OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    CONST_OPER_STATE_READY = "ready"
    CONST_OPER_STATE_REBOOTING = "rebooting"
    CONST_OPER_STATE_SCHEDULED = "scheduled"
    CONST_OPER_STATE_SET_STARTUP = "set-startup"
    CONST_OPER_STATE_THROTTLED = "throttled"
    CONST_OPER_STATE_UPDATING = "updating"
    CONST_RESET_ON_ACTIVATE_FALSE = "false"
    CONST_RESET_ON_ACTIVATE_NO = "no"
    CONST_RESET_ON_ACTIVATE_TRUE = "true"
    CONST_RESET_ON_ACTIVATE_YES = "yes"

class FirmwareBootDefinition(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "FirmwareBootDefinition")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "firmwareBootDefinition"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"

    CONST_TYPE_ADAPTOR = "adaptor"
    CONST_TYPE_BLADE_BIOS = "blade-bios"
    CONST_TYPE_BLADE_CONTROLLER = "blade-controller"
    CONST_TYPE_FEX = "fex"
    CONST_TYPE_SIOC = "sioc"
    CONST_TYPE_STORAGE_CONTROLLER = "storage-controller"
    CONST_TYPE_SYSTEM = "system"

class StandardPowerProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StandardPowerProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "standardPowerProfile"

    ALLOW_THROTTLE = "AllowThrottle"
    CORR_ACTION = "CorrAction"
    CORR_TIME = "CorrTime"
    DN = "Dn"
    HARD_CAP = "HardCap"
    POWER_LIMIT = "PowerLimit"
    PROFILE_ENABLED = "ProfileEnabled"
    PROFILE_TYPE = "ProfileType"
    RN = "Rn"
    STATUS = "Status"
    SUSPEND_PERIOD = "SuspendPeriod"

    CONST_CORR_ACTION_ALERT = "alert"
    CONST_CORR_ACTION_ALERT_SHUTDOWN = "alert,shutdown"
    CONST_CORR_ACTION_NONE = "none"
    CONST_CORR_ACTION_SHUTDOWN = "shutdown"

class AdaptorUnit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorUnit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorUnit"

    ADMIN_STATE = "AdminState"
    CIMC_MANAGEMENT_ENABLED = "CimcManagementEnabled"
    DESCRIPTION = "Description"
    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    PCI_ADDR = "PciAddr"
    PCI_SLOT = "PciSlot"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    VENDOR = "Vendor"

    CONST_ADMIN_STATE_ADAPTOR_RESET = "adaptor-reset"
    CONST_ADMIN_STATE_ADAPTOR_RESET_DEFAULT = "adaptor-reset-default"
    CONST_ADMIN_STATE_POLICY = "policy"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNKNOWN = "unknown"

class SysdebugMEpLog(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "SysdebugMEpLog")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "sysdebugMEpLog"

    ADMIN_STATE = "AdminState"
    CAPACITY = "Capacity"
    DN = "Dn"
    ID = "Id"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"

    CONST_ADMIN_STATE_BACKUP = "backup"
    CONST_ADMIN_STATE_CLEAR = "clear"
    CONST_ADMIN_STATE_POLICY = "policy"
    CONST_CAPACITY_AVAILABLE = "available"
    CONST_CAPACITY_FULL = "full"
    CONST_CAPACITY_LOW = "low"
    CONST_CAPACITY_UNKNOWN = "unknown"
    CONST_CAPACITY_VERY_LOW = "very-low"
    CONST_TYPE_OBFL = "OBFL"
    CONST_TYPE_SEL = "SEL"
    CONST_TYPE_SYSLOG = "Syslog"

class BiosVfPOSTErrorPause(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPOSTErrorPause")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPOSTErrorPause"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_POSTERROR_PAUSE = "VpPOSTErrorPause"

    CONST_VP_POSTERROR_PAUSE_DISABLED = "Disabled"
    CONST_VP_POSTERROR_PAUSE_ENABLED = "Enabled"
    CONST__VP_POSTERROR_PAUSE_DISABLED = "disabled"
    CONST__VP_POSTERROR_PAUSE_ENABLED = "enabled"
    CONST_VP_POSTERROR_PAUSE_PLATFORM_DEFAULT = "platform-default"

class LsbootSd(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootSd")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootSd"

    DN = "Dn"
    NAME = "Name"
    ORDER = "Order"
    RN = "Rn"
    STATE = "State"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_SUBTYPE_SDCARD = "SDCARD"
    CONST_TYPE_SDCARD = "SDCARD"

class CommNtpProvider(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommNtpProvider")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commNtpProvider"

    DESCRIPTION = "Description"
    DN = "Dn"
    NTP_ENABLE = "NtpEnable"
    NTP_SERVER1 = "NtpServer1"
    NTP_SERVER2 = "NtpServer2"
    NTP_SERVER3 = "NtpServer3"
    NTP_SERVER4 = "NtpServer4"
    RN = "Rn"
    STATUS = "Status"


class BiosVfLOMPortOptionROM(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfLOMPortOptionROM")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfLOMPortOptionROM"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_LOMPORT0_STATE = "VpLOMPort0State"
    VP_LOMPORT1_STATE = "VpLOMPort1State"
    VP_LOMPORT2_STATE = "VpLOMPort2State"
    VP_LOMPORT3_STATE = "VpLOMPort3State"
    VP_LOMPORTS_ALL_STATE = "VpLOMPortsAllState"

    CONST_VP_LOMPORT0_STATE_DISABLED = "Disabled"
    CONST_VP_LOMPORT0_STATE_ENABLED = "Enabled"
    CONST_VP_LOMPORT0_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_LOMPORT0_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_LOMPORT0_STATE_DISABLED = "disabled"
    CONST__VP_LOMPORT0_STATE_ENABLED = "enabled"
    CONST_VP_LOMPORT0_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_LOMPORT1_STATE_DISABLED = "Disabled"
    CONST_VP_LOMPORT1_STATE_ENABLED = "Enabled"
    CONST_VP_LOMPORT1_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_LOMPORT1_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_LOMPORT1_STATE_DISABLED = "disabled"
    CONST__VP_LOMPORT1_STATE_ENABLED = "enabled"
    CONST_VP_LOMPORT1_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_LOMPORT2_STATE_DISABLED = "Disabled"
    CONST_VP_LOMPORT2_STATE_ENABLED = "Enabled"
    CONST_VP_LOMPORT2_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_LOMPORT2_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_LOMPORT2_STATE_DISABLED = "disabled"
    CONST__VP_LOMPORT2_STATE_ENABLED = "enabled"
    CONST_VP_LOMPORT2_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_LOMPORT3_STATE_DISABLED = "Disabled"
    CONST_VP_LOMPORT3_STATE_ENABLED = "Enabled"
    CONST_VP_LOMPORT3_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_LOMPORT3_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_LOMPORT3_STATE_DISABLED = "disabled"
    CONST__VP_LOMPORT3_STATE_ENABLED = "enabled"
    CONST_VP_LOMPORT3_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_LOMPORTS_ALL_STATE_DISABLED = "Disabled"
    CONST_VP_LOMPORTS_ALL_STATE_ENABLED = "Enabled"
    CONST__VP_LOMPORTS_ALL_STATE_DISABLED = "disabled"
    CONST__VP_LOMPORTS_ALL_STATE_ENABLED = "enabled"
    CONST_VP_LOMPORTS_ALL_STATE_PLATFORM_DEFAULT = "platform-default"

class BiosVfOnboardStorage(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfOnboardStorage")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfOnboardStorage"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ONBOARD_SCUSTORAGE_SUPPORT = "VpOnboardSCUStorageSupport"

    CONST_VP_ONBOARD_SCUSTORAGE_SUPPORT_DISABLED = "Disabled"
    CONST_VP_ONBOARD_SCUSTORAGE_SUPPORT_ENABLED = "Enabled"
    CONST__VP_ONBOARD_SCUSTORAGE_SUPPORT_DISABLED = "disabled"
    CONST__VP_ONBOARD_SCUSTORAGE_SUPPORT_ENABLED = "enabled"
    CONST_VP_ONBOARD_SCUSTORAGE_SUPPORT_PLATFORM_DEFAULT = "platform-default"

class BiosBOT(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosBOT")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosBOT"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class BiosVfMirroringMode(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfMirroringMode")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfMirroringMode"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_MIRRORING_MODE = "VpMirroringMode"

    CONST_VP_MIRRORING_MODE_INTER_SOCKET = "inter-socket"
    CONST_VP_MIRRORING_MODE_INTRA_SOCKET = "intra-socket"
    CONST_VP_MIRRORING_MODE_PLATFORM_DEFAULT = "platform-default"

class AdaptorCfgImporter(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorCfgImporter")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorCfgImporter"

    ADMIN_STATE = "AdminState"
    DESCR = "Descr"
    DN = "Dn"
    HOSTNAME = "Hostname"
    PROGRESS = "Progress"
    PROTO = "Proto"
    PWD = "Pwd"
    REMOTE_FILE = "RemoteFile"
    RN = "Rn"
    STATUS = "Status"
    USER = "User"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_PROTO_FTP = "ftp"
    CONST_PROTO_HTTP = "http"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_SCP = "scp"
    CONST_PROTO_SFTP = "sftp"
    CONST_PROTO_TFTP = "tftp"

class StorageControllerSettings(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageControllerSettings")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageControllerSettings"

    AUTO_ENHANCED_IMPORT = "AutoEnhancedImport"
    BATTERY_WARNING = "BatteryWarning"
    CACHE_FLUSH_INTERVAL = "CacheFlushInterval"
    CLUSTER_ENABLE = "ClusterEnable"
    CONSISTENCY_CHECK_RATE = "ConsistencyCheckRate"
    DN = "Dn"
    ECC_BUCKET_LEAK_RATE = "EccBucketLeakRate"
    ENABLE_COPYBACK_ON_SMART = "EnableCopybackOnSmart"
    ENABLE_COPYBACK_TO_SSD_ON_SMART_ERROR = "EnableCopybackToSsdOnSmartError"
    ENABLE_JBOD = "EnableJbod"
    ENABLE_SSD_PATROL_READ = "EnableSsdPatrolRead"
    EXPOSE_ENCLOSURE_DEVICES = "ExposeEnclosureDevices"
    MAINTAIN_PD_FAIL_HISTORY = "MaintainPdFailHistory"
    NCQ_STATUS = "NcqStatus"
    PATROL_READ_RATE = "PatrolReadRate"
    PCI_SLOT = "PciSlot"
    PHYS_DRIVE_COERCION_MODE = "PhysDriveCoercionMode"
    PREDICTIVE_FAIL_POLL_INTERVAL = "PredictiveFailPollInterval"
    REBUILD_RATE = "RebuildRate"
    RECONSTRUCTION_RATE = "ReconstructionRate"
    RN = "Rn"
    SPIN_DOWN_UNCONFIGURED = "SpinDownUnconfigured"
    SPINUP_DELAY = "SpinupDelay"
    SPINUP_DRIVE_COUNT = "SpinupDriveCount"
    STATUS = "Status"


class BiosVfDemandScrub(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfDemandScrub")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfDemandScrub"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_DEMAND_SCRUB = "VpDemandScrub"

    CONST_VP_DEMAND_SCRUB_DISABLED = "Disabled"
    CONST_VP_DEMAND_SCRUB_ENABLED = "Enabled"
    CONST__VP_DEMAND_SCRUB_DISABLED = "disabled"
    CONST__VP_DEMAND_SCRUB_ENABLED = "enabled"
    CONST_VP_DEMAND_SCRUB_PLATFORM_DEFAULT = "platform-default"

class CommSnmpUser(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommSnmpUser")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commSnmpUser"

    AUTH = "Auth"
    AUTH_PWD = "AuthPwd"
    DN = "Dn"
    ID = "Id"
    NAME = "Name"
    PRIVACY = "Privacy"
    PRIVACY_PWD = "PrivacyPwd"
    RN = "Rn"
    SECURITY_LEVEL = "SecurityLevel"
    STATUS = "Status"

    CONST_AUTH_ = ""
    CONST_AUTH_MD5 = "MD5"
    CONST_AUTH_SHA = "SHA"
    CONST_PRIVACY_ = ""
    CONST_PRIVACY_AES = "AES"
    CONST_PRIVACY_DES = "DES"
    CONST_SECURITY_LEVEL_ = ""
    CONST_SECURITY_LEVEL_AUTHNOPRIV = "authnopriv"
    CONST_SECURITY_LEVEL_AUTHPRIV = "authpriv"
    CONST_SECURITY_LEVEL_NOAUTHNOPRIV = "noauthnopriv"

class BiosVfPackageCStateLimit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPackageCStateLimit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPackageCStateLimit"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PACKAGE_CSTATE_LIMIT = "VpPackageCStateLimit"

    CONST_VP_PACKAGE_CSTATE_LIMIT_C0_C1 = "C0/C1"
    CONST_VP_PACKAGE_CSTATE_LIMIT_C2 = "C2"
    CONST_VP_PACKAGE_CSTATE_LIMIT_C6_RETENTION = "C6 Retention"
    CONST_VP_PACKAGE_CSTATE_LIMIT_C6__NON_RETENTION = "C6 non Retention"
    CONST_VP_PACKAGE_CSTATE_LIMIT_C0_STATE = "c0-state"
    CONST_VP_PACKAGE_CSTATE_LIMIT_C1_STATE = "c1-state"
    CONST_VP_PACKAGE_CSTATE_LIMIT_C3_STATE = "c3-state"
    CONST_VP_PACKAGE_CSTATE_LIMIT_C6_STATE = "c6-state"
    CONST_VP_PACKAGE_CSTATE_LIMIT_NO_LIMIT = "no-limit"
    CONST_VP_PACKAGE_CSTATE_LIMIT_PLATFORM_DEFAULT = "platform-default"

class BiosVfCPUEnergyPerformance(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCPUEnergyPerformance")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCPUEnergyPerformance"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CPUENERGY_PERFORMANCE = "VpCPUEnergyPerformance"

    CONST_VP_CPUENERGY_PERFORMANCE_BALANCED_ENERGY = "balanced-energy"
    CONST_VP_CPUENERGY_PERFORMANCE_BALANCED_PERFORMANCE = "balanced-performance"
    CONST_VP_CPUENERGY_PERFORMANCE_ENERGY_EFFICIENT = "energy-efficient"
    CONST_VP_CPUENERGY_PERFORMANCE_PERFORMANCE = "performance"
    CONST_VP_CPUENERGY_PERFORMANCE_PLATFORM_DEFAULT = "platform-default"

class BiosVfUSBPortsConfig(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfUSBPortsConfig")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfUSBPortsConfig"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ALL_USB_DEVICES = "VpAllUsbDevices"
    VP_USB_PORT_FRONT = "VpUsbPortFront"
    VP_USB_PORT_INTERNAL = "VpUsbPortInternal"
    VP_USB_PORT_KVM = "VpUsbPortKVM"
    VP_USB_PORT_REAR = "VpUsbPortRear"
    VP_USB_PORT_SDCARD = "VpUsbPortSDCard"
    VP_USB_PORT_VMEDIA = "VpUsbPortVMedia"

    CONST_VP_ALL_USB_DEVICES_DISABLED = "Disabled"
    CONST_VP_ALL_USB_DEVICES_ENABLED = "Enabled"
    CONST__VP_ALL_USB_DEVICES_DISABLED = "disabled"
    CONST__VP_ALL_USB_DEVICES_ENABLED = "enabled"
    CONST_VP_ALL_USB_DEVICES_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_USB_PORT_FRONT_DISABLED = "Disabled"
    CONST_VP_USB_PORT_FRONT_ENABLED = "Enabled"
    CONST__VP_USB_PORT_FRONT_DISABLED = "disabled"
    CONST__VP_USB_PORT_FRONT_ENABLED = "enabled"
    CONST_VP_USB_PORT_FRONT_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_USB_PORT_INTERNAL_DISABLED = "Disabled"
    CONST_VP_USB_PORT_INTERNAL_ENABLED = "Enabled"
    CONST__VP_USB_PORT_INTERNAL_DISABLED = "disabled"
    CONST__VP_USB_PORT_INTERNAL_ENABLED = "enabled"
    CONST_VP_USB_PORT_INTERNAL_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_USB_PORT_KVM_DISABLED = "Disabled"
    CONST_VP_USB_PORT_KVM_ENABLED = "Enabled"
    CONST__VP_USB_PORT_KVM_DISABLED = "disabled"
    CONST__VP_USB_PORT_KVM_ENABLED = "enabled"
    CONST_VP_USB_PORT_KVM_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_USB_PORT_REAR_DISABLED = "Disabled"
    CONST_VP_USB_PORT_REAR_ENABLED = "Enabled"
    CONST__VP_USB_PORT_REAR_DISABLED = "disabled"
    CONST__VP_USB_PORT_REAR_ENABLED = "enabled"
    CONST_VP_USB_PORT_REAR_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_USB_PORT_SDCARD_DISABLED = "Disabled"
    CONST_VP_USB_PORT_SDCARD_ENABLED = "Enabled"
    CONST__VP_USB_PORT_SDCARD_DISABLED = "disabled"
    CONST__VP_USB_PORT_SDCARD_ENABLED = "enabled"
    CONST_VP_USB_PORT_SDCARD_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_USB_PORT_VMEDIA_DISABLED = "Disabled"
    CONST_VP_USB_PORT_VMEDIA_ENABLED = "Enabled"
    CONST__VP_USB_PORT_VMEDIA_DISABLED = "disabled"
    CONST__VP_USB_PORT_VMEDIA_ENABLED = "enabled"
    CONST_VP_USB_PORT_VMEDIA_PLATFORM_DEFAULT = "platform-default"

class StorageRaidBattery(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageRaidBattery")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageRaidBattery"

    ABSOLUTE_STATE_OF_CHARGE = "AbsoluteStateOfCharge"
    ADMIN_ACTION = "AdminAction"
    BATTERY_PRESENT = "BatteryPresent"
    BATTERY_STATUS = "BatteryStatus"
    BATTERY_TYPE = "BatteryType"
    CHARGING_STATE = "ChargingState"
    COMPLETED_CHARGE_CYCLES = "CompletedChargeCycles"
    CURRENT = "Current"
    DATE_OF_MANUFACTURE = "DateOfManufacture"
    DESIGN_CAPACITY = "DesignCapacity"
    DESIGN_VOLTAGE = "DesignVoltage"
    DN = "Dn"
    EXPECTED_MARGIN_OF_ERROR = "ExpectedMarginOfError"
    FIRMWARE_VERSION = "FirmwareVersion"
    FULL_CAPACITY = "FullCapacity"
    HEALTH = "Health"
    LEARN_CYCLE_REQUESTED = "LearnCycleRequested"
    LEARN_CYCLE_STATUS = "LearnCycleStatus"
    LEARN_MODE = "LearnMode"
    MANUFACTURER = "Manufacturer"
    NEXT_LEARN_CYCLE = "NextLearnCycle"
    RELATIVE_STATE_OF_CHARGE = "RelativeStateOfCharge"
    REMAINING_CAPACITY = "RemainingCapacity"
    RETENTION_TIME = "RetentionTime"
    RN = "Rn"
    SERIAL_NUMBER = "SerialNumber"
    STATUS = "Status"
    TEMPERATURE = "Temperature"
    TEMPERATURE_HIGH = "TemperatureHigh"
    VOLTAGE = "Voltage"

    CONST_ADMIN_ACTION_DISABLE_AUTO_LEARN = "disable-auto-learn"
    CONST_ADMIN_ACTION_ENABLE_AUTO_LEARN = "enable-auto-learn"
    CONST_ADMIN_ACTION_START_LEARN_CYCLE = "start-learn-cycle"

class BiosVfResumeOnACPowerLoss(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfResumeOnACPowerLoss")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfResumeOnACPowerLoss"

    DELAY = "Delay"
    DELAY_TYPE = "DelayType"
    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_RESUME_ON_ACPOWER_LOSS = "VpResumeOnACPowerLoss"

    CONST_DELAY_TYPE_FIXED = "fixed"
    CONST_DELAY_TYPE_RANDOM = "random"
    CONST_VP_RESUME_ON_ACPOWER_LOSS_LAST_STATE = "last-state"
    CONST_VP_RESUME_ON_ACPOWER_LOSS_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_RESUME_ON_ACPOWER_LOSS_RESET = "reset"
    CONST_VP_RESUME_ON_ACPOWER_LOSS_STAY_OFF = "stay-off"

class BiosVfExtendedAPIC(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfExtendedAPIC")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfExtendedAPIC"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_EXTENDED_APIC = "VpExtendedAPIC"

    CONST_VP_EXTENDED_APIC_DISABLED = "Disabled"
    CONST_VP_EXTENDED_APIC_ENABLED = "Enabled"
    CONST_VP_EXTENDED_APIC_X2_APIC = "X2APIC"
    CONST_VP_EXTENDED_APIC_XAPIC = "XAPIC"
    CONST_VP_EXTENDED_APIC_PLATFORM_DEFAULT = "platform-default"

class AdaptorFcErrorRecoveryProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcErrorRecoveryProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcErrorRecoveryProfile"

    DN = "Dn"
    ERROR_DETECT_TIMEOUT = "ErrorDetectTimeout"
    FCP_ERROR_RECOVERY = "FcpErrorRecovery"
    LINK_DOWN_TIMEOUT = "LinkDownTimeout"
    PORT_DOWN_IO_RETRY_COUNT = "PortDownIoRetryCount"
    PORT_DOWN_TIMEOUT = "PortDownTimeout"
    RESOURCE_ALLOCATION_TIMEOUT = "ResourceAllocationTimeout"
    RN = "Rn"
    STATUS = "Status"


class CommVMediaMap(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommVMediaMap")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commVMediaMap"

    DN = "Dn"
    DRIVE_TYPE = "DriveType"
    MAP = "Map"
    MAPPING_STATUS = "MappingStatus"
    MOUNT_OPTIONS = "MountOptions"
    PASSWORD = "Password"
    REMOTE_FILE = "RemoteFile"
    REMOTE_SHARE = "RemoteShare"
    RN = "Rn"
    STATUS = "Status"
    USERNAME = "Username"
    VOLUME_NAME = "VolumeName"

    CONST_DRIVE_TYPE_CD = "cd"
    CONST_DRIVE_TYPE_FLOPPY = "floppy"
    CONST_MAP_CIFS = "cifs"
    CONST_MAP_NFS = "nfs"
    CONST_MAP_WWW = "www"

class LsbootPchStorage(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootPchStorage")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootPchStorage"

    DN = "Dn"
    LUN = "Lun"
    NAME = "Name"
    ORDER = "Order"
    RN = "Rn"
    STATE = "State"
    STATUS = "Status"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_TYPE_PCHSTORAGE = "PCHSTORAGE"

class BiosVfCDNEnable(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCDNEnable")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCDNEnable"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CDNENABLE = "VpCDNEnable"

    CONST_VP_CDNENABLE_DISABLED = "Disabled"
    CONST_VP_CDNENABLE_ENABLED = "Enabled"
    CONST__VP_CDNENABLE_DISABLED = "disabled"
    CONST__VP_CDNENABLE_ENABLED = "enabled"
    CONST_VP_CDNENABLE_PLATFORM_DEFAULT = "platform-default"

class CommKvm(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommKvm")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commKvm"

    ACTIVE_SESSIONS = "ActiveSessions"
    ADMIN_STATE = "AdminState"
    DN = "Dn"
    ENCRYPTION_STATE = "EncryptionState"
    LOCAL_VIDEO_STATE = "LocalVideoState"
    PORT = "Port"
    RN = "Rn"
    STATUS = "Status"
    TOTAL_SESSIONS = "TotalSessions"


class LsbootDef(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootDef")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootDef"

    DN = "Dn"
    NAME = "Name"
    PURPOSE = "Purpose"
    REBOOT_ON_UPDATE = "RebootOnUpdate"
    RN = "Rn"
    STATUS = "Status"

    CONST_PURPOSE_OPERATIONAL = "operational"
    CONST_PURPOSE_UTILITY = "utility"
    CONST_REBOOT_ON_UPDATE_FALSE = "false"
    CONST_REBOOT_ON_UPDATE_NO = "no"
    CONST_REBOOT_ON_UPDATE_TRUE = "true"
    CONST_REBOOT_ON_UPDATE_YES = "yes"

class AdaptorEthRecvQueueProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthRecvQueueProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthRecvQueueProfile"

    COUNT = "Count"
    DN = "Dn"
    RING_SIZE = "RingSize"
    RN = "Rn"
    STATUS = "Status"


class AdaptorEthOffloadProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthOffloadProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthOffloadProfile"

    DN = "Dn"
    LARGE_RECEIVE = "LargeReceive"
    RN = "Rn"
    STATUS = "Status"
    TCP_RX_CHECKSUM = "TcpRxChecksum"
    TCP_SEGMENT = "TcpSegment"
    TCP_TX_CHECKSUM = "TcpTxChecksum"


class LsbootHdd(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootHdd")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootHdd"

    DN = "Dn"
    NAME = "Name"
    ORDER = "Order"
    RN = "Rn"
    SLOT = "Slot"
    STATE = "State"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_SUBTYPE_LOCALHDD = "LOCALHDD"
    CONST_TYPE_LOCALHDD = "LOCALHDD"

class PidCatalogDimm(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PidCatalogDimm")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "pidCatalogDimm"

    CAPACITY = "Capacity"
    DATAWIDTH = "Datawidth"
    DESCRIPTION = "Description"
    DN = "Dn"
    MANUFACTURER = "Manufacturer"
    MFGID = "Mfgid"
    MODEL = "Model"
    NAME = "Name"
    OPERABILITY = "Operability"
    PID = "Pid"
    RN = "Rn"
    SERIALNUMBER = "Serialnumber"
    SPEED = "Speed"
    STATUS = "Status"


class BiosVfCPUPerformance(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCPUPerformance")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCPUPerformance"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CPUPERFORMANCE = "VpCPUPerformance"

    CONST_VP_CPUPERFORMANCE_CUSTOM = "custom"
    CONST_VP_CPUPERFORMANCE_ENTERPRISE = "enterprise"
    CONST_VP_CPUPERFORMANCE_HIGH_THROUGHPUT = "high-throughput"
    CONST_VP_CPUPERFORMANCE_HPC = "hpc"
    CONST_VP_CPUPERFORMANCE_PLATFORM_DEFAULT = "platform-default"

class AdaptorFcRecvQueueProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcRecvQueueProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcRecvQueueProfile"

    DN = "Dn"
    RING_SIZE = "RingSize"
    RN = "Rn"
    STATUS = "Status"


class AdaptorEthInterruptProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthInterruptProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthInterruptProfile"

    COALESCING_TIME = "CoalescingTime"
    COALESCING_TYPE = "CoalescingType"
    COUNT = "Count"
    DN = "Dn"
    MODE = "Mode"
    RN = "Rn"
    STATUS = "Status"

    CONST_COALESCING_TYPE_IDLE = "IDLE"
    CONST_COALESCING_TYPE_MIN = "MIN"
    CONST_MODE_INTX = "INTx"
    CONST_MODE_MSI = "MSI"
    CONST_MODE_MSIX = "MSIx"

class AaaLdapRoleGroup(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AaaLdapRoleGroup")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "aaaLdapRoleGroup"

    ADMIN_ACTION = "AdminAction"
    DN = "Dn"
    DOMAIN = "Domain"
    ID = "Id"
    NAME = "Name"
    RN = "Rn"
    ROLE = "Role"
    STATUS = "Status"

    CONST_ADMIN_ACTION_CLEAR = "clear"
    CONST_ROLE_ = ""
    CONST_ROLE_ADMIN = "admin"
    CONST_ROLE_READ_ONLY = "read-only"
    CONST_ROLE_USER = "user"

class AdaptorLinkTraining(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorLinkTraining")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorLinkTraining"

    DN = "Dn"
    LINK_TRAINING = "LinkTraining"
    RN = "Rn"
    STATUS = "Status"

    CONST_LINK_TRAINING_OFF = "off"
    CONST_LINK_TRAINING_ON = "on"

class StorageFlexFlashController(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageFlexFlashController")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageFlexFlashController"

    ADMIN_ACTION = "AdminAction"
    AUTO_SYNC = "AutoSync"
    CARD_SLOT = "CardSlot"
    CARDS_MANAGEABLE = "CardsManageable"
    CONFIGURED_MODE = "ConfiguredMode"
    CONTROLLER_STATUS = "ControllerStatus"
    DN = "Dn"
    FW_VERSION = "FwVersion"
    HEALTH = "Health"
    ID = "Id"
    INTERNAL_STATE = "InternalState"
    NON_UTIL_PARTITION_NAME = "NonUtilPartitionName"
    PARTITION_NAME = "PartitionName"
    PRODUCT_NAME = "ProductName"
    RN = "Rn"
    RUNNING_FW_VERSION = "RunningFwVersion"
    STARTUP_FW_VERSION = "StartupFwVersion"
    STATUS = "Status"
    VENDOR = "Vendor"

    CONST_ADMIN_ACTION_CONFIGURE_CARDS = "configure-cards"
    CONST_ADMIN_ACTION_CONFIGURE_FIRMWARE_MODE = "configure-firmware-mode"
    CONST_ADMIN_ACTION_RESET_FLEXFLASH_CONTROLLER = "reset-flexflash-controller"
    CONST_ADMIN_ACTION_RESET_PARTITION_DEFAULT = "reset-partition-default"
    CONST_ADMIN_ACTION_SYNC_CARD_CONFIGURATION = "sync-card-configuration"
    CONST_CARD_SLOT_NONE = "none"
    CONST_CARD_SLOT_SLOT_1 = "slot-1"
    CONST_CARD_SLOT_SLOT_2 = "slot-2"
    CONST_CONFIGURED_MODE_MIRROR = "mirror"
    CONST_CONFIGURED_MODE_UTIL = "util"

class BiosVfCoreMultiProcessing(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCoreMultiProcessing")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCoreMultiProcessing"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CORE_MULTI_PROCESSING = "VpCoreMultiProcessing"

    CONST_VP_CORE_MULTI_PROCESSING_1 = "1"
    CONST_VP_CORE_MULTI_PROCESSING_10 = "10"
    CONST_VP_CORE_MULTI_PROCESSING_11 = "11"
    CONST_VP_CORE_MULTI_PROCESSING_12 = "12"
    CONST_VP_CORE_MULTI_PROCESSING_13 = "13"
    CONST_VP_CORE_MULTI_PROCESSING_14 = "14"
    CONST_VP_CORE_MULTI_PROCESSING_2 = "2"
    CONST_VP_CORE_MULTI_PROCESSING_3 = "3"
    CONST_VP_CORE_MULTI_PROCESSING_4 = "4"
    CONST_VP_CORE_MULTI_PROCESSING_5 = "5"
    CONST_VP_CORE_MULTI_PROCESSING_6 = "6"
    CONST_VP_CORE_MULTI_PROCESSING_7 = "7"
    CONST_VP_CORE_MULTI_PROCESSING_8 = "8"
    CONST_VP_CORE_MULTI_PROCESSING_9 = "9"
    CONST_VP_CORE_MULTI_PROCESSING_ALL = "all"
    CONST_VP_CORE_MULTI_PROCESSING_PLATFORM_DEFAULT = "platform-default"

class AdaptorCfgBackup(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorCfgBackup")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorCfgBackup"

    ADMIN_STATE = "AdminState"
    DESCR = "Descr"
    DN = "Dn"
    HOSTNAME = "Hostname"
    PROGRESS = "Progress"
    PROTO = "Proto"
    PWD = "Pwd"
    REMOTE_FILE = "RemoteFile"
    RN = "Rn"
    STATUS = "Status"
    USER = "User"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_PROTO_FTP = "ftp"
    CONST_PROTO_HTTP = "http"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_SCP = "scp"
    CONST_PROTO_SFTP = "sftp"
    CONST_PROTO_TFTP = "tftp"

class StorageVirtualDriveWithDriveGroupSpace(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageVirtualDriveWithDriveGroupSpace")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageVirtualDriveWithDriveGroupSpace"

    DN = "Dn"
    HEALTH = "Health"
    ID = "Id"
    MAX_AVAILABLE_SPACE = "MaxAvailableSpace"
    NAME = "Name"
    RAID_LEVEL = "RaidLevel"
    RN = "Rn"
    STATUS = "Status"
    USED_PHYSICAL_DRIVE_IDS = "UsedPhysicalDriveIds"
    VD_STATUS = "VdStatus"


class EquipmentTpm(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentTpm")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentTpm"

    ACTIVE_STATUS = "ActiveStatus"
    DN = "Dn"
    ENABLED_STATUS = "EnabledStatus"
    MODEL = "Model"
    OWNERSHIP = "Ownership"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    TPM_REVISION = "TpmRevision"
    VENDOR = "Vendor"
    VERSION = "Version"

    CONST_ACTIVE_STATUS_ACTIVATED = "activated"
    CONST_ACTIVE_STATUS_DEACTIVATED = "deactivated"
    CONST_ACTIVE_STATUS_UNKNOWN = "unknown"
    CONST_ENABLED_STATUS_DISABLED = "disabled"
    CONST_ENABLED_STATUS_ENABLED = "enabled"
    CONST_ENABLED_STATUS_UNKNOWN = "unknown"
    CONST_OWNERSHIP_OWNED = "owned"
    CONST_OWNERSHIP_UNKNOWN = "unknown"
    CONST_OWNERSHIP_UNOWNED = "unowned"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"

class AdaptorFcBootTable(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcBootTable")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcBootTable"

    BOOT_LUN = "BootLun"
    DN = "Dn"
    INDEX = "Index"
    RN = "Rn"
    STATUS = "Status"
    TARGET_WWPN = "TargetWwpn"


class BiosVfIntelHyperThreadingTech(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfIntelHyperThreadingTech")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfIntelHyperThreadingTech"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_INTEL_HYPER_THREADING_TECH = "VpIntelHyperThreadingTech"

    CONST_VP_INTEL_HYPER_THREADING_TECH_DISABLED = "Disabled"
    CONST_VP_INTEL_HYPER_THREADING_TECH_ENABLED = "Enabled"
    CONST__VP_INTEL_HYPER_THREADING_TECH_DISABLED = "disabled"
    CONST__VP_INTEL_HYPER_THREADING_TECH_ENABLED = "enabled"
    CONST_VP_INTEL_HYPER_THREADING_TECH_PLATFORM_DEFAULT = "platform-default"

class BiosVfMemoryMappedIOAbove4GB(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfMemoryMappedIOAbove4GB")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfMemoryMappedIOAbove4GB"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_MEMORY_MAPPED_IOABOVE4_GB = "VpMemoryMappedIOAbove4GB"

    CONST_VP_MEMORY_MAPPED_IOABOVE4_GB_DISABLED = "Disabled"
    CONST_VP_MEMORY_MAPPED_IOABOVE4_GB_ENABLED = "Enabled"
    CONST__VP_MEMORY_MAPPED_IOABOVE4_GB_DISABLED = "disabled"
    CONST__VP_MEMORY_MAPPED_IOABOVE4_GB_ENABLED = "enabled"
    CONST_VP_MEMORY_MAPPED_IOABOVE4_GB_PLATFORM_DEFAULT = "platform-default"

class BiosVfEnhancedIntelSpeedStepTech(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfEnhancedIntelSpeedStepTech")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfEnhancedIntelSpeedStepTech"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ENHANCED_INTEL_SPEED_STEP_TECH = "VpEnhancedIntelSpeedStepTech"

    CONST_VP_ENHANCED_INTEL_SPEED_STEP_TECH_DISABLED = "Disabled"
    CONST_VP_ENHANCED_INTEL_SPEED_STEP_TECH_ENABLED = "Enabled"
    CONST__VP_ENHANCED_INTEL_SPEED_STEP_TECH_DISABLED = "disabled"
    CONST__VP_ENHANCED_INTEL_SPEED_STEP_TECH_ENABLED = "enabled"
    CONST_VP_ENHANCED_INTEL_SPEED_STEP_TECH_PLATFORM_DEFAULT = "platform-default"

class AdaptorHostFcIf(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorHostFcIf")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorHostFcIf"

    ADMIN_PERSISTENT_BINDINGS = "AdminPersistentBindings"
    CHANNEL_NUMBER = "ChannelNumber"
    DN = "Dn"
    IF_TYPE = "IfType"
    NAME = "Name"
    PORT_PROFILE = "PortProfile"
    RN = "Rn"
    SAN_BOOT = "SanBoot"
    STATUS = "Status"
    UPLINK_PORT = "UplinkPort"
    WWNN = "Wwnn"
    WWPN = "Wwpn"

    CONST_ADMIN_PERSISTENT_BINDINGS_POLICY = "policy"
    CONST_ADMIN_PERSISTENT_BINDINGS_REBUILD = "rebuild"
    CONST_IF_TYPE_VIRTUAL = "virtual"
    CONST_UPLINK_PORT_0 = "0"
    CONST_UPLINK_PORT_1 = "1"
    CONST_WWNN_AUTO = "AUTO"
    CONST_WWPN_AUTO = "AUTO"

class IodSnapshotCancel(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "IodSnapshotCancel")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "iodSnapshotCancel"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    TIME_OUT = "TimeOut"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"

class AdaptorHostEthIf(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorHostEthIf")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorHostEthIf"

    CDN = "Cdn"
    CHANNEL_NUMBER = "ChannelNumber"
    CLASS_OF_SERVICE = "ClassOfService"
    DN = "Dn"
    IF_TYPE = "IfType"
    ISCSI_BOOT = "IscsiBoot"
    MAC = "Mac"
    MTU = "Mtu"
    NAME = "Name"
    PORT_PROFILE = "PortProfile"
    PXE_BOOT = "PxeBoot"
    RN = "Rn"
    STATUS = "Status"
    UPLINK_PORT = "UplinkPort"
    USNIC_COUNT = "UsnicCount"

    CONST_IF_TYPE_VIRTUAL = "virtual"
    CONST_MAC_AUTO = "AUTO"
    CONST_UPLINK_PORT_0 = "0"
    CONST_UPLINK_PORT_1 = "1"

class AdaptorEthISCSIProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthISCSIProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthISCSIProfile"

    DHCP_ISCSI = "DhcpISCSI"
    DHCP_ID = "DhcpId"
    DHCP_NETWORK_SETTINGS = "DhcpNetworkSettings"
    DHCP_TIMEOUT = "DhcpTimeout"
    DN = "Dn"
    INITIATOR_CHAP_NAME = "InitiatorChapName"
    INITIATOR_CHAP_SECRET = "InitiatorChapSecret"
    INITIATOR_GATEWAY = "InitiatorGateway"
    INITIATOR_IPADDRESS = "InitiatorIPAddress"
    INITIATOR_NAME = "InitiatorName"
    INITIATOR_PRIMARY_DNS = "InitiatorPrimaryDns"
    INITIATOR_SECONDARY_DNS = "InitiatorSecondaryDns"
    INITIATOR_SUBNET_MASK = "InitiatorSubnetMask"
    INITIATOR_TCPTIMEOUT = "InitiatorTCPTimeout"
    IP_VER = "IpVer"
    LINK_BUSY_RETRY_COUNT = "LinkBusyRetryCount"
    LINKUP_TIMEOUT = "LinkupTimeout"
    PRIMARY_TARGET_BOOT_LUN = "PrimaryTargetBootLun"
    PRIMARY_TARGET_CHAP_NAME = "PrimaryTargetChapName"
    PRIMARY_TARGET_CHAP_SECRET = "PrimaryTargetChapSecret"
    PRIMARY_TARGET_IPADDRESS = "PrimaryTargetIPAddress"
    PRIMARY_TARGET_NAME = "PrimaryTargetName"
    PRIMARY_TARGET_PORT = "PrimaryTargetPort"
    RN = "Rn"
    SECONDARY_TARGET_BOOT_LUN = "SecondaryTargetBootLun"
    SECONDARY_TARGET_CHAP_NAME = "SecondaryTargetChapName"
    SECONDARY_TARGET_CHAP_SECRET = "SecondaryTargetChapSecret"
    SECONDARY_TARGET_IPADDRESS = "SecondaryTargetIPAddress"
    SECONDARY_TARGET_NAME = "SecondaryTargetName"
    SECONDARY_TARGET_PORT = "SecondaryTargetPort"
    STATUS = "Status"


class LsbootEfi(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootEfi")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootEfi"

    ACCESS = "Access"
    DN = "Dn"
    ORDER = "Order"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"

    CONST_ACCESS_READ_ONLY = "read-only"
    CONST_TYPE_EFI = "efi"

class BiosVfPCISlotOptionROMEnable(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPCISlotOptionROMEnable")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPCISlotOptionROMEnable"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_SLOT10_LINK_SPEED = "VpSlot10LinkSpeed"
    VP_SLOT10_STATE = "VpSlot10State"
    VP_SLOT1_LINK_SPEED = "VpSlot1LinkSpeed"
    VP_SLOT1_STATE = "VpSlot1State"
    VP_SLOT2_LINK_SPEED = "VpSlot2LinkSpeed"
    VP_SLOT2_STATE = "VpSlot2State"
    VP_SLOT3_LINK_SPEED = "VpSlot3LinkSpeed"
    VP_SLOT3_STATE = "VpSlot3State"
    VP_SLOT4_LINK_SPEED = "VpSlot4LinkSpeed"
    VP_SLOT4_STATE = "VpSlot4State"
    VP_SLOT5_LINK_SPEED = "VpSlot5LinkSpeed"
    VP_SLOT5_STATE = "VpSlot5State"
    VP_SLOT6_LINK_SPEED = "VpSlot6LinkSpeed"
    VP_SLOT6_STATE = "VpSlot6State"
    VP_SLOT7_LINK_SPEED = "VpSlot7LinkSpeed"
    VP_SLOT7_STATE = "VpSlot7State"
    VP_SLOT8_LINK_SPEED = "VpSlot8LinkSpeed"
    VP_SLOT8_STATE = "VpSlot8State"
    VP_SLOT9_LINK_SPEED = "VpSlot9LinkSpeed"
    VP_SLOT9_STATE = "VpSlot9State"
    VP_SLOT_HBALINK_SPEED = "VpSlotHBALinkSpeed"
    VP_SLOT_HBASTATE = "VpSlotHBAState"
    VP_SLOT_MLOMSTATE = "VpSlotMLOMState"
    VP_SLOT_MEZZ_STATE = "VpSlotMezzState"
    VP_SLOT_N1_STATE = "VpSlotN1State"
    VP_SLOT_N2_STATE = "VpSlotN2State"
    VP_SLOT_SASSTATE = "VpSlotSASState"

    CONST_VP_SLOT10_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT10_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT10_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT10_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT10_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT10_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT10_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT10_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT10_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT10_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT10_STATE_DISABLED = "disabled"
    CONST__VP_SLOT10_STATE_ENABLED = "enabled"
    CONST_VP_SLOT10_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT1_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT1_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT1_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT1_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT1_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT1_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT1_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT1_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT1_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT1_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT1_STATE_DISABLED = "disabled"
    CONST__VP_SLOT1_STATE_ENABLED = "enabled"
    CONST_VP_SLOT1_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT2_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT2_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT2_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT2_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT2_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT2_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT2_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT2_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT2_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT2_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT2_STATE_DISABLED = "disabled"
    CONST__VP_SLOT2_STATE_ENABLED = "enabled"
    CONST_VP_SLOT2_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT3_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT3_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT3_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT3_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT3_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT3_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT3_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT3_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT3_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT3_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT3_STATE_DISABLED = "disabled"
    CONST__VP_SLOT3_STATE_ENABLED = "enabled"
    CONST_VP_SLOT3_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT4_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT4_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT4_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT4_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT4_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT4_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT4_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT4_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT4_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT4_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT4_STATE_DISABLED = "disabled"
    CONST__VP_SLOT4_STATE_ENABLED = "enabled"
    CONST_VP_SLOT4_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT5_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT5_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT5_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT5_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT5_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT5_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT5_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT5_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT5_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT5_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT5_STATE_DISABLED = "disabled"
    CONST__VP_SLOT5_STATE_ENABLED = "enabled"
    CONST_VP_SLOT5_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT6_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT6_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT6_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT6_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT6_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT6_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT6_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT6_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT6_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT6_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT6_STATE_DISABLED = "disabled"
    CONST__VP_SLOT6_STATE_ENABLED = "enabled"
    CONST_VP_SLOT6_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT7_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT7_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT7_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT7_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT7_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT7_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT7_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT7_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT7_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT7_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT7_STATE_DISABLED = "disabled"
    CONST__VP_SLOT7_STATE_ENABLED = "enabled"
    CONST_VP_SLOT7_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT8_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT8_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT8_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT8_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT8_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT8_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT8_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT8_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT8_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT8_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT8_STATE_DISABLED = "disabled"
    CONST__VP_SLOT8_STATE_ENABLED = "enabled"
    CONST_VP_SLOT8_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT9_LINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT9_LINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT9_LINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT9_LINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT9_LINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT9_LINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT9_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT9_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT9_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT9_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT9_STATE_DISABLED = "disabled"
    CONST__VP_SLOT9_STATE_ENABLED = "enabled"
    CONST_VP_SLOT9_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT_HBALINK_SPEED_AUTO = "Auto"
    CONST_VP_SLOT_HBALINK_SPEED_DISABLED = "Disabled"
    CONST_VP_SLOT_HBALINK_SPEED_GEN1 = "GEN1"
    CONST_VP_SLOT_HBALINK_SPEED_GEN2 = "GEN2"
    CONST_VP_SLOT_HBALINK_SPEED_GEN3 = "GEN3"
    CONST_VP_SLOT_HBALINK_SPEED_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT_HBASTATE_DISABLED = "Disabled"
    CONST_VP_SLOT_HBASTATE_ENABLED = "Enabled"
    CONST_VP_SLOT_HBASTATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT_HBASTATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT_HBASTATE_DISABLED = "disabled"
    CONST__VP_SLOT_HBASTATE_ENABLED = "enabled"
    CONST_VP_SLOT_HBASTATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT_MLOMSTATE_DISABLED = "Disabled"
    CONST_VP_SLOT_MLOMSTATE_ENABLED = "Enabled"
    CONST_VP_SLOT_MLOMSTATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT_MLOMSTATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT_MLOMSTATE_DISABLED = "disabled"
    CONST__VP_SLOT_MLOMSTATE_ENABLED = "enabled"
    CONST_VP_SLOT_MLOMSTATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT_MEZZ_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT_MEZZ_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT_MEZZ_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT_MEZZ_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT_MEZZ_STATE_DISABLED = "disabled"
    CONST__VP_SLOT_MEZZ_STATE_ENABLED = "enabled"
    CONST_VP_SLOT_MEZZ_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT_N1_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT_N1_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT_N1_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT_N1_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT_N1_STATE_DISABLED = "disabled"
    CONST__VP_SLOT_N1_STATE_ENABLED = "enabled"
    CONST_VP_SLOT_N1_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT_N2_STATE_DISABLED = "Disabled"
    CONST_VP_SLOT_N2_STATE_ENABLED = "Enabled"
    CONST_VP_SLOT_N2_STATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT_N2_STATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT_N2_STATE_DISABLED = "disabled"
    CONST__VP_SLOT_N2_STATE_ENABLED = "enabled"
    CONST_VP_SLOT_N2_STATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SLOT_SASSTATE_DISABLED = "Disabled"
    CONST_VP_SLOT_SASSTATE_ENABLED = "Enabled"
    CONST_VP_SLOT_SASSTATE_LEGACY_ONLY = "Legacy Only"
    CONST_VP_SLOT_SASSTATE_UEFI_ONLY = "UEFI Only"
    CONST__VP_SLOT_SASSTATE_DISABLED = "disabled"
    CONST__VP_SLOT_SASSTATE_ENABLED = "enabled"
    CONST_VP_SLOT_SASSTATE_PLATFORM_DEFAULT = "platform-default"

class BiosVfProcessorC3Report(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfProcessorC3Report")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfProcessorC3Report"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PROCESSOR_C3_REPORT = "VpProcessorC3Report"

    CONST_VP_PROCESSOR_C3_REPORT_DISABLED = "Disabled"
    CONST_VP_PROCESSOR_C3_REPORT_ENABLED = "Enabled"
    CONST__VP_PROCESSOR_C3_REPORT_DISABLED = "disabled"
    CONST__VP_PROCESSOR_C3_REPORT_ENABLED = "enabled"
    CONST_VP_PROCESSOR_C3_REPORT_PLATFORM_DEFAULT = "platform-default"

class AdaptorEthCompQueueProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthCompQueueProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthCompQueueProfile"

    COUNT = "Count"
    DN = "Dn"
    RING_SIZE = "RingSize"
    RN = "Rn"
    STATUS = "Status"


class HuuFirmwareCatalogComponent(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuFirmwareCatalogComponent")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuFirmwareCatalogComponent"

    COMPONENT_NAME = "ComponentName"
    DESCRIPTION = "Description"
    DN = "Dn"
    ID = "Id"
    RN = "Rn"
    STATUS = "Status"


class BiosVfCPUFrequencyFloor(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCPUFrequencyFloor")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCPUFrequencyFloor"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CPUFREQUENCY_FLOOR = "VpCPUFrequencyFloor"

    CONST_VP_CPUFREQUENCY_FLOOR_DISABLED = "Disabled"
    CONST_VP_CPUFREQUENCY_FLOOR_ENABLED = "Enabled"
    CONST__VP_CPUFREQUENCY_FLOOR_DISABLED = "disabled"
    CONST__VP_CPUFREQUENCY_FLOOR_ENABLED = "enabled"
    CONST_VP_CPUFREQUENCY_FLOOR_PLATFORM_DEFAULT = "platform-default"

class EquipmentIndicatorLed(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentIndicatorLed")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentIndicatorLed"

    COLOR = "Color"
    DN = "Dn"
    ID = "Id"
    NAME = "Name"
    OPER_STATE = "OperState"
    RN = "Rn"
    STATUS = "Status"

    CONST_COLOR_AMBER = "amber"
    CONST_COLOR_BLUE = "blue"
    CONST_COLOR_GREEN = "green"
    CONST_COLOR_RED = "red"
    CONST_COLOR_UNKNOWN = "unknown"
    CONST_OPER_STATE_BLINKING = "blinking"
    CONST_OPER_STATE_ETH = "eth"
    CONST_OPER_STATE_FC = "fc"
    CONST_OPER_STATE_OFF = "off"
    CONST_OPER_STATE_ON = "on"
    CONST_OPER_STATE_UNKNOWN = "unknown"

class BiosVfAltitude(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfAltitude")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfAltitude"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ALTITUDE = "VpAltitude"

    CONST_VP_ALTITUDE_1500_M = "1500-m"
    CONST_VP_ALTITUDE_300_M = "300-m"
    CONST_VP_ALTITUDE_3000_M = "3000-m"
    CONST_VP_ALTITUDE_900_M = "900-m"
    CONST_VP_ALTITUDE_AUTO = "auto"
    CONST_VP_ALTITUDE_PLATFORM_DEFAULT = "platform-default"

class LsbootStorage(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootStorage")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootStorage"

    ACCESS = "Access"
    DN = "Dn"
    ORDER = "Order"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"

    CONST_ACCESS_READ_WRITE = "read-write"
    CONST_TYPE_STORAGE = "storage"

class LsbootUsb(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootUsb")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootUsb"

    DN = "Dn"
    NAME = "Name"
    ORDER = "Order"
    RN = "Rn"
    STATE = "State"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_SUBTYPE_ = ""
    CONST_SUBTYPE_USB_CD = "usb-cd"
    CONST_SUBTYPE_USB_FDD = "usb-fdd"
    CONST_SUBTYPE_USB_HDD = "usb-hdd"
    CONST_TYPE_USB = "USB"

class ComputeMbPowerStats(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "ComputeMbPowerStats")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "computeMbPowerStats"

    CONSUMED_POWER = "ConsumedPower"
    DN = "Dn"
    INPUT_CURRENT = "InputCurrent"
    INPUT_VOLTAGE = "InputVoltage"
    RN = "Rn"
    STATUS = "Status"
    TIME_COLLECTED = "TimeCollected"


class BiosVfIntelTurboBoostTech(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfIntelTurboBoostTech")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfIntelTurboBoostTech"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_INTEL_TURBO_BOOST_TECH = "VpIntelTurboBoostTech"

    CONST_VP_INTEL_TURBO_BOOST_TECH_DISABLED = "Disabled"
    CONST_VP_INTEL_TURBO_BOOST_TECH_ENABLED = "Enabled"
    CONST__VP_INTEL_TURBO_BOOST_TECH_DISABLED = "disabled"
    CONST__VP_INTEL_TURBO_BOOST_TECH_ENABLED = "enabled"
    CONST_VP_INTEL_TURBO_BOOST_TECH_PLATFORM_DEFAULT = "platform-default"

class CommSvcEp(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommSvcEp")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commSvcEp"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class AaaUser(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AaaUser")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "aaaUser"

    ACCOUNT_STATUS = "AccountStatus"
    DN = "Dn"
    ID = "Id"
    NAME = "Name"
    PRIV = "Priv"
    PWD = "Pwd"
    RN = "Rn"
    STATUS = "Status"

    CONST_ACCOUNT_STATUS_ACTIVE = "active"
    CONST_ACCOUNT_STATUS_INACTIVE = "inactive"
    CONST_PRIV_ = ""
    CONST_PRIV_ADMIN = "admin"
    CONST_PRIV_READ_ONLY = "read-only"
    CONST_PRIV_USER = "user"

class StorageVirtualDrive(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageVirtualDrive")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageVirtualDrive"

    ACCESS_POLICY = "AccessPolicy"
    ADMIN_ACTION = "AdminAction"
    ALLOW_BACKGROUND_INIT = "AllowBackgroundInit"
    AUTO_DELETE_OLDEST = "AutoDeleteOldest"
    AUTO_SNAPSHOT = "AutoSnapshot"
    BOOT_DRIVE = "BootDrive"
    CACHE_POLICY = "CachePolicy"
    CURRENT_WRITE_CACHE_POLICY = "CurrentWriteCachePolicy"
    DISK_CACHE_POLICY = "DiskCachePolicy"
    DN = "Dn"
    DRIVE_STATE = "DriveState"
    DRIVES_PER_SPAN = "DrivesPerSpan"
    HEALTH = "Health"
    ID = "Id"
    NAME = "Name"
    PHYSICAL_DRIVES_LIST = "PhysicalDrivesList"
    RAID_LEVEL = "RaidLevel"
    READ_POLICY = "ReadPolicy"
    REQUESTED_WRITE_CACHE_POLICY = "RequestedWriteCachePolicy"
    RN = "Rn"
    SIZE = "Size"
    SPAN_DEPTH = "SpanDepth"
    STATUS = "Status"
    STRIP_SIZE = "StripSize"
    TARGET_ID = "TargetId"
    VD_STATUS = "VdStatus"
    WRITE_CACHE_POLICY = "WriteCachePolicy"

    CONST_ACCESS_POLICY_ = ""
    CONST_ACCESS_POLICY_BLOCKED = "blocked"
    CONST_ACCESS_POLICY_HIDDEN = "hidden"
    CONST_ACCESS_POLICY_READ_ONLY = "read-only"
    CONST_ACCESS_POLICY_READ_WRITE = "read-write"
    CONST_ADMIN_ACTION_CANCEL_INITIALIZATION = "cancel-initialization"
    CONST_ADMIN_ACTION_RECONSTRUCT_VIRTUAL_DRIVE = "reconstruct-virtual-drive"
    CONST_ADMIN_ACTION_SET_BOOT_DRIVE = "set-boot-drive"
    CONST_ADMIN_ACTION_START_FAST_INITIALIZATION = "start-fast-initialization"
    CONST_ADMIN_ACTION_START_FULL_INITIALIZATION = "start-full-initialization"
    CONST_CACHE_POLICY_ = ""
    CONST_CACHE_POLICY_CACHED_IO = "cached-io"
    CONST_CACHE_POLICY_DIRECT_IO = "direct-io"
    CONST_DISK_CACHE_POLICY_ = ""
    CONST_DISK_CACHE_POLICY_DISABLED = "disabled"
    CONST_DISK_CACHE_POLICY_ENABLED = "enabled"
    CONST_DISK_CACHE_POLICY_UNCHANGED = "unchanged"
    CONST_RAID_LEVEL_0 = "0"
    CONST_RAID_LEVEL_1 = "1"
    CONST_RAID_LEVEL_5 = "5"
    CONST_RAID_LEVEL_6 = "6"
    CONST_READ_POLICY_ = ""
    CONST_READ_POLICY_ALWAYS_READ_AHEAD = "always-read-ahead"
    CONST_READ_POLICY_NO_READ_AHEAD = "no-read-ahead"
    CONST_REQUESTED_WRITE_CACHE_POLICY_ALWAYS_WRITE_BACK = "Always Write Back"
    CONST_REQUESTED_WRITE_CACHE_POLICY_WRITE_BACK_GOOD_BBU = "Write Back Good BBU"
    CONST_REQUESTED_WRITE_CACHE_POLICY_WRITE_THROUGH = "Write Through"
    CONST__REQUESTED_WRITE_CACHE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    CONST__REQUESTED_WRITE_CACHE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    CONST__REQUESTED_WRITE_CACHE_POLICY_WRITE_THROUGH = "write-through"
    CONST_STRIP_SIZE_ = ""
    CONST_STRIP_SIZE_1024K = "1024k"
    CONST_STRIP_SIZE_128K = "128k"
    CONST_STRIP_SIZE_16K = "16k"
    CONST_STRIP_SIZE_256K = "256k"
    CONST_STRIP_SIZE_32K = "32k"
    CONST_STRIP_SIZE_512K = "512k"
    CONST_STRIP_SIZE_64K = "64k"
    CONST_STRIP_SIZE_8K = "8k"

class AdaptorExtEthIf(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorExtEthIf")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorExtEthIf"

    ADMIN_SPEED = "AdminSpeed"
    DN = "Dn"
    IF_TYPE = "IfType"
    LINK_STATE = "LinkState"
    MAC = "Mac"
    OPER_SPEED = "OperSpeed"
    PORT_ID = "PortId"
    RN = "Rn"
    STATUS = "Status"
    TRANSPORT = "Transport"

    CONST_ADMIN_SPEED_ = "-"
    CONST_ADMIN_SPEED_10_GBPS = "10Gbps"
    CONST_ADMIN_SPEED_1_GBPS = "1Gbps"
    CONST_ADMIN_SPEED_40_GBPS = "40Gbps"
    CONST_ADMIN_SPEED_4X10_GBPS = "4x10Gbps"
    CONST_ADMIN_SPEED_AUTO = "Auto"
    CONST_IF_TYPE_AGGREGATION = "aggregation"
    CONST_IF_TYPE_PHYSICAL = "physical"
    CONST_IF_TYPE_UNKNOWN = "unknown"
    CONST_IF_TYPE_VIRTUAL = "virtual"
    CONST_LINK_STATE_ADMIN_DOWN = "admin-down"
    CONST_LINK_STATE_DOWN = "down"
    CONST_LINK_STATE_ERROR = "error"
    CONST_LINK_STATE_UNALLOCATED = "unallocated"
    CONST_LINK_STATE_UNAVAILABLE = "unavailable"
    CONST_LINK_STATE_UNKNOWN = "unknown"
    CONST_LINK_STATE_UP = "up"
    CONST_OPER_SPEED_ = "-"
    CONST_OPER_SPEED_10_GBPS = "10Gbps"
    CONST_OPER_SPEED_1_GBPS = "1Gbps"
    CONST_OPER_SPEED_40_GBPS = "40Gbps"
    CONST_OPER_SPEED_4X10_GBPS = "4x10Gbps"
    CONST_OPER_SPEED_AUTO = "Auto"
    CONST_PORT_ID_0 = "0"
    CONST_PORT_ID_1 = "1"

class BiosBootDev(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosBootDev")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosBootDev"

    DESCR = "Descr"
    DN = "Dn"
    ORDER = "Order"
    RN = "Rn"
    STATUS = "Status"

    CONST_ORDER_1 = "1"
    CONST_ORDER_10 = "10"
    CONST_ORDER_11 = "11"
    CONST_ORDER_12 = "12"
    CONST_ORDER_13 = "13"
    CONST_ORDER_14 = "14"
    CONST_ORDER_15 = "15"
    CONST_ORDER_2 = "2"
    CONST_ORDER_3 = "3"
    CONST_ORDER_4 = "4"
    CONST_ORDER_5 = "5"
    CONST_ORDER_6 = "6"
    CONST_ORDER_7 = "7"
    CONST_ORDER_8 = "8"
    CONST_ORDER_9 = "9"

class HuuController(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuController")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuController"

    DESCRIPTION = "Description"
    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class LsbootPxe(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootPxe")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootPxe"

    DN = "Dn"
    NAME = "Name"
    ORDER = "Order"
    PORT = "Port"
    RN = "Rn"
    SLOT = "Slot"
    STATE = "State"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_SUBTYPE_PXE = "PXE"
    CONST_TYPE_PXE = "PXE"

class BiosVfProcessorC6Report(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfProcessorC6Report")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfProcessorC6Report"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PROCESSOR_C6_REPORT = "VpProcessorC6Report"

    CONST_VP_PROCESSOR_C6_REPORT_DISABLED = "Disabled"
    CONST_VP_PROCESSOR_C6_REPORT_ENABLED = "Enabled"
    CONST__VP_PROCESSOR_C6_REPORT_DISABLED = "disabled"
    CONST__VP_PROCESSOR_C6_REPORT_ENABLED = "enabled"
    CONST_VP_PROCESSOR_C6_REPORT_PLATFORM_DEFAULT = "platform-default"

class BiosVfDCUPrefetch(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfDCUPrefetch")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfDCUPrefetch"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_IPPREFETCH = "VpIPPrefetch"
    VP_STREAMER_PREFETCH = "VpStreamerPrefetch"

    CONST_VP_IPPREFETCH_DISABLED = "Disabled"
    CONST_VP_IPPREFETCH_ENABLED = "Enabled"
    CONST__VP_IPPREFETCH_DISABLED = "disabled"
    CONST__VP_IPPREFETCH_ENABLED = "enabled"
    CONST_VP_IPPREFETCH_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_STREAMER_PREFETCH_DISABLED = "Disabled"
    CONST_VP_STREAMER_PREFETCH_ENABLED = "Enabled"
    CONST__VP_STREAMER_PREFETCH_DISABLED = "disabled"
    CONST__VP_STREAMER_PREFETCH_ENABLED = "enabled"
    CONST_VP_STREAMER_PREFETCH_PLATFORM_DEFAULT = "platform-default"

class BiosVfFRB2Enable(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfFRB2Enable")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfFRB2Enable"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_FRB2_ENABLE = "VpFRB2Enable"

    CONST_VP_FRB2_ENABLE_DISABLED = "Disabled"
    CONST_VP_FRB2_ENABLE_ENABLED = "Enabled"
    CONST__VP_FRB2_ENABLE_DISABLED = "disabled"
    CONST__VP_FRB2_ENABLE_ENABLED = "enabled"
    CONST_VP_FRB2_ENABLE_PLATFORM_DEFAULT = "platform-default"

class AdaptorFcPortFLogiProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcPortFLogiProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcPortFLogiProfile"

    DN = "Dn"
    RETRIES = "Retries"
    RN = "Rn"
    STATUS = "Status"
    TIMEOUT = "Timeout"

    CONST_RETRIES_INFINITE = "INFINITE"

class StorageVirtualDriveCreatorUsingUnusedPhysicalDrive(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageVirtualDriveCreatorUsingUnusedPhysicalDrive")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageVirtualDriveCreatorUsingUnusedPhysicalDrive"

    ACCESS_POLICY = "AccessPolicy"
    ADMIN_STATE = "AdminState"
    CACHE_POLICY = "CachePolicy"
    CREATED_VIRTUAL_DRIVE_DN = "CreatedVirtualDriveDn"
    DESCRIPTION = "Description"
    DISK_CACHE_POLICY = "DiskCachePolicy"
    DN = "Dn"
    DRIVE_GROUP = "DriveGroup"
    MIN_REQUIRED_PHYSICAL_DRIVES = "MinRequiredPhysicalDrives"
    OPER_STATUS = "OperStatus"
    RAID_LEVEL = "RaidLevel"
    READ_POLICY = "ReadPolicy"
    RN = "Rn"
    SIZE = "Size"
    STATUS = "Status"
    STRIP_SIZE = "StripSize"
    VIRTUAL_DRIVE_NAME = "VirtualDriveName"
    WRITE_POLICY = "WritePolicy"

    CONST_ACCESS_POLICY_ = ""
    CONST_ACCESS_POLICY_BLOCKED = "blocked"
    CONST_ACCESS_POLICY_HIDDEN = "hidden"
    CONST_ACCESS_POLICY_READ_ONLY = "read-only"
    CONST_ACCESS_POLICY_READ_WRITE = "read-write"
    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_CACHE_POLICY_ = ""
    CONST_CACHE_POLICY_CACHED_IO = "cached-io"
    CONST_CACHE_POLICY_DIRECT_IO = "direct-io"
    CONST_DISK_CACHE_POLICY_ = ""
    CONST_DISK_CACHE_POLICY_DISABLED = "disabled"
    CONST_DISK_CACHE_POLICY_ENABLED = "enabled"
    CONST_DISK_CACHE_POLICY_UNCHANGED = "unchanged"
    CONST_RAID_LEVEL_ = ""
    CONST_RAID_LEVEL_0 = "0"
    CONST_RAID_LEVEL_1 = "1"
    CONST_RAID_LEVEL_10 = "10"
    CONST_RAID_LEVEL_5 = "5"
    CONST_RAID_LEVEL_50 = "50"
    CONST_RAID_LEVEL_6 = "6"
    CONST_RAID_LEVEL_60 = "60"
    CONST_READ_POLICY_ = ""
    CONST_READ_POLICY_ALWAYS_READ_AHEAD = "always-read-ahead"
    CONST_READ_POLICY_NO_READ_AHEAD = "no-read-ahead"
    CONST_STRIP_SIZE_ = ""
    CONST_STRIP_SIZE_1024K = "1024k"
    CONST_STRIP_SIZE_128K = "128k"
    CONST_STRIP_SIZE_16K = "16k"
    CONST_STRIP_SIZE_256K = "256k"
    CONST_STRIP_SIZE_32K = "32k"
    CONST_STRIP_SIZE_512K = "512k"
    CONST_STRIP_SIZE_64K = "64k"
    CONST_STRIP_SIZE_8K = "8k"
    CONST_WRITE_POLICY_ = ""
    CONST_WRITE_POLICY_ALWAYS_WRITE_BACK = "Always Write Back"
    CONST_WRITE_POLICY_WRITE_BACK_GOOD_BBU = "Write Back Good BBU"
    CONST_WRITE_POLICY_WRITE_THROUGH = "Write Through"
    CONST__WRITE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    CONST__WRITE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    CONST__WRITE_POLICY_WRITE_THROUGH = "write-through"

class LsbootDevPrecision(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootDevPrecision")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootDevPrecision"

    CONFIGURED_BOOT_MODE = "ConfiguredBootMode"
    DN = "Dn"
    LAST_CONFIGURED_BOOT_ORDER_SOURCE = "LastConfiguredBootOrderSource"
    NAME = "Name"
    PURPOSE = "Purpose"
    REAPPLY = "Reapply"
    REBOOT_ON_UPDATE = "RebootOnUpdate"
    RN = "Rn"
    STATUS = "Status"

    CONST_CONFIGURED_BOOT_MODE_LEGACY = "Legacy"
    CONST_CONFIGURED_BOOT_MODE_NONE = "None"
    CONST_CONFIGURED_BOOT_MODE_UEFI = "Uefi"
    CONST_LAST_CONFIGURED_BOOT_ORDER_SOURCE_BIOS = "BIOS"
    CONST_LAST_CONFIGURED_BOOT_ORDER_SOURCE_CIMC = "CIMC"
    CONST_LAST_CONFIGURED_BOOT_ORDER_SOURCE_UNKNOWN = "UNKNOWN"
    CONST_PURPOSE_OPERATIONAL = "operational"
    CONST_PURPOSE_UTILITY = "utility"
    CONST_REAPPLY_FALSE = "false"
    CONST_REAPPLY_NO = "no"
    CONST_REAPPLY_TRUE = "true"
    CONST_REAPPLY_YES = "yes"
    CONST_REBOOT_ON_UPDATE_FALSE = "false"
    CONST_REBOOT_ON_UPDATE_NO = "no"
    CONST_REBOOT_ON_UPDATE_TRUE = "true"
    CONST_REBOOT_ON_UPDATE_YES = "yes"

class BiosVfNUMAOptimized(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfNUMAOptimized")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfNUMAOptimized"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_NUMAOPTIMIZED = "VpNUMAOptimized"

    CONST_VP_NUMAOPTIMIZED_DISABLED = "Disabled"
    CONST_VP_NUMAOPTIMIZED_ENABLED = "Enabled"
    CONST__VP_NUMAOPTIMIZED_DISABLED = "disabled"
    CONST__VP_NUMAOPTIMIZED_ENABLED = "enabled"
    CONST_VP_NUMAOPTIMIZED_PLATFORM_DEFAULT = "platform-default"

class CommSsh(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommSsh")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commSsh"

    ACTIVE_SESSIONS = "ActiveSessions"
    ADMIN_STATE = "AdminState"
    DESCR = "Descr"
    DN = "Dn"
    MAXIMUM_SESSIONS = "MaximumSessions"
    NAME = "Name"
    PORT = "Port"
    PROTO = "Proto"
    RN = "Rn"
    SESSION_TIMEOUT = "SessionTimeout"
    STATUS = "Status"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_PROTO_ALL = "all"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_TCP = "tcp"
    CONST_PROTO_UDP = "udp"

class BiosVfLvDIMMSupport(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfLvDIMMSupport")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfLvDIMMSupport"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_LV_DDRMODE = "VpLvDDRMode"

    CONST_VP_LV_DDRMODE_AUTO = "auto"
    CONST_VP_LV_DDRMODE_PERFORMANCE_MODE = "performance-mode"
    CONST_VP_LV_DDRMODE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_LV_DDRMODE_POWER_SAVING_MODE = "power-saving-mode"

class BiosVfProcessorC1E(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfProcessorC1E")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfProcessorC1E"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PROCESSOR_C1_E = "VpProcessorC1E"

    CONST_VP_PROCESSOR_C1_E_DISABLED = "Disabled"
    CONST_VP_PROCESSOR_C1_E_ENABLED = "Enabled"
    CONST__VP_PROCESSOR_C1_E_DISABLED = "disabled"
    CONST__VP_PROCESSOR_C1_E_ENABLED = "enabled"
    CONST_VP_PROCESSOR_C1_E_PLATFORM_DEFAULT = "platform-default"

class BiosVfCDNSupport(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCDNSupport")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCDNSupport"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CDNSUPPORT = "VpCDNSupport"

    CONST_VP_CDNSUPPORT_DISABLED = "Disabled"
    CONST_VP_CDNSUPPORT_LOMS_ONLY = "LOMs Only"
    CONST_VP_CDNSUPPORT_PLATFORM_DEFAULT = "platform-default"

class CommVMedia(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommVMedia")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commVMedia"

    ACTIVE_SESSIONS = "ActiveSessions"
    ADMIN_STATE = "AdminState"
    DN = "Dn"
    ENCRYPTION_STATE = "EncryptionState"
    RN = "Rn"
    STATUS = "Status"


class BiosVfPwrPerfTuning(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPwrPerfTuning")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPwrPerfTuning"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PWR_PERF_TUNING = "VpPwrPerfTuning"

    CONST_VP_PWR_PERF_TUNING_BIOS = "bios"
    CONST_VP_PWR_PERF_TUNING_OS = "os"
    CONST_VP_PWR_PERF_TUNING_PLATFORM_DEFAULT = "platform-default"

class NetworkAdapterUnit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "NetworkAdapterUnit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "networkAdapterUnit"

    DN = "Dn"
    MODEL = "Model"
    NUM_INTF = "NumIntf"
    RN = "Rn"
    SLOT = "Slot"
    STATUS = "Status"


class AdaptorFcCdbWorkQueueProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcCdbWorkQueueProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcCdbWorkQueueProfile"

    COUNT = "Count"
    DN = "Dn"
    RING_SIZE = "RingSize"
    RN = "Rn"
    STATUS = "Status"


class StorageFlexFlashControllerProps(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageFlexFlashControllerProps")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageFlexFlashControllerProps"

    ADMIN_ACTION = "AdminAction"
    AUTO_SYNC = "AutoSync"
    CARD_SLOT = "CardSlot"
    CARDS_MANAGEABLE = "CardsManageable"
    CONFIGURED_MODE = "ConfiguredMode"
    CONTROLLER_NAME = "ControllerName"
    CONTROLLER_STATUS = "ControllerStatus"
    DN = "Dn"
    FW_VERSION = "FwVersion"
    HEALTH = "Health"
    INTERNAL_STATE = "InternalState"
    NON_UTIL_PARTITION_NAME = "NonUtilPartitionName"
    OPERATING_MODE = "OperatingMode"
    PARTITION_NAME = "PartitionName"
    PHYSICAL_DRIVE_COUNT = "PhysicalDriveCount"
    PRODUCT_NAME = "ProductName"
    RN = "Rn"
    RUNNING_FW_VERSION = "RunningFwVersion"
    STARTUP_FW_VERSION = "StartupFwVersion"
    STATUS = "Status"
    VENDOR = "Vendor"
    VIRTUAL_DRIVE_COUNT = "VirtualDriveCount"


class AaaLdap(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AaaLdap")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "aaaLdap"

    ADMIN_STATE = "AdminState"
    ATTRIBUTE = "Attribute"
    BASEDN = "Basedn"
    BIND_DN = "BindDn"
    BIND_METHOD = "BindMethod"
    DN = "Dn"
    DNS_DOMAIN_SOURCE = "DnsDomainSource"
    DNS_SEARCH_DOMAIN = "DnsSearchDomain"
    DNS_SEARCH_FOREST = "DnsSearchForest"
    DOMAIN = "Domain"
    ENCRYPTION = "Encryption"
    FILTER = "Filter"
    GROUP_ATTRIBUTE = "GroupAttribute"
    GROUP_AUTH = "GroupAuth"
    GROUP_NESTED_SEARCH = "GroupNestedSearch"
    LDAP_SERVER1 = "LdapServer1"
    LDAP_SERVER2 = "LdapServer2"
    LDAP_SERVER3 = "LdapServer3"
    LDAP_SERVER4 = "LdapServer4"
    LDAP_SERVER5 = "LdapServer5"
    LDAP_SERVER6 = "LdapServer6"
    LDAP_SERVER_PORT1 = "LdapServerPort1"
    LDAP_SERVER_PORT2 = "LdapServerPort2"
    LDAP_SERVER_PORT3 = "LdapServerPort3"
    LDAP_SERVER_PORT4 = "LdapServerPort4"
    LDAP_SERVER_PORT5 = "LdapServerPort5"
    LDAP_SERVER_PORT6 = "LdapServerPort6"
    LOCATE_DIRECTORY_USING_DNS = "LocateDirectoryUsingDNS"
    PASSWORD = "Password"
    RN = "Rn"
    STATUS = "Status"
    TIMEOUT = "Timeout"

    CONST_BIND_METHOD_ANONYMOUS = "anonymous"
    CONST_BIND_METHOD_CONFIGURED_CREDENTIALS = "configured-credentials"
    CONST_BIND_METHOD_LOGIN_CREDENTIALS = "login-credentials"
    CONST_DNS_DOMAIN_SOURCE_CONFIGURED_DOMAIN = "configured-domain"
    CONST_DNS_DOMAIN_SOURCE_EXTRACTED_CONFIGURED_DOMAIN = "extracted-configured-domain"
    CONST_DNS_DOMAIN_SOURCE_EXTRACTED_DOMAIN = "extracted-domain"
    CONST_LOCATE_DIRECTORY_USING_DNS_NO = "no"
    CONST_LOCATE_DIRECTORY_USING_DNS_YES = "yes"

class BiosVfOSBootWatchdogTimerTimeout(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfOSBootWatchdogTimerTimeout")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfOSBootWatchdogTimerTimeout"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT = "VpOSBootWatchdogTimerTimeout"

    CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_10_MINUTES = "10-minutes"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_15_MINUTES = "15-minutes"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_20_MINUTES = "20-minutes"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_5_MINUTES = "5-minutes"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_PLATFORM_DEFAULT = "platform-default"

class AdaptorFcWorkQueueProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcWorkQueueProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcWorkQueueProfile"

    DN = "Dn"
    RING_SIZE = "RingSize"
    RN = "Rn"
    STATUS = "Status"


class BiosVfAssertNMIOnSERR(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfAssertNMIOnSERR")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfAssertNMIOnSERR"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ASSERT_NMION_SERR = "VpAssertNMIOnSERR"

    CONST_VP_ASSERT_NMION_SERR_DISABLED = "Disabled"
    CONST_VP_ASSERT_NMION_SERR_ENABLED = "Enabled"
    CONST__VP_ASSERT_NMION_SERR_DISABLED = "disabled"
    CONST__VP_ASSERT_NMION_SERR_ENABLED = "enabled"
    CONST_VP_ASSERT_NMION_SERR_PLATFORM_DEFAULT = "platform-default"

class StorageControllerProps(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageControllerProps")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageControllerProps"

    BACKEND_PORT_COUNT = "BackendPortCount"
    BATTERY_STATUS = "BatteryStatus"
    BBU_PRESENT = "BbuPresent"
    BOOT_BLOCK_VERSION = "BootBlockVersion"
    BOOT_DRIVE = "BootDrive"
    BOOT_DRIVE_IS_PHYSICAL_DRIVE = "BootDriveIsPhysicalDrive"
    BOOT_VERSION = "BootVersion"
    CACHE_MEMORY_SIZE = "CacheMemorySize"
    CONTROLLER_STATUS = "ControllerStatus"
    CRITICAL_PHYSICAL_DRIVE_COUNT = "CriticalPhysicalDriveCount"
    DATE_OF_MANUFACTURE = "DateOfManufacture"
    DEGRADED_VIRTUAL_DRIVE_COUNT = "DegradedVirtualDriveCount"
    DN = "Dn"
    FAILED_PHYSICAL_DRIVE_COUNT = "FailedPhysicalDriveCount"
    FIRMWARE_PACKAGE_BUILD = "FirmwarePackageBuild"
    FLASH_PRESENT = "FlashPresent"
    HEALTH = "Health"
    MEMORY_CORRECTABLE_ERRORS = "MemoryCorrectableErrors"
    MEMORY_PRESENT = "MemoryPresent"
    MEMORY_SIZE = "MemorySize"
    MEMORY_UNCORRECTABLE_ERRORS = "MemoryUncorrectableErrors"
    NVDATA_VERSION = "NvdataVersion"
    NVRAM_PRESENT = "NvramPresent"
    OFFLINE_VIRTUAL_DRIVE_COUNT = "OfflineVirtualDriveCount"
    PCI_SLOT = "PciSlot"
    PHYSICAL_DRIVE_COUNT = "PhysicalDriveCount"
    PREBOOT_CLI_VERSION = "PrebootCliVersion"
    RAID_CHIP_TEMP_CENTIGRADE = "RaidChipTempCentigrade"
    REVISION = "Revision"
    RN = "Rn"
    SAS_ADDRESS0 = "SasAddress0"
    SAS_ADDRESS1 = "SasAddress1"
    SAS_ADDRESS2 = "SasAddress2"
    SAS_ADDRESS3 = "SasAddress3"
    SAS_ADDRESS4 = "SasAddress4"
    SAS_ADDRESS5 = "SasAddress5"
    SAS_ADDRESS6 = "SasAddress6"
    SAS_ADDRESS7 = "SasAddress7"
    SERIAL = "Serial"
    SERIAL_DEBUGGER_PRESENT = "SerialDebuggerPresent"
    STATUS = "Status"
    SUPPORTS_RAID0 = "SupportsRaid0"
    SUPPORTS_RAID00 = "SupportsRaid00"
    SUPPORTS_RAID1 = "SupportsRaid1"
    SUPPORTS_RAID10 = "SupportsRaid10"
    SUPPORTS_RAID1E = "SupportsRaid1e"
    SUPPORTS_RAID1E0RLQ0 = "SupportsRaid1e0rlq0"
    SUPPORTS_RAID1ERLQ0 = "SupportsRaid1erlq0"
    SUPPORTS_RAID5 = "SupportsRaid5"
    SUPPORTS_RAID50 = "SupportsRaid50"
    SUPPORTS_RAID6 = "SupportsRaid6"
    SUPPORTS_RAID60 = "SupportsRaid60"
    SUPPORTS_RAIDSRL03 = "SupportsRaidsrl03"
    TTY_LOG_STATUS = "TtyLogStatus"
    VIRTUAL_DRIVE_COUNT = "VirtualDriveCount"
    WEB_BIOS_VERSION = "WebBiosVersion"


class LsbootIscsi(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootIscsi")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootIscsi"

    DN = "Dn"
    NAME = "Name"
    ORDER = "Order"
    PORT = "Port"
    RN = "Rn"
    SLOT = "Slot"
    STATE = "State"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_SUBTYPE_ISCSI = "ISCSI"
    CONST_TYPE_ISCSI = "ISCSI"

class PowerBudget(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PowerBudget")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "powerBudget"

    ADMIN_ACTION = "AdminAction"
    ADMIN_STATE = "AdminState"
    DN = "Dn"
    MAX_CPU_POWER = "MaxCpuPower"
    MAX_MEMORY_POWER = "MaxMemoryPower"
    MAX_POWER = "MaxPower"
    MIN_CPU_POWER = "MinCpuPower"
    MIN_MEMORY_POWER = "MinMemoryPower"
    MIN_POWER = "MinPower"
    POWER_CHAR_STATUS = "PowerCharStatus"
    RN = "Rn"
    RUN_POW_CHAR_AT_BOOT = "RunPowCharAtBoot"
    STATUS = "Status"

    CONST_ADMIN_ACTION_RESET_POWER_PROFILE_DEFAULT = "reset-power-profile-default"
    CONST_ADMIN_ACTION_START_POWER_CHAR = "start-power-char"

class CommHttps(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommHttps")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commHttps"

    ACTIVE_SESSIONS = "ActiveSessions"
    ADMIN_STATE = "AdminState"
    DESCR = "Descr"
    DN = "Dn"
    MAXIMUM_SESSIONS = "MaximumSessions"
    NAME = "Name"
    PORT = "Port"
    PROTO = "Proto"
    RN = "Rn"
    SESSION_TIMEOUT = "SessionTimeout"
    STATUS = "Status"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_PROTO_ALL = "all"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_TCP = "tcp"
    CONST_PROTO_UDP = "udp"

class MgmtController(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "MgmtController")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "mgmtController"

    DN = "Dn"
    MODEL = "Model"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    SUBJECT = "Subject"
    VENDOR = "Vendor"

    CONST_SUBJECT_ADAPTOR = "adaptor"
    CONST_SUBJECT_BLADE = "blade"
    CONST_SUBJECT_BOARD_CONTROLLER = "board-controller"
    CONST_SUBJECT_SYSTEM = "system"
    CONST_SUBJECT_UNKNOWN = "unknown"

class BiosVfLegacyUSBSupport(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfLegacyUSBSupport")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfLegacyUSBSupport"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_LEGACY_USBSUPPORT = "VpLegacyUSBSupport"

    CONST_VP_LEGACY_USBSUPPORT_AUTO = "Auto"
    CONST_VP_LEGACY_USBSUPPORT_DISABLED = "Disabled"
    CONST_VP_LEGACY_USBSUPPORT_ENABLED = "Enabled"
    CONST__VP_LEGACY_USBSUPPORT_AUTO = "auto"
    CONST__VP_LEGACY_USBSUPPORT_DISABLED = "disabled"
    CONST__VP_LEGACY_USBSUPPORT_ENABLED = "enabled"
    CONST_VP_LEGACY_USBSUPPORT_PLATFORM_DEFAULT = "platform-default"

class BiosVfCkeLowPolicy(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfCkeLowPolicy")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfCkeLowPolicy"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CKE_LOW_POLICY = "VpCkeLowPolicy"

    CONST_VP_CKE_LOW_POLICY_AUTO = "auto"
    CONST_VP_CKE_LOW_POLICY_DISABLED = "disabled"
    CONST_VP_CKE_LOW_POLICY_FAST = "fast"
    CONST_VP_CKE_LOW_POLICY_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_CKE_LOW_POLICY_SLOW = "slow"

class CommHttp(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommHttp")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commHttp"

    ACTIVE_SESSIONS = "ActiveSessions"
    ADMIN_STATE = "AdminState"
    DESCR = "Descr"
    DN = "Dn"
    MAXIMUM_SESSIONS = "MaximumSessions"
    NAME = "Name"
    PORT = "Port"
    PROTO = "Proto"
    REDIRECT_STATE = "RedirectState"
    RN = "Rn"
    SESSION_TIMEOUT = "SessionTimeout"
    STATUS = "Status"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_PROTO_ALL = "all"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_TCP = "tcp"
    CONST_PROTO_UDP = "udp"
    CONST_REDIRECT_STATE_DISABLED = "disabled"
    CONST_REDIRECT_STATE_ENABLED = "enabled"

class BiosVfOnboardStorageSWStack(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfOnboardStorageSWStack")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfOnboardStorageSWStack"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ONBOARD_SCUSTORAGE_SWSTACK = "VpOnboardSCUStorageSWStack"

    CONST_VP_ONBOARD_SCUSTORAGE_SWSTACK_INTEL_RSTE = "Intel RSTe"
    CONST_VP_ONBOARD_SCUSTORAGE_SWSTACK_LSI_SW_RAID = "LSI SW RAID"
    CONST_VP_ONBOARD_SCUSTORAGE_SWSTACK_PLATFORM_DEFAULT = "platform-default"

class AdaptorGenProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorGenProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorGenProfile"

    CONFIGURATION_PENDING = "ConfigurationPending"
    DN = "Dn"
    FIP_MODE = "FipMode"
    ISCSI_BOOT_SUPPORTED = "IscsiBootSupported"
    MODEL = "Model"
    NUM_OF_VMFEX_IFS = "NumOfVMFexIfs"
    PCI_SLOT = "PciSlot"
    PRODUCT_NAME = "ProductName"
    REVISION = "Revision"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    USNIC_SUPPORTED = "UsnicSupported"
    VENDOR = "Vendor"
    VENDOR_ID = "VendorId"
    VNTAG_MODE = "VntagMode"


class StorageVirtualDriveCreatorUsingVirtualDriveGroup(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageVirtualDriveCreatorUsingVirtualDriveGroup")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageVirtualDriveCreatorUsingVirtualDriveGroup"

    ACCESS_POLICY = "AccessPolicy"
    ADMIN_STATE = "AdminState"
    CACHE_POLICY = "CachePolicy"
    CREATED_VIRTUAL_DRIVE_DN = "CreatedVirtualDriveDn"
    DESCRIPTION = "Description"
    DISK_CACHE_POLICY = "DiskCachePolicy"
    DN = "Dn"
    OPER_STATUS = "OperStatus"
    READ_POLICY = "ReadPolicy"
    RN = "Rn"
    SHARED_VIRTUAL_DRIVE_ID = "SharedVirtualDriveId"
    SIZE = "Size"
    STATUS = "Status"
    STRIP_SIZE = "StripSize"
    VIRTUAL_DRIVE_NAME = "VirtualDriveName"
    WRITE_POLICY = "WritePolicy"

    CONST_ACCESS_POLICY_ = ""
    CONST_ACCESS_POLICY_BLOCKED = "blocked"
    CONST_ACCESS_POLICY_HIDDEN = "hidden"
    CONST_ACCESS_POLICY_READ_ONLY = "read-only"
    CONST_ACCESS_POLICY_READ_WRITE = "read-write"
    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_CACHE_POLICY_ = ""
    CONST_CACHE_POLICY_CACHED_IO = "cached-io"
    CONST_CACHE_POLICY_DIRECT_IO = "direct-io"
    CONST_DISK_CACHE_POLICY_ = ""
    CONST_DISK_CACHE_POLICY_DISABLED = "disabled"
    CONST_DISK_CACHE_POLICY_ENABLED = "enabled"
    CONST_DISK_CACHE_POLICY_UNCHANGED = "unchanged"
    CONST_READ_POLICY_ = ""
    CONST_READ_POLICY_ALWAYS_READ_AHEAD = "always-read-ahead"
    CONST_READ_POLICY_NO_READ_AHEAD = "no-read-ahead"
    CONST_SHARED_VIRTUAL_DRIVE_ID_ = ""
    CONST_STRIP_SIZE_ = ""
    CONST_STRIP_SIZE_1024K = "1024k"
    CONST_STRIP_SIZE_128K = "128k"
    CONST_STRIP_SIZE_16K = "16k"
    CONST_STRIP_SIZE_256K = "256k"
    CONST_STRIP_SIZE_32K = "32k"
    CONST_STRIP_SIZE_512K = "512k"
    CONST_STRIP_SIZE_64K = "64k"
    CONST_STRIP_SIZE_8K = "8k"
    CONST_WRITE_POLICY_ = ""
    CONST_WRITE_POLICY_ALWAYS_WRITE_BACK = "Always Write Back"
    CONST_WRITE_POLICY_WRITE_BACK_GOOD_BBU = "Write Back Good BBU"
    CONST_WRITE_POLICY_WRITE_THROUGH = "Write Through"
    CONST__WRITE_POLICY_ALWAYS_WRITE_BACK = "always-write-back"
    CONST__WRITE_POLICY_WRITE_BACK_GOOD_BBU = "write-back-good-bbu"
    CONST__WRITE_POLICY_WRITE_THROUGH = "write-through"

class EquipmentPsuColdRedundancy(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentPsuColdRedundancy")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentPsuColdRedundancy"

    DN = "Dn"
    ENABLED = "Enabled"
    RN = "Rn"
    STATUS = "Status"


class PciEquipSlot(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PciEquipSlot")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "pciEquipSlot"

    CONTROLLER_REPORTED = "ControllerReported"
    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    RN = "Rn"
    SMBIOS_ID = "SmbiosId"
    STATUS = "Status"
    VENDOR = "Vendor"
    VERSION = "Version"


class CommSyslogClient(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommSyslogClient")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commSyslogClient"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    HOSTNAME = "Hostname"
    NAME = "Name"
    PORT = "Port"
    RN = "Rn"
    STATUS = "Status"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_NAME_PRIMARY = "primary"
    CONST_NAME_SECONDARY = "secondary"
    CONST_NAME_TERTIARY = "tertiary"

class CommSnmpTrap(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommSnmpTrap")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commSnmpTrap"

    ADMIN_STATE = "AdminState"
    COMMUNITY = "Community"
    DN = "Dn"
    HOSTNAME = "Hostname"
    ID = "Id"
    NOTIFICATION_TYPE = "NotificationType"
    PORT = "Port"
    RN = "Rn"
    STATUS = "Status"
    USER = "User"
    VERSION = "Version"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_NOTIFICATION_TYPE_INFORMS = "informs"
    CONST_NOTIFICATION_TYPE_TRAPS = "traps"
    CONST_VERSION_V1 = "v1"
    CONST_VERSION_V2C = "v2c"
    CONST_VERSION_V3 = "v3"

class StorageLocalDiskUsage(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageLocalDiskUsage")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageLocalDiskUsage"

    DN = "Dn"
    NUMBER_OF_BLOCKS = "NumberOfBlocks"
    PHYSICAL_DRIVE = "PhysicalDrive"
    RN = "Rn"
    SPAN = "Span"
    STARTING_BLOCK = "StartingBlock"
    STATE = "State"
    STATUS = "Status"
    VIRTUAL_DRIVE = "VirtualDrive"


class AdaptorIpV6RssHashProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorIpV6RssHashProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorIpV6RssHashProfile"

    DN = "Dn"
    IP_HASH = "IpHash"
    RN = "Rn"
    STATUS = "Status"
    TCP_HASH = "TcpHash"


class BiosBootDevPrecision(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosBootDevPrecision")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosBootDevPrecision"

    DESCR = "Descr"
    DN = "Dn"
    LUN = "Lun"
    NAME = "Name"
    ORDER = "Order"
    PORT = "Port"
    RN = "Rn"
    SLOT = "Slot"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_SUBTYPE_CIMC_MAPPED_DVD = "cimc-mapped-dvd"
    CONST_SUBTYPE_CIMC_MAPPED_HDD = "cimc-mapped-hdd"
    CONST_SUBTYPE_KVM_MAPPED_DVD = "kvm-mapped-dvd"
    CONST_SUBTYPE_KVM_MAPPED_FDD = "kvm-mapped-fdd"
    CONST_SUBTYPE_KVM_MAPPED_HDD = "kvm-mapped-hdd"
    CONST_SUBTYPE_USB_CD = "usb-cd"
    CONST_SUBTYPE_USB_FDD = "usb-fdd"
    CONST_SUBTYPE_USB_HDD = "usb-hdd"
    CONST_TYPE_EFI = "EFI"
    CONST_TYPE_HDD = "HDD"
    CONST_TYPE_ISCSI = "ISCSI"
    CONST_TYPE_PCHSTORAGE = "PCHSTORAGE"
    CONST_TYPE_PXE = "PXE"
    CONST_TYPE_SAN = "SAN"
    CONST_TYPE_SDCARD = "SDCARD"
    CONST_TYPE_USB = "USB"
    CONST_TYPE_VMEDIA = "VMEDIA"

class LsbootLan(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootLan")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootLan"

    ACCESS = "Access"
    DN = "Dn"
    ORDER = "Order"
    PROT = "Prot"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"

    CONST_ACCESS_READ_ONLY = "read-only"
    CONST_PROT_GPXE = "gpxe"
    CONST_PROT_I_SCSI = "iSCSI"
    CONST_PROT_PXE = "pxe"
    CONST_TYPE_LAN = "lan"

class LsbootUefiShell(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootUefiShell")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootUefiShell"

    DN = "Dn"
    NAME = "Name"
    ORDER = "Order"
    RN = "Rn"
    STATE = "State"
    STATUS = "Status"
    TYPE = "Type"

    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_TYPE_UEFISHELL = "UEFISHELL"

class AdaptorEthUSNICProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthUSNICProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthUSNICProfile"

    CLASS_OF_SERVICE = "ClassOfService"
    COALESCING_TIME = "CoalescingTime"
    COALESCING_TYPE = "CoalescingType"
    COMPLETION_QUEUE_COUNT = "CompletionQueueCount"
    DN = "Dn"
    INTERRUPT_COUNT = "InterruptCount"
    LARGE_RECEIVE = "LargeReceive"
    RECEIVE_QUEUE_COUNT = "ReceiveQueueCount"
    RECEIVE_QUEUE_RING_SIZE = "ReceiveQueueRingSize"
    RN = "Rn"
    STATUS = "Status"
    TCP_RX_CHECKSUM = "TcpRxChecksum"
    TCP_SEGMENT = "TcpSegment"
    TCP_TX_CHECKSUM = "TcpTxChecksum"
    TRANSMIT_QUEUE_COUNT = "TransmitQueueCount"
    TRANSMIT_QUEUE_RING_SIZE = "TransmitQueueRingSize"
    USNIC_COUNT = "UsnicCount"

    CONST_COALESCING_TYPE_IDLE = "IDLE"
    CONST_COALESCING_TYPE_MIN = "MIN"

class LsbootLocalStorage(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootLocalStorage")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootLocalStorage"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class EquipmentLocatorLed(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentLocatorLed")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentLocatorLed"

    ADMIN_STATE = "AdminState"
    COLOR = "Color"
    DN = "Dn"
    ID = "Id"
    NAME = "Name"
    OPER_STATE = "OperState"
    RN = "Rn"
    STATUS = "Status"

    CONST_ADMIN_STATE_INACTIVE = "inactive"
    CONST_ADMIN_STATE_OFF = "off"
    CONST_ADMIN_STATE_ON = "on"
    CONST_COLOR_AMBER = "amber"
    CONST_COLOR_BLUE = "blue"
    CONST_COLOR_GREEN = "green"
    CONST_COLOR_RED = "red"
    CONST_COLOR_UNKNOWN = "unknown"
    CONST_OPER_STATE_BLINKING = "blinking"
    CONST_OPER_STATE_ETH = "eth"
    CONST_OPER_STATE_FC = "fc"
    CONST_OPER_STATE_OFF = "off"
    CONST_OPER_STATE_ON = "on"
    CONST_OPER_STATE_UNKNOWN = "unknown"

class HuuFirmwareUpdater(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuFirmwareUpdater")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuFirmwareUpdater"

    ADMIN_STATE = "AdminState"
    CIMC_SECURE_BOOT = "CimcSecureBoot"
    DN = "Dn"
    MAP_TYPE = "MapType"
    PASSWORD = "Password"
    REMOTE_IP = "RemoteIp"
    REMOTE_SHARE = "RemoteShare"
    REMOTE_SHARE_FILE = "RemoteShareFile"
    REMOTE_SHARE_PATH = "RemoteSharePath"
    RN = "Rn"
    STATUS = "Status"
    STOP_ON_ERROR = "StopOnError"
    TIME_OUT = "TimeOut"
    UPDATE_COMPONENT = "UpdateComponent"
    USERNAME = "Username"
    VERIFY_UPDATE = "VerifyUpdate"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_MAP_TYPE_CIFS = "cifs"
    CONST_MAP_TYPE_NFS = "nfs"
    CONST_MAP_TYPE_WWW = "www"

class BiosVfAssertNMIOnPERR(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfAssertNMIOnPERR")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfAssertNMIOnPERR"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ASSERT_NMION_PERR = "VpAssertNMIOnPERR"

    CONST_VP_ASSERT_NMION_PERR_DISABLED = "Disabled"
    CONST_VP_ASSERT_NMION_PERR_ENABLED = "Enabled"
    CONST__VP_ASSERT_NMION_PERR_DISABLED = "disabled"
    CONST__VP_ASSERT_NMION_PERR_ENABLED = "enabled"
    CONST_VP_ASSERT_NMION_PERR_PLATFORM_DEFAULT = "platform-default"

class FirmwareRunning(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "FirmwareRunning")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "firmwareRunning"

    DEPLOYMENT = "Deployment"
    DESCRIPTION = "Description"
    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"
    VERSION = "Version"

    CONST_DEPLOYMENT_BOOT_LOADER = "boot-loader"
    CONST_DEPLOYMENT_KERNEL = "kernel"
    CONST_DEPLOYMENT_SYSTEM = "system"
    CONST_DEPLOYMENT_UNSPECIFIED = "unspecified"
    CONST_TYPE_ADAPTOR = "adaptor"
    CONST_TYPE_BLADE_BIOS = "blade-bios"
    CONST_TYPE_BLADE_CONTROLLER = "blade-controller"
    CONST_TYPE_SIOC = "sioc"
    CONST_TYPE_STORAGE_CONTROLLER = "storage-controller"
    CONST_TYPE_SYSTEM = "system"
    CONST_TYPE_UNSPECIFIED = "unspecified"

class PidCatalogHdd(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PidCatalogHdd")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "pidCatalogHdd"

    CONTROLLER = "Controller"
    DESCRIPTION = "Description"
    DISK = "Disk"
    DN = "Dn"
    MODEL = "Model"
    PID = "Pid"
    RN = "Rn"
    SERIALNUMBER = "Serialnumber"
    STATUS = "Status"
    VENDOR = "Vendor"


class BiosVfASPMSupport(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfASPMSupport")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfASPMSupport"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ASPMSUPPORT = "VpASPMSupport"

    CONST_VP_ASPMSUPPORT_AUTO = "Auto"
    CONST_VP_ASPMSUPPORT_DISABLED = "Disabled"
    CONST_VP_ASPMSUPPORT_FORCE_L0S = "Force L0s"
    CONST_VP_ASPMSUPPORT_PLATFORM_DEFAULT = "platform-default"

class AdaptorVMFexEthIf(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorVMFexEthIf")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorVMFexEthIf"

    CLASS_OF_SERVICE = "ClassOfService"
    DN = "Dn"
    IF_TYPE = "IfType"
    MTU = "Mtu"
    NAME = "Name"
    PXE_BOOT = "PxeBoot"
    RN = "Rn"
    STATUS = "Status"
    UPLINK_FAILBACK_TIMEOUT = "UplinkFailbackTimeout"
    UPLINK_FAILOVER = "UplinkFailover"
    UPLINK_PORT = "UplinkPort"
    VLAN = "Vlan"
    VLAN_MODE = "VlanMode"

    CONST_IF_TYPE_VIRTUAL = "virtual"
    CONST_UPLINK_FAILOVER_DISABLED = "Disabled"
    CONST_UPLINK_FAILOVER_ENABLED = "Enabled"
    CONST__UPLINK_FAILOVER_DISABLED = "disabled"
    CONST__UPLINK_FAILOVER_ENABLED = "enabled"
    CONST_UPLINK_PORT_0 = "0"
    CONST_UPLINK_PORT_1 = "1"

class AdaptorExtIpV6RssHashProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorExtIpV6RssHashProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorExtIpV6RssHashProfile"

    DN = "Dn"
    IP_HASH = "IpHash"
    RN = "Rn"
    STATUS = "Status"
    TCP_HASH = "TcpHash"


class BiosVfMemoryInterleave(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfMemoryInterleave")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfMemoryInterleave"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_CHANNEL_INTER_LEAVE = "VpChannelInterLeave"
    VP_MEMORY_INTER_LEAVE = "VpMemoryInterLeave"
    VP_RANK_INTER_LEAVE = "VpRankInterLeave"

    CONST_VP_CHANNEL_INTER_LEAVE_1_WAY = "1-way"
    CONST_VP_CHANNEL_INTER_LEAVE_2_WAY = "2-way"
    CONST_VP_CHANNEL_INTER_LEAVE_3_WAY = "3-way"
    CONST_VP_CHANNEL_INTER_LEAVE_4_WAY = "4-way"
    CONST_VP_CHANNEL_INTER_LEAVE_AUTO = "auto"
    CONST_VP_CHANNEL_INTER_LEAVE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_MEMORY_INTER_LEAVE_1_WAY_NODE_INTERLEAVE = "1 Way Node Interleave"
    CONST_VP_MEMORY_INTER_LEAVE_2_WAY_NODE_INTERLEAVE = "2 Way Node Interleave"
    CONST_VP_MEMORY_INTER_LEAVE_4_WAY_NODE_INTERLEAVE = "4 Way Node Interleave"
    CONST_VP_MEMORY_INTER_LEAVE_8_WAY_NODE_INTERLEAVE = "8 Way Node Interleave"
    CONST_VP_MEMORY_INTER_LEAVE_DISABLED = "Disabled"
    CONST_VP_MEMORY_INTER_LEAVE_ENABLED = "Enabled"
    CONST__VP_MEMORY_INTER_LEAVE_DISABLED = "disabled"
    CONST__VP_MEMORY_INTER_LEAVE_ENABLED = "enabled"
    CONST_VP_MEMORY_INTER_LEAVE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_RANK_INTER_LEAVE_1_WAY = "1-way"
    CONST_VP_RANK_INTER_LEAVE_2_WAY = "2-way"
    CONST_VP_RANK_INTER_LEAVE_4_WAY = "4-way"
    CONST_VP_RANK_INTER_LEAVE_8_WAY = "8-way"
    CONST_VP_RANK_INTER_LEAVE_AUTO = "auto"
    CONST_VP_RANK_INTER_LEAVE_PLATFORM_DEFAULT = "platform-default"

class BiosVfConsoleRedirection(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfConsoleRedirection")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfConsoleRedirection"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_BAUD_RATE = "VpBaudRate"
    VP_CONSOLE_REDIRECTION = "VpConsoleRedirection"
    VP_FLOW_CONTROL = "VpFlowControl"
    VP_LEGACY_OSREDIRECTION = "VpLegacyOSRedirection"
    VP_PUTTY_KEY_PAD = "VpPuttyKeyPad"
    VP_REDIRECTION_AFTER_POST = "VpRedirectionAfterPOST"
    VP_TERMINAL_TYPE = "VpTerminalType"

    CONST_VP_BAUD_RATE_115200 = "115200"
    CONST_VP_BAUD_RATE_19200 = "19200"
    CONST_VP_BAUD_RATE_38400 = "38400"
    CONST_VP_BAUD_RATE_57600 = "57600"
    CONST_VP_BAUD_RATE_9600 = "9600"
    CONST_VP_BAUD_RATE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_CONSOLE_REDIRECTION_COM_0 = "com-0"
    CONST_VP_CONSOLE_REDIRECTION_COM_1 = "com-1"
    CONST_VP_CONSOLE_REDIRECTION_DISABLED = "disabled"
    CONST_VP_CONSOLE_REDIRECTION_ENABLED = "enabled"
    CONST_VP_CONSOLE_REDIRECTION_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_CONSOLE_REDIRECTION_SERIAL_PORT_A = "serial-port-a"
    CONST_VP_FLOW_CONTROL_NONE = "none"
    CONST_VP_FLOW_CONTROL_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_FLOW_CONTROL_RTS_CTS = "rts-cts"
    CONST_VP_LEGACY_OSREDIRECTION_DISABLED = "Disabled"
    CONST_VP_LEGACY_OSREDIRECTION_ENABLED = "Enabled"
    CONST__VP_LEGACY_OSREDIRECTION_DISABLED = "disabled"
    CONST__VP_LEGACY_OSREDIRECTION_ENABLED = "enabled"
    CONST_VP_LEGACY_OSREDIRECTION_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_PUTTY_KEY_PAD_ESCN = "ESCN"
    CONST_VP_PUTTY_KEY_PAD_LINUX = "LINUX"
    CONST_VP_PUTTY_KEY_PAD_SCO = "SCO"
    CONST_VP_PUTTY_KEY_PAD_VT100 = "VT100"
    CONST_VP_PUTTY_KEY_PAD_VT400 = "VT400"
    CONST_VP_PUTTY_KEY_PAD_XTERMR6 = "XTERMR6"
    CONST_VP_PUTTY_KEY_PAD_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_REDIRECTION_AFTER_POST_ALWAYS_ENABLE = "Always Enable"
    CONST_VP_REDIRECTION_AFTER_POST_BOOTLOADER = "Bootloader"
    CONST_VP_REDIRECTION_AFTER_POST_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_TERMINAL_TYPE_PC_ANSI = "pc-ansi"
    CONST_VP_TERMINAL_TYPE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_TERMINAL_TYPE_VT_UTF8 = "vt-utf8"
    CONST_VP_TERMINAL_TYPE_VT100 = "vt100"
    CONST_VP_TERMINAL_TYPE_VT100_PLUS = "vt100-plus"

class HuuFirmwareRunning(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuFirmwareRunning")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuFirmwareRunning"

    CURRENT_TIME = "CurrentTime"
    DESCRIPTION = "Description"
    DN = "Dn"
    LAST_QUERIED_TIME_STAMP = "LastQueriedTimeStamp"
    RN = "Rn"
    STATUS = "Status"


class StorageFlexFlashVirtualDrive(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageFlexFlashVirtualDrive")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageFlexFlashVirtualDrive"

    ADMIN_ACTION = "AdminAction"
    DN = "Dn"
    DRIVE_SCOPE = "DriveScope"
    DRIVE_STATUS = "DriveStatus"
    DRIVE_TYPE = "DriveType"
    HOST_ACCESSIBLE = "HostAccessible"
    LAST_OPERATION_STATUS = "LastOperationStatus"
    OPERATION_IN_PROGRESS = "OperationInProgress"
    PARTITION_ID = "PartitionId"
    RN = "Rn"
    SIZE = "Size"
    STATUS = "Status"
    VIRTUAL_DRIVE = "VirtualDrive"

    CONST_ADMIN_ACTION_DISABLE_VD = "disable-vd"
    CONST_ADMIN_ACTION_ENABLE_VD = "enable-vd"
    CONST_ADMIN_ACTION_ERASE_VD = "erase-vd"
    CONST_ADMIN_ACTION_SYNC_VD = "sync-vd"
    CONST_ADMIN_ACTION_UPDATE_VD = "update-vd"

class BiosPlatformDefaults(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosPlatformDefaults")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosPlatformDefaults"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class AdaptorVMFexEthProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorVMFexEthProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorVMFexEthProfile"

    COALESCING_TIME = "CoalescingTime"
    COALESCING_TYPE = "CoalescingType"
    COMPLETION_QUEUE_COUNT = "CompletionQueueCount"
    COMPLETION_QUEUE_RING_SIZE = "CompletionQueueRingSize"
    DN = "Dn"
    INTERRUPT_COUNT = "InterruptCount"
    INTERRUPT_MODE = "InterruptMode"
    LARGE_RECEIVE = "LargeReceive"
    NAME = "Name"
    PCI_ORDER = "PciOrder"
    RECEIVE_QUEUE_COUNT = "ReceiveQueueCount"
    RECEIVE_QUEUE_RING_SIZE = "ReceiveQueueRingSize"
    RECEIVE_SIDE_SCALING = "ReceiveSideScaling"
    RECEIVE_SIDE_SCALING_EXT_IP_V6_HASH = "ReceiveSideScalingExtIpV6Hash"
    RECEIVE_SIDE_SCALING_EXT_TCPIP_V6_HASH = "ReceiveSideScalingExtTCPIpV6Hash"
    RECEIVE_SIDE_SCALING_IP_V4_HASH = "ReceiveSideScalingIpV4Hash"
    RECEIVE_SIDE_SCALING_IP_V6_HASH = "ReceiveSideScalingIpV6Hash"
    RECEIVE_SIDE_SCALING_TCPIP_V4_HASH = "ReceiveSideScalingTCPIpV4Hash"
    RECEIVE_SIDE_SCALING_TCPIP_V6_HASH = "ReceiveSideScalingTCPIpV6Hash"
    RN = "Rn"
    STATUS = "Status"
    TCP_RX_CHECKSUM = "TcpRxChecksum"
    TCP_SEGMENT = "TcpSegment"
    TCP_TX_CHECKSUM = "TcpTxChecksum"
    TRANSMIT_QUEUE_COUNT = "TransmitQueueCount"
    TRANSMIT_QUEUE_RING_SIZE = "TransmitQueueRingSize"
    TRUSTED_CLASS_OF_SERVICE = "TrustedClassOfService"


class BiosVfSparingMode(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfSparingMode")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfSparingMode"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_SPARING_MODE = "VpSparingMode"

    CONST_VP_SPARING_MODE_DIMM_SPARING = "dimm-sparing"
    CONST_VP_SPARING_MODE_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SPARING_MODE_RANK_SPARING = "rank-sparing"

class BiosVfDRAMClockThrottling(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfDRAMClockThrottling")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfDRAMClockThrottling"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_DRAMCLOCK_THROTTLING = "VpDRAMClockThrottling"

    CONST_VP_DRAMCLOCK_THROTTLING_AUTO = "Auto"
    CONST_VP_DRAMCLOCK_THROTTLING_BALANCED = "Balanced"
    CONST_VP_DRAMCLOCK_THROTTLING_ENERGY_EFFICIENT = "Energy Efficient"
    CONST_VP_DRAMCLOCK_THROTTLING_PERFORMANCE = "Performance"
    CONST_VP_DRAMCLOCK_THROTTLING_PLATFORM_DEFAULT = "platform-default"

class BiosVfIntelVirtualizationTechnology(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfIntelVirtualizationTechnology")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfIntelVirtualizationTechnology"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_INTEL_VIRTUALIZATION_TECHNOLOGY = "VpIntelVirtualizationTechnology"

    CONST_VP_INTEL_VIRTUALIZATION_TECHNOLOGY_DISABLED = "Disabled"
    CONST_VP_INTEL_VIRTUALIZATION_TECHNOLOGY_ENABLED = "Enabled"
    CONST__VP_INTEL_VIRTUALIZATION_TECHNOLOGY_DISABLED = "disabled"
    CONST__VP_INTEL_VIRTUALIZATION_TECHNOLOGY_ENABLED = "enabled"
    CONST_VP_INTEL_VIRTUALIZATION_TECHNOLOGY_PLATFORM_DEFAULT = "platform-default"

class EquipmentPsu(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentPsu")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentPsu"

    DN = "Dn"
    FW_VERSION = "FwVersion"
    ID = "Id"
    INPUT = "Input"
    MAX_OUTPUT = "MaxOutput"
    MODEL = "Model"
    OPERABILITY = "Operability"
    POWER = "Power"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    THERMAL = "Thermal"
    VENDOR = "Vendor"
    VOLTAGE = "Voltage"

    CONST_OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPERABILITY_CONFIG = "config"
    CONST_OPERABILITY_DECOMISSIONING = "decomissioning"
    CONST_OPERABILITY_DEGRADED = "degraded"
    CONST_OPERABILITY_DISABLED = "disabled"
    CONST_OPERABILITY_DISCOVERY = "discovery"
    CONST_OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPERABILITY_IDENTIFY = "identify"
    CONST_OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPERABILITY_INOPERABLE = "inoperable"
    CONST_OPERABILITY_MALFORMED_FRU = "malformed-fru"
    CONST_OPERABILITY_NOT_SUPPORTED = "not-supported"
    CONST_OPERABILITY_OPERABLE = "operable"
    CONST_OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPERABILITY_POST_FAILURE = "post-failure"
    CONST_OPERABILITY_POWER_PROBLEM = "power-problem"
    CONST_OPERABILITY_POWERED_OFF = "powered-off"
    CONST_OPERABILITY_REMOVED = "removed"
    CONST_OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPERABILITY_UNKNOWN = "unknown"
    CONST_OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_POWER_DEGRADED = "degraded"
    CONST_POWER_ERROR = "error"
    CONST_POWER_NOT_SUPPORTED = "not-supported"
    CONST_POWER_OFF = "off"
    CONST_POWER_OFFDUTY = "offduty"
    CONST_POWER_OFFLINE = "offline"
    CONST_POWER_ON = "on"
    CONST_POWER_ONLINE = "online"
    CONST_POWER_POWER_SAVE = "power-save"
    CONST_POWER_TEST = "test"
    CONST_POWER_UNKNOWN = "unknown"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"
    CONST_THERMAL_LOWER_CRITICAL = "lower-critical"
    CONST_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_THERMAL_NOT_SUPPORTED = "not-supported"
    CONST_THERMAL_OK = "ok"
    CONST_THERMAL_UNKNOWN = "unknown"
    CONST_THERMAL_UPPER_CRITICAL = "upper-critical"
    CONST_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    CONST_VOLTAGE_LOWER_CRITICAL = "lower-critical"
    CONST_VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_VOLTAGE_NOT_SUPPORTED = "not-supported"
    CONST_VOLTAGE_OK = "ok"
    CONST_VOLTAGE_UNKNOWN = "unknown"
    CONST_VOLTAGE_UPPER_CRITICAL = "upper-critical"
    CONST_VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"

class PidCatalogPCIAdapter(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PidCatalogPCIAdapter")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "pidCatalogPCIAdapter"

    DESCRIPTION = "Description"
    DEVICE = "Device"
    DN = "Dn"
    PID = "Pid"
    RN = "Rn"
    SLOT = "Slot"
    STATUS = "Status"
    SUBDEVICE = "Subdevice"
    SUBVENDOR = "Subvendor"
    VENDOR = "Vendor"


class StorageLocalDiskProps(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageLocalDiskProps")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageLocalDiskProps"

    BLOCK_COUNT = "BlockCount"
    BLOCK_SIZE = "BlockSize"
    BOOT_DRIVE = "BootDrive"
    COERCED_SIZE = "CoercedSize"
    DEVICE_ID = "DeviceId"
    DN = "Dn"
    ENCLOSURE_DEVICE_ID = "EnclosureDeviceId"
    HEALTH = "Health"
    INTERFACE_TYPE = "InterfaceType"
    LINK_SPEED = "LinkSpeed"
    MEDIA_ERROR_COUNT = "MediaErrorCount"
    MEDIA_TYPE = "MediaType"
    NON_COERCED_SIZE = "NonCoercedSize"
    OTHER_ERROR_COUNT = "OtherErrorCount"
    PD_STATUS = "PdStatus"
    PHYSICAL_DRIVE = "PhysicalDrive"
    POWER_STATE = "PowerState"
    PREDICTIVE_FAILURE_COUNT = "PredictiveFailureCount"
    RAW_SIZE = "RawSize"
    RN = "Rn"
    SAS_ADDRESS0 = "SasAddress0"
    SAS_ADDRESS1 = "SasAddress1"
    SEQUENCE_NUMBER = "SequenceNumber"
    STATUS = "Status"


class BiosVfUSBBootConfig(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfUSBBootConfig")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfUSBBootConfig"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_MAKE_DEVICE_NON_BOOTABLE = "VpMakeDeviceNonBootable"

    CONST_VP_MAKE_DEVICE_NON_BOOTABLE_DISABLED = "Disabled"
    CONST_VP_MAKE_DEVICE_NON_BOOTABLE_ENABLED = "Enabled"
    CONST__VP_MAKE_DEVICE_NON_BOOTABLE_DISABLED = "disabled"
    CONST__VP_MAKE_DEVICE_NON_BOOTABLE_ENABLED = "enabled"
    CONST_VP_MAKE_DEVICE_NON_BOOTABLE_PLATFORM_DEFAULT = "platform-default"

class ProcessorUnit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "ProcessorUnit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "processorUnit"

    ARCH = "Arch"
    CORES = "Cores"
    CORES_ENABLED = "CoresEnabled"
    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    OPER_STATE = "OperState"
    PRESENCE = "Presence"
    RN = "Rn"
    SOCKET_DESIGNATION = "SocketDesignation"
    SPEED = "Speed"
    STATUS = "Status"
    STEPPING = "Stepping"
    THREADS = "Threads"
    VENDOR = "Vendor"

    CONST_ARCH_DUAL_CORE_OPTERON = "Dual-Core_Opteron"
    CONST_ARCH_INTEL_P4_C = "Intel_P4_C"
    CONST_ARCH_OPTERON = "Opteron"
    CONST_ARCH_PENTIUM__4 = "Pentium_4"
    CONST_ARCH_TURION__64 = "Turion_64"
    CONST_ARCH_XEON = "Xeon"
    CONST_ARCH_XEON_MP = "Xeon_MP"
    CONST_ARCH_ANY = "any"
    CONST_CORES_UNSPECIFIED = "unspecified"
    CONST_CORES_ENABLED_UNSPECIFIED = "unspecified"
    CONST_OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPER_STATE_CONFIG = "config"
    CONST_OPER_STATE_DECOMISSIONING = "decomissioning"
    CONST_OPER_STATE_DEGRADED = "degraded"
    CONST_OPER_STATE_DISABLED = "disabled"
    CONST_OPER_STATE_DISCOVERY = "discovery"
    CONST_OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPER_STATE_IDENTIFY = "identify"
    CONST_OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPER_STATE_INOPERABLE = "inoperable"
    CONST_OPER_STATE_MALFORMED_FRU = "malformed-fru"
    CONST_OPER_STATE_NOT_SUPPORTED = "not-supported"
    CONST_OPER_STATE_OPERABLE = "operable"
    CONST_OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPER_STATE_POST_FAILURE = "post-failure"
    CONST_OPER_STATE_POWER_PROBLEM = "power-problem"
    CONST_OPER_STATE_POWERED_OFF = "powered-off"
    CONST_OPER_STATE_REMOVED = "removed"
    CONST_OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPER_STATE_UNKNOWN = "unknown"
    CONST_OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"
    CONST_SPEED_UNSPECIFIED = "unspecified"
    CONST_STEPPING_UNSPECIFIED = "unspecified"
    CONST_THREADS_UNSPECIFIED = "unspecified"

class PowerMonitor(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "PowerMonitor")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "powerMonitor"

    AVERAGE = "Average"
    CURRENT = "Current"
    DN = "Dn"
    DOMAIN = "Domain"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    RN = "Rn"
    STATUS = "Status"

    CONST_DOMAIN_CPU = "CPU"
    CONST_DOMAIN_MEMORY = "Memory"
    CONST_DOMAIN_PLATFORM = "Platform"

class CommIpmiLan(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommIpmiLan")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commIpmiLan"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    KEY = "Key"
    PRIV = "Priv"
    RN = "Rn"
    STATUS = "Status"

    CONST_PRIV_ADMIN = "admin"
    CONST_PRIV_READ_ONLY = "read-only"
    CONST_PRIV_USER = "user"

class Error(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "Error")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "error"

    COOKIE = "Cookie"
    ERROR_CODE = "ErrorCode"
    ERROR_DESCR = "ErrorDescr"
    INVOCATION_RESULT = "InvocationResult"
    RESPONSE = "Response"


class BiosVfWorkLoadConfig(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfWorkLoadConfig")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfWorkLoadConfig"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_WORK_LOAD_CONFIG = "VpWorkLoadConfig"

    CONST_VP_WORK_LOAD_CONFIG_BALANCED = "Balanced"
    CONST_VP_WORK_LOAD_CONFIG_I_O_SENSITIVE = "I/O Sensitive"
    CONST_VP_WORK_LOAD_CONFIG_PLATFORM_DEFAULT = "platform-default"

class BiosVfOSBootWatchdogTimerPolicy(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfOSBootWatchdogTimerPolicy")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfOSBootWatchdogTimerPolicy"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_OSBOOT_WATCHDOG_TIMER_POLICY = "VpOSBootWatchdogTimerPolicy"

    CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_DO_NOTHING = "do-nothing"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_POWER_OFF = "power-off"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_POLICY_RESET = "reset"

class BiosSettings(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosSettings")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosSettings"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class StorageUnusedLocalDisk(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageUnusedLocalDisk")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageUnusedLocalDisk"

    COERCED_SIZE = "CoercedSize"
    DN = "Dn"
    HEALTH = "Health"
    ID = "Id"
    MEDIA_TYPE = "MediaType"
    PD_STATUS = "PdStatus"
    RN = "Rn"
    STATUS = "Status"
    VENDOR = "Vendor"


class HuuFirmwareUpdateCancel(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuFirmwareUpdateCancel")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuFirmwareUpdateCancel"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"

class FaultInst(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "FaultInst")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "faultInst"

    ACK = "Ack"
    AFFECTED_DN = "AffectedDN"
    CAUSE = "Cause"
    CHANGE_SET = "ChangeSet"
    CODE = "Code"
    CREATED = "Created"
    DESCR = "Descr"
    DN = "Dn"
    HIGHEST_SEVERITY = "HighestSeverity"
    ID = "Id"
    LAST_TRANSITION = "LastTransition"
    LC = "Lc"
    OCCUR = "Occur"
    ORIG_SEVERITY = "OrigSeverity"
    PREV_SEVERITY = "PrevSeverity"
    RN = "Rn"
    RULE = "Rule"
    SEVERITY = "Severity"
    STATUS = "Status"
    TAGS = "Tags"
    TYPE = "Type"

    CONST_ACK_FALSE = "false"
    CONST_ACK_NO = "no"
    CONST_ACK_TRUE = "true"
    CONST_ACK_YES = "yes"
    CONST_HIGHEST_SEVERITY_CLEARED = "cleared"
    CONST_HIGHEST_SEVERITY_CONDITION = "condition"
    CONST_HIGHEST_SEVERITY_CRITICAL = "critical"
    CONST_HIGHEST_SEVERITY_INFO = "info"
    CONST_HIGHEST_SEVERITY_MAJOR = "major"
    CONST_HIGHEST_SEVERITY_MINOR = "minor"
    CONST_HIGHEST_SEVERITY_WARNING = "warning"
    CONST_ORIG_SEVERITY_CLEARED = "cleared"
    CONST_ORIG_SEVERITY_CONDITION = "condition"
    CONST_ORIG_SEVERITY_CRITICAL = "critical"
    CONST_ORIG_SEVERITY_INFO = "info"
    CONST_ORIG_SEVERITY_MAJOR = "major"
    CONST_ORIG_SEVERITY_MINOR = "minor"
    CONST_ORIG_SEVERITY_WARNING = "warning"
    CONST_PREV_SEVERITY_CLEARED = "cleared"
    CONST_PREV_SEVERITY_CONDITION = "condition"
    CONST_PREV_SEVERITY_CRITICAL = "critical"
    CONST_PREV_SEVERITY_INFO = "info"
    CONST_PREV_SEVERITY_MAJOR = "major"
    CONST_PREV_SEVERITY_MINOR = "minor"
    CONST_PREV_SEVERITY_WARNING = "warning"
    CONST_SEVERITY_CLEARED = "cleared"
    CONST_SEVERITY_CONDITION = "condition"
    CONST_SEVERITY_CRITICAL = "critical"
    CONST_SEVERITY_INFO = "info"
    CONST_SEVERITY_MAJOR = "major"
    CONST_SEVERITY_MINOR = "minor"
    CONST_SEVERITY_WARNING = "warning"
    CONST_TYPE_CONFIGURATION = "configuration"
    CONST_TYPE_CONNECTIVITY = "connectivity"
    CONST_TYPE_ENVIRONMENTAL = "environmental"
    CONST_TYPE_EQUIPMENT = "equipment"
    CONST_TYPE_FSM = "fsm"
    CONST_TYPE_GENERIC = "generic"
    CONST_TYPE_MANAGEMENT = "management"
    CONST_TYPE_NETWORK = "network"
    CONST_TYPE_OPERATIONAL = "operational"
    CONST_TYPE_SERVER = "server"
    CONST_TYPE_SYSDEBUG = "sysdebug"

class BiosVfPciRomClp(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPciRomClp")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPciRomClp"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PCI_ROM_CLP = "VpPciRomClp"

    CONST_VP_PCI_ROM_CLP_DISABLED = "Disabled"
    CONST_VP_PCI_ROM_CLP_ENABLED = "Enabled"
    CONST__VP_PCI_ROM_CLP_DISABLED = "disabled"
    CONST__VP_PCI_ROM_CLP_ENABLED = "enabled"
    CONST_VP_PCI_ROM_CLP_PLATFORM_DEFAULT = "platform-default"

class StorageFlexFlashOperationalProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageFlexFlashOperationalProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageFlexFlashOperationalProfile"

    ADMIN_ACTION = "AdminAction"
    CONTROLLER = "Controller"
    DN = "Dn"
    IO_READ_ERROR_THRESHOLD = "IoReadErrorThreshold"
    IO_WRITE_ERROR_THRESHOLD = "IoWriteErrorThreshold"
    OPERATING_MODE = "OperatingMode"
    RAID_PRIMARY_MEMBER = "RaidPrimaryMember"
    RAID_SECONDARY_ROLE = "RaidSecondaryRole"
    RD_ERR_COUNT_SLOT1_THRESHOLD = "RdErrCountSlot1Threshold"
    RD_ERR_COUNT_SLOT2_THRESHOLD = "RdErrCountSlot2Threshold"
    RN = "Rn"
    STATUS = "Status"
    VIRTUAL_DRIVES_ENABLED = "VirtualDrivesEnabled"
    WR_ERR_COUNT_SLOT1_THRESHOLD = "WrErrCountSlot1Threshold"
    WR_ERR_COUNT_SLOT2_THRESHOLD = "WrErrCountSlot2Threshold"

    CONST_ADMIN_ACTION_CLEAR_ERRORS = "clear-errors"
    CONST_RAID_PRIMARY_MEMBER_SLOT_1 = "slot-1"
    CONST_RAID_PRIMARY_MEMBER_SLOT_2 = "slot-2"
    CONST_RAID_SECONDARY_ROLE_ACTIVE = "active"
    CONST_RAID_SECONDARY_ROLE_INITIALIZING = "initializing"

class AdaptorRssProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorRssProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorRssProfile"

    DN = "Dn"
    RECEIVE_SIDE_SCALING = "ReceiveSideScaling"
    RN = "Rn"
    STATUS = "Status"


class AdvancedPowerProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdvancedPowerProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "advancedPowerProfile"

    ALLOW_THROTTLE = "AllowThrottle"
    CORR_ACTION = "CorrAction"
    CORR_TIME = "CorrTime"
    CPU_POWER_LIMIT = "CpuPowerLimit"
    CPU_SAFE_THROT_LVL = "CpuSafeThrotLvl"
    DN = "Dn"
    HARD_CAP = "HardCap"
    MEM_SAFE_THROT_LVL = "MemSafeThrotLvl"
    MEMORY_POWER_LIMIT = "MemoryPowerLimit"
    MISS_RDG_TIMEOUT = "MissRdgTimeout"
    PLAT_SAFE_THROT_LVL = "PlatSafeThrotLvl"
    PLATFORM_THERMAL = "PlatformThermal"
    POWER_LIMIT = "PowerLimit"
    PROFILE_ENABLED = "ProfileEnabled"
    PROFILE_TYPE = "ProfileType"
    RN = "Rn"
    STATUS = "Status"
    SUSPEND_PERIOD = "SuspendPeriod"
    THERMAL_POW_LIMIT = "ThermalPowLimit"

    CONST_CORR_ACTION_ALERT = "alert"
    CONST_CORR_ACTION_ALERT_SHUTDOWN = "alert,shutdown"
    CONST_CORR_ACTION_NONE = "none"
    CONST_CORR_ACTION_SHUTDOWN = "shutdown"

class CommSnmp(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "CommSnmp")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "commSnmp"

    ADMIN_STATE = "AdminState"
    COM2_SEC = "Com2Sec"
    COMMUNITY = "Community"
    DESCR = "Descr"
    DN = "Dn"
    NAME = "Name"
    PORT = "Port"
    PROTO = "Proto"
    RN = "Rn"
    STATUS = "Status"
    SYS_CONTACT = "SysContact"
    SYS_LOCATION = "SysLocation"
    TRAP_COMMUNITY = "TrapCommunity"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_COM2_SEC_NONE = "None"
    CONST_COM2_SEC_DISABLED = "disabled"
    CONST_COM2_SEC_FULL = "full"
    CONST_COM2_SEC_LIMITED = "limited"
    CONST_PROTO_ALL = "all"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_TCP = "tcp"
    CONST_PROTO_UDP = "udp"

class HuuUpdateComponentStatus(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuUpdateComponentStatus")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuUpdateComponentStatus"

    CNTRL_ID = "CntrlId"
    COMPONENT = "Component"
    DESCRIPTION = "Description"
    DEVICE_ID = "DeviceId"
    DN = "Dn"
    ERROR_DESCRIPTION = "ErrorDescription"
    ID = "Id"
    MAC_ADDR = "MacAddr"
    NEW_VERSION = "NewVersion"
    RN = "Rn"
    RUNNING_VERSION = "RunningVersion"
    SLOT = "Slot"
    STATUS = "Status"
    SUB_DEVICE_ID = "SubDeviceId"
    SUB_VENDOR_ID = "SubVendorId"
    UPDATE_STATUS = "UpdateStatus"
    VENDOR_ID = "VendorId"
    VERIFY_STATUS = "VerifyStatus"


class BiosPassword(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosPassword")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosPassword"

    DN = "Dn"
    PASSWORD = "Password"
    RN = "Rn"
    STATUS = "Status"


class BiosBootDevGrp(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosBootDevGrp")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosBootDevGrp"

    DESCR = "Descr"
    DN = "Dn"
    ORDER = "Order"
    RN = "Rn"
    STATUS = "Status"
    TYPE = "Type"

    CONST_TYPE_BEV_ORDER = "bev-order"
    CONST_TYPE_CD_ORDER = "cd-order"
    CONST_TYPE_FDD_ORDER = "fdd-order"
    CONST_TYPE_HDD_ORDER = "hdd-order"
    CONST_TYPE_INTERNAL_EFI_SHELL = "internal-efi-shell"
    CONST_TYPE_NETWORK_DEVICE_ORDER = "network-device-order"
    CONST_TYPE_SYSTEM_BOOT_ORDER = "system-boot-order"

class SystemIOController(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "SystemIOController")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "systemIOController"

    DESCRIPTION = "Description"
    DN = "Dn"
    ID = "Id"
    RN = "Rn"
    STATUS = "Status"


class BiosVfMMCFGBase(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfMMCFGBase")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfMMCFGBase"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_MMCFGBASE = "VpMMCFGBase"

    CONST_VP_MMCFGBASE_1_GB = "1 GB"
    CONST_VP_MMCFGBASE_2_GB = "2 GB"
    CONST_VP_MMCFGBASE_2_5_GB = "2.5 GB"
    CONST_VP_MMCFGBASE_3_GB = "3 GB"
    CONST_VP_MMCFGBASE_AUTO = "Auto"
    CONST_VP_MMCFGBASE_PLATFORM_DEFAULT = "platform-default"

class AaaUserEp(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AaaUserEp")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "aaaUserEp"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class NetworkAdapterEthIf(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "NetworkAdapterEthIf")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "networkAdapterEthIf"

    DN = "Dn"
    ID = "Id"
    MAC = "Mac"
    RN = "Rn"
    STATUS = "Status"


class FirmwareUpdatable(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "FirmwareUpdatable")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "firmwareUpdatable"

    ADMIN_STATE = "AdminState"
    DEPLOYMENT = "Deployment"
    DESCRIPTION = "Description"
    DN = "Dn"
    OPER_STATE = "OperState"
    PROGRESS = "Progress"
    PROTOCOL = "Protocol"
    PWD = "Pwd"
    REMOTE_PATH = "RemotePath"
    REMOTE_SERVER = "RemoteServer"
    RN = "Rn"
    SECURE_BOOT = "SecureBoot"
    STATUS = "Status"
    TYPE = "Type"
    USER = "User"
    VERSION = "Version"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_DEPLOYMENT_BACKUP = "backup"
    CONST_DEPLOYMENT_PRIMARY = "primary"
    CONST_OPER_STATE_ACTIVATING = "activating"
    CONST_OPER_STATE_BAD_IMAGE = "bad-image"
    CONST_OPER_STATE_FAILED = "failed"
    CONST_OPER_STATE_PENDING_NEXT_BOOT = "pending-next-boot"
    CONST_OPER_STATE_READY = "ready"
    CONST_OPER_STATE_REBOOTING = "rebooting"
    CONST_OPER_STATE_SCHEDULED = "scheduled"
    CONST_OPER_STATE_SET_STARTUP = "set-startup"
    CONST_OPER_STATE_THROTTLED = "throttled"
    CONST_OPER_STATE_UPDATING = "updating"
    CONST_OPER_STATE_UPGRADING = "upgrading"
    CONST_PROTOCOL_FTP = "ftp"
    CONST_PROTOCOL_HTTP = "http"
    CONST_PROTOCOL_NONE = "none"
    CONST_PROTOCOL_SCP = "scp"
    CONST_PROTOCOL_SFTP = "sftp"
    CONST_PROTOCOL_TFTP = "tftp"
    CONST_SECURE_BOOT_DISABLE = "disable"
    CONST_SECURE_BOOT_DISABLED = "disabled"
    CONST_SECURE_BOOT_ENABLE = "enable"
    CONST_SECURE_BOOT_ENABLED = "enabled"
    CONST_TYPE_ADAPTOR = "adaptor"
    CONST_TYPE_BLADE_BIOS = "blade-bios"
    CONST_TYPE_BLADE_CONTROLLER = "blade-controller"
    CONST_TYPE_SIOC = "sioc"

class BiosVfSelectMemoryRASConfiguration(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfSelectMemoryRASConfiguration")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfSelectMemoryRASConfiguration"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_SELECT_MEMORY_RASCONFIGURATION = "VpSelectMemoryRASConfiguration"

    CONST_VP_SELECT_MEMORY_RASCONFIGURATION_LOCKSTEP = "lockstep"
    CONST_VP_SELECT_MEMORY_RASCONFIGURATION_MAXIMUM_PERFORMANCE = "maximum-performance"
    CONST_VP_SELECT_MEMORY_RASCONFIGURATION_MIRRORING = "mirroring"
    CONST_VP_SELECT_MEMORY_RASCONFIGURATION_PLATFORM_DEFAULT = "platform-default"
    CONST_VP_SELECT_MEMORY_RASCONFIGURATION_SPARING = "sparing"

class IodSnapshotStart(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "IodSnapshotStart")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "iodSnapshotStart"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    ISO_SHARE = "IsoShare"
    ISO_SHARE_FILE = "IsoShareFile"
    ISO_SHARE_IP = "IsoShareIp"
    ISO_SHARE_PATH = "IsoSharePath"
    ISO_SHARE_TYPE = "IsoShareType"
    PASSWORD = "Password"
    REMOTE_SHARE_FILE = "RemoteShareFile"
    REMOTE_SHARE_IP = "RemoteShareIp"
    REMOTE_SHARE_PASSWORD = "RemoteSharePassword"
    REMOTE_SHARE_PATH = "RemoteSharePath"
    REMOTE_SHARE_TYPE = "RemoteShareType"
    REMOTE_SHARE_USERNAME = "RemoteShareUsername"
    RN = "Rn"
    STATUS = "Status"
    TIME_OUT = "TimeOut"
    USERNAME = "Username"

    CONST_ADMIN_STATE_TRIGGER = "trigger"
    CONST_ADMIN_STATE_TRIGGERED = "triggered"
    CONST_ISO_SHARE_TYPE_CIFS = "cifs"
    CONST_ISO_SHARE_TYPE_NFS = "nfs"
    CONST_ISO_SHARE_TYPE_SD = "sd"
    CONST_ISO_SHARE_TYPE_WWW = "www"
    CONST_REMOTE_SHARE_TYPE_SCP = "scp"
    CONST_REMOTE_SHARE_TYPE_SFTP = "sftp"
    CONST_REMOTE_SHARE_TYPE_TFTP = "tftp"

class SysdebugTechSupportExport(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "SysdebugTechSupportExport")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "sysdebugTechSupportExport"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    FSM_PROGR = "FsmProgr"
    FSM_STAGE_DESCR = "FsmStageDescr"
    FSM_STATUS = "FsmStatus"
    HOSTNAME = "Hostname"
    PROTOCOL = "Protocol"
    PWD = "Pwd"
    REMOTE_FILE = "RemoteFile"
    RN = "Rn"
    STATUS = "Status"
    USER = "User"

    CONST_PROTOCOL_FTP = "ftp"
    CONST_PROTOCOL_HTTP = "http"
    CONST_PROTOCOL_SCP = "scp"
    CONST_PROTOCOL_SFTP = "sftp"
    CONST_PROTOCOL_TFTP = "tftp"

class EquipmentFan(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "EquipmentFan")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "equipmentFan"

    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    MODULE = "Module"
    OPERABILITY = "Operability"
    POWER = "Power"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    THERMAL = "Thermal"
    TRAY = "Tray"
    VENDOR = "Vendor"
    VOLTAGE = "Voltage"

    CONST_OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPERABILITY_CONFIG = "config"
    CONST_OPERABILITY_DECOMISSIONING = "decomissioning"
    CONST_OPERABILITY_DEGRADED = "degraded"
    CONST_OPERABILITY_DISABLED = "disabled"
    CONST_OPERABILITY_DISCOVERY = "discovery"
    CONST_OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPERABILITY_IDENTIFY = "identify"
    CONST_OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPERABILITY_INOPERABLE = "inoperable"
    CONST_OPERABILITY_MALFORMED_FRU = "malformed-fru"
    CONST_OPERABILITY_NOT_SUPPORTED = "not-supported"
    CONST_OPERABILITY_OPERABLE = "operable"
    CONST_OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPERABILITY_POST_FAILURE = "post-failure"
    CONST_OPERABILITY_POWER_PROBLEM = "power-problem"
    CONST_OPERABILITY_POWERED_OFF = "powered-off"
    CONST_OPERABILITY_REMOVED = "removed"
    CONST_OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPERABILITY_UNKNOWN = "unknown"
    CONST_OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_POWER_DEGRADED = "degraded"
    CONST_POWER_ERROR = "error"
    CONST_POWER_NOT_SUPPORTED = "not-supported"
    CONST_POWER_OFF = "off"
    CONST_POWER_OFFDUTY = "offduty"
    CONST_POWER_OFFLINE = "offline"
    CONST_POWER_ON = "on"
    CONST_POWER_ONLINE = "online"
    CONST_POWER_POWER_SAVE = "power-save"
    CONST_POWER_TEST = "test"
    CONST_POWER_UNKNOWN = "unknown"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"
    CONST_THERMAL_LOWER_CRITICAL = "lower-critical"
    CONST_THERMAL_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_THERMAL_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_THERMAL_NOT_SUPPORTED = "not-supported"
    CONST_THERMAL_OK = "ok"
    CONST_THERMAL_UNKNOWN = "unknown"
    CONST_THERMAL_UPPER_CRITICAL = "upper-critical"
    CONST_THERMAL_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_THERMAL_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    CONST_VOLTAGE_LOWER_CRITICAL = "lower-critical"
    CONST_VOLTAGE_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_VOLTAGE_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_VOLTAGE_NOT_SUPPORTED = "not-supported"
    CONST_VOLTAGE_OK = "ok"
    CONST_VOLTAGE_UNKNOWN = "unknown"
    CONST_VOLTAGE_UPPER_CRITICAL = "upper-critical"
    CONST_VOLTAGE_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_VOLTAGE_UPPER_NON_RECOVERABLE = "upper-non-recoverable"

class BiosVfVgaPriority(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfVgaPriority")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfVgaPriority"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_VGA_PRIORITY = "VpVgaPriority"

    CONST_VP_VGA_PRIORITY_OFFBOARD = "Offboard"
    CONST_VP_VGA_PRIORITY_ONBOARD = "Onboard"
    CONST_VP_VGA_PRIORITY_ONBOARD_VGA_DISABLED = "Onboard VGA Disabled"
    CONST_VP_VGA_PRIORITY_PLATFORM_DEFAULT = "platform-default"

class MgmtImporter(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "MgmtImporter")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "mgmtImporter"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    FSM_DESCR = "FsmDescr"
    FSM_RMT_INV_ERR_CODE = "FsmRmtInvErrCode"
    FSM_RMT_INV_ERR_DESCR = "FsmRmtInvErrDescr"
    FSM_STAGE_DESCR = "FsmStageDescr"
    HOSTNAME = "Hostname"
    PASSPHRASE = "Passphrase"
    PROTO = "Proto"
    PWD = "Pwd"
    REMOTE_FILE = "RemoteFile"
    RN = "Rn"
    STATUS = "Status"
    USER = "User"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_FSM_RMT_INV_ERR_CODE_ = ""
    CONST_FSM_RMT_INV_ERR_CODE_ABORTED = "Aborted"
    CONST_FSM_RMT_INV_ERR_CODE_ERROR__COLLECTING__CONFIGURATION__DATA = "Error collecting configuration data"
    CONST_FSM_RMT_INV_ERR_CODE_ERROR__IMPORTING__CONFIGURATION = "Error importing configuration"
    CONST_FSM_RMT_INV_ERR_CODE_PARTIALLY_IMPORTED = "Partially Imported"
    CONST_FSM_RMT_INV_ERR_CODE_TFTP_ERROR = "TFTP Error"
    CONST_FSM_RMT_INV_ERR_CODE_UNKNOWN__ERROR = "Unknown error"
    CONST_FSM_RMT_INV_ERR_CODE_NONE = "none"
    CONST_PROTO_FTP = "ftp"
    CONST_PROTO_HTTP = "http"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_SCP = "scp"
    CONST_PROTO_SFTP = "sftp"
    CONST_PROTO_TFTP = "tftp"

class LsbootVMedia(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootVMedia")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootVMedia"

    ACCESS = "Access"
    DN = "Dn"
    NAME = "Name"
    ORDER = "Order"
    RN = "Rn"
    STATE = "State"
    STATUS = "Status"
    SUBTYPE = "Subtype"
    TYPE = "Type"

    CONST_ACCESS_ = ""
    CONST_ACCESS_READ_ONLY_LOCAL = "read-only-local"
    CONST_ACCESS_READ_ONLY_REMOTE = "read-only-remote"
    CONST_ACCESS_READ_WRITE_DRIVE = "read-write-drive"
    CONST_ACCESS_READ_WRITE_LOCAL = "read-write-local"
    CONST_ACCESS_READ_WRITE_REMOTE = "read-write-remote"
    CONST_STATE_DISABLED = "Disabled"
    CONST_STATE_ENABLED = "Enabled"
    CONST_SUBTYPE_ = ""
    CONST_SUBTYPE_CIMC_MAPPED_DVD = "cimc-mapped-dvd"
    CONST_SUBTYPE_CIMC_MAPPED_HDD = "cimc-mapped-hdd"
    CONST_SUBTYPE_KVM_MAPPED_DVD = "kvm-mapped-dvd"
    CONST_SUBTYPE_KVM_MAPPED_FDD = "kvm-mapped-fdd"
    CONST_SUBTYPE_KVM_MAPPED_HDD = "kvm-mapped-hdd"
    CONST_TYPE_VMEDIA = "VMEDIA"

class BiosVfOSBootWatchdogTimer(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfOSBootWatchdogTimer")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfOSBootWatchdogTimer"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_OSBOOT_WATCHDOG_TIMER = "VpOSBootWatchdogTimer"

    CONST_VP_OSBOOT_WATCHDOG_TIMER_DISABLED = "Disabled"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_ENABLED = "Enabled"
    CONST__VP_OSBOOT_WATCHDOG_TIMER_DISABLED = "disabled"
    CONST__VP_OSBOOT_WATCHDOG_TIMER_ENABLED = "enabled"
    CONST_VP_OSBOOT_WATCHDOG_TIMER_PLATFORM_DEFAULT = "platform-default"

class BiosVfAdjacentCacheLinePrefetch(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfAdjacentCacheLinePrefetch")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfAdjacentCacheLinePrefetch"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_ADJACENT_CACHE_LINE_PREFETCH = "VpAdjacentCacheLinePrefetch"

    CONST_VP_ADJACENT_CACHE_LINE_PREFETCH_DISABLED = "Disabled"
    CONST_VP_ADJACENT_CACHE_LINE_PREFETCH_ENABLED = "Enabled"
    CONST__VP_ADJACENT_CACHE_LINE_PREFETCH_DISABLED = "disabled"
    CONST__VP_ADJACENT_CACHE_LINE_PREFETCH_ENABLED = "enabled"
    CONST_VP_ADJACENT_CACHE_LINE_PREFETCH_PLATFORM_DEFAULT = "platform-default"

class MgmtIf(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "MgmtIf")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "mgmtIf"

    DDNS_DOMAIN = "DdnsDomain"
    DDNS_ENABLE = "DdnsEnable"
    DESCRIPTION = "Description"
    DHCP_ENABLE = "DhcpEnable"
    DN = "Dn"
    DNS_ALTERNATE = "DnsAlternate"
    DNS_PREFERRED = "DnsPreferred"
    DNS_USING_DHCP = "DnsUsingDhcp"
    EXT_ENABLED = "ExtEnabled"
    EXT_GW = "ExtGw"
    EXT_IP = "ExtIp"
    EXT_MASK = "ExtMask"
    HOSTNAME = "Hostname"
    ID = "Id"
    IF_TYPE = "IfType"
    MAC = "Mac"
    NIC_MODE = "NicMode"
    NIC_REDUNDANCY = "NicRedundancy"
    PORT_PROFILE = "PortProfile"
    RN = "Rn"
    STATUS = "Status"
    SUBJECT = "Subject"
    V6_SLAAC_IP = "V6SlaacIp"
    V6DHCP_ENABLE = "V6dhcpEnable"
    V6DNS_ALTERNATE = "V6dnsAlternate"
    V6DNS_PREFERRED = "V6dnsPreferred"
    V6DNS_USING_DHCP = "V6dnsUsingDhcp"
    V6EXT_ENABLED = "V6extEnabled"
    V6EXT_GW = "V6extGw"
    V6EXT_IP = "V6extIp"
    V6LINK_LOCAL = "V6linkLocal"
    V6PREFIX = "V6prefix"
    VIC_SLOT = "VicSlot"
    VLAN_ENABLE = "VlanEnable"
    VLAN_ID = "VlanId"
    VLAN_PRIORITY = "VlanPriority"

    CONST_IF_TYPE_PHYSICAL = "physical"
    CONST_NIC_MODE_CISCO__CARD = "cisco_card"
    CONST_NIC_MODE_DEDICATED = "dedicated"
    CONST_NIC_MODE_SHARED__LOM = "shared_lom"
    CONST_NIC_MODE_SHARED__LOM__10G = "shared_lom_10g"
    CONST_NIC_MODE_SHARED__LOM__EXT = "shared_lom_ext"
    CONST_NIC_MODE_SHIPPING = "shipping"
    CONST_NIC_REDUNDANCY_ACTIVE_ACTIVE = "active-active"
    CONST_NIC_REDUNDANCY_ACTIVE_STANDBY = "active-standby"
    CONST_NIC_REDUNDANCY_NONE = "none"
    CONST_VIC_SLOT_0 = "0"
    CONST_VIC_SLOT_1 = "1"
    CONST_VIC_SLOT_10 = "10"
    CONST_VIC_SLOT_2 = "2"
    CONST_VIC_SLOT_4 = "4"
    CONST_VIC_SLOT_5 = "5"
    CONST_VIC_SLOT_9 = "9"
    CONST_VIC_SLOT_FLEX_LOM = "flex-lom"
    CONST_VIC_SLOT_RISER1 = "riser1"
    CONST_VIC_SLOT_RISER2 = "riser2"

class AdaptorFcGenProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorFcGenProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorFcGenProfile"

    CLASS_OF_SERVICE = "ClassOfService"
    DN = "Dn"
    MAC = "Mac"
    MAX_DATA_FIELD_SIZE = "MaxDataFieldSize"
    ORDER = "Order"
    PERSISTENT_LUN_BIND = "PersistentLunBind"
    RATE_LIMIT = "RateLimit"
    RN = "Rn"
    STATUS = "Status"
    VLAN = "Vlan"

    CONST_MAC_AUTO = "AUTO"
    CONST_ORDER_ANY = "ANY"
    CONST_RATE_LIMIT_OFF = "OFF"
    CONST_VLAN_NONE = "NONE"

class MgmtBackup(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "MgmtBackup")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "mgmtBackup"

    ADMIN_STATE = "AdminState"
    DN = "Dn"
    FSM_DESCR = "FsmDescr"
    FSM_RMT_INV_ERR_CODE = "FsmRmtInvErrCode"
    FSM_RMT_INV_ERR_DESCR = "FsmRmtInvErrDescr"
    FSM_STAGE_DESCR = "FsmStageDescr"
    HOSTNAME = "Hostname"
    PASSPHRASE = "Passphrase"
    PROTO = "Proto"
    PWD = "Pwd"
    REMOTE_FILE = "RemoteFile"
    RN = "Rn"
    STATUS = "Status"
    USER = "User"

    CONST_ADMIN_STATE_DISABLED = "disabled"
    CONST_ADMIN_STATE_ENABLED = "enabled"
    CONST_FSM_RMT_INV_ERR_CODE_ = ""
    CONST_FSM_RMT_INV_ERR_CODE_ABORTED = "Aborted"
    CONST_FSM_RMT_INV_ERR_CODE_ERROR__COLLECTING__CONFIGURATION__DATA = "Error collecting configuration data"
    CONST_FSM_RMT_INV_ERR_CODE_ERROR__IMPORTING__CONFIGURATION = "Error importing configuration"
    CONST_FSM_RMT_INV_ERR_CODE_PARTIALLY_IMPORTED = "Partially Imported"
    CONST_FSM_RMT_INV_ERR_CODE_TFTP_ERROR = "TFTP Error"
    CONST_FSM_RMT_INV_ERR_CODE_UNKNOWN__ERROR = "Unknown error"
    CONST_FSM_RMT_INV_ERR_CODE_NONE = "none"
    CONST_PROTO_FTP = "ftp"
    CONST_PROTO_HTTP = "http"
    CONST_PROTO_NONE = "none"
    CONST_PROTO_SCP = "scp"
    CONST_PROTO_SFTP = "sftp"
    CONST_PROTO_TFTP = "tftp"

class BiosVfExecuteDisableBit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfExecuteDisableBit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfExecuteDisableBit"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_EXECUTE_DISABLE_BIT = "VpExecuteDisableBit"

    CONST_VP_EXECUTE_DISABLE_BIT_DISABLED = "Disabled"
    CONST_VP_EXECUTE_DISABLE_BIT_ENABLED = "Enabled"
    CONST__VP_EXECUTE_DISABLE_BIT_DISABLED = "disabled"
    CONST__VP_EXECUTE_DISABLE_BIT_ENABLED = "enabled"
    CONST_VP_EXECUTE_DISABLE_BIT_PLATFORM_DEFAULT = "platform-default"

class LsbootBootSecurity(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "LsbootBootSecurity")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "lsbootBootSecurity"

    DN = "Dn"
    RN = "Rn"
    SECURE_BOOT = "SecureBoot"
    STATUS = "Status"

    CONST_SECURE_BOOT_DISABLE = "disable"
    CONST_SECURE_BOOT_DISABLED = "disabled"
    CONST_SECURE_BOOT_ENABLE = "enable"
    CONST_SECURE_BOOT_ENABLED = "enabled"

class HuuFirmwareCatalog(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuFirmwareCatalog")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuFirmwareCatalog"

    DESCRIPTION = "Description"
    DN = "Dn"
    NUM_OF_COMPONENTS = "NumOfComponents"
    RN = "Rn"
    STATUS = "Status"


class TopRoot(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "TopRoot")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "topRoot"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class BiosVfSrIov(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfSrIov")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfSrIov"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_SR_IOV = "VpSrIov"

    CONST_VP_SR_IOV_DISABLED = "Disabled"
    CONST_VP_SR_IOV_ENABLED = "Enabled"
    CONST__VP_SR_IOV_DISABLED = "disabled"
    CONST__VP_SR_IOV_ENABLED = "enabled"
    CONST_VP_SR_IOV_PLATFORM_DEFAULT = "platform-default"

class StorageFlexFlashVirtualDriveImageMap(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageFlexFlashVirtualDriveImageMap")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageFlexFlashVirtualDriveImageMap"

    ADMIN_ACTION = "AdminAction"
    DN = "Dn"
    MAP = "Map"
    MOUNT_OPTIONS = "MountOptions"
    PASSWORD = "Password"
    REMOTE_FILE = "RemoteFile"
    REMOTE_SHARE = "RemoteShare"
    RN = "Rn"
    STATUS = "Status"
    TO_ENABLE_MAPPING = "ToEnableMapping"
    USERNAME = "Username"
    VIRTUAL_DRIVE = "VirtualDrive"

    CONST_ADMIN_ACTION_MAP = "map"
    CONST_ADMIN_ACTION_UNMAP = "unmap"
    CONST_MAP_CIFS = "cifs"
    CONST_MAP_NFS = "nfs"

class ComputeRackUnitMbTempStats(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "ComputeRackUnitMbTempStats")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "computeRackUnitMbTempStats"

    AMBIENT_TEMP = "AmbientTemp"
    DN = "Dn"
    FRONT_TEMP = "FrontTemp"
    IOH1_TEMP = "Ioh1Temp"
    IOH2_TEMP = "Ioh2Temp"
    REAR_TEMP = "RearTemp"
    RN = "Rn"
    STATUS = "Status"
    TIME_COLLECTED = "TimeCollected"

    CONST_AMBIENT_TEMP_ = ""
    CONST_FRONT_TEMP_ = ""
    CONST_IOH1_TEMP_ = ""
    CONST_IOH2_TEMP_ = ""
    CONST_REAR_TEMP_ = ""

class AdaptorPortProfiles(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorPortProfiles")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorPortProfiles"

    DN = "Dn"
    PORT_PROFILES_COUNT = "PortProfilesCount"
    PORT_PROFILES_NAME = "PortProfilesName"
    RN = "Rn"
    STATUS = "Status"


class ServerUtilization(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "ServerUtilization")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "serverUtilization"

    CPU_UTILIZATION = "CpuUtilization"
    DN = "Dn"
    IO_UTILIZATION = "IoUtilization"
    MEMORY_UTILIZATION = "MemoryUtilization"
    OVERALL_UTILIZATION = "OverallUtilization"
    RN = "Rn"
    STATUS = "Status"


class AaaSession(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AaaSession")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "aaaSession"

    DN = "Dn"
    HOST = "Host"
    ID = "Id"
    RN = "Rn"
    STATUS = "Status"
    UI = "Ui"
    USER = "User"

    CONST_UI_EP = "ep"
    CONST_UI_NONE = "none"
    CONST_UI_SHELL = "shell"
    CONST_UI_V_MEDIA = "vMedia"
    CONST_UI_WEB = "web"

class BiosBootMode(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosBootMode")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosBootMode"

    ACTUAL_BOOT_MODE = "ActualBootMode"
    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"

    CONST_ACTUAL_BOOT_MODE_LEGACY = "Legacy"
    CONST_ACTUAL_BOOT_MODE_UEFI = "Uefi"
    CONST_ACTUAL_BOOT_MODE_UNKNOWN = "Unknown"

class BiosVfTPMSupport(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfTPMSupport")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfTPMSupport"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_TPMSUPPORT = "VpTPMSupport"

    CONST_VP_TPMSUPPORT_DISABLED = "Disabled"
    CONST_VP_TPMSUPPORT_ENABLED = "Enabled"
    CONST__VP_TPMSUPPORT_DISABLED = "disabled"
    CONST__VP_TPMSUPPORT_ENABLED = "enabled"
    CONST_VP_TPMSUPPORT_PLATFORM_DEFAULT = "platform-default"

class StorageFlexFlashPhysicalDrive(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageFlexFlashPhysicalDrive")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageFlexFlashPhysicalDrive"

    BLOCK_SIZE = "BlockSize"
    CAPACITY = "Capacity"
    CARD_MODE = "CardMode"
    CARD_STATUS = "CardStatus"
    CARD_TYPE = "CardType"
    CONTROLLER = "Controller"
    DN = "Dn"
    DRIVES_ENABLED = "DrivesEnabled"
    HEALTH = "Health"
    MANUFACTURER_DATE = "ManufacturerDate"
    MANUFACTURER_ID = "ManufacturerId"
    OEM_ID = "OemId"
    PARTITION_COUNT = "PartitionCount"
    PASSWORD_PROTECTED = "PasswordProtected"
    PD_STATUS = "PdStatus"
    PHYSICAL_DRIVE = "PhysicalDrive"
    PHYSICAL_DRIVE_ID = "PhysicalDriveId"
    PRODUCT_NAME = "ProductName"
    PRODUCT_REVISION = "ProductRevision"
    RAID_ROLE = "RaidRole"
    READ_ERROR_COUNT = "ReadErrorCount"
    READ_ERROR_THRESHOLD = "ReadErrorThreshold"
    RN = "Rn"
    SERIAL_NUMBER = "SerialNumber"
    SIGNATURE = "Signature"
    SLOT_NUMBER = "SlotNumber"
    STATUS = "Status"
    SYNC_MODE = "SyncMode"
    WRITE_ENABLED = "WriteEnabled"
    WRITE_ERROR_COUNT = "WriteErrorCount"
    WRITE_ERROR_THRESHOLD = "WriteErrorThreshold"


class BiosVfQpiSnoopMode(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfQpiSnoopMode")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfQpiSnoopMode"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_QPI_SNOOP_MODE = "VpQpiSnoopMode"

    CONST_VP_QPI_SNOOP_MODE_CLUSTER_ON_DIE = "cluster-on-die"
    CONST_VP_QPI_SNOOP_MODE_EARLY_SNOOP = "early-snoop"
    CONST_VP_QPI_SNOOP_MODE_HOME_SNOOP = "home-snoop"
    CONST_VP_QPI_SNOOP_MODE_PLATFORM_DEFAULT = "platform-default"

class OneTimeBootDevice(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "OneTimeBootDevice")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "oneTimeBootDevice"

    DEVICE = "Device"
    DN = "Dn"
    NAME = "Name"
    RN = "Rn"
    STATUS = "Status"

    CONST_DEVICE_HUU = "huu"
    CONST_DEVICE_HV = "hv"
    CONST_DEVICE_NONE = "none"
    CONST_DEVICE_SCU = "scu"

class BiosVfPatrolScrubDuration(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPatrolScrubDuration")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPatrolScrubDuration"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PATROL_SCRUB_DURATION = "VpPatrolScrubDuration"

    CONST_VP_PATROL_SCRUB_DURATION_PLATFORM_DEFAULT = "platform-default"

class BiosVfPCIOptionROMs(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPCIOptionROMs")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPCIOptionROMs"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PCIOPTION_ROMS = "VpPCIOptionROMs"

    CONST_VP_PCIOPTION_ROMS_DISABLED = "Disabled"
    CONST_VP_PCIOPTION_ROMS_ENABLED = "Enabled"
    CONST_VP_PCIOPTION_ROMS_LEGACY_ONLY = "Legacy Only"
    CONST_VP_PCIOPTION_ROMS_UEFI_ONLY = "UEFI Only"
    CONST__VP_PCIOPTION_ROMS_DISABLED = "disabled"
    CONST__VP_PCIOPTION_ROMS_ENABLED = "enabled"
    CONST_VP_PCIOPTION_ROMS_PLATFORM_DEFAULT = "platform-default"

class StorageLocalDisk(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageLocalDisk")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageLocalDisk"

    ADMIN_ACTION = "AdminAction"
    COERCED_SIZE = "CoercedSize"
    DEDICATED_HOT_SPARE_FOR_VDID = "DedicatedHotSpareForVDId"
    DN = "Dn"
    DRIVE_FIRMWARE = "DriveFirmware"
    DRIVE_SERIAL_NUMBER = "DriveSerialNumber"
    DRIVE_STATE = "DriveState"
    HEALTH = "Health"
    ID = "Id"
    INTERFACE_TYPE = "InterfaceType"
    LINK_SPEED = "LinkSpeed"
    MEDIA_TYPE = "MediaType"
    ONLINE = "Online"
    PD_STATUS = "PdStatus"
    PREDICTIVE_FAILURE_COUNT = "PredictiveFailureCount"
    PRODUCT_ID = "ProductId"
    RN = "Rn"
    STATUS = "Status"
    VENDOR = "Vendor"

    CONST_ADMIN_ACTION_LOCATOR_LED_OFF = "locator-led-off"
    CONST_ADMIN_ACTION_LOCATOR_LED_ON = "locator-led-on"
    CONST_ADMIN_ACTION_MAKE_DEDICATED_HOT_SPARE = "make-dedicated-hot-spare"
    CONST_ADMIN_ACTION_MAKE_GLOBAL_HOT_SPARE = "make-global-hot-spare"
    CONST_ADMIN_ACTION_MAKE_JBOD = "make-jbod"
    CONST_ADMIN_ACTION_MAKE_UNCONFIGURED_GOOD = "make-unconfigured-good"
    CONST_ADMIN_ACTION_PREPARE_FOR_REMOVAL = "prepare-for-removal"
    CONST_ADMIN_ACTION_REMOVE_HOT_SPARE = "remove-hot-spare"
    CONST_ADMIN_ACTION_SET_BOOT_DRIVE = "set-boot-drive"
    CONST_ADMIN_ACTION_UNDO_PREPARE_FOR_REMOVAL = "undo-prepare-for-removal"
    CONST_DEDICATED_HOT_SPARE_FOR_VDID_ = ""

class BiosUnit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosUnit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosUnit"

    ADMIN_ACTION = "AdminAction"
    DN = "Dn"
    MODEL = "Model"
    RN = "Rn"
    STATUS = "Status"
    VENDOR = "Vendor"

    CONST_ADMIN_ACTION_ENTER_BIOS_SETUP = "enter-bios-setup"

class BiosVfPStateCoordType(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPStateCoordType")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPStateCoordType"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PSTATE_COORD_TYPE = "VpPStateCoordType"

    CONST_VP_PSTATE_COORD_TYPE_HW_ALL = "HW ALL"
    CONST_VP_PSTATE_COORD_TYPE_SW_ALL = "SW ALL"
    CONST_VP_PSTATE_COORD_TYPE_SW_ANY = "SW ANY"
    CONST_VP_PSTATE_COORD_TYPE_PLATFORM_DEFAULT = "platform-default"

class IodController(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "IodController")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "iodController"

    DESCRIPTION = "Description"
    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"


class BiosVfDirectCacheAccess(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfDirectCacheAccess")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfDirectCacheAccess"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_DIRECT_CACHE_ACCESS = "VpDirectCacheAccess"

    CONST_VP_DIRECT_CACHE_ACCESS_AUTO = "Auto"
    CONST_VP_DIRECT_CACHE_ACCESS_DISABLED = "Disabled"
    CONST_VP_DIRECT_CACHE_ACCESS_ENABLED = "Enabled"
    CONST__VP_DIRECT_CACHE_ACCESS_AUTO = "auto"
    CONST__VP_DIRECT_CACHE_ACCESS_DISABLED = "disabled"
    CONST__VP_DIRECT_CACHE_ACCESS_ENABLED = "enabled"
    CONST_VP_DIRECT_CACHE_ACCESS_PLATFORM_DEFAULT = "platform-default"

class StorageController(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageController")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageController"

    ADMIN_ACTION = "AdminAction"
    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    PCI_SLOT = "PciSlot"
    PRESENCE = "Presence"
    RAID_SUPPORT = "RaidSupport"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    TYPE = "Type"
    VENDOR = "Vendor"

    CONST_ADMIN_ACTION_CLEAR_BOOT_DRIVE = "clear-boot-drive"
    CONST_ADMIN_ACTION_CLEAR_FOREIGN_CONFIG = "clear-foreign-config"
    CONST_ADMIN_ACTION_DELETE_ALL_VDS_RESET_PDS = "delete-all-vds-reset-pds"
    CONST_ADMIN_ACTION_DISABLE_JBOD = "disable-jbod"
    CONST_ADMIN_ACTION_ENABLE_JBOD = "enable-jbod"
    CONST_ADMIN_ACTION_GET_TTY_LOG = "get-tty-log"
    CONST_ADMIN_ACTION_IMPORT_FOREIGN_CONFIG = "import-foreign-config"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"

class MemoryUnit(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "MemoryUnit")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "memoryUnit"

    ARRAY = "Array"
    BANK_LOCATOR = "BankLocator"
    CAPACITY = "Capacity"
    CLOCK = "Clock"
    DN = "Dn"
    FORM_FACTOR = "FormFactor"
    ID = "Id"
    LOCATION = "Location"
    MEMORY_TYPE_DETAIL = "MemoryTypeDetail"
    MODEL = "Model"
    OPER_STATE = "OperState"
    OPERABILITY = "Operability"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    TYPE = "Type"
    VENDOR = "Vendor"
    VISIBILITY = "Visibility"
    WIDTH = "Width"

    CONST_CAPACITY_UNSPECIFIED = "unspecified"
    CONST_CLOCK_UNSPECIFIED = "unspecified"
    CONST_FORM_FACTOR_DIMM = "DIMM"
    CONST_FORM_FACTOR_FB_DIMM = "FB-DIMM"
    CONST_FORM_FACTOR_OTHER = "Other"
    CONST_FORM_FACTOR_RIMM = "RIMM"
    CONST_FORM_FACTOR_SIMM = "SIMM"
    CONST_FORM_FACTOR_SODIMM = "SODIMM"
    CONST_FORM_FACTOR_SRIMM = "SRIMM"
    CONST_FORM_FACTOR_TSOP = "TSOP"
    CONST_FORM_FACTOR_UNKNOWN = "Unknown"
    CONST_FORM_FACTOR_UNDISCOVERED = "undiscovered"
    CONST_OPER_STATE_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPER_STATE_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPER_STATE_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPER_STATE_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPER_STATE_CONFIG = "config"
    CONST_OPER_STATE_DECOMISSIONING = "decomissioning"
    CONST_OPER_STATE_DEGRADED = "degraded"
    CONST_OPER_STATE_DISABLED = "disabled"
    CONST_OPER_STATE_DISCOVERY = "discovery"
    CONST_OPER_STATE_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPER_STATE_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPER_STATE_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPER_STATE_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPER_STATE_IDENTIFY = "identify"
    CONST_OPER_STATE_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPER_STATE_INOPERABLE = "inoperable"
    CONST_OPER_STATE_MALFORMED_FRU = "malformed-fru"
    CONST_OPER_STATE_NOT_SUPPORTED = "not-supported"
    CONST_OPER_STATE_OPERABLE = "operable"
    CONST_OPER_STATE_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPER_STATE_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPER_STATE_POST_FAILURE = "post-failure"
    CONST_OPER_STATE_POWER_PROBLEM = "power-problem"
    CONST_OPER_STATE_POWERED_OFF = "powered-off"
    CONST_OPER_STATE_REMOVED = "removed"
    CONST_OPER_STATE_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPER_STATE_UNKNOWN = "unknown"
    CONST_OPER_STATE_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPER_STATE_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPERABILITY_CONFIG = "config"
    CONST_OPERABILITY_DECOMISSIONING = "decomissioning"
    CONST_OPERABILITY_DEGRADED = "degraded"
    CONST_OPERABILITY_DISABLED = "disabled"
    CONST_OPERABILITY_DISCOVERY = "discovery"
    CONST_OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPERABILITY_IDENTIFY = "identify"
    CONST_OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPERABILITY_INOPERABLE = "inoperable"
    CONST_OPERABILITY_MALFORMED_FRU = "malformed-fru"
    CONST_OPERABILITY_NOT_SUPPORTED = "not-supported"
    CONST_OPERABILITY_OPERABLE = "operable"
    CONST_OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPERABILITY_POST_FAILURE = "post-failure"
    CONST_OPERABILITY_POWER_PROBLEM = "power-problem"
    CONST_OPERABILITY_POWERED_OFF = "powered-off"
    CONST_OPERABILITY_REMOVED = "removed"
    CONST_OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPERABILITY_UNKNOWN = "unknown"
    CONST_OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"
    CONST_TYPE_3_DRAM = "3DRAM"
    CONST_TYPE_CDRAM = "CDRAM"
    CONST_TYPE_DDR = "DDR"
    CONST_TYPE_DDR2 = "DDR2"
    CONST_TYPE_DDR2_FB_DIMM = "DDR2 FB-DIMM"
    CONST_TYPE_DDR3 = "DDR3"
    CONST_TYPE_DRAM = "DRAM"
    CONST_TYPE_EDRAM = "EDRAM"
    CONST_TYPE_EEPROM = "EEPROM"
    CONST_TYPE_EPROM = "EPROM"
    CONST_TYPE_FBD2 = "FBD2"
    CONST_TYPE_FEPROM = "FEPROM"
    CONST_TYPE_FLASH = "FLASH"
    CONST_TYPE_OTHER = "Other"
    CONST_TYPE_RAM = "RAM"
    CONST_TYPE_RDRAM = "RDRAM"
    CONST_TYPE_ROM = "ROM"
    CONST_TYPE_SDRAM = "SDRAM"
    CONST_TYPE_SGRAM = "SGRAM"
    CONST_TYPE_SRAM = "SRAM"
    CONST_TYPE_UNKNOWN = "Unknown"
    CONST_TYPE_VRAM = "VRAM"
    CONST_TYPE_UNDISCOVERED = "undiscovered"
    CONST_VISIBILITY_NO = "no"
    CONST_VISIBILITY_UNKNOWN = "unknown"
    CONST_VISIBILITY_YES = "yes"
    CONST_WIDTH_UNSPECIFIED = "unspecified"

class BiosVfPatrolScrub(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfPatrolScrub")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfPatrolScrub"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_PATROL_SCRUB = "VpPatrolScrub"

    CONST_VP_PATROL_SCRUB_DISABLED = "Disabled"
    CONST_VP_PATROL_SCRUB_ENABLED = "Enabled"
    CONST__VP_PATROL_SCRUB_DISABLED = "disabled"
    CONST__VP_PATROL_SCRUB_ENABLED = "enabled"
    CONST_VP_PATROL_SCRUB_PLATFORM_DEFAULT = "platform-default"

class MemoryUnitEnvStats(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "MemoryUnitEnvStats")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "memoryUnitEnvStats"

    DESCRIPTION = "Description"
    DN = "Dn"
    ID = "Id"
    RN = "Rn"
    STATUS = "Status"
    TEMPERATURE = "Temperature"
    TIME_COLLECTED = "TimeCollected"


class AdaptorEthGenProfile(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "AdaptorEthGenProfile")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "adaptorEthGenProfile"

    ARFS = "Arfs"
    DN = "Dn"
    ORDER = "Order"
    RATE_LIMIT = "RateLimit"
    RN = "Rn"
    STATUS = "Status"
    TRUSTED_CLASS_OF_SERVICE = "TrustedClassOfService"
    UPLINK_FAILBACK_TIMEOUT = "UplinkFailbackTimeout"
    UPLINK_FAILOVER = "UplinkFailover"
    VLAN = "Vlan"
    VLAN_MODE = "VlanMode"
    VMQ = "Vmq"

    CONST_ARFS_DISABLED = "Disabled"
    CONST_ARFS_ENABLED = "Enabled"
    CONST__ARFS_DISABLED = "disabled"
    CONST__ARFS_ENABLED = "enabled"
    CONST_ORDER_ANY = "ANY"
    CONST_RATE_LIMIT_OFF = "OFF"
    CONST_UPLINK_FAILOVER_DISABLED = "Disabled"
    CONST_UPLINK_FAILOVER_ENABLED = "Enabled"
    CONST__UPLINK_FAILOVER_DISABLED = "disabled"
    CONST__UPLINK_FAILOVER_ENABLED = "enabled"
    CONST_VLAN_NONE = "NONE"
    CONST_VLAN_MODE_ACCESS = "ACCESS"
    CONST_VLAN_MODE_TRUNK = "TRUNK"
    CONST_VMQ_DISABLED = "Disabled"
    CONST_VMQ_ENABLED = "Enabled"
    CONST__VMQ_DISABLED = "disabled"
    CONST__VMQ_ENABLED = "enabled"

class BiosVfUCSMBootOrderRuleControl(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfUCSMBootOrderRuleControl")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfUCSMBootOrderRuleControl"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_UCSMBOOT_ORDER_RULE = "VpUCSMBootOrderRule"

    CONST_VP_UCSMBOOT_ORDER_RULE_LOOSE = "Loose"
    CONST_VP_UCSMBOOT_ORDER_RULE_STRICT = "Strict"
    CONST_VP_UCSMBOOT_ORDER_RULE_PLATFORM_DEFAULT = "platform-default"

class StorageLocalDiskSlotEp(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "StorageLocalDiskSlotEp")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "storageLocalDiskSlotEp"

    DN = "Dn"
    ID = "Id"
    OPERABILITY = "Operability"
    PRESENCE = "Presence"
    RN = "Rn"
    STATUS = "Status"

    CONST_OPERABILITY_ACCESSIBILITY_PROBLEM = "accessibility-problem"
    CONST_OPERABILITY_AUTO_UPGRADE = "auto-upgrade"
    CONST_OPERABILITY_BIOS_POST_TIMEOUT = "bios-post-timeout"
    CONST_OPERABILITY_CHASSIS_LIMIT_EXCEEDED = "chassis-limit-exceeded"
    CONST_OPERABILITY_CONFIG = "config"
    CONST_OPERABILITY_DECOMISSIONING = "decomissioning"
    CONST_OPERABILITY_DEGRADED = "degraded"
    CONST_OPERABILITY_DISABLED = "disabled"
    CONST_OPERABILITY_DISCOVERY = "discovery"
    CONST_OPERABILITY_DISCOVERY_FAILED = "discovery-failed"
    CONST_OPERABILITY_EQUIPMENT_PROBLEM = "equipment-problem"
    CONST_OPERABILITY_FABRIC_CONN_PROBLEM = "fabric-conn-problem"
    CONST_OPERABILITY_FABRIC_UNSUPPORTED_CONN = "fabric-unsupported-conn"
    CONST_OPERABILITY_IDENTIFY = "identify"
    CONST_OPERABILITY_IDENTITY_UNESTABLISHABLE = "identity-unestablishable"
    CONST_OPERABILITY_INOPERABLE = "inoperable"
    CONST_OPERABILITY_MALFORMED_FRU = "malformed-fru"
    CONST_OPERABILITY_NOT_SUPPORTED = "not-supported"
    CONST_OPERABILITY_OPERABLE = "operable"
    CONST_OPERABILITY_PEER_COMM_PROBLEM = "peer-comm-problem"
    CONST_OPERABILITY_PERFORMANCE_PROBLEM = "performance-problem"
    CONST_OPERABILITY_POST_FAILURE = "post-failure"
    CONST_OPERABILITY_POWER_PROBLEM = "power-problem"
    CONST_OPERABILITY_POWERED_OFF = "powered-off"
    CONST_OPERABILITY_REMOVED = "removed"
    CONST_OPERABILITY_THERMAL_PROBLEM = "thermal-problem"
    CONST_OPERABILITY_UNKNOWN = "unknown"
    CONST_OPERABILITY_UPGRADE_PROBLEM = "upgrade-problem"
    CONST_OPERABILITY_VOLTAGE_PROBLEM = "voltage-problem"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"

class ComputeBoard(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "ComputeBoard")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "computeBoard"

    DN = "Dn"
    ID = "Id"
    MODEL = "Model"
    OPER_POWER = "OperPower"
    PERF = "Perf"
    POWER = "Power"
    PRESENCE = "Presence"
    RN = "Rn"
    SERIAL = "Serial"
    STATUS = "Status"
    VENDOR = "Vendor"

    CONST_OPER_POWER_DEGRADED = "degraded"
    CONST_OPER_POWER_ERROR = "error"
    CONST_OPER_POWER_NOT_SUPPORTED = "not-supported"
    CONST_OPER_POWER_OFF = "off"
    CONST_OPER_POWER_OFFDUTY = "offduty"
    CONST_OPER_POWER_OFFLINE = "offline"
    CONST_OPER_POWER_ON = "on"
    CONST_OPER_POWER_ONLINE = "online"
    CONST_OPER_POWER_POWER_SAVE = "power-save"
    CONST_OPER_POWER_TEST = "test"
    CONST_OPER_POWER_UNKNOWN = "unknown"
    CONST_PERF_LOWER_CRITICAL = "lower-critical"
    CONST_PERF_LOWER_NON_CRITICAL = "lower-non-critical"
    CONST_PERF_LOWER_NON_RECOVERABLE = "lower-non-recoverable"
    CONST_PERF_NOT_SUPPORTED = "not-supported"
    CONST_PERF_OK = "ok"
    CONST_PERF_UNKNOWN = "unknown"
    CONST_PERF_UPPER_CRITICAL = "upper-critical"
    CONST_PERF_UPPER_NON_CRITICAL = "upper-non-critical"
    CONST_PERF_UPPER_NON_RECOVERABLE = "upper-non-recoverable"
    CONST_POWER_DEGRADED = "degraded"
    CONST_POWER_ERROR = "error"
    CONST_POWER_NOT_SUPPORTED = "not-supported"
    CONST_POWER_OFF = "off"
    CONST_POWER_OFFDUTY = "offduty"
    CONST_POWER_OFFLINE = "offline"
    CONST_POWER_ON = "on"
    CONST_POWER_ONLINE = "online"
    CONST_POWER_POWER_SAVE = "power-save"
    CONST_POWER_TEST = "test"
    CONST_POWER_UNKNOWN = "unknown"
    CONST_PRESENCE_EMPTY = "empty"
    CONST_PRESENCE_EQUIPPED = "equipped"
    CONST_PRESENCE_EQUIPPED_IDENTITY_UNESTABLISHABLE = "equipped-identity-unestablishable"
    CONST_PRESENCE_EQUIPPED_NOT_PRIMARY = "equipped-not-primary"
    CONST_PRESENCE_EQUIPPED_WITH_MALFORMED_FRU = "equipped-with-malformed-fru"
    CONST_PRESENCE_INACCESSIBLE = "inaccessible"
    CONST_PRESENCE_MISMATCH = "mismatch"
    CONST_PRESENCE_MISMATCH_IDENTITY_UNESTABLISHABLE = "mismatch-identity-unestablishable"
    CONST_PRESENCE_MISSING = "missing"
    CONST_PRESENCE_NOT_SUPPORTED = "not-supported"
    CONST_PRESENCE_UNAUTHORIZED = "unauthorized"
    CONST_PRESENCE_UNKNOWN = "unknown"

class HuuFirmwareComponent(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "HuuFirmwareComponent")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "huuFirmwareComponent"

    CNTRL_ID = "CntrlId"
    COMPONENT = "Component"
    DESCRIPTION = "Description"
    DEVICE_ID = "DeviceId"
    DN = "Dn"
    ID = "Id"
    MAC_ADDR = "MacAddr"
    RN = "Rn"
    RUNNING_VERSION = "RunningVersion"
    SLOT = "Slot"
    STATUS = "Status"
    SUB_DEVICE_ID = "SubDeviceId"
    SUB_VENDOR_ID = "SubVendorId"
    VENDOR_ID = "VendorId"


class IodSnapshotStatus(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "IodSnapshotStatus")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "iodSnapshotStatus"

    CURRENT_STATUS = "CurrentStatus"
    CURRENT_TIME = "CurrentTime"
    DN = "Dn"
    IOD_IMAGE_VERSION = "IodImageVersion"
    REMOTE_SHARE_FILE = "RemoteShareFile"
    REMOTE_SHARE_IP = "RemoteShareIp"
    REMOTE_SHARE_PATH = "RemoteSharePath"
    RN = "Rn"
    RUNNING_TIME = "RunningTime"
    SNAPSHOT_CANCEL_OP = "SnapshotCancelOp"
    SNAPSHOT_REPORT = "SnapshotReport"
    START_TIME = "StartTime"
    STATUS = "Status"


class TopSystem(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "TopSystem")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "topSystem"

    ADDRESS = "Address"
    CURRENT_TIME = "CurrentTime"
    DN = "Dn"
    LOCAL_TIME = "LocalTime"
    MODE = "Mode"
    NAME = "Name"
    RN = "Rn"
    STATUS = "Status"
    TIME_ZONE = "TimeZone"

    CONST_MODE_CLUSTER = "cluster"
    CONST_MODE_STAND_ALONE = "stand-alone"
    CONST_MODE_UNSPECIFIED = "unspecified"
    CONST_TIME_ZONE_AFRICA_ABIDJAN = "Africa/Abidjan"
    CONST_TIME_ZONE_AFRICA_ACCRA = "Africa/Accra"
    CONST_TIME_ZONE_AFRICA_ADDIS_ABABA = "Africa/Addis Ababa"
    CONST_TIME_ZONE_AFRICA_ALGIERS = "Africa/Algiers"
    CONST_TIME_ZONE_AFRICA_ASMARA = "Africa/Asmara"
    CONST_TIME_ZONE_AFRICA_BAMAKO = "Africa/Bamako"
    CONST_TIME_ZONE_AFRICA_BANGUI = "Africa/Bangui"
    CONST_TIME_ZONE_AFRICA_BANJUL = "Africa/Banjul"
    CONST_TIME_ZONE_AFRICA_BISSAU = "Africa/Bissau"
    CONST_TIME_ZONE_AFRICA_BLANTYRE = "Africa/Blantyre"
    CONST_TIME_ZONE_AFRICA_BRAZZAVILLE = "Africa/Brazzaville"
    CONST_TIME_ZONE_AFRICA_BUJUMBURA = "Africa/Bujumbura"
    CONST_TIME_ZONE_AFRICA_CAIRO = "Africa/Cairo"
    CONST_TIME_ZONE_AFRICA_CASABLANCA = "Africa/Casablanca"
    CONST_TIME_ZONE_AFRICA_CEUTA = "Africa/Ceuta"
    CONST_TIME_ZONE_AFRICA_CONAKRY = "Africa/Conakry"
    CONST_TIME_ZONE_AFRICA_DAKAR = "Africa/Dakar"
    CONST_TIME_ZONE_AFRICA_DAR__ES_SALAAM = "Africa/Dar es Salaam"
    CONST_TIME_ZONE_AFRICA_DJIBOUTI = "Africa/Djibouti"
    CONST_TIME_ZONE_AFRICA_DOUALA = "Africa/Douala"
    CONST_TIME_ZONE_AFRICA_EL_AAIUN = "Africa/El Aaiun"
    CONST_TIME_ZONE_AFRICA_FREETOWN = "Africa/Freetown"
    CONST_TIME_ZONE_AFRICA_GABORONE = "Africa/Gaborone"
    CONST_TIME_ZONE_AFRICA_HARARE = "Africa/Harare"
    CONST_TIME_ZONE_AFRICA_JOHANNESBURG = "Africa/Johannesburg"
    CONST_TIME_ZONE_AFRICA_JUBA = "Africa/Juba"
    CONST_TIME_ZONE_AFRICA_KAMPALA = "Africa/Kampala"
    CONST_TIME_ZONE_AFRICA_KHARTOUM = "Africa/Khartoum"
    CONST_TIME_ZONE_AFRICA_KIGALI = "Africa/Kigali"
    CONST_TIME_ZONE_AFRICA_KINSHASA = "Africa/Kinshasa"
    CONST_TIME_ZONE_AFRICA_LAGOS = "Africa/Lagos"
    CONST_TIME_ZONE_AFRICA_LIBREVILLE = "Africa/Libreville"
    CONST_TIME_ZONE_AFRICA_LOME = "Africa/Lome"
    CONST_TIME_ZONE_AFRICA_LUANDA = "Africa/Luanda"
    CONST_TIME_ZONE_AFRICA_LUBUMBASHI = "Africa/Lubumbashi"
    CONST_TIME_ZONE_AFRICA_LUSAKA = "Africa/Lusaka"
    CONST_TIME_ZONE_AFRICA_MALABO = "Africa/Malabo"
    CONST_TIME_ZONE_AFRICA_MAPUTO = "Africa/Maputo"
    CONST_TIME_ZONE_AFRICA_MASERU = "Africa/Maseru"
    CONST_TIME_ZONE_AFRICA_MBABANE = "Africa/Mbabane"
    CONST_TIME_ZONE_AFRICA_MOGADISHU = "Africa/Mogadishu"
    CONST_TIME_ZONE_AFRICA_MONROVIA = "Africa/Monrovia"
    CONST_TIME_ZONE_AFRICA_NAIROBI = "Africa/Nairobi"
    CONST_TIME_ZONE_AFRICA_NDJAMENA = "Africa/Ndjamena"
    CONST_TIME_ZONE_AFRICA_NIAMEY = "Africa/Niamey"
    CONST_TIME_ZONE_AFRICA_NOUAKCHOTT = "Africa/Nouakchott"
    CONST_TIME_ZONE_AFRICA_OUAGADOUGOU = "Africa/Ouagadougou"
    CONST_TIME_ZONE_AFRICA_PORTO_NOVO = "Africa/Porto-Novo"
    CONST_TIME_ZONE_AFRICA_SAO_TOME = "Africa/Sao Tome"
    CONST_TIME_ZONE_AFRICA_TRIPOLI = "Africa/Tripoli"
    CONST_TIME_ZONE_AFRICA_TUNIS = "Africa/Tunis"
    CONST_TIME_ZONE_AFRICA_WINDHOEK = "Africa/Windhoek"
    CONST_TIME_ZONE_AMERICA_ADAK = "America/Adak"
    CONST_TIME_ZONE_AMERICA_ANCHORAGE = "America/Anchorage"
    CONST_TIME_ZONE_AMERICA_ANGUILLA = "America/Anguilla"
    CONST_TIME_ZONE_AMERICA_ANTIGUA = "America/Antigua"
    CONST_TIME_ZONE_AMERICA_ARAGUAINA = "America/Araguaina"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_BUENOS_AIRES = "America/Argentina/Buenos Aires"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_CATAMARCA = "America/Argentina/Catamarca"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_CORDOBA = "America/Argentina/Cordoba"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_JUJUY = "America/Argentina/Jujuy"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_LA_RIOJA = "America/Argentina/La Rioja"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_MENDOZA = "America/Argentina/Mendoza"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_RIO_GALLEGOS = "America/Argentina/Rio Gallegos"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_SALTA = "America/Argentina/Salta"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_SAN_JUAN = "America/Argentina/San Juan"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_SAN_LUIS = "America/Argentina/San Luis"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_TUCUMAN = "America/Argentina/Tucuman"
    CONST_TIME_ZONE_AMERICA_ARGENTINA_USHUAIA = "America/Argentina/Ushuaia"
    CONST_TIME_ZONE_AMERICA_ARUBA = "America/Aruba"
    CONST_TIME_ZONE_AMERICA_ASUNCION = "America/Asuncion"
    CONST_TIME_ZONE_AMERICA_ATIKOKAN = "America/Atikokan"
    CONST_TIME_ZONE_AMERICA_BAHIA = "America/Bahia"
    CONST_TIME_ZONE_AMERICA_BAHIA_BANDERAS = "America/Bahia Banderas"
    CONST_TIME_ZONE_AMERICA_BARBADOS = "America/Barbados"
    CONST_TIME_ZONE_AMERICA_BELEM = "America/Belem"
    CONST_TIME_ZONE_AMERICA_BELIZE = "America/Belize"
    CONST_TIME_ZONE_AMERICA_BLANC_SABLON = "America/Blanc-Sablon"
    CONST_TIME_ZONE_AMERICA_BOA_VISTA = "America/Boa Vista"
    CONST_TIME_ZONE_AMERICA_BOGOTA = "America/Bogota"
    CONST_TIME_ZONE_AMERICA_BOISE = "America/Boise"
    CONST_TIME_ZONE_AMERICA_CAMBRIDGE_BAY = "America/Cambridge Bay"
    CONST_TIME_ZONE_AMERICA_CAMPO_GRANDE = "America/Campo Grande"
    CONST_TIME_ZONE_AMERICA_CANCUN = "America/Cancun"
    CONST_TIME_ZONE_AMERICA_CARACAS = "America/Caracas"
    CONST_TIME_ZONE_AMERICA_CAYENNE = "America/Cayenne"
    CONST_TIME_ZONE_AMERICA_CAYMAN = "America/Cayman"
    CONST_TIME_ZONE_AMERICA_CHICAGO = "America/Chicago"
    CONST_TIME_ZONE_AMERICA_CHIHUAHUA = "America/Chihuahua"
    CONST_TIME_ZONE_AMERICA_COSTA_RICA = "America/Costa Rica"
    CONST_TIME_ZONE_AMERICA_CRESTON = "America/Creston"
    CONST_TIME_ZONE_AMERICA_CUIABA = "America/Cuiaba"
    CONST_TIME_ZONE_AMERICA_CURACAO = "America/Curacao"
    CONST_TIME_ZONE_AMERICA_DANMARKSHAVN = "America/Danmarkshavn"
    CONST_TIME_ZONE_AMERICA_DAWSON = "America/Dawson"
    CONST_TIME_ZONE_AMERICA_DAWSON_CREEK = "America/Dawson Creek"
    CONST_TIME_ZONE_AMERICA_DENVER = "America/Denver"
    CONST_TIME_ZONE_AMERICA_DETROIT = "America/Detroit"
    CONST_TIME_ZONE_AMERICA_DOMINICA = "America/Dominica"
    CONST_TIME_ZONE_AMERICA_EDMONTON = "America/Edmonton"
    CONST_TIME_ZONE_AMERICA_EIRUNEPE = "America/Eirunepe"
    CONST_TIME_ZONE_AMERICA_EL_SALVADOR = "America/El Salvador"
    CONST_TIME_ZONE_AMERICA_FORTALEZA = "America/Fortaleza"
    CONST_TIME_ZONE_AMERICA_GLACE_BAY = "America/Glace Bay"
    CONST_TIME_ZONE_AMERICA_GODTHAB = "America/Godthab"
    CONST_TIME_ZONE_AMERICA_GOOSE_BAY = "America/Goose Bay"
    CONST_TIME_ZONE_AMERICA_GRAND_TURK = "America/Grand Turk"
    CONST_TIME_ZONE_AMERICA_GRENADA = "America/Grenada"
    CONST_TIME_ZONE_AMERICA_GUADELOUPE = "America/Guadeloupe"
    CONST_TIME_ZONE_AMERICA_GUATEMALA = "America/Guatemala"
    CONST_TIME_ZONE_AMERICA_GUAYAQUIL = "America/Guayaquil"
    CONST_TIME_ZONE_AMERICA_GUYANA = "America/Guyana"
    CONST_TIME_ZONE_AMERICA_HALIFAX = "America/Halifax"
    CONST_TIME_ZONE_AMERICA_HAVANA = "America/Havana"
    CONST_TIME_ZONE_AMERICA_HERMOSILLO = "America/Hermosillo"
    CONST_TIME_ZONE_AMERICA_INDIANA_INDIANAPOLIS = "America/Indiana/Indianapolis"
    CONST_TIME_ZONE_AMERICA_INDIANA_KNOX = "America/Indiana/Knox"
    CONST_TIME_ZONE_AMERICA_INDIANA_MARENGO = "America/Indiana/Marengo"
    CONST_TIME_ZONE_AMERICA_INDIANA_PETERSBURG = "America/Indiana/Petersburg"
    CONST_TIME_ZONE_AMERICA_INDIANA_TELL_CITY = "America/Indiana/Tell City"
    CONST_TIME_ZONE_AMERICA_INDIANA_VEVAY = "America/Indiana/Vevay"
    CONST_TIME_ZONE_AMERICA_INDIANA_VINCENNES = "America/Indiana/Vincennes"
    CONST_TIME_ZONE_AMERICA_INDIANA_WINAMAC = "America/Indiana/Winamac"
    CONST_TIME_ZONE_AMERICA_INUVIK = "America/Inuvik"
    CONST_TIME_ZONE_AMERICA_IQALUIT = "America/Iqaluit"
    CONST_TIME_ZONE_AMERICA_JAMAICA = "America/Jamaica"
    CONST_TIME_ZONE_AMERICA_JUNEAU = "America/Juneau"
    CONST_TIME_ZONE_AMERICA_KENTUCKY_LOUISVILLE = "America/Kentucky/Louisville"
    CONST_TIME_ZONE_AMERICA_KENTUCKY_MONTICELLO = "America/Kentucky/Monticello"
    CONST_TIME_ZONE_AMERICA_KRALENDIJK = "America/Kralendijk"
    CONST_TIME_ZONE_AMERICA_LA_PAZ = "America/La Paz"
    CONST_TIME_ZONE_AMERICA_LIMA = "America/Lima"
    CONST_TIME_ZONE_AMERICA_LOS_ANGELES = "America/Los Angeles"
    CONST_TIME_ZONE_AMERICA_LOWER_PRINCES = "America/Lower Princes"
    CONST_TIME_ZONE_AMERICA_MACEIO = "America/Maceio"
    CONST_TIME_ZONE_AMERICA_MANAGUA = "America/Managua"
    CONST_TIME_ZONE_AMERICA_MANAUS = "America/Manaus"
    CONST_TIME_ZONE_AMERICA_MARIGOT = "America/Marigot"
    CONST_TIME_ZONE_AMERICA_MARTINIQUE = "America/Martinique"
    CONST_TIME_ZONE_AMERICA_MATAMOROS = "America/Matamoros"
    CONST_TIME_ZONE_AMERICA_MAZATLAN = "America/Mazatlan"
    CONST_TIME_ZONE_AMERICA_MENOMINEE = "America/Menominee"
    CONST_TIME_ZONE_AMERICA_MERIDA = "America/Merida"
    CONST_TIME_ZONE_AMERICA_METLAKATLA = "America/Metlakatla"
    CONST_TIME_ZONE_AMERICA_MEXICO_CITY = "America/Mexico City"
    CONST_TIME_ZONE_AMERICA_MIQUELON = "America/Miquelon"
    CONST_TIME_ZONE_AMERICA_MONCTON = "America/Moncton"
    CONST_TIME_ZONE_AMERICA_MONTERREY = "America/Monterrey"
    CONST_TIME_ZONE_AMERICA_MONTEVIDEO = "America/Montevideo"
    CONST_TIME_ZONE_AMERICA_MONTREAL = "America/Montreal"
    CONST_TIME_ZONE_AMERICA_MONTSERRAT = "America/Montserrat"
    CONST_TIME_ZONE_AMERICA_NASSAU = "America/Nassau"
    CONST_TIME_ZONE_AMERICA_NEW_YORK = "America/New York"
    CONST_TIME_ZONE_AMERICA_NIPIGON = "America/Nipigon"
    CONST_TIME_ZONE_AMERICA_NOME = "America/Nome"
    CONST_TIME_ZONE_AMERICA_NORONHA = "America/Noronha"
    CONST_TIME_ZONE_AMERICA_NORTH_DAKOTA_BEULAH = "America/North Dakota/Beulah"
    CONST_TIME_ZONE_AMERICA_NORTH_DAKOTA_CENTER = "America/North Dakota/Center"
    CONST_TIME_ZONE_AMERICA_NORTH_DAKOTA_NEW_SALEM = "America/North Dakota/New Salem"
    CONST_TIME_ZONE_AMERICA_OJINAGA = "America/Ojinaga"
    CONST_TIME_ZONE_AMERICA_PANAMA = "America/Panama"
    CONST_TIME_ZONE_AMERICA_PANGNIRTUNG = "America/Pangnirtung"
    CONST_TIME_ZONE_AMERICA_PARAMARIBO = "America/Paramaribo"
    CONST_TIME_ZONE_AMERICA_PHOENIX = "America/Phoenix"
    CONST_TIME_ZONE_AMERICA_PORT__OF_SPAIN = "America/Port of Spain"
    CONST_TIME_ZONE_AMERICA_PORT_AU_PRINCE = "America/Port-au-Prince"
    CONST_TIME_ZONE_AMERICA_PORTO_VELHO = "America/Porto Velho"
    CONST_TIME_ZONE_AMERICA_PUERTO_RICO = "America/Puerto Rico"
    CONST_TIME_ZONE_AMERICA_RAINY_RIVER = "America/Rainy River"
    CONST_TIME_ZONE_AMERICA_RANKIN_INLET = "America/Rankin Inlet"
    CONST_TIME_ZONE_AMERICA_RECIFE = "America/Recife"
    CONST_TIME_ZONE_AMERICA_REGINA = "America/Regina"
    CONST_TIME_ZONE_AMERICA_RESOLUTE = "America/Resolute"
    CONST_TIME_ZONE_AMERICA_RIO_BRANCO = "America/Rio Branco"
    CONST_TIME_ZONE_AMERICA_SANTA_ISABEL = "America/Santa Isabel"
    CONST_TIME_ZONE_AMERICA_SANTAREM = "America/Santarem"
    CONST_TIME_ZONE_AMERICA_SANTIAGO = "America/Santiago"
    CONST_TIME_ZONE_AMERICA_SANTO_DOMINGO = "America/Santo Domingo"
    CONST_TIME_ZONE_AMERICA_SAO_PAULO = "America/Sao Paulo"
    CONST_TIME_ZONE_AMERICA_SCORESBYSUND = "America/Scoresbysund"
    CONST_TIME_ZONE_AMERICA_SHIPROCK = "America/Shiprock"
    CONST_TIME_ZONE_AMERICA_SITKA = "America/Sitka"
    CONST_TIME_ZONE_AMERICA_ST_BARTHELEMY = "America/St Barthelemy"
    CONST_TIME_ZONE_AMERICA_ST_JOHNS = "America/St Johns"
    CONST_TIME_ZONE_AMERICA_ST_KITTS = "America/St Kitts"
    CONST_TIME_ZONE_AMERICA_ST_LUCIA = "America/St Lucia"
    CONST_TIME_ZONE_AMERICA_ST_THOMAS = "America/St Thomas"
    CONST_TIME_ZONE_AMERICA_ST_VINCENT = "America/St Vincent"
    CONST_TIME_ZONE_AMERICA_SWIFT_CURRENT = "America/Swift Current"
    CONST_TIME_ZONE_AMERICA_TEGUCIGALPA = "America/Tegucigalpa"
    CONST_TIME_ZONE_AMERICA_THULE = "America/Thule"
    CONST_TIME_ZONE_AMERICA_THUNDER_BAY = "America/Thunder Bay"
    CONST_TIME_ZONE_AMERICA_TIJUANA = "America/Tijuana"
    CONST_TIME_ZONE_AMERICA_TORONTO = "America/Toronto"
    CONST_TIME_ZONE_AMERICA_TORTOLA = "America/Tortola"
    CONST_TIME_ZONE_AMERICA_VANCOUVER = "America/Vancouver"
    CONST_TIME_ZONE_AMERICA_WHITEHORSE = "America/Whitehorse"
    CONST_TIME_ZONE_AMERICA_WINNIPEG = "America/Winnipeg"
    CONST_TIME_ZONE_AMERICA_YAKUTAT = "America/Yakutat"
    CONST_TIME_ZONE_AMERICA_YELLOWKNIFE = "America/Yellowknife"
    CONST_TIME_ZONE_ANTARCTICA_CASEY = "Antarctica/Casey"
    CONST_TIME_ZONE_ANTARCTICA_DAVIS = "Antarctica/Davis"
    CONST_TIME_ZONE_ANTARCTICA_DUMONT_DURVILLE = "Antarctica/DumontDUrville"
    CONST_TIME_ZONE_ANTARCTICA_MACQUARIE = "Antarctica/Macquarie"
    CONST_TIME_ZONE_ANTARCTICA_MAWSON = "Antarctica/Mawson"
    CONST_TIME_ZONE_ANTARCTICA_MC_MURDO = "Antarctica/McMurdo"
    CONST_TIME_ZONE_ANTARCTICA_PALMER = "Antarctica/Palmer"
    CONST_TIME_ZONE_ANTARCTICA_ROTHERA = "Antarctica/Rothera"
    CONST_TIME_ZONE_ANTARCTICA_SOUTH_POLE = "Antarctica/South Pole"
    CONST_TIME_ZONE_ANTARCTICA_SYOWA = "Antarctica/Syowa"
    CONST_TIME_ZONE_ANTARCTICA_TROLL = "Antarctica/Troll"
    CONST_TIME_ZONE_ANTARCTICA_VOSTOK = "Antarctica/Vostok"
    CONST_TIME_ZONE_ARCTIC_LONGYEARBYEN = "Arctic/Longyearbyen"
    CONST_TIME_ZONE_ASIA_ADEN = "Asia/Aden"
    CONST_TIME_ZONE_ASIA_ALMATY = "Asia/Almaty"
    CONST_TIME_ZONE_ASIA_AMMAN = "Asia/Amman"
    CONST_TIME_ZONE_ASIA_ANADYR = "Asia/Anadyr"
    CONST_TIME_ZONE_ASIA_AQTAU = "Asia/Aqtau"
    CONST_TIME_ZONE_ASIA_AQTOBE = "Asia/Aqtobe"
    CONST_TIME_ZONE_ASIA_ASHGABAT = "Asia/Ashgabat"
    CONST_TIME_ZONE_ASIA_BAGHDAD = "Asia/Baghdad"
    CONST_TIME_ZONE_ASIA_BAHRAIN = "Asia/Bahrain"
    CONST_TIME_ZONE_ASIA_BAKU = "Asia/Baku"
    CONST_TIME_ZONE_ASIA_BANGKOK = "Asia/Bangkok"
    CONST_TIME_ZONE_ASIA_BEIRUT = "Asia/Beirut"
    CONST_TIME_ZONE_ASIA_BISHKEK = "Asia/Bishkek"
    CONST_TIME_ZONE_ASIA_BRUNEI = "Asia/Brunei"
    CONST_TIME_ZONE_ASIA_CHOIBALSAN = "Asia/Choibalsan"
    CONST_TIME_ZONE_ASIA_CHONGQING = "Asia/Chongqing"
    CONST_TIME_ZONE_ASIA_COLOMBO = "Asia/Colombo"
    CONST_TIME_ZONE_ASIA_DAMASCUS = "Asia/Damascus"
    CONST_TIME_ZONE_ASIA_DHAKA = "Asia/Dhaka"
    CONST_TIME_ZONE_ASIA_DILI = "Asia/Dili"
    CONST_TIME_ZONE_ASIA_DUBAI = "Asia/Dubai"
    CONST_TIME_ZONE_ASIA_DUSHANBE = "Asia/Dushanbe"
    CONST_TIME_ZONE_ASIA_GAZA = "Asia/Gaza"
    CONST_TIME_ZONE_ASIA_HARBIN = "Asia/Harbin"
    CONST_TIME_ZONE_ASIA_HEBRON = "Asia/Hebron"
    CONST_TIME_ZONE_ASIA_HO_CHI_MINH = "Asia/Ho Chi Minh"
    CONST_TIME_ZONE_ASIA_HONG_KONG = "Asia/Hong Kong"
    CONST_TIME_ZONE_ASIA_HOVD = "Asia/Hovd"
    CONST_TIME_ZONE_ASIA_IRKUTSK = "Asia/Irkutsk"
    CONST_TIME_ZONE_ASIA_JAKARTA = "Asia/Jakarta"
    CONST_TIME_ZONE_ASIA_JAYAPURA = "Asia/Jayapura"
    CONST_TIME_ZONE_ASIA_JERUSALEM = "Asia/Jerusalem"
    CONST_TIME_ZONE_ASIA_KABUL = "Asia/Kabul"
    CONST_TIME_ZONE_ASIA_KAMCHATKA = "Asia/Kamchatka"
    CONST_TIME_ZONE_ASIA_KARACHI = "Asia/Karachi"
    CONST_TIME_ZONE_ASIA_KASHGAR = "Asia/Kashgar"
    CONST_TIME_ZONE_ASIA_KATHMANDU = "Asia/Kathmandu"
    CONST_TIME_ZONE_ASIA_KHANDYGA = "Asia/Khandyga"
    CONST_TIME_ZONE_ASIA_KOLKATA = "Asia/Kolkata"
    CONST_TIME_ZONE_ASIA_KRASNOYARSK = "Asia/Krasnoyarsk"
    CONST_TIME_ZONE_ASIA_KUALA_LUMPUR = "Asia/Kuala Lumpur"
    CONST_TIME_ZONE_ASIA_KUCHING = "Asia/Kuching"
    CONST_TIME_ZONE_ASIA_KUWAIT = "Asia/Kuwait"
    CONST_TIME_ZONE_ASIA_MACAU = "Asia/Macau"
    CONST_TIME_ZONE_ASIA_MAGADAN = "Asia/Magadan"
    CONST_TIME_ZONE_ASIA_MAKASSAR = "Asia/Makassar"
    CONST_TIME_ZONE_ASIA_MANILA = "Asia/Manila"
    CONST_TIME_ZONE_ASIA_MUSCAT = "Asia/Muscat"
    CONST_TIME_ZONE_ASIA_NICOSIA = "Asia/Nicosia"
    CONST_TIME_ZONE_ASIA_NOVOKUZNETSK = "Asia/Novokuznetsk"
    CONST_TIME_ZONE_ASIA_NOVOSIBIRSK = "Asia/Novosibirsk"
    CONST_TIME_ZONE_ASIA_OMSK = "Asia/Omsk"
    CONST_TIME_ZONE_ASIA_ORAL = "Asia/Oral"
    CONST_TIME_ZONE_ASIA_PHNOM_PENH = "Asia/Phnom Penh"
    CONST_TIME_ZONE_ASIA_PONTIANAK = "Asia/Pontianak"
    CONST_TIME_ZONE_ASIA_PYONGYANG = "Asia/Pyongyang"
    CONST_TIME_ZONE_ASIA_QATAR = "Asia/Qatar"
    CONST_TIME_ZONE_ASIA_QYZYLORDA = "Asia/Qyzylorda"
    CONST_TIME_ZONE_ASIA_RANGOON = "Asia/Rangoon"
    CONST_TIME_ZONE_ASIA_RIYADH = "Asia/Riyadh"
    CONST_TIME_ZONE_ASIA_SAKHALIN = "Asia/Sakhalin"
    CONST_TIME_ZONE_ASIA_SAMARKAND = "Asia/Samarkand"
    CONST_TIME_ZONE_ASIA_SEOUL = "Asia/Seoul"
    CONST_TIME_ZONE_ASIA_SHANGHAI = "Asia/Shanghai"
    CONST_TIME_ZONE_ASIA_SINGAPORE = "Asia/Singapore"
    CONST_TIME_ZONE_ASIA_TAIPEI = "Asia/Taipei"
    CONST_TIME_ZONE_ASIA_TASHKENT = "Asia/Tashkent"
    CONST_TIME_ZONE_ASIA_TBILISI = "Asia/Tbilisi"
    CONST_TIME_ZONE_ASIA_TEHRAN = "Asia/Tehran"
    CONST_TIME_ZONE_ASIA_THIMPHU = "Asia/Thimphu"
    CONST_TIME_ZONE_ASIA_TOKYO = "Asia/Tokyo"
    CONST_TIME_ZONE_ASIA_ULAANBAATAR = "Asia/Ulaanbaatar"
    CONST_TIME_ZONE_ASIA_URUMQI = "Asia/Urumqi"
    CONST_TIME_ZONE_ASIA_UST_NERA = "Asia/Ust-Nera"
    CONST_TIME_ZONE_ASIA_VIENTIANE = "Asia/Vientiane"
    CONST_TIME_ZONE_ASIA_VLADIVOSTOK = "Asia/Vladivostok"
    CONST_TIME_ZONE_ASIA_YAKUTSK = "Asia/Yakutsk"
    CONST_TIME_ZONE_ASIA_YEKATERINBURG = "Asia/Yekaterinburg"
    CONST_TIME_ZONE_ASIA_YEREVAN = "Asia/Yerevan"
    CONST_TIME_ZONE_ATLANTIC_AZORES = "Atlantic/Azores"
    CONST_TIME_ZONE_ATLANTIC_BERMUDA = "Atlantic/Bermuda"
    CONST_TIME_ZONE_ATLANTIC_CANARY = "Atlantic/Canary"
    CONST_TIME_ZONE_ATLANTIC_CAPE_VERDE = "Atlantic/Cape Verde"
    CONST_TIME_ZONE_ATLANTIC_FAROE = "Atlantic/Faroe"
    CONST_TIME_ZONE_ATLANTIC_MADEIRA = "Atlantic/Madeira"
    CONST_TIME_ZONE_ATLANTIC_REYKJAVIK = "Atlantic/Reykjavik"
    CONST_TIME_ZONE_ATLANTIC_SOUTH_GEORGIA = "Atlantic/South Georgia"
    CONST_TIME_ZONE_ATLANTIC_ST_HELENA = "Atlantic/St Helena"
    CONST_TIME_ZONE_ATLANTIC_STANLEY = "Atlantic/Stanley"
    CONST_TIME_ZONE_AUSTRALIA_ADELAIDE = "Australia/Adelaide"
    CONST_TIME_ZONE_AUSTRALIA_BRISBANE = "Australia/Brisbane"
    CONST_TIME_ZONE_AUSTRALIA_BROKEN_HILL = "Australia/Broken Hill"
    CONST_TIME_ZONE_AUSTRALIA_CURRIE = "Australia/Currie"
    CONST_TIME_ZONE_AUSTRALIA_DARWIN = "Australia/Darwin"
    CONST_TIME_ZONE_AUSTRALIA_EUCLA = "Australia/Eucla"
    CONST_TIME_ZONE_AUSTRALIA_HOBART = "Australia/Hobart"
    CONST_TIME_ZONE_AUSTRALIA_LINDEMAN = "Australia/Lindeman"
    CONST_TIME_ZONE_AUSTRALIA_LORD_HOWE = "Australia/Lord Howe"
    CONST_TIME_ZONE_AUSTRALIA_MELBOURNE = "Australia/Melbourne"
    CONST_TIME_ZONE_AUSTRALIA_PERTH = "Australia/Perth"
    CONST_TIME_ZONE_AUSTRALIA_SYDNEY = "Australia/Sydney"
    CONST_TIME_ZONE_EUROPE_AMSTERDAM = "Europe/Amsterdam"
    CONST_TIME_ZONE_EUROPE_ANDORRA = "Europe/Andorra"
    CONST_TIME_ZONE_EUROPE_ATHENS = "Europe/Athens"
    CONST_TIME_ZONE_EUROPE_BELGRADE = "Europe/Belgrade"
    CONST_TIME_ZONE_EUROPE_BERLIN = "Europe/Berlin"
    CONST_TIME_ZONE_EUROPE_BRATISLAVA = "Europe/Bratislava"
    CONST_TIME_ZONE_EUROPE_BRUSSELS = "Europe/Brussels"
    CONST_TIME_ZONE_EUROPE_BUCHAREST = "Europe/Bucharest"
    CONST_TIME_ZONE_EUROPE_BUDAPEST = "Europe/Budapest"
    CONST_TIME_ZONE_EUROPE_BUSINGEN = "Europe/Busingen"
    CONST_TIME_ZONE_EUROPE_CHISINAU = "Europe/Chisinau"
    CONST_TIME_ZONE_EUROPE_COPENHAGEN = "Europe/Copenhagen"
    CONST_TIME_ZONE_EUROPE_DUBLIN = "Europe/Dublin"
    CONST_TIME_ZONE_EUROPE_GIBRALTAR = "Europe/Gibraltar"
    CONST_TIME_ZONE_EUROPE_GUERNSEY = "Europe/Guernsey"
    CONST_TIME_ZONE_EUROPE_HELSINKI = "Europe/Helsinki"
    CONST_TIME_ZONE_EUROPE_ISLE__OF_MAN = "Europe/Isle of Man"
    CONST_TIME_ZONE_EUROPE_ISTANBUL = "Europe/Istanbul"
    CONST_TIME_ZONE_EUROPE_JERSEY = "Europe/Jersey"
    CONST_TIME_ZONE_EUROPE_KALININGRAD = "Europe/Kaliningrad"
    CONST_TIME_ZONE_EUROPE_KIEV = "Europe/Kiev"
    CONST_TIME_ZONE_EUROPE_LISBON = "Europe/Lisbon"
    CONST_TIME_ZONE_EUROPE_LJUBLJANA = "Europe/Ljubljana"
    CONST_TIME_ZONE_EUROPE_LONDON = "Europe/London"
    CONST_TIME_ZONE_EUROPE_LUXEMBOURG = "Europe/Luxembourg"
    CONST_TIME_ZONE_EUROPE_MADRID = "Europe/Madrid"
    CONST_TIME_ZONE_EUROPE_MALTA = "Europe/Malta"
    CONST_TIME_ZONE_EUROPE_MARIEHAMN = "Europe/Mariehamn"
    CONST_TIME_ZONE_EUROPE_MINSK = "Europe/Minsk"
    CONST_TIME_ZONE_EUROPE_MONACO = "Europe/Monaco"
    CONST_TIME_ZONE_EUROPE_MOSCOW = "Europe/Moscow"
    CONST_TIME_ZONE_EUROPE_OSLO = "Europe/Oslo"
    CONST_TIME_ZONE_EUROPE_PARIS = "Europe/Paris"
    CONST_TIME_ZONE_EUROPE_PODGORICA = "Europe/Podgorica"
    CONST_TIME_ZONE_EUROPE_PRAGUE = "Europe/Prague"
    CONST_TIME_ZONE_EUROPE_RIGA = "Europe/Riga"
    CONST_TIME_ZONE_EUROPE_ROME = "Europe/Rome"
    CONST_TIME_ZONE_EUROPE_SAMARA = "Europe/Samara"
    CONST_TIME_ZONE_EUROPE_SAN_MARINO = "Europe/San Marino"
    CONST_TIME_ZONE_EUROPE_SARAJEVO = "Europe/Sarajevo"
    CONST_TIME_ZONE_EUROPE_SIMFEROPOL = "Europe/Simferopol"
    CONST_TIME_ZONE_EUROPE_SKOPJE = "Europe/Skopje"
    CONST_TIME_ZONE_EUROPE_SOFIA = "Europe/Sofia"
    CONST_TIME_ZONE_EUROPE_STOCKHOLM = "Europe/Stockholm"
    CONST_TIME_ZONE_EUROPE_TALLINN = "Europe/Tallinn"
    CONST_TIME_ZONE_EUROPE_TIRANE = "Europe/Tirane"
    CONST_TIME_ZONE_EUROPE_UZHGOROD = "Europe/Uzhgorod"
    CONST_TIME_ZONE_EUROPE_VADUZ = "Europe/Vaduz"
    CONST_TIME_ZONE_EUROPE_VATICAN = "Europe/Vatican"
    CONST_TIME_ZONE_EUROPE_VIENNA = "Europe/Vienna"
    CONST_TIME_ZONE_EUROPE_VILNIUS = "Europe/Vilnius"
    CONST_TIME_ZONE_EUROPE_VOLGOGRAD = "Europe/Volgograd"
    CONST_TIME_ZONE_EUROPE_WARSAW = "Europe/Warsaw"
    CONST_TIME_ZONE_EUROPE_ZAGREB = "Europe/Zagreb"
    CONST_TIME_ZONE_EUROPE_ZAPOROZHYE = "Europe/Zaporozhye"
    CONST_TIME_ZONE_EUROPE_ZURICH = "Europe/Zurich"
    CONST_TIME_ZONE_INDIAN_ANTANANARIVO = "Indian/Antananarivo"
    CONST_TIME_ZONE_INDIAN_CHAGOS = "Indian/Chagos"
    CONST_TIME_ZONE_INDIAN_CHRISTMAS = "Indian/Christmas"
    CONST_TIME_ZONE_INDIAN_COCOS = "Indian/Cocos"
    CONST_TIME_ZONE_INDIAN_COMORO = "Indian/Comoro"
    CONST_TIME_ZONE_INDIAN_KERGUELEN = "Indian/Kerguelen"
    CONST_TIME_ZONE_INDIAN_MAHE = "Indian/Mahe"
    CONST_TIME_ZONE_INDIAN_MALDIVES = "Indian/Maldives"
    CONST_TIME_ZONE_INDIAN_MAURITIUS = "Indian/Mauritius"
    CONST_TIME_ZONE_INDIAN_MAYOTTE = "Indian/Mayotte"
    CONST_TIME_ZONE_INDIAN_REUNION = "Indian/Reunion"
    CONST_TIME_ZONE_PACIFIC_APIA = "Pacific/Apia"
    CONST_TIME_ZONE_PACIFIC_AUCKLAND = "Pacific/Auckland"
    CONST_TIME_ZONE_PACIFIC_CHATHAM = "Pacific/Chatham"
    CONST_TIME_ZONE_PACIFIC_CHUUK = "Pacific/Chuuk"
    CONST_TIME_ZONE_PACIFIC_EASTER = "Pacific/Easter"
    CONST_TIME_ZONE_PACIFIC_EFATE = "Pacific/Efate"
    CONST_TIME_ZONE_PACIFIC_ENDERBURY = "Pacific/Enderbury"
    CONST_TIME_ZONE_PACIFIC_FAKAOFO = "Pacific/Fakaofo"
    CONST_TIME_ZONE_PACIFIC_FIJI = "Pacific/Fiji"
    CONST_TIME_ZONE_PACIFIC_FUNAFUTI = "Pacific/Funafuti"
    CONST_TIME_ZONE_PACIFIC_GALAPAGOS = "Pacific/Galapagos"
    CONST_TIME_ZONE_PACIFIC_GAMBIER = "Pacific/Gambier"
    CONST_TIME_ZONE_PACIFIC_GUADALCANAL = "Pacific/Guadalcanal"
    CONST_TIME_ZONE_PACIFIC_GUAM = "Pacific/Guam"
    CONST_TIME_ZONE_PACIFIC_HONOLULU = "Pacific/Honolulu"
    CONST_TIME_ZONE_PACIFIC_JOHNSTON = "Pacific/Johnston"
    CONST_TIME_ZONE_PACIFIC_KIRITIMATI = "Pacific/Kiritimati"
    CONST_TIME_ZONE_PACIFIC_KOSRAE = "Pacific/Kosrae"
    CONST_TIME_ZONE_PACIFIC_KWAJALEIN = "Pacific/Kwajalein"
    CONST_TIME_ZONE_PACIFIC_MAJURO = "Pacific/Majuro"
    CONST_TIME_ZONE_PACIFIC_MARQUESAS = "Pacific/Marquesas"
    CONST_TIME_ZONE_PACIFIC_MIDWAY = "Pacific/Midway"
    CONST_TIME_ZONE_PACIFIC_NAURU = "Pacific/Nauru"
    CONST_TIME_ZONE_PACIFIC_NIUE = "Pacific/Niue"
    CONST_TIME_ZONE_PACIFIC_NORFOLK = "Pacific/Norfolk"
    CONST_TIME_ZONE_PACIFIC_NOUMEA = "Pacific/Noumea"
    CONST_TIME_ZONE_PACIFIC_PAGO_PAGO = "Pacific/Pago Pago"
    CONST_TIME_ZONE_PACIFIC_PALAU = "Pacific/Palau"
    CONST_TIME_ZONE_PACIFIC_PITCAIRN = "Pacific/Pitcairn"
    CONST_TIME_ZONE_PACIFIC_POHNPEI = "Pacific/Pohnpei"
    CONST_TIME_ZONE_PACIFIC_PORT_MORESBY = "Pacific/Port Moresby"
    CONST_TIME_ZONE_PACIFIC_RAROTONGA = "Pacific/Rarotonga"
    CONST_TIME_ZONE_PACIFIC_SAIPAN = "Pacific/Saipan"
    CONST_TIME_ZONE_PACIFIC_TAHITI = "Pacific/Tahiti"
    CONST_TIME_ZONE_PACIFIC_TARAWA = "Pacific/Tarawa"
    CONST_TIME_ZONE_PACIFIC_TONGATAPU = "Pacific/Tongatapu"
    CONST_TIME_ZONE_PACIFIC_WAKE = "Pacific/Wake"
    CONST_TIME_ZONE_PACIFIC_WALLIS = "Pacific/Wallis"
    CONST_TIME_ZONE_UTC = "UTC"

class BiosVfBootOptionRetry(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfBootOptionRetry")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfBootOptionRetry"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_BOOT_OPTION_RETRY = "VpBootOptionRetry"

    CONST_VP_BOOT_OPTION_RETRY_DISABLED = "Disabled"
    CONST_VP_BOOT_OPTION_RETRY_ENABLED = "Enabled"
    CONST__VP_BOOT_OPTION_RETRY_DISABLED = "disabled"
    CONST__VP_BOOT_OPTION_RETRY_ENABLED = "enabled"
    CONST_VP_BOOT_OPTION_RETRY_PLATFORM_DEFAULT = "platform-default"

class BiosVfDramRefreshRate(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfDramRefreshRate")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfDramRefreshRate"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_DRAM_REFRESH_RATE = "VpDramRefreshRate"

    CONST_VP_DRAM_REFRESH_RATE_1X = "1x"
    CONST_VP_DRAM_REFRESH_RATE_2X = "2x"
    CONST_VP_DRAM_REFRESH_RATE_3X = "3x"
    CONST_VP_DRAM_REFRESH_RATE_4X = "4x"
    CONST_VP_DRAM_REFRESH_RATE_AUTO = "Auto"
    CONST_VP_DRAM_REFRESH_RATE_PLATFORM_DEFAULT = "platform-default"

class BiosVfHardwarePrefetch(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfHardwarePrefetch")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfHardwarePrefetch"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_HARDWARE_PREFETCH = "VpHardwarePrefetch"

    CONST_VP_HARDWARE_PREFETCH_DISABLED = "Disabled"
    CONST_VP_HARDWARE_PREFETCH_ENABLED = "Enabled"
    CONST__VP_HARDWARE_PREFETCH_DISABLED = "disabled"
    CONST__VP_HARDWARE_PREFETCH_ENABLED = "enabled"
    CONST_VP_HARDWARE_PREFETCH_PLATFORM_DEFAULT = "platform-default"

class BiosVfSerialPortAEnable(ManagedObject):
    """This class contains the relevant properties and constant supported by this MO."""
    def __init__(self):
        ManagedObject.__init__(self, "BiosVfSerialPortAEnable")

    @staticmethod
    def class_id():
        """This method returns the class_id string."""
        return "biosVfSerialPortAEnable"

    DN = "Dn"
    RN = "Rn"
    STATUS = "Status"
    VP_SERIAL_PORT_AENABLE = "VpSerialPortAEnable"

    CONST_VP_SERIAL_PORT_AENABLE_DISABLED = "Disabled"
    CONST_VP_SERIAL_PORT_AENABLE_ENABLED = "Enabled"
    CONST__VP_SERIAL_PORT_AENABLE_DISABLED = "disabled"
    CONST__VP_SERIAL_PORT_AENABLE_ENABLED = "enabled"
    CONST_VP_SERIAL_PORT_AENABLE_PLATFORM_DEFAULT = "platform-default"
