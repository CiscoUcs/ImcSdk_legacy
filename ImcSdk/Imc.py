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
It contains supporting classes for Filter and External Method.

ClassFactory Method: It returns the object of type ManagedObject, ExternalMethod
or supporting classes available in this module for a given className.
"""

try:
	import xml.etree.cElementTree as ET
	from xml.etree.cElementTree import Element, SubElement
except ImportError:
	import cElementTree as ET
	from cElementTree import Element, SubElement
import ImcUtils
from ImcCore import ImcBase, ManagedObject, ExternalMethod, AbstractFilter

def base_object(name):
    """This method returns the object if its not of type MO or ExternalMethod."""
    if name == "Method":
        return Method()
    elif name == "AllbitsFilter":
        return AllbitsFilter()
    elif name == "AndFilter":
        return AndFilter()
    elif name == "AnybitFilter":
        return AnybitFilter()
    elif name == "BwFilter":
        return BwFilter()
    elif name == "ConfigConfig":
        return ConfigConfig()
    elif name == "ConfigMap":
        return ConfigMap()
    elif name == "ConfigSet":
        return ConfigSet()
    elif name == "EqFilter":
        return EqFilter()
    elif name == "FilterFilter":
        return FilterFilter()
    elif name == "GeFilter":
        return GeFilter()
    elif name == "GtFilter":
        return GtFilter()
    elif name == "LeFilter":
        return LeFilter()
    elif name == "LtFilter":
        return LtFilter()
    elif name == "NeFilter":
        return NeFilter()
    elif name == "NotFilter":
        return NotFilter()
    elif name == "OrFilter":
        return OrFilter()
    elif name == "Pair":
        return Pair()
    elif name == "WcardFilter":
        return WcardFilter()
    else:
        return ManagedObject(ImcUtils.word_l(name))

def class_factory(name):
    """This method returns the object of type MO or ExternalMethod."""
    from ImcMoMeta import _MANAGED_OBJECT_META
    from ImcMethodMeta import _METHOD_FACTORY_META
    if name in _MANAGED_OBJECT_META:
        return ManagedObject(name)
    elif name in _METHOD_FACTORY_META:
        return ExternalMethod(name)
    else:
        return base_object(ImcUtils.word_u(name))

class Method(ImcBase):
    """Method Class."""
    def __init__(self):
        ImcBase.__init__(self, "Method")

    def add_child(self, mo):
        """This method adds child Method object to a Method object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the Method object."""
        if xml_doc is None:
            xml_obj=Element("method")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"method")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the Method object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the Method object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the Method object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "aaaGetComputeAuthTokens",
                    "aaaKeepAlive",
                    "aaaLogin",
                    "aaaLogout",
                    "aaaRefresh",
                    "configConfMo",
                    "configResolveChildren",
                    "configResolveClass",
                    "configResolveDn",
                    "configResolveParent",
                    "eventSubscribe",
                    "eventUnsubscribe",
                    "externalMethod",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class AllbitsFilter(AbstractFilter):
    """AllbitsFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "AllbitsFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child AllbitsFilter object to a AllbitsFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the AllbitsFilter object."""
        if xml_doc is None:
            xml_obj=Element("allbits")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"allbits")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the AllbitsFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the AllbitsFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the AllbitsFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class AndFilter(AbstractFilter):
    """AndFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "AndFilter")

    def add_child(self, mo):
        """This method adds child AndFilter object to a AndFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the AndFilter object."""
        if xml_doc is None:
            xml_obj=Element("and")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"and")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the AndFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the AndFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the AndFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "abstractFilter",
                    "allbits",
                    "and",
                    "anybit",
                    "bw",
                    "eq",
                    "ge",
                    "gt",
                    "le",
                    "lt",
                    "ne",
                    "not",
                    "or",
                    "wcard",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class AnybitFilter(AbstractFilter):
    """AnybitFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "AnybitFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child AnybitFilter object to a AnybitFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the AnybitFilter object."""
        if xml_doc is None:
            xml_obj=Element("anybit")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"anybit")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the AnybitFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the AnybitFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the AnybitFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class BwFilter(AbstractFilter):
    """BwFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "BwFilter")
        self.__class = None
        self.__first_value = None
        self.__property = None
        self.__second_value = None

    def add_child(self, mo):
        """This method adds child BwFilter object to a BwFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the BwFilter object."""
        if xml_doc is None:
            xml_obj=Element("bw")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"bw")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("firstValue", self.get_attr("FirstValue"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("secondValue", self.get_attr("SecondValue"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the BwFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the BwFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the BwFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class ConfigConfig(ImcBase):
    """ConfigConfig Class."""
    def __init__(self):
        ImcBase.__init__(self, "ConfigConfig")

    def add_child(self, mo):
        """This method adds child ConfigConfig object to a ConfigConfig object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the ConfigConfig object."""
        if xml_doc is None:
            xml_obj=Element("configConfig")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"configConfig")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the ConfigConfig object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the ConfigConfig object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the ConfigConfig object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "aaaLdap",
                    "aaaLdapRoleGroup",
                    "aaaSession",
                    "aaaUser",
                    "aaaUserEp",
                    "adaptorCfgBackup",
                    "adaptorCfgImporter",
                    "adaptorConnectorInfo",
                    "adaptorEthCompQueueProfile",
                    "adaptorEthGenProfile",
                    "adaptorEthISCSIProfile",
                    "adaptorEthInterruptProfile",
                    "adaptorEthOffloadProfile",
                    "adaptorEthRecvQueueProfile",
                    "adaptorEthUSNICProfile",
                    "adaptorEthWorkQueueProfile",
                    "adaptorExtEthIf",
                    "adaptorExtIpV6RssHashProfile",
                    "adaptorFcBootTable",
                    "adaptorFcCdbWorkQueueProfile",
                    "adaptorFcErrorRecoveryProfile",
                    "adaptorFcGenProfile",
                    "adaptorFcInterruptProfile",
                    "adaptorFcPersistentBindings",
                    "adaptorFcPortFLogiProfile",
                    "adaptorFcPortPLogiProfile",
                    "adaptorFcPortProfile",
                    "adaptorFcRecvQueueProfile",
                    "adaptorFcWorkQueueProfile",
                    "adaptorGenProfile",
                    "adaptorHostEthIf",
                    "adaptorHostFcIf",
                    "adaptorIpV4RssHashProfile",
                    "adaptorIpV6RssHashProfile",
                    "adaptorLinkTraining",
                    "adaptorPortProfiles",
                    "adaptorRssProfile",
                    "adaptorUnit",
                    "adaptorVMFexEthIf",
                    "adaptorVMFexEthProfile",
                    "advancedPowerProfile",
                    "biosBOT",
                    "biosBootDev",
                    "biosBootDevGrp",
                    "biosBootDevPrecision",
                    "biosBootMode",
                    "biosPassword",
                    "biosPlatformDefaults",
                    "biosSettings",
                    "biosUnit",
                    "biosVfASPMSupport",
                    "biosVfAdjacentCacheLinePrefetch",
                    "biosVfAltitude",
                    "biosVfAssertNMIOnPERR",
                    "biosVfAssertNMIOnSERR",
                    "biosVfBootOptionRetry",
                    "biosVfCDNEnable",
                    "biosVfCDNSupport",
                    "biosVfCPUEnergyPerformance",
                    "biosVfCPUFrequencyFloor",
                    "biosVfCPUPerformance",
                    "biosVfCPUPowerManagement",
                    "biosVfCkeLowPolicy",
                    "biosVfConsoleRedirection",
                    "biosVfCoreMultiProcessing",
                    "biosVfDCUPrefetch",
                    "biosVfDRAMClockThrottling",
                    "biosVfDemandScrub",
                    "biosVfDirectCacheAccess",
                    "biosVfDramRefreshRate",
                    "biosVfEnhancedIntelSpeedStepTech",
                    "biosVfExecuteDisableBit",
                    "biosVfExtendedAPIC",
                    "biosVfFRB2Enable",
                    "biosVfHardwarePrefetch",
                    "biosVfIOHResource",
                    "biosVfIntelHyperThreadingTech",
                    "biosVfIntelTurboBoostTech",
                    "biosVfIntelVTForDirectedIO",
                    "biosVfIntelVirtualizationTechnology",
                    "biosVfLOMPortOptionROM",
                    "biosVfLegacyUSBSupport",
                    "biosVfLvDIMMSupport",
                    "biosVfMMCFGBase",
                    "biosVfMemoryInterleave",
                    "biosVfMemoryMappedIOAbove4GB",
                    "biosVfMirroringMode",
                    "biosVfNUMAOptimized",
                    "biosVfOSBootWatchdogTimer",
                    "biosVfOSBootWatchdogTimerPolicy",
                    "biosVfOSBootWatchdogTimerTimeout",
                    "biosVfOnboardNIC",
                    "biosVfOnboardStorage",
                    "biosVfOnboardStorageSWStack",
                    "biosVfOutOfBandMgmtPort",
                    "biosVfPCIOptionROMs",
                    "biosVfPCISlotOptionROMEnable",
                    "biosVfPOSTErrorPause",
                    "biosVfPStateCoordType",
                    "biosVfPackageCStateLimit",
                    "biosVfPatrolScrub",
                    "biosVfPatrolScrubDuration",
                    "biosVfPchUsb30Mode",
                    "biosVfPciRomClp",
                    "biosVfProcessorC1E",
                    "biosVfProcessorC3Report",
                    "biosVfProcessorC6Report",
                    "biosVfProcessorCState",
                    "biosVfPwrPerfTuning",
                    "biosVfQPIConfig",
                    "biosVfQpiSnoopMode",
                    "biosVfResumeOnACPowerLoss",
                    "biosVfSataModeSelect",
                    "biosVfSelectMemoryRASConfiguration",
                    "biosVfSerialPortAEnable",
                    "biosVfSparingMode",
                    "biosVfSrIov",
                    "biosVfTPMSupport",
                    "biosVfUCSMBootOrderRuleControl",
                    "biosVfUSBBootConfig",
                    "biosVfUSBEmulation",
                    "biosVfUSBPortsConfig",
                    "biosVfVgaPriority",
                    "biosVfWorkLoadConfig",
                    "commHttp",
                    "commHttps",
                    "commIpmiLan",
                    "commKvm",
                    "commNtpProvider",
                    "commSnmp",
                    "commSnmpTrap",
                    "commSnmpUser",
                    "commSsh",
                    "commSvcEp",
                    "commSyslog",
                    "commSyslogClient",
                    "commVMedia",
                    "commVMediaMap",
                    "computeBoard",
                    "computeMbPowerStats",
                    "computeRackUnit",
                    "computeRackUnitMbTempStats",
                    "equipmentFan",
                    "equipmentFanModule",
                    "equipmentIndicatorLed",
                    "equipmentLocatorLed",
                    "equipmentPsu",
                    "equipmentPsuColdRedundancy",
                    "equipmentPsuFan",
                    "equipmentTpm",
                    "error",
                    "faultInst",
                    "firmwareBootDefinition",
                    "firmwareBootUnit",
                    "firmwareRunning",
                    "firmwareUpdatable",
                    "huuController",
                    "huuFirmwareCatalog",
                    "huuFirmwareCatalogComponent",
                    "huuFirmwareComponent",
                    "huuFirmwareRunning",
                    "huuFirmwareUpdateCancel",
                    "huuFirmwareUpdateStatus",
                    "huuFirmwareUpdater",
                    "huuUpdateComponentStatus",
                    "iodController",
                    "iodSnapshotCancel",
                    "iodSnapshotStart",
                    "iodSnapshotStatus",
                    "ipBlocking",
                    "lsbootBootSecurity",
                    "lsbootDef",
                    "lsbootDevPrecision",
                    "lsbootEfi",
                    "lsbootHdd",
                    "lsbootIscsi",
                    "lsbootLan",
                    "lsbootLocalStorage",
                    "lsbootPchStorage",
                    "lsbootPxe",
                    "lsbootSan",
                    "lsbootSd",
                    "lsbootStorage",
                    "lsbootUefiShell",
                    "lsbootUsb",
                    "lsbootVMedia",
                    "lsbootVirtualMedia",
                    "managedObject",
                    "memoryArray",
                    "memoryUnit",
                    "memoryUnitEnvStats",
                    "mgmtBackup",
                    "mgmtController",
                    "mgmtIf",
                    "mgmtImporter",
                    "networkAdapterEthIf",
                    "networkAdapterUnit",
                    "oneTimeBootDevice",
                    "pciEquipSlot",
                    "pidCatalog",
                    "pidCatalogCpu",
                    "pidCatalogDimm",
                    "pidCatalogHdd",
                    "pidCatalogPCIAdapter",
                    "powerBudget",
                    "powerMonitor",
                    "processorEnvStats",
                    "processorUnit",
                    "serverUtilization",
                    "solIf",
                    "standardPowerProfile",
                    "storageController",
                    "storageControllerProps",
                    "storageControllerSettings",
                    "storageFlexFlashController",
                    "storageFlexFlashControllerProps",
                    "storageFlexFlashOperationalProfile",
                    "storageFlexFlashPhysicalDrive",
                    "storageFlexFlashVirtualDrive",
                    "storageFlexFlashVirtualDriveImageMap",
                    "storageLocalDisk",
                    "storageLocalDiskProps",
                    "storageLocalDiskSlotEp",
                    "storageLocalDiskUsage",
                    "storageOperation",
                    "storageRaidBattery",
                    "storageUnusedLocalDisk",
                    "storageVirtualDrive",
                    "storageVirtualDriveCreatorUsingUnusedPhysicalDrive",
                    "storageVirtualDriveCreatorUsingVirtualDriveGroup",
                    "storageVirtualDriveWithDriveGroupSpace",
                    "sysdebugMEpLog",
                    "sysdebugTechSupportExport",
                    "systemIOController",
                    "topRoot",
                    "topSystem",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class ConfigMap(ImcBase):
    """ConfigMap Class."""
    def __init__(self):
        ImcBase.__init__(self, "ConfigMap")

    def add_child(self, mo):
        """This method adds child ConfigMap object to a ConfigMap object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the ConfigMap object."""
        if xml_doc is None:
            xml_obj=Element("configMap")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"configMap")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the ConfigMap object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the ConfigMap object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the ConfigMap object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "pair",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class ConfigSet(ImcBase):
    """ConfigSet Class."""
    def __init__(self):
        ImcBase.__init__(self, "ConfigSet")

    def add_child(self, mo):
        """This method adds child ConfigSet object to a ConfigSet object."""
        self._child.append(mo)

    def set_attr(self, key, value):
        """This method sets attribute value of the ConfigSet object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the ConfigSet object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the ConfigSet object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "aaaLdap",
                    "aaaLdapRoleGroup",
                    "aaaSession",
                    "aaaUser",
                    "aaaUserEp",
                    "adaptorCfgBackup",
                    "adaptorCfgImporter",
                    "adaptorConnectorInfo",
                    "adaptorEthCompQueueProfile",
                    "adaptorEthGenProfile",
                    "adaptorEthISCSIProfile",
                    "adaptorEthInterruptProfile",
                    "adaptorEthOffloadProfile",
                    "adaptorEthRecvQueueProfile",
                    "adaptorEthUSNICProfile",
                    "adaptorEthWorkQueueProfile",
                    "adaptorExtEthIf",
                    "adaptorExtIpV6RssHashProfile",
                    "adaptorFcBootTable",
                    "adaptorFcCdbWorkQueueProfile",
                    "adaptorFcErrorRecoveryProfile",
                    "adaptorFcGenProfile",
                    "adaptorFcInterruptProfile",
                    "adaptorFcPersistentBindings",
                    "adaptorFcPortFLogiProfile",
                    "adaptorFcPortPLogiProfile",
                    "adaptorFcPortProfile",
                    "adaptorFcRecvQueueProfile",
                    "adaptorFcWorkQueueProfile",
                    "adaptorGenProfile",
                    "adaptorHostEthIf",
                    "adaptorHostFcIf",
                    "adaptorIpV4RssHashProfile",
                    "adaptorIpV6RssHashProfile",
                    "adaptorLinkTraining",
                    "adaptorPortProfiles",
                    "adaptorRssProfile",
                    "adaptorUnit",
                    "adaptorVMFexEthIf",
                    "adaptorVMFexEthProfile",
                    "advancedPowerProfile",
                    "biosBOT",
                    "biosBootDev",
                    "biosBootDevGrp",
                    "biosBootDevPrecision",
                    "biosBootMode",
                    "biosPassword",
                    "biosPlatformDefaults",
                    "biosSettings",
                    "biosUnit",
                    "biosVfASPMSupport",
                    "biosVfAdjacentCacheLinePrefetch",
                    "biosVfAltitude",
                    "biosVfAssertNMIOnPERR",
                    "biosVfAssertNMIOnSERR",
                    "biosVfBootOptionRetry",
                    "biosVfCDNEnable",
                    "biosVfCDNSupport",
                    "biosVfCPUEnergyPerformance",
                    "biosVfCPUFrequencyFloor",
                    "biosVfCPUPerformance",
                    "biosVfCPUPowerManagement",
                    "biosVfCkeLowPolicy",
                    "biosVfConsoleRedirection",
                    "biosVfCoreMultiProcessing",
                    "biosVfDCUPrefetch",
                    "biosVfDRAMClockThrottling",
                    "biosVfDemandScrub",
                    "biosVfDirectCacheAccess",
                    "biosVfDramRefreshRate",
                    "biosVfEnhancedIntelSpeedStepTech",
                    "biosVfExecuteDisableBit",
                    "biosVfExtendedAPIC",
                    "biosVfFRB2Enable",
                    "biosVfHardwarePrefetch",
                    "biosVfIOHResource",
                    "biosVfIntelHyperThreadingTech",
                    "biosVfIntelTurboBoostTech",
                    "biosVfIntelVTForDirectedIO",
                    "biosVfIntelVirtualizationTechnology",
                    "biosVfLOMPortOptionROM",
                    "biosVfLegacyUSBSupport",
                    "biosVfLvDIMMSupport",
                    "biosVfMMCFGBase",
                    "biosVfMemoryInterleave",
                    "biosVfMemoryMappedIOAbove4GB",
                    "biosVfMirroringMode",
                    "biosVfNUMAOptimized",
                    "biosVfOSBootWatchdogTimer",
                    "biosVfOSBootWatchdogTimerPolicy",
                    "biosVfOSBootWatchdogTimerTimeout",
                    "biosVfOnboardNIC",
                    "biosVfOnboardStorage",
                    "biosVfOnboardStorageSWStack",
                    "biosVfOutOfBandMgmtPort",
                    "biosVfPCIOptionROMs",
                    "biosVfPCISlotOptionROMEnable",
                    "biosVfPOSTErrorPause",
                    "biosVfPStateCoordType",
                    "biosVfPackageCStateLimit",
                    "biosVfPatrolScrub",
                    "biosVfPatrolScrubDuration",
                    "biosVfPchUsb30Mode",
                    "biosVfPciRomClp",
                    "biosVfProcessorC1E",
                    "biosVfProcessorC3Report",
                    "biosVfProcessorC6Report",
                    "biosVfProcessorCState",
                    "biosVfPwrPerfTuning",
                    "biosVfQPIConfig",
                    "biosVfQpiSnoopMode",
                    "biosVfResumeOnACPowerLoss",
                    "biosVfSataModeSelect",
                    "biosVfSelectMemoryRASConfiguration",
                    "biosVfSerialPortAEnable",
                    "biosVfSparingMode",
                    "biosVfSrIov",
                    "biosVfTPMSupport",
                    "biosVfUCSMBootOrderRuleControl",
                    "biosVfUSBBootConfig",
                    "biosVfUSBEmulation",
                    "biosVfUSBPortsConfig",
                    "biosVfVgaPriority",
                    "biosVfWorkLoadConfig",
                    "commHttp",
                    "commHttps",
                    "commIpmiLan",
                    "commKvm",
                    "commNtpProvider",
                    "commSnmp",
                    "commSnmpTrap",
                    "commSnmpUser",
                    "commSsh",
                    "commSvcEp",
                    "commSyslog",
                    "commSyslogClient",
                    "commVMedia",
                    "commVMediaMap",
                    "computeBoard",
                    "computeMbPowerStats",
                    "computeRackUnit",
                    "computeRackUnitMbTempStats",
                    "equipmentFan",
                    "equipmentFanModule",
                    "equipmentIndicatorLed",
                    "equipmentLocatorLed",
                    "equipmentPsu",
                    "equipmentPsuColdRedundancy",
                    "equipmentPsuFan",
                    "equipmentTpm",
                    "error",
                    "faultInst",
                    "firmwareBootDefinition",
                    "firmwareBootUnit",
                    "firmwareRunning",
                    "firmwareUpdatable",
                    "huuController",
                    "huuFirmwareCatalog",
                    "huuFirmwareCatalogComponent",
                    "huuFirmwareComponent",
                    "huuFirmwareRunning",
                    "huuFirmwareUpdateCancel",
                    "huuFirmwareUpdateStatus",
                    "huuFirmwareUpdater",
                    "huuUpdateComponentStatus",
                    "iodController",
                    "iodSnapshotCancel",
                    "iodSnapshotStart",
                    "iodSnapshotStatus",
                    "ipBlocking",
                    "lsbootBootSecurity",
                    "lsbootDef",
                    "lsbootDevPrecision",
                    "lsbootEfi",
                    "lsbootHdd",
                    "lsbootIscsi",
                    "lsbootLan",
                    "lsbootLocalStorage",
                    "lsbootPchStorage",
                    "lsbootPxe",
                    "lsbootSan",
                    "lsbootSd",
                    "lsbootStorage",
                    "lsbootUefiShell",
                    "lsbootUsb",
                    "lsbootVMedia",
                    "lsbootVirtualMedia",
                    "managedObject",
                    "memoryArray",
                    "memoryUnit",
                    "memoryUnitEnvStats",
                    "mgmtBackup",
                    "mgmtController",
                    "mgmtIf",
                    "mgmtImporter",
                    "networkAdapterEthIf",
                    "networkAdapterUnit",
                    "oneTimeBootDevice",
                    "pciEquipSlot",
                    "pidCatalog",
                    "pidCatalogCpu",
                    "pidCatalogDimm",
                    "pidCatalogHdd",
                    "pidCatalogPCIAdapter",
                    "powerBudget",
                    "powerMonitor",
                    "processorEnvStats",
                    "processorUnit",
                    "serverUtilization",
                    "solIf",
                    "standardPowerProfile",
                    "storageController",
                    "storageControllerProps",
                    "storageControllerSettings",
                    "storageFlexFlashController",
                    "storageFlexFlashControllerProps",
                    "storageFlexFlashOperationalProfile",
                    "storageFlexFlashPhysicalDrive",
                    "storageFlexFlashVirtualDrive",
                    "storageFlexFlashVirtualDriveImageMap",
                    "storageLocalDisk",
                    "storageLocalDiskProps",
                    "storageLocalDiskSlotEp",
                    "storageLocalDiskUsage",
                    "storageOperation",
                    "storageRaidBattery",
                    "storageUnusedLocalDisk",
                    "storageVirtualDrive",
                    "storageVirtualDriveCreatorUsingUnusedPhysicalDrive",
                    "storageVirtualDriveCreatorUsingVirtualDriveGroup",
                    "storageVirtualDriveWithDriveGroupSpace",
                    "sysdebugMEpLog",
                    "sysdebugTechSupportExport",
                    "systemIOController",
                    "topRoot",
                    "topSystem",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class EqFilter(AbstractFilter):
    """EqFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "EqFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child EqFilter object to a EqFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the EqFilter object."""
        if xml_doc is None:
            xml_obj=Element("eq")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"eq")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the EqFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the EqFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the EqFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class FilterFilter(ImcBase):
    """FilterFilter Class."""
    def __init__(self):
        ImcBase.__init__(self, "FilterFilter")

    def add_child(self, mo):
        """This method adds child FilterFilter object to a FilterFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the FilterFilter object."""
        if xml_doc is None:
            xml_obj=Element("filter")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"filter")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the FilterFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the FilterFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the FilterFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "abstractFilter",
                    "allbits",
                    "and",
                    "anybit",
                    "bw",
                    "eq",
                    "ge",
                    "gt",
                    "le",
                    "lt",
                    "ne",
                    "not",
                    "or",
                    "wcard",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class GeFilter(AbstractFilter):
    """GeFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "GeFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child GeFilter object to a GeFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the GeFilter object."""
        if xml_doc is None:
            xml_obj=Element("ge")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"ge")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the GeFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the GeFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the GeFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class GtFilter(AbstractFilter):
    """GtFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "GtFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child GtFilter object to a GtFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the GtFilter object."""
        if xml_doc is None:
            xml_obj=Element("gt")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"gt")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the GtFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the GtFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the GtFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class LeFilter(AbstractFilter):
    """LeFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "LeFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child LeFilter object to a LeFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the LeFilter object."""
        if xml_doc is None:
            xml_obj=Element("le")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"le")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the LeFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the LeFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the LeFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class LtFilter(AbstractFilter):
    """LtFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "LtFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child LtFilter object to a LtFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the LtFilter object."""
        if xml_doc is None:
            xml_obj=Element("lt")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"lt")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the LtFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the LtFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the LtFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class NeFilter(AbstractFilter):
    """NeFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "NeFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child NeFilter object to a NeFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the NeFilter object."""
        if xml_doc is None:
            xml_obj=Element("ne")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"ne")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the NeFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the NeFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the NeFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class NotFilter(AbstractFilter):
    """NotFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "NotFilter")

    def add_child(self, mo):
        """This method adds child NotFilter object to a NotFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the NotFilter object."""
        if xml_doc is None:
            xml_obj=Element("not")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"not")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the NotFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the NotFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the NotFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "abstractFilter",
                    "allbits",
                    "and",
                    "anybit",
                    "bw",
                    "eq",
                    "ge",
                    "gt",
                    "le",
                    "lt",
                    "ne",
                    "not",
                    "or",
                    "wcard",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class OrFilter(AbstractFilter):
    """OrFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "OrFilter")

    def add_child(self, mo):
        """This method adds child OrFilter object to a OrFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the OrFilter object."""
        if xml_doc is None:
            xml_obj=Element("or")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"or")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the OrFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the OrFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the OrFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "abstractFilter",
                    "allbits",
                    "and",
                    "anybit",
                    "bw",
                    "eq",
                    "ge",
                    "gt",
                    "le",
                    "lt",
                    "ne",
                    "not",
                    "or",
                    "wcard",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class Pair(ImcBase):
    """Pair Class."""
    def __init__(self):
        ImcBase.__init__(self, "Pair")
        self.__key = None

    def add_child(self, mo):
        """This method adds child Pair object to a Pair object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the Pair object."""
        if xml_doc is None:
            xml_obj=Element("pair")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"pair")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("key", self.get_attr("Key"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the Pair object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the Pair object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the Pair object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                    "aaaLdap",
                    "aaaLdapRoleGroup",
                    "aaaSession",
                    "aaaUser",
                    "aaaUserEp",
                    "adaptorCfgBackup",
                    "adaptorCfgImporter",
                    "adaptorConnectorInfo",
                    "adaptorEthCompQueueProfile",
                    "adaptorEthGenProfile",
                    "adaptorEthISCSIProfile",
                    "adaptorEthInterruptProfile",
                    "adaptorEthOffloadProfile",
                    "adaptorEthRecvQueueProfile",
                    "adaptorEthUSNICProfile",
                    "adaptorEthWorkQueueProfile",
                    "adaptorExtEthIf",
                    "adaptorExtIpV6RssHashProfile",
                    "adaptorFcBootTable",
                    "adaptorFcCdbWorkQueueProfile",
                    "adaptorFcErrorRecoveryProfile",
                    "adaptorFcGenProfile",
                    "adaptorFcInterruptProfile",
                    "adaptorFcPersistentBindings",
                    "adaptorFcPortFLogiProfile",
                    "adaptorFcPortPLogiProfile",
                    "adaptorFcPortProfile",
                    "adaptorFcRecvQueueProfile",
                    "adaptorFcWorkQueueProfile",
                    "adaptorGenProfile",
                    "adaptorHostEthIf",
                    "adaptorHostFcIf",
                    "adaptorIpV4RssHashProfile",
                    "adaptorIpV6RssHashProfile",
                    "adaptorLinkTraining",
                    "adaptorPortProfiles",
                    "adaptorRssProfile",
                    "adaptorUnit",
                    "adaptorVMFexEthIf",
                    "adaptorVMFexEthProfile",
                    "advancedPowerProfile",
                    "biosBOT",
                    "biosBootDev",
                    "biosBootDevGrp",
                    "biosBootDevPrecision",
                    "biosBootMode",
                    "biosPassword",
                    "biosPlatformDefaults",
                    "biosSettings",
                    "biosUnit",
                    "biosVfASPMSupport",
                    "biosVfAdjacentCacheLinePrefetch",
                    "biosVfAltitude",
                    "biosVfAssertNMIOnPERR",
                    "biosVfAssertNMIOnSERR",
                    "biosVfBootOptionRetry",
                    "biosVfCDNEnable",
                    "biosVfCDNSupport",
                    "biosVfCPUEnergyPerformance",
                    "biosVfCPUFrequencyFloor",
                    "biosVfCPUPerformance",
                    "biosVfCPUPowerManagement",
                    "biosVfCkeLowPolicy",
                    "biosVfConsoleRedirection",
                    "biosVfCoreMultiProcessing",
                    "biosVfDCUPrefetch",
                    "biosVfDRAMClockThrottling",
                    "biosVfDemandScrub",
                    "biosVfDirectCacheAccess",
                    "biosVfDramRefreshRate",
                    "biosVfEnhancedIntelSpeedStepTech",
                    "biosVfExecuteDisableBit",
                    "biosVfExtendedAPIC",
                    "biosVfFRB2Enable",
                    "biosVfHardwarePrefetch",
                    "biosVfIOHResource",
                    "biosVfIntelHyperThreadingTech",
                    "biosVfIntelTurboBoostTech",
                    "biosVfIntelVTForDirectedIO",
                    "biosVfIntelVirtualizationTechnology",
                    "biosVfLOMPortOptionROM",
                    "biosVfLegacyUSBSupport",
                    "biosVfLvDIMMSupport",
                    "biosVfMMCFGBase",
                    "biosVfMemoryInterleave",
                    "biosVfMemoryMappedIOAbove4GB",
                    "biosVfMirroringMode",
                    "biosVfNUMAOptimized",
                    "biosVfOSBootWatchdogTimer",
                    "biosVfOSBootWatchdogTimerPolicy",
                    "biosVfOSBootWatchdogTimerTimeout",
                    "biosVfOnboardNIC",
                    "biosVfOnboardStorage",
                    "biosVfOnboardStorageSWStack",
                    "biosVfOutOfBandMgmtPort",
                    "biosVfPCIOptionROMs",
                    "biosVfPCISlotOptionROMEnable",
                    "biosVfPOSTErrorPause",
                    "biosVfPStateCoordType",
                    "biosVfPackageCStateLimit",
                    "biosVfPatrolScrub",
                    "biosVfPatrolScrubDuration",
                    "biosVfPchUsb30Mode",
                    "biosVfPciRomClp",
                    "biosVfProcessorC1E",
                    "biosVfProcessorC3Report",
                    "biosVfProcessorC6Report",
                    "biosVfProcessorCState",
                    "biosVfPwrPerfTuning",
                    "biosVfQPIConfig",
                    "biosVfQpiSnoopMode",
                    "biosVfResumeOnACPowerLoss",
                    "biosVfSataModeSelect",
                    "biosVfSelectMemoryRASConfiguration",
                    "biosVfSerialPortAEnable",
                    "biosVfSparingMode",
                    "biosVfSrIov",
                    "biosVfTPMSupport",
                    "biosVfUCSMBootOrderRuleControl",
                    "biosVfUSBBootConfig",
                    "biosVfUSBEmulation",
                    "biosVfUSBPortsConfig",
                    "biosVfVgaPriority",
                    "biosVfWorkLoadConfig",
                    "commHttp",
                    "commHttps",
                    "commIpmiLan",
                    "commKvm",
                    "commNtpProvider",
                    "commSnmp",
                    "commSnmpTrap",
                    "commSnmpUser",
                    "commSsh",
                    "commSvcEp",
                    "commSyslog",
                    "commSyslogClient",
                    "commVMedia",
                    "commVMediaMap",
                    "computeBoard",
                    "computeMbPowerStats",
                    "computeRackUnit",
                    "computeRackUnitMbTempStats",
                    "equipmentFan",
                    "equipmentFanModule",
                    "equipmentIndicatorLed",
                    "equipmentLocatorLed",
                    "equipmentPsu",
                    "equipmentPsuColdRedundancy",
                    "equipmentPsuFan",
                    "equipmentTpm",
                    "error",
                    "faultInst",
                    "firmwareBootDefinition",
                    "firmwareBootUnit",
                    "firmwareRunning",
                    "firmwareUpdatable",
                    "huuController",
                    "huuFirmwareCatalog",
                    "huuFirmwareCatalogComponent",
                    "huuFirmwareComponent",
                    "huuFirmwareRunning",
                    "huuFirmwareUpdateCancel",
                    "huuFirmwareUpdateStatus",
                    "huuFirmwareUpdater",
                    "huuUpdateComponentStatus",
                    "iodController",
                    "iodSnapshotCancel",
                    "iodSnapshotStart",
                    "iodSnapshotStatus",
                    "ipBlocking",
                    "lsbootBootSecurity",
                    "lsbootDef",
                    "lsbootDevPrecision",
                    "lsbootEfi",
                    "lsbootHdd",
                    "lsbootIscsi",
                    "lsbootLan",
                    "lsbootLocalStorage",
                    "lsbootPchStorage",
                    "lsbootPxe",
                    "lsbootSan",
                    "lsbootSd",
                    "lsbootStorage",
                    "lsbootUefiShell",
                    "lsbootUsb",
                    "lsbootVMedia",
                    "lsbootVirtualMedia",
                    "managedObject",
                    "memoryArray",
                    "memoryUnit",
                    "memoryUnitEnvStats",
                    "mgmtBackup",
                    "mgmtController",
                    "mgmtIf",
                    "mgmtImporter",
                    "networkAdapterEthIf",
                    "networkAdapterUnit",
                    "oneTimeBootDevice",
                    "pciEquipSlot",
                    "pidCatalog",
                    "pidCatalogCpu",
                    "pidCatalogDimm",
                    "pidCatalogHdd",
                    "pidCatalogPCIAdapter",
                    "powerBudget",
                    "powerMonitor",
                    "processorEnvStats",
                    "processorUnit",
                    "serverUtilization",
                    "solIf",
                    "standardPowerProfile",
                    "storageController",
                    "storageControllerProps",
                    "storageControllerSettings",
                    "storageFlexFlashController",
                    "storageFlexFlashControllerProps",
                    "storageFlexFlashOperationalProfile",
                    "storageFlexFlashPhysicalDrive",
                    "storageFlexFlashVirtualDrive",
                    "storageFlexFlashVirtualDriveImageMap",
                    "storageLocalDisk",
                    "storageLocalDiskProps",
                    "storageLocalDiskSlotEp",
                    "storageLocalDiskUsage",
                    "storageOperation",
                    "storageRaidBattery",
                    "storageUnusedLocalDisk",
                    "storageVirtualDrive",
                    "storageVirtualDriveCreatorUsingUnusedPhysicalDrive",
                    "storageVirtualDriveCreatorUsingVirtualDriveGroup",
                    "storageVirtualDriveWithDriveGroupSpace",
                    "sysdebugMEpLog",
                    "sysdebugTechSupportExport",
                    "systemIOController",
                    "topRoot",
                    "topSystem",
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

class WcardFilter(AbstractFilter):
    """WcardFilter Class."""
    def __init__(self):
        AbstractFilter.__init__(self, "WcardFilter")
        self.__class = None
        self.__property = None
        self.__value = None

    def add_child(self, mo):
        """This method adds child WcardFilter object to a WcardFilter object."""
        self._child.append(mo)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """This method writes the xml representation of the WcardFilter object."""
        if xml_doc is None:
            xml_obj=Element("wcard")
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,"wcard")
            else:
                xml_obj = SubElement(xml_doc, element_name)
        xml_obj.set("class", self.get_attr("Class"))
        xml_obj.set("property", self.get_attr("Property"))
        xml_obj.set("value", self.get_attr("Value"))
        self.child_write_xml(xml_obj, option)
        return xml_obj

    def set_attr(self, key, value):
        """This method sets attribute value of the WcardFilter object."""
        self.__dict__[key] = value

    def get_attr(self, key):
        """This method gets attribute value of the WcardFilter object."""
        return self.__dict__[key]

    def load_from_xml(self, element, handle):
        """This method creates the object from the xml representation of the WcardFilter object."""
        self.set_handle(handle)

        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.setattr(ImcUtils.word_u(attr_name), str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element):
                    continue
                child_field_names = [
                ]

                cln = ImcUtils.word_u(child_element.tag)
                child = class_factory(cln)
                self._child.append(child)
                child.load_from_xml(child_element, handle)

