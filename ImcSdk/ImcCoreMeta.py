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
This module contains the different meta classes to support ImcSdk.
"""

_EXTERNAL_METHOD_ATTRS = {'errorCode':'error_code', 'errorDescr': 'error_descr', 'invocationResult':'invocation_result', 'response':'response'}

class WriteXmlOption(object):
    """Class to replicate enum behavious."""
    ALL = 0
    ALL_CONFIG = 1
    DIRTY = 2

class ImcError(Exception):
    """Base class for exceptions in Imc module."""
    pass

class ImcException(ImcError):
    """User defined Exception Class for error returned from IMC"""
    def __init__(self, error_code, error_descr):
        self.error_code = error_code
        self.error_descr = error_descr

    def __str__(self):
        return "[ErrorCode]: %s [ErrorDescription]: %s" %(self.error_code, self.error_descr)

class ImcValidationException(ImcError):
    """ User defined exception class for validation"""
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return "[ErrorMessage]: %s" %(self.error_msg)
import re

class ImcVersion(object):
    """
    This class handles the operations related to the ImcVersions.
    It provides functionality to compare Imc version objects.
    """
    def __init__(self, version):
        if version == None:
            return None

        match_obj = re.match(r"""^(?P<major>[1-9][0-9]{0,2})\.(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\((?P<mr>(([0-9])|([1-9][0-9]{0,2})))\.(?P<patch>(([0-9])|([1-9][0-9]{0,4})))\)$""", version, 0)
        if match_obj:
            self.major = match_obj.group("major")
            self.minor = match_obj.group("minor")
            self.mr = match_obj.group("mr")
            self.patch = match_obj.group("patch")
            return

        match_obj = re.match(r"""^(?P<major>[1-9][0-9]{0,2})\.(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\((?P<mr>(([0-9])|([1-9][0-9]{0,2})))(?P<patch>[a-z])\)$""", version, 0)
        if match_obj:
            self.major = match_obj.group("major")
            self.minor = match_obj.group("minor")
            self.mr = match_obj.group("mr")
            self.patch = match_obj.group("patch")
            return

        match_obj = re.match(r"""^(?P<major>[1-9][0-9]{0,2})\.(?P<minor>(([0-9])|([1-9][0-9]{0,1})))\((?P<mr>(([0-9])|([1-9][0-9]{0,2})))\)$""", version, 0)
        if match_obj:
            self.major = match_obj.group("major")
            self.minor = match_obj.group("minor")
            self.mr = match_obj.group("mr")
            return

    def compare_to(self, version):
        """This method compares the version with self."""
        if version == None or not isinstance(version, ImcVersion):
            return 1

        if self.major != version.major:
            return ord(self.major) - ord(version.major)
        if self.minor != version.minor:
            return ord(self.minor) - ord(version.major)
        if self.mr != version.mr:
            return ord(self.mr) - ord(version.mr)
        return ord(self.patch) - ord(version.patch)

    def __gt__(self, version):
        return self.compare_to(version) > 0

    def __lt__(self, version):
        return self.compare_to(version) < 0

    def __ge__(self, version):
        return self.compare_to(version) >= 0

    def __le__(self, version):
        return self.compare_to(version) <= 0


class ImcPropertyRestriction(object):
    """ This class handles the restriction information of the properties of managed Object. """
    def __init__(self, min_length=None, max_length=None, pattern=None, value_set=None, range_val=None):
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern
        self.range_val = range_val
        self.value_set = value_set
        self.range_roc = None
        self.value_set_roc = None

class MoPropertyMeta(object):
    """ This class handles the meta information of the properties of managed Object. """
    NAMING = 0
    CREATE_ONLY = 1
    READ_ONLY = 2
    READ_WRITE = 3
    INTERNAL = 4

    def __init__(self, name, xml_attribute, field_type, version, access, mask, min_length, max_length, pattern, value_set, range_val):
        self.name = name
        self.xml_attribute = xml_attribute
        self.field_type = field_type
        self.version = version
        self.access = access
        self.mask = mask
        self.restriction = ImcPropertyRestriction(min_length, max_length, pattern, value_set, range_val)

    def validate_property_value(self, input_val):
        """This method does the property validation of Managed Object property value."""
        if input_val == None:
            return False

        if self.restriction.min_length != None and len(input_val) < self.restriction.min_length:
            return False

        if self.restriction.max_length != None and len(input_val) > self.restriction.max_length:
            return False

        if self.restriction.range_val != None and len(self.restriction.range_val) > 0:
            for rest_range in self.restriction.range_val:
                match = re.match(r"""^(?P<minimum>[0-9]{1,})\-(?P<maximum>[0-9]{1,})$""", rest_range, 0)
                if match:
                    minimum = match.group("minimum")
                    maximum = match.group("maximum")
                else:
                    continue

                if minimum <= input_val and maximum >= input_val:
                    return True

        if self.restriction.value_set != None and len(self.restriction.value_set) > 0:
            for rest_range in self.restriction.value_set:
                if rest_range == input_val:
                    return True

        if self.restriction.pattern != None:
            match = re.match(re.escape('"""' + self.restriction.pattern + '"""'), input_val, 0)
            if match:
                return True

        if (self.restriction.range_val != None and len(self.restriction.range_val) > 0) or (self.restriction.value_set != None and len(self.restriction.value_set) > 0) or self.restriction.pattern != None:
            return True

class MoMeta(object):
    """ This class handles the meta information of the managed Object. """
    ACCESS_TYPE_IO = "InputOutput"
    ACCESS_TYPE_OUTPUTONLY = "OutputOnly"

    def __init__(self, name, xml_attribute, rn, version, io, mask, field_names, child_field_names, verbs, access, parents):
        self.name = name
        self.xml_attribute = xml_attribute
        self.rn = rn
        self.version = version
        self.io = io
        self.mask = mask
        self.field_names = field_names
        self.child_field_names = child_field_names
        self.verbs = verbs
        self.access = access
        self.parents = parents

class MethodPropertyMeta(object):
    """ This class handles the meta information of the properties of external method Object. """
    def __init__(self, name, xml_attribute, field_type, version, io, is_complex_type):
        self.name = name
        self.xml_attribute = xml_attribute
        self.field_type = field_type
        self.version = version
        self.io = io
        self.is_complex_type = is_complex_type

class MethodMeta(object):
    """ This class handles the meta information of the meta property of external method Object. """
    def __init__(self, name, xml_attribute, version):
        self.name = name
        self.xml_attribute = xml_attribute
        self.version = version
