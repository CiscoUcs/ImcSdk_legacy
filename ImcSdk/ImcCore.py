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
This module contains the ImcSdk base classes.
"""

import os, sys
import re
import types

try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

import ImcUtils
from ImcMoMeta import _MANAGED_OBJECT_META
from ImcMethodMeta import _METHOD_FACTORY_META
from ImcCoreMeta import MoPropertyMeta, MoMeta, ImcValidationException, WriteXmlOption, _EXTERNAL_METHOD_ATTRS
from ImcConstants import NamingPropertyId

class ImcBase(object):
    """
    This is base class for ManagedObject, AbstractFilter and ExternalMethod classes.

    This class provides the basic functionality to add/remove/get child managed objects or handle object.
    """
    WRITE_XML_OPTION_ALL = 0
    WRITE_XML_OPTION_ALLCONFIG = 1
    WRITE_XML_OPTION_DIRTY = 2

    def __init__(self, class_id):
        self._class_id = class_id
        self._child = []
        self._handle = None
        self._dirty_mask = None

    @property
    def class_id(self):
        """Getter Method of ImcBase Class"""
        return self._class_id

    @property
    def child(self):
        """Getter Method of ImcBase Class"""
        return self._child

    @property
    def handle(self):
        """Getter Method of ImcBase Class"""
        return self._handle

    @property
    def dirty_mask(self):
        """Getter Method of ImcBase Class"""
        return self._dirty_mask

    def to_xml(self, options):
        """Convert the XML Object to XML Document format"""
        xml_doc = xml.dom.minidom.Document()
        xml_doc.appendChild(self.write_xml(xml_doc, options))
        return xml_doc.toxml()

    def set_handle(self, handle):
        """ Method sets the Imc Handle object. """
        self._handle = handle

    def get_child_count(self):
        """ Method returns the child managed object count. """
        return len(self._child)

    def child_write_xml(self, xml_doc, option):
        """ Method writes the xml representation for the object. """
        #child_list = []
        for child in self._child:
            child.write_xml(xml_doc, option)
            #child_list.append(child.write_xml(xml_doc, option))
#        return child_list

    def remove_child(self, obj):
        """ Method removes the child managed object. """
        self._child.remove(obj)

    def child_is_dirty(self):
        """ Method checks whether the child object is dirty or not. """
        for child in self._child:
            if child.is_dirty():
                return True
        return False

    def child_mark_clean(self):
        """ Method cleans the dirty mask of the child managed objects. """
        for child in self._child:
            child.mark_clean()

    def mark_clean(self):
        """ Method cleans the dirty mask of the managed object. """
        self._dirty_mask = 0

    def is_dirty(self):
        """ Method checks whether the object is dirty or not. """
        return self.child_is_dirty()

    def write_object(self):
        """ Method writes the string representation of the object. """
        for child in self._child:
            if child != None:
                child.write_object()

    def clone(self):
        """ Method returns the clone of the Managed Object. """
        import copy
        return copy.deepcopy(self)

#    def __copy__(self):
#        return self
#
    def __deepcopy__(self, memo):
        """ Overridden method to support deepcopy of Managed Object. """
        import copy
        clone = copy.copy(self)
        clone_child = []
        for child in clone.child:
            clone_child.append(copy.deepcopy(child))
        clone.child = clone_child
        return clone

class AbstractFilter(ImcBase):
    """This is the base class for all the filters"""
    def __init__(self, class_id):
        ImcBase.__init__(self, class_id)

class ManagedObject(ImcBase):
    """ This class structures/represents all the managed objects in IMC. """
    DUMMYDIRTY = "0x1L"

    def __init__(self, class_id):
        unknown_mo = False
        # make class_id case insensitive
        meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
        if meta_class_id == None:
            self._class_id = class_id
            self.prop_mo_meta = MoMeta(class_id, class_id, "", "", "InputOutput", ManagedObject.DUMMYDIRTY, [], [], [], [], [])
            unknown_mo = True
        else:
            self._class_id = meta_class_id
            self.prop_mo_meta = CoreUtils.get_mo_property_meta(self.class_id, "Meta")

        # __init__ of the ImcBase class
        ImcBase.__init__(self, self._class_id)

        self.__xtra_property = {}

        # instantiate class variables
        if not unknown_mo:
            for prop in _MANAGED_OBJECT_META[self._class_id]:
                if prop != "Meta":
                    self.__dict__[prop] = None

        if unknown_mo:
            self.mark_dirty()
        else:
            self.mark_clean()

    @property
    def xtra_property(self):
        """Getter Method of ManagedObject Class"""
        return self.__xtra_property

    def filter_version(self, version):
        """Update the filter version"""
        if self.prop_mo_meta != None and version != None:
            if self.__dict__.has_key("__xtra_property"):
                self._exclude_prop_list.append("__xtra_property")

            for prop in CoreUtils.get_property_list(self._class_id):
                prop_meta = CoreUtils.is_property_in_meta_ignore_case(self._class_id, prop)
                if prop_meta == None or version < prop_meta.version or prop_meta.access == MoPropertyMeta.INTERNAL:
                    self._exclude_prop_list.append(prop)

        for child in self.get_child():
            child.filter_version(version)

    def set_attr(self, key, value):
        """ This method sets attribute of a Managed Object. """
        if CoreUtils.find_class_id_in_mo_meta_ignore_case(self._class_id) != None:
            if key in _MANAGED_OBJECT_META[self._class_id]:
                prop_meta = CoreUtils.get_mo_property_meta(self._class_id, key)

                if prop_meta.validate_property_value(value) == False:
                    #print "Validation Failure"
                    return False

                if prop_meta.mask != None:
                    self._dirty_mask |= prop_meta.mask

                self.__dict__[key] = value
            else:
                self.__xtra_property[key] = value
        else:
            # no such property
            self.__xtra_property[ImcUtils.word_u(key)] = value
            #return None

    def __setattr__(self, key, value):
        """ Overridden standard set_attr method. """
        if key == "_class_id" or CoreUtils.find_class_id_in_mo_meta_ignore_case(self._class_id) == None or key not in _MANAGED_OBJECT_META[self._class_id]:
            self.__dict__[key] = value
            return

        return self.set_attr(key, value)

    def get_attr(self, key):
        """ This method gets attribute value of a Managed Object. """
        if key == "_class_id" and self.__dict__.has_key(key):
            return self.__dict__[key]

        if CoreUtils.find_class_id_in_mo_meta_ignore_case(self.class_id):
            if self.__dict__.has_key(key):
                if key in _MANAGED_OBJECT_META[self.class_id]:
                    # property exists
                    return self.__dict__[key]
            else:
                if self.__dict__.has_key('_ManagedObject__xtra_property'):
                    if self.__xtra_property.has_key(key):
                        return self.__xtra_property[ImcUtils.word_u(key)]
                    else:
                        raise AttributeError(key)
                else:
                    print "No xtra_property in mo:", self.class_id, " key:", key
        else:
            # property does not exist
            if self.__dict__['_ManagedObject__xtra_property'].has_key(key):
                return self.__xtra_property[ImcUtils.word_u(key)]
            elif key == "Dn" or key == "Rn":
                return None
            else:
                raise AttributeError(key)

    def __getattr__(self, key):
        """ Overridden standard get_attr method. """
        return self.get_attr(key)

    def add_child(self, mo):
        """ This method adds child managed object to a managed object. """
        self._child.append(mo)

    def mark_dirty(self):
        """ This method marks the managed object dirty. """
        if CoreUtils.find_class_id_in_mo_meta_ignore_case(self._class_id) == None and not self.is_dirty():
            self._dirty_mask = ManagedObject.DUMMYDIRTY
        else:
            self._dirty_mask = self.prop_mo_meta.mask

    def is_dirty(self):
        """ This method checks if managed object is dirty. """
        return self._dirty_mask != 0 or self.child_is_dirty()

    def make_rn(self):
        """ This method returns the Rn for a managed object. """
        rn_pattern = self.prop_mo_meta.rn
        for prop in re.findall(r"\[([^\]]*)\]", rn_pattern):
            if prop in CoreUtils.get_property_list(self._class_id):
                if self.get_attr(prop) != None:
                    rn_pattern = re.sub(r'\[%s\]' % prop, '%s' % self.get_attr(prop), rn_pattern)
                else:
                    raise ImcValidationException('Property "%s" was None in make_rn' %prop)
                    #raise Exception('Property "%s" was None in make_rn' %prop)
            else:
                raise ImcValidationException('Property "%s" was not found in make_rn arguments' %prop)
                #raise Exception('Property "%s" was not found in make_rn arguments' %prop)
        #print rn_pattern
        return rn_pattern

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """ Method writes the xml representation of the managed object. """
        if option == WriteXmlOption.DIRTY and not self.is_dirty():
            return
        if xml_doc is None:
            xml_obj = Element(self.prop_mo_meta.xml_attribute)
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc, self.prop_mo_meta.xml_attribute)
            else:
                xml_obj = SubElement(xml_doc, element_name)
        if CoreUtils.find_class_id_in_mo_meta_ignore_case(self._class_id) != None:
            for prop in CoreUtils.get_property_list(self._class_id):
                prop_meta = CoreUtils.get_mo_property_meta(self._class_id, prop)
                #if (at_meta.access == MoPropertyMeta.Internal):
            #        continue
                #elif ((option != WriteXmlOption.DIRTY) or ((at_meta.mask != None) and (self._dirty_mask & at_meta.mask) != 0)):
                if option != WriteXmlOption.DIRTY or (prop_meta.mask != None and (self._dirty_mask & prop_meta.mask) != 0):
                    if self.get_attr(prop) != None:
                        #xml_obj.setAttribute(prop_meta.xml_attribute, self.get_attr(prop))
                        xml_obj.set(prop_meta.xml_attribute,self.get_attr(prop))
        #Adding xtraProperties from object into Xml query document
        for xtra_prop in self.__xtra_property:
            #xml_obj.setAttribute(ImcUtils.word_l(xtra_prop), self.__xtra_property[xtra_prop])
            xml_obj.set(ImcUtils.word_l(xtra_prop),self.__xtra_property[xtra_prop])
        self.child_write_xml(xml_obj, option)
#        x_child = self.child_write_xml(xml_obj, option)
#        for xchild in x_child:
#            if xchild != None:
#                xml_obj.append(xchild)
        return xml_obj

    def load_from_xml(self, element, handle):
        """ Method creates the object from the xml representation of the managed object. """
        self.set_handle(handle)
        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                attr = ImcUtils.word_u(attr_name)
                if CoreUtils.find_class_id_in_mo_meta_ignore_case(self._class_id) != None:
                    if attr in CoreUtils.get_property_list(self._class_id):
                        self.set_attr(attr, str(attr_value))
                    else:
                        self.set_attr(attr, str(attr_value))
                else:
                    self.set_attr(ImcUtils.word_u(attr), str(attr_value))
            
            if self.get_attr("Rn") == None and self.get_attr("Dn") != None:
                self.set_attr("Rn", str(re.sub(r'^.*/', '', self.get_attr("Dn"))))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element) :
                    continue
    
                if child_element.tag in self.prop_mo_meta.field_names:
                    pass
                #TODO: Need code analysis.
                child = ManagedObject(ImcUtils.word_u(child_element.tag))
                self._child.append(child)
                child.load_from_xml(child_element, handle)

    def __str__(self):
        """Overridden standard str method to use standard print method for a managed object."""
        #from ImcBase import _write_mo
        return _write_mo(self)

class ExternalMethod(ImcBase):
    """
    This class represents the IMC XML api's query/configuration methods.
    """
    def __init__(self, class_id):

        # make class_id case insensitive
        meta_class_id = CoreUtils.find_class_id_in_method_meta_ignore_case(class_id)
        if meta_class_id == None:
            raise ImcValidationException("Invalid class Id %s" % class_id)
        else:
            class_id = meta_class_id

        # __init__ of the ImcBase class
        ImcBase.__init__(self, class_id)

        self._class_id = class_id
        self.prop_mo_meta = CoreUtils.get_method_property_meta(self._class_id, "Meta")

        # instantiate class variables
        for prop in _METHOD_FACTORY_META[class_id]:
            if prop != "Meta":
                self.__dict__[prop] = None

        self.error_code = 0
        self.error_descr = None
        self.invocation_result = None
        self.response = None

        self.mark_clean()

    def add_child(self, mo):
        """ This method adds child external method object to a external method object. """
        self._child.append(mo)

    def set_attr(self, key, value):
        """ This method sets the attribute of external method object. """
        if key in _METHOD_FACTORY_META[self._class_id]:
            self.__dict__[key] = value
        elif key == 'error_code':
            self.error_code = value
        elif key == 'error_descr':
            self.error_descr = value
        elif key == 'invocation_result':
            self.invocation_result = value
        elif key == 'response':
            self.response = value
        else:
            # no such property
            #print "No such property ClassId: %s Property:%s" %(self._class_id, key)
            return None
        
#    def __setattr__(self, key, value):
#        """ Overridden standard set_attr method. """
#        return self.set_attr(key, value)

    def get_attr(self, key):
        """ This method gets the attribute value of external method object. """
        if key in _METHOD_FACTORY_META[self._class_id]:
            """ property exists """
            return self.__dict__[key]
        else:
            # property does not exist
            return None
    
#    def __getattr__(self, key):
#        """ Overridden standard get_attr method. """
#        return self.get_attr(key)

    def get_error_response(self, error_code, error_descr):
        """ This methods sets error attributes of an external method object. """
        self.error_code = error_code
        self.error_descr = error_descr
        self.response = "yes"
        return self

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """ Method writes the XML representation of the external method object. """
        if xml_doc is None:
            xml_obj = Element(self.prop_mo_meta.xml_attribute)
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc, self.prop_mo_meta.xml_attribute)
            else:
                xml_obj = SubElement(xml_doc, element_name)
        
        for prop in CoreUtils.get_property_list(self._class_id):
            prop_meta = CoreUtils.get_method_property_meta(self._class_id, prop)
            if prop_meta.io == "Output":
                continue
            if prop_meta.is_complex_type:
                if self.get_attr(prop) != None:
                    self.__dict__[prop].write_xml(xml_obj, option, ImcUtils.word_l(prop))
                    #xml_obj.append(self.__dict__[prop].write_xml(xml_obj, option, ImcUtils.word_l(prop)))
                    #print ET.tostring(xml_obj)
            elif self.get_attr(prop) != None:
                xml_obj.set(prop_meta.xml_attribute, self.get_attr(prop))
                
        self.child_write_xml(xml_obj, option)
#        x_child = self.child_write_xml(xml_obj, option)
#        for xchild in x_child:
#            if xchild != None:
#                xml_obj.append(xchild)
        return xml_obj

    def load_from_xml(self, element, handle):
        """ Method creates the object from the XML representation of the an external method object. """
        from Imc import class_factory
        self.set_handle(handle)
        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                attr = ImcUtils.word_u(attr_name)
                if attr in CoreUtils.get_property_list(self._class_id):
                    at_meta = CoreUtils.get_method_property_meta(self._class_id, attr)
                    if at_meta.io == "Input" or at_meta.is_complex_type:
                        continue
                    self.set_attr(attr, str(attr_value))
                elif attr_name in _EXTERNAL_METHOD_ATTRS:
                    self.set_attr(_EXTERNAL_METHOD_ATTRS[attr_name], str(attr_value))

        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element) :
                    continue
        
                cln = ImcUtils.word_u(child_element.tag)
                if cln in CoreUtils.get_property_list(self._class_id):
                    prop_meta = CoreUtils.get_method_property_meta(self._class_id, cln)
                    if prop_meta.io == "Output" and prop_meta.is_complex_type:
                        child = class_factory(prop_meta.field_type)
                        if child != None:
                            self.set_attr(cln, child)
                            child.load_from_xml(child_element, handle)

class GenericMO(ManagedObject):
    """ This class handles the exceptional behaviour of Generic managed object. """
    def __init__(self, mo, option):
        ManagedObject.__init__(self, mo.class_id)
        self._exclude_prop_list = []
#        xml_doc = xml.dom.minidom.Document()
#        xml_doc.appendChild(mo.write_xml(xml_doc, option))
        xml_doc = mo.write_xml(option=option)

#        doc = parseString(xml_doc.toxml())
        doc = ET.tostring(xml_doc)
        
        root_element = ET.fromstring(doc)
        self.load_from_xml(root_element, mo.handle)
#        self.load_from_xml(doc.childNodes[0], mo.handle)
    
    @property
    def exclude_prop_list(self):
        """Getter Method of GenericMO Class"""
        return self._exclude_prop_list


class _GenericMO(ManagedObject):
    """ This class provides the functionality to create Generic managed objects. """
    def __init__(self, load_xml=None, mo=None, option=WriteXmlOption.ALL_CONFIG):
        ManagedObject.__init__(self, "GMO")
        self.dn = None
        self.rn = None
        self.properties = {}
        self.load_xml = load_xml
        self.mo = mo
        self.option = option

        if load_xml:
            self.get_root_node(load_xml)

        if mo:
            self.from_managed_object()

    def get_root_node(self, xml_string):
        """Convert XML to _GenericMO object"""
        root_element = ET.fromstring(xml_string)
#        _doc = xml.dom.minidom.parseString(xml_string)
#        root_node = _doc.documentElement
        self.load_from_xml(root_element)

    def get_attribute(self, attr):
        """Get Attribute of Generic Managed Object"""
        if attr in self.properties:
            return self.properties[attr]
        return None

    def write_to_attributes(self, element):
        """Set Attribute of Generic Managed Object"""
        if element.attrib:
            for attr_name, attr_value in element.attrib.iteritems():
                self.properties[attr_name] = attr_value
#        if node.hasAttributes():
#            for _attr, _val in node.attributes.items():
#                self.properties[_attr] = _val

    def load_from_xml(self, element):
        """Populate object using Xml Document Node"""
        self._class_id = element.tag
        meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(self._class_id)

        if meta_class_id:
            self._class_id = meta_class_id

        if NamingPropertyId.DN in element.attrib:
            self.dn = element.attrib[NamingPropertyId.DN]

        if self.dn:
            self.rn = os.path.basename(self.dn)

        # Write the attribute and value to dictionary properties, as it is .
        self.write_to_attributes(element)

        # Run the load_from_xml for each child_node recursively and populate child list too.
        child_elements = element.getchildren()
        if child_elements:
            for child_element in child_elements:
                if not ET.iselement(child_element) :
                    continue
                child = _GenericMO()
                self._child.append(child)
                child.load_from_xml(child_element)
        
#        if node.hasChildNodes():
#            child_list = node.childNodes
#            child_count = len(child_list)
#            for count in range(child_count):
#                child_node = child_list.item(count)
#                if child_node.nodeType != Node.ELEMENT_NODE:
#                    continue
#                child = _GenericMO()
#                self._child.append(child)
#                child.load_from_xml(child_node)

    def write_xml(self, xml_doc=None, option=None, element_name=None):
        """create Xml Document Node using object attributes"""
        if xml_doc is None:
            xml_obj=Element(self._class_id)
        else:
            if element_name == None:
                xml_obj = SubElement(xml_doc,self._class_id)
            else:
                xml_obj = SubElement(xml_doc,element_name)
                               
#        if element_name == None:
#            xml_obj = xml_doc.createElement(self._class_id)
#        else:
#            xml_obj = xml_doc.createElement(element_name)

        for prop in self.__dict__['properties']:
            xml_obj.setAttribute(ImcUtils.word_l(prop), self.__dict__['properties'][prop])
        self.child_write_xml(xml_obj, option)
#        x_child = self.child_write_xml(xml_doc, option)
#        for xchild in x_child:
#            if xchild != None:
#                xml_obj.appendChild(xchild)
        return xml_obj

    def to_managed_object(self):
        """
        Method creates and returns an object of ManagedObject class using the class_id and information from the
        Generic managed object.
        """
        from Imc import class_factory

        cln = ImcUtils.word_u(self._class_id)
        mo = class_factory(cln)
        if mo and isinstance(mo, ManagedObject) == True:
            meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(self._class_id)
            mo.set_handle(self._handle)
            for prop in self.properties:
                if ImcUtils.word_u(prop) in CoreUtils.get_property_list(meta_class_id):
                    mo.set_attr(ImcUtils.word_u(prop), self.properties[prop])
                else:
                    ImcUtils.write_imc_warning("Property %s Not Exist in MO %s" %(ImcUtils.word_u(prop), meta_class_id))

            if len(self._child):
                for child in self._child:
                    moch = child.to_managed_object()
                    mo.child.append(moch)
            return mo
        else:
            return None


    def from_managed_object(self):
        """
        Method creates and returns an object of _GenericMO class using the class_id and other information from the
        managed object.
        """
        if isinstance(self.mo, ManagedObject) == True:
            self._class_id = self.mo.class_id
            self._handle = self.mo.handle

            if self.mo.get_attr('Dn'):
                self.dn = self.mo.get_attr('Dn')

            if self.mo.get_attr('Rn'):
                self.rn = self.mo.get_attr('Rn')
            elif self.dn:
                self.rn = os.path.basename(self.dn)


            for prop in CoreUtils.get_property_list(self.mo.class_id):
                self.properties[prop] = self.mo.get_attr(prop)

            if len(self.mo.child):
                for child in self.mo.child:
                    if not child.get_attr('dn'):
                        _dn = self.mo.get_attr('dn') + "/" + child.get_attr('Rn')
                        child.set_attr('dn', _dn)
                    gmo = _GenericMO(mo=child)
                    self._child.append(gmo)

    def __str__(self):
        tabsize = 8
        if isinstance(self, _GenericMO) == True:
            out_str = "\n"
            out_str += 'class_id'.ljust(tabsize*4) + ':' + str(self.__dict__['_class_id']) + "\n"
            out_str += 'dn'.ljust(tabsize*4) + ':' + str(self.__dict__['dn']) + "\n"
            out_str += 'rn'.ljust(tabsize*4) + ':' + str(self.__dict__['rn']) + "\n"
            for key, value in self.__dict__['properties'].items():
                out_str += key.ljust(tabsize*4) + ':' + str(value) + "\n"

            for child in self._child:
                out_str += str(child) + "\n"

            #print out_str
            return out_str

    def get_child_class_id(self, class_id):
        """
        Method extracts and returns the child object list same as the given class_id
        """
        child_list = []
        for child in self._child:
            if child.class_id.lower() == class_id.lower():
                child_list.append(child)
        return child_list

    def get_child(self):
        """ Method returns the child object. """
        return self._child

class CoreUtils(object):
    """
    This class provides the basic utility functionality for the IMC SDK Library.
    """
    @staticmethod
    def is_valid_class_id(class_id):
        """ Methods checks whether the provided class_id is valid or not. """
        if class_id in _MANAGED_OBJECT_META or class_id in _METHOD_FACTORY_META:
            return True
        return False

    @staticmethod
    def get_mo_property_meta(class_id, key):
        """ Methods returns the property meta of the provided key for the given class_id. """
        if class_id in _MANAGED_OBJECT_META:
            if key in _MANAGED_OBJECT_META[class_id]:
                return _MANAGED_OBJECT_META[class_id][key]
        return None

    @staticmethod
    def get_method_property_meta(class_id, key):
        """ Methods returns the method meta of the ExternalMethod. """
        if class_id in _METHOD_FACTORY_META:
            if key in _METHOD_FACTORY_META[class_id]:
                return _METHOD_FACTORY_META[class_id][key]
        return None

    @staticmethod
    def get_property_list(class_id):
        """ Methods returns the property list for a given class_id. """
        if class_id in _MANAGED_OBJECT_META:
            attr_list = _MANAGED_OBJECT_META[class_id].keys()
            attr_list.remove("Meta")
            return attr_list
        if class_id in _METHOD_FACTORY_META:
            attr_list = _METHOD_FACTORY_META[class_id].keys()
            attr_list.remove("Meta")
            return attr_list

        #If the case of class_id is not as in Meta
        nci = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
        if nci != None:
            attr_list = _MANAGED_OBJECT_META[nci].keys()
            attr_list.remove("Meta")
            return attr_list

        nci = CoreUtils.find_class_id_in_method_meta_ignore_case(class_id)
        if nci != None:
            attr_list = _METHOD_FACTORY_META[nci].keys()
            attr_list.remove("Meta")
            return attr_list

        return None

    @staticmethod
    def is_property_in_meta_ignore_case(class_id, key):
        """
        Methods returns the property meta of the provided key for the given class_id.
        Given key is case insensitive.
        """
        if class_id in _MANAGED_OBJECT_META:
            for prop in _MANAGED_OBJECT_META[class_id]:
                if prop.lower() == key.lower():
                    return _MANAGED_OBJECT_META[class_id][prop]
        if class_id in _METHOD_FACTORY_META:
            for prop in _METHOD_FACTORY_META[class_id]:
                if prop.lower() == key.lower():
                    return _METHOD_FACTORY_META[class_id][prop]
        return None

    @staticmethod
    def find_class_id_in_mo_meta_ignore_case(class_id):
        """
        Methods checks if a given class_id is valid Managed Object Class.
        Given class is case insensitive.
        """
        for key in _MANAGED_OBJECT_META:
            if key.lower() == class_id.lower():
                return key
        return None

    @staticmethod
    def find_class_id_in_method_meta_ignore_case(class_id):
        """
        Methods checks if a given class_id is valid External Method Class.
        Given class is case insensitive.
        """
        for key in _METHOD_FACTORY_META:
            if key.lower() == class_id.lower():
                return key
        return None

    @staticmethod
    def handle_filter_max_component_limit(handle, lfilter):
        """
        Method checks the filter count and if the filter count exceeds the max_components(number of filters),
        then the given filter objects get distributed among small groups and then again binded together in
        complex filters(like and , or) so that the count of filters can be reduced.
        """
        from Imc import AndFilter, OrFilter, AbstractFilter
        max_components = 10
        if lfilter == None or lfilter.get_child_count() <= max_components:
            return lfilter

        if not isinstance(lfilter, AndFilter) and not isinstance(lfilter, OrFilter):
            return lfilter

        result_filter = None
        if isinstance(lfilter, AndFilter) == True:
            parent_filter = AndFilter()
            child_filter = AndFilter()
            parent_filter.add_child(child_filter)
            for childf in lfilter.get_child():
                if isinstance(childf, AbstractFilter) == True:
                    if child_filter.get_child_count() == max_components:
                        child_filter = AndFilter()
                        parent_filter.add_child(child_filter)
                    child_filter.add_child(childf)
            result_filter = parent_filter
        else:
            parent_filter = OrFilter()
            child_filter = OrFilter()
            parent_filter.add_child(child_filter)
            for childf in lfilter.get_child():
                if isinstance(childf, AbstractFilter) == True:
                    if child_filter.get_child_count() == max_components:
                        child_filter = OrFilter()
                        parent_filter.add_child(child_filter)
                    child_filter.add_child(childf)
            result_filter = parent_filter
        return CoreUtils.handle_filter_max_component_limit(handle, result_filter)

    @staticmethod
    def make_dn(rn_array):
        """ Method forms dn out of array of rns. """
        return '/'.join(rn_array)

    @staticmethod
    def make_rn(class_id, **kwargs):
        """ Method makes Rn for using a given class_id and required attributes. """
        class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
        if class_id == None:
            raise Exception("Invalid ClassId <%s>" %(class_id))

        prop_mo_meta = CoreUtils.get_mo_property_meta(class_id, "Meta")
        rn_pattern = prop_mo_meta.rn
        rn_prop_list = re.findall(r"\[([^\]]*)\]", rn_pattern)
        if not rn_prop_list:
            return rn_pattern

        if len(kwargs) == 0:
            raise ImcValidationException('Required Properties "%s" was not found in make_rn arguments' %rn_prop_list)

        for prop in rn_prop_list:
            prop_exists = False
            for key, value in kwargs.iteritems():
                if prop.lower() == key.lower():
                    rn_pattern = re.sub(r'\[%s\]' % prop, '%s' % value, rn_pattern)
                    prop_exists = True
            if not prop_exists:
                raise ImcValidationException('Property "%s" was not found in make_rn arguments' %prop)

        return rn_pattern

def _write_mo(mo):
    """ Method to return string representation of a managed object. """
    class_not_found = False
    if CoreUtils.find_class_id_in_mo_meta_ignore_case(mo.class_id) == None:
        class_not_found = True
    tab_size = 8
    out_str = "\n"
    if class_not_found:
        out_str += "Managed Object\t\t\t:\t" + str(ImcUtils.word_u(mo.class_id)) + "\n"
    else:
        out_str += "Managed Object\t\t\t:\t" + str(mo.prop_mo_meta.name) + "\n"
    out_str += "-"*len("Managed Object") + "\n"
    if not class_not_found:
        for prop in CoreUtils.get_property_list(mo.prop_mo_meta.name):
            #prop_meta = CoreUtils.get_mo_property_meta(mo.prop_mo_meta.name, prop)
            #if (prop_meta.access == MoPropertyMeta.Internal):
                #continue
            val = mo.get_attr(prop)
            #if val != None and val != "":
            out_str += str(prop).ljust(tab_size*4) + ':' + str(val) + "\n"
    else:
        for prop in mo.__dict__:
            if prop in ['_class_id', '_ManagedObject__xtra_property', '_handle', 'prop_mo_meta', '_dirty_mask', '_child']:
                continue
            val = mo.__dict__[prop]
            out_str += str(ImcUtils.word_u(prop)).ljust(tab_size*4) + ':' + str(val) + "\n"
    if mo.__dict__.has_key('_ManagedObject__xtra_property'):
        for xtra_prop in mo.__dict__['_ManagedObject__xtra_property']:
            out_str += ('[X]' + str(ImcUtils.word_u(xtra_prop))).ljust(tab_size*4) + ':' + str(mo.__dict__['_ManagedObject__xtra_property'][xtra_prop]) + "\n"

    out_str += str("Imc").ljust(tab_size*4) + ':' + str(mo.handle.imc) + "\n"

    out_str += "\n"
    return out_str

def write_object(molist):
    """ Writes the managed object on the terminal in form of key value pairs. """
    #tabsize = 8
    if isinstance(molist, _GenericMO) == True:
        print str(molist)
    elif isinstance(molist, ExternalMethod) == True:
        if hasattr(molist, "OutConfigs") == True:
            for child in molist.OutConfigs.get_child():
                if isinstance(child, ManagedObject) == True:
                    write_object(child)
    elif isinstance(molist, ManagedObject) == True:
        print str(_write_mo(molist))
    elif isinstance(molist, list) == True and len(molist) > 0:
#        if isinstance(molist[0], ImcMoDiff):
#            print "dn".ljust(tabsize*10), "input_object".ljust(tabsize*4), "side_indicator".ljust(tabsize*3), "diff_property"
#            print "--".ljust(tabsize*10), "-----------".ljust(tabsize*4), "-------------".ljust(tabsize*3), "------------"
        for mo in molist:
            if isinstance(mo, ManagedObject) == True:
                print str(_write_mo(mo))
            #elif(isinstance(mo, dn) == True):
            #    print mo.get_attr("value")
#            elif isinstance(mo, ImcMoDiff) == True:
#                write_mo_diff(mo)

def load_imc_config():
    from ConfigParser import SafeConfigParser

    config_file = os.path.join(os.path.dirname(__file__),"ImcConfig.cfg")
    parser = SafeConfigParser()
    parser.read(config_file)
    
    ssl_protocol = parser.get('ssl_connection', 'ssl_protocol').strip('"')
    is_verify_certificate = parser.getboolean('ssl_connection', 'verify_certificate')
    
    if not sys.version_info < (2, 6):
        from functools import partial
        import ssl
        
        ssl_protocol_dict = {'SSLv2': ssl.PROTOCOL_SSLv2,
                             'SSLv23': ssl.PROTOCOL_SSLv23,
                             'SSLv3': ssl.PROTOCOL_SSLv3,
                             'TLSv1': ssl.PROTOCOL_TLSv1
                             }
        
        ssl.wrap_socket = partial(ssl.wrap_socket, ssl_version=ssl_protocol_dict[ssl_protocol])
        
        if not sys.version_info < (2, 7, 9) and not is_verify_certificate:
            ssl._create_default_https_context = ssl._create_unverified_context
