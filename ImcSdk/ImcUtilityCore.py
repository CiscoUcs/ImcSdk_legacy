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
""" This  module contains the supporting methods for ImcUtility Module. """

import os
import re

import ImcUtils
from ImcCoreMeta import ImcVersion
from ImcCore import CoreUtils, MoPropertyMeta


class ImcConstant(object):
    """
    ImcHandleConstant class is used as enum for storing constant used in API exposed by ImcHandle.
    """
    TIME_OUT_IN_SEC = 600
    POLL_INTERVAL_IN_SEC = 2

class _ImcLoginXml(object):
    """ Internal class to support Export and Import Imc Session. """
    IMC_HANDLES = "Imchandles"
    IMC = "Imc"
    NAME = "name"
    USER_NAME = "username"
    NO_SSL = "nossl"
    PORT = "port"
    PASSWORD = "password"

class _ImcMoDiff(object):
    """
    This class structures an object which will be creatd by compare_imc_managedobject and contains all the information
    about the difference object which will be used by the sync_imc_managedobject method.
    """
    REMOVE = "<="
    ADD_MODIFY = "=>"
    EQUAL = "=="

    def __init__(self, input_object, side_indicator, diff_property=None, ref_values=None, diff_values=None):
        self.input_object = input_object
        self.dn = input_object.Dn
        self.side_indicator = side_indicator
        self.diff_property = diff_property
        self.ref_prop_values = ref_values
        self.diff_prop_values = diff_values

def write_mo_diff(diff_obj):
    """ Writes the difference managedObject(output of CompareManagedObject) on the terminal. """
    diff_obj
    tab_size = 8
#    print str(diff_obj.dn).ljust(tab_size*10), str(diff_obj.input_object.prop_mo_meta.name).ljust(tab_size*4), str(diff_obj.side_indicator).ljust(tab_size*3), str(diff_obj.diff_property)
    if isinstance(diff_obj, list) == True and len(diff_obj) > 0:
        if isinstance(diff_obj[0], _ImcMoDiff):
            print "dn".ljust(tab_size*10), "input_object".ljust(tab_size*4), "side_indicator".ljust(tab_size*3), "diff_property"
            print "--".ljust(tab_size*10), "-----------".ljust(tab_size*4), "-------------".ljust(tab_size*3), "------------"
        for mo in diff_obj:
            if isinstance(mo, _ImcMoDiff) == True:
                print str(mo.dn).ljust(tab_size*10), str(mo.input_object.prop_mo_meta.name).ljust(tab_size*4), str(mo.side_indicator).ljust(tab_size*3), str(mo.diff_property)

    

class _SyncAction(object):
    """ Internal class to support sync_imc_managedobject functionality. """
    STATUS_CHANGE = "STATUS_CHANGE"
    IGNORE = "IGNORE"
    NONE = "NONE"

class _SyncMoConfig(object):
    """ Internal class to support sync_imc_managedobject functionality. """

    def __init__(self, class_id, noun, version, action_version, action, ignore_reason, status, exclude_list):
        self.__class_id = class_id
        self.__noun = noun

        if version:
            self.__version = ImcVersion(version)
        else:
            self.__version = None

        if action_version:
            self.__action_version = ImcVersion(action_version)
        else:
            self.__action_version = None

        self.__status = status

        if action.strip().lower() == "statusChange".lower():
            self.__action = _SyncAction.STATUS_CHANGE
        elif action.strip().lower() == "ignore".lower():
            self.__action = _SyncAction.IGNORE
        else:
            self.__action = _SyncAction.NONE

        if exclude_list:
            self.__exclude_list = exclude_list.split(",")
        else:
            self.__exclude_list = None

        ir_map = {}
        if ignore_reason and self.__action == _SyncAction.IGNORE:

            pairs = ignore_reason.strip().split(",")
            for pair in pairs:
                key_val = pair.strip().split("=")
                if key_val is None or len(key_val) != 2:
                    continue
                ir_map[key_val[0]] = key_val[1]

        if ir_map:
            self.__ignore_reason = ir_map

    @property
    def class_id(self):
        """Getter Method of _SyncAction Class"""
        return self.__class_id

    @property
    def noun(self):
        """Getter Method of _SyncAction Class"""
        return self.__noun

    @property
    def version(self):
        """Getter Method of _SyncAction Class"""
        return self.__version

    @property
    def action_version(self):
        """Getter Method of _SyncAction Class"""
        return self.__action_version

    @property
    def action(self):
        """Getter Method of _SyncAction Class"""
        return self.__action

    @property
    def status(self):
        """Getter Method of _SyncAction Class"""
        return self.__status

    @property
    def exclude_list(self):
        """Getter Method of _SyncAction Class"""
        return self.__exclude_list

    @property
    def ignore_reason(self):
        """Getter Method of _SyncAction Class"""
        return self.__ignore_reason


def _get_sync_mo_config_file_path():
    """ Method returs the path of _SyncAction.xml file. """
    return os.path.join(os.path.join(os.path.dirname(__file__), "resources"), "_SyncAction.xml")

def _get_sync_mo_config(config_doc):
    """ Internal support method for sync_imc_managedobject. """
    mo_config_map = {}
    config_list = config_doc.getElementsByTagName("mo")

    for mo_config_node in config_list:
        class_id = None
        noun = None
        version = None
        action_version = None
        action = None
        ignore_reason = None
        status = None
        exclude_list = None

        if mo_config_node.hasAttribute("class_id"):
            class_id = mo_config_node.getAttribute("class_id")

        if mo_config_node.hasAttribute("noun"):
            noun = mo_config_node.getAttribute("noun")

        if mo_config_node.hasAttribute("version"):
            version = mo_config_node.getAttribute("version")

        if mo_config_node.hasAttribute("action_version"):
            action_version = mo_config_node.getAttribute("action_version")

        if mo_config_node.hasAttribute("action"):
            action = mo_config_node.getAttribute("action")

        if mo_config_node.hasAttribute("ignore_reason"):
            ignore_reason = mo_config_node.getAttribute("ignore_reason")

        if mo_config_node.hasAttribute("status"):
            status = mo_config_node.getAttribute("status")

        if mo_config_node.hasAttribute("exclude_list"):
            exclude_list = mo_config_node.getAttribute("exclude_list")

        # _SyncAction Object
        mo_config = None

        if class_id:
            mo_config = _SyncAction(class_id, noun, version, action_version, action, ignore_reason, status, exclude_list)

        if mo_config:
            if class_id in mo_config_map:
                mo_config_map[class_id] = mo_config
            else:
                mo_config_list = []
                mo_config_list.append(mo_config)
                mo_config_map[class_id] = mo_config_list

    return mo_config_map

class _CompareStatus(object):
    """ Internal class to support compare_imc_managedobject functionality. """
    TYPES_DIFFERENT = 0
    PROPS_DIFFERENT = 1
    EQUAL = 2


def _compare(from_mo, to_mo, diff):
    """ Internal method to support compare_imc_managedobject functionality. """

    if from_mo.class_id != to_mo.class_id:
        return _CompareStatus.TYPES_DIFFERENT

    for prop in CoreUtils.get_property_list(str(from_mo.class_id)):
        prop_meta = CoreUtils.is_property_in_meta_ignore_case(from_mo.class_id, prop)
        if prop_meta != None:
            if prop_meta.access == MoPropertyMeta.INTERNAL or prop_meta.access == MoPropertyMeta.READ_ONLY or prop in to_mo.exclude_prop_list:
            #if (prop in to_mo._excludePropList):
                continue
            if to_mo.__dict__.has_key(prop) and from_mo.get_attr(prop) != to_mo.get_attr(prop):
                diff.append(prop)

    if len(diff) > 0:
        return _CompareStatus.PROPS_DIFFERENT

    return _CompareStatus.EQUAL

def _translate_imc_managedobject(m_obj, xlate_map):
    """ Method used to translate a managedobject. This method is used in compare_imc_managedobject. """

    x_mo = m_obj.clone()
    x_mo.set_handle(m_obj.get_handle())

    if xlate_map != None:
        original_dn = x_mo.dn
        if original_dn in xlate_map:
            x_mometa = CoreUtils.get_mo_property_meta(ImcUtils.word_u(x_mo.class_id), "Meta")
            if x_mometa == None:
                ImcUtils.write_imc_warning('[Warning]: Could not translate [%s]' %(original_dn))
                return x_mo

            #Check for naming property
            match_obj = re.findall(r'(\[[^\]]+\])', x_mometa.rn)
            if match_obj:
                _update_mo_dn_along_with_naming_properties(x_mo, x_mometa, xlate_map[original_dn])
            else:
                #print "Translating", x_mo.dn, " => ", xlate_map[original_dn]
                x_mo.dn = xlate_map[original_dn]
        else:
            original_dn = re.sub(r'[/]*[^/]+$', '', original_dn)
            while original_dn != None or original_dn == "":
                if not original_dn in xlate_map:
                    original_dn = re.sub(r'[/]*[^/]+$', '', original_dn)
                    continue

                new_dn = re.sub("^%s/"%(original_dn), "%s/"%(xlate_map[original_dn]), x_mo.dn)
                #print "Translating", x_mo.dn, " => ", new_dn
                x_mo.dn = new_dn
                break

    return x_mo

def _update_mo_dn_along_with_naming_properties(mo, org_mo_meta, new_dn):
    mo.dn = new_dn
    new_rn = re.sub(r'^.*/', '', new_dn)
    modmeta_rn = re.sub(r'\[([^\]]+)\]', r'(?P<\1>.*?)', org_mo_meta.rn)
    match_obj = re.match(r'\|', modmeta_rn)
    if match_obj:
        modmeta_rn = re.sub(r'\|', r'\|', modmeta_rn)

    pattern = "^" + modmeta_rn + "$"
    match_obj = re.match(pattern, new_rn)
    name_prop_dict = match_obj.groupdict()
    for group_name in name_prop_dict:
        _update_named_property_field(mo, group_name, name_prop_dict[group_name])

def _update_named_property_field(mo, field_name, field_value):

    property_meta = CoreUtils.is_property_in_meta_ignore_case(mo.class_id, field_name)
    if property_meta != None and property_meta.access == MoPropertyMeta.NAMING:
        #ImcUtils.write_imc_warning('Translating [%s] from [%s] => [%s]' %(field_name, mo.get_attr(field_name), field_value))
        mo.set_attr(field_name, field_value)
