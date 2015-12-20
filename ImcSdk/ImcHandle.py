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
""" This  module is the interface to the user to interact with IMC Server. """

import re
import time
import urllib2
from threading import Timer
try:
    import xml.etree.cElementTree as ET
    from xml.etree.cElementTree import Element, SubElement
except ImportError:
    import cElementTree as ET
    from cElementTree import Element, SubElement

import ImcUtils
from ImcConstants import NamingId, YesOrNo, Status
from ImcCoreMeta import ImcVersion, MoPropertyMeta, MoMeta, WriteXmlOption, ImcValidationException, ImcException
from ImcCore import ManagedObject, ExternalMethod, CoreUtils
from Imc import Pair, ConfigMap, ConfigConfig

default_imc = {}

class ImcHandle(object):
    """
    ImcHandle class handles all the Session and XML request related functionality.

    This class provides all the functionality related to session creation/refresh/destroy, XML/XMLRaw request handling,
    BackUp IMC, Import IMC BackUp, Firmware Upgrade, Generating Tech Support File,
    _compare and synchronise managed objects and Get/Set/Add/Remove operations on managed objects.
    """
    def __init__(self):
        self.__name = None
        self.__username = None
        self.__password = None
        self.__nossl = False
        self.__port = 443
        self.__proxy = None
        self.__version = None
        self.__imc = None
        self.__cookie = None
        self.__session_id = None
        self.__domains = None
        self.__priv = None
        self.__last_update_time = None
        self.__virtual_ipv4_address = None
        self.__prevent_logout = False
        self.__refresh_period = None
        self.__refresh_timer = None
        self.__refreshable = False
        self.__dump_xml = False

    @property
    def name(self):
        """Getter Method of ImcHandle Class"""
        return self.__name

    @property
    def username(self):
        """Getter Method of ImcHandle Class"""
        return self.__username

    @property
    def password(self):
        """Getter Method of ImcHandle Class"""
        return self.__password

    @property
    def nossl(self):
        """Getter Method of ImcHandle Class"""
        return self.__nossl

    @property
    def port(self):
        """Getter Method of ImcHandle Class"""
        return self.__port

    @property
    def proxy(self):
        """Getter Method of ImcHandle Class"""
        return self.__proxy

    @property
    def version(self):
        """Getter Method of ImcHandle Class"""
        return self.__version

    @property
    def imc(self):
        """Getter Method of ImcHandle Class"""
        return self.__imc

    @property
    def cookie(self):
        """Getter Method of ImcHandle Class"""
        return self.__cookie

    @property
    def session_id(self):
        """Getter Method of ImcHandle Class"""
        return self.__session_id

    @property
    def domains(self):
        """Getter Method of ImcHandle Class"""
        return self.__domains

    @property
    def priv(self):
        """Getter Method of ImcHandle Class"""
        return self.__priv

    @property
    def last_update_time(self):
        """Getter Method of ImcHandle Class"""
        return self.__last_update_time

    @property
    def virtual_ipv4_address(self):
        """Getter Method of ImcHandle Class"""
        return self.__virtual_ipv4_address

    @property
    def prevent_logout(self):
        """Getter Method of ImcHandle Class"""
        return self.__prevent_logout

    @property
    def refresh_period(self):
        """Getter Method of ImcHandle Class"""
        return self.__refresh_period

    @property
    def refresh_timer(self):
        """Getter Method of ImcHandle Class"""
        return self.__refresh_timer

    @property
    def refreshable(self):
        """Getter Method of ImcHandle Class"""
        return self.__refreshable
    
    @property
    def dump_xml(self):
        """Getter Method of ImcHandle Class"""
        return self.__dump_xml

    def set_dumpxml(self):
        """ set_dumpxml method sets the flag at handle level to display XML request and response. """
        self.__dump_xml = True

    def unset_dumpxml(self):
        """ unset_dumpxml method sets the flag at handle level to hide XML request and response. """
        self.__dump_xml = False

    def uri(self):
        """ Constructs the connection URI from name, nossl and port instance variables. """
        return "%s://%s%s" % (
        ("https", "http")[self.__nossl == True],
        self.__name,
        (":" + str(self.__port), "")[(
        ((self.__nossl == False) and (self.__port == 443)) or
        ((self.__nossl == True) and (self.__port == 80))
        )]
        )

    def xml_query(self, method, options, dump_xml=None):
        """
        xml_query method opens a connection to URL, sends the xmlQuery string to URL location,
        and returns result.
        Prepares objects from XML query result and returns external method response.
        """
        #import sys
        #if not sys.version_info < (2, 5):
        #    from functools import partial
        #    import ssl
        #    ssl.wrap_socket = partial(ssl.wrap_socket, ssl_version=ssl.PROTOCOL_TLSv1)

        
        if dump_xml == None:
            dump_xml = self.__dump_xml

        try:
            #xml_doc = xml.dom.minidom.Document()
            #xml_doc.appendChild(method.write_xml(xml_doc, options))
            #print method.__dict__
            xml_doc=method.write_xml(option=options)
            
            uri = self.uri() + '/nuova'
            if dump_xml in ImcUtils.AFFIRMATIVE_LIST:
                print '%s ====> %s' % (self.__imc, ET.tostring(xml_doc))

            if self.__proxy is None:
                if self.__nossl:
                    req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
                    opener = urllib2.build_opener(ImcUtils.SmartRedirectHandler())
                    resp = opener.open(req)
                    if type(resp) is list:
                        if len(resp) == 2 and (resp[0] == 302 or resp[0] == 301):
                            uri = resp[1]
                            req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
                            resp = urllib2.urlopen(req)
                else:
                    req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
                    opener = urllib2.build_opener(ImcUtils.TLS1Handler())
                    resp = opener.open(req)
            else:
                proxy_handler = urllib2.ProxyHandler({'http': self.__proxy, 'https': self.__proxy})

                if self.__nossl:
                    req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
                    opener = urllib2.build_opener(proxy_handler, ImcUtils.SmartRedirectHandler())
                    resp = opener.open(req)

                    if type(resp) is list:
                        if len(resp) == 2 and (resp[0] == 302 or resp[0] == 301):
                            uri = resp[1]
                            req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
                            opener = urllib2.build_opener(proxy_handler)
                            resp = opener.open(req)
                else:
                    req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
                    opener = urllib2.build_opener(ImcUtils.TLS1Handler(),
                                                  proxy_handler)
                    resp = opener.open(req)

            rsp = resp.read()

            if dump_xml in ImcUtils.AFFIRMATIVE_LIST:
                print '%s <==== %s' % (self.__imc, rsp)

            response = ExternalMethod(method.prop_mo_meta.name)
            root_element = ET.fromstring(rsp)
            response.load_from_xml(root_element, self)
            return response
        except Exception:
            raise

    def xml_rawquery(self, xml_str, dump_xml=None):
        """
        Accepts xmlQuery String and returns XML response String. No object manipulation is done in this method.
        """

        if dump_xml == None:
            dump_xml = self.__dump_xml

        uri = self.uri() + '/nuova'
        if dump_xml in ImcUtils.AFFIRMATIVE_LIST:
            print '%s ====> %s' % (self.__imc, xml_str)
            
        xml_doc = ET.fromstring(xml_str)
        
        if self.__nossl:
            req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
            opener = urllib2.build_opener(ImcUtils.SmartRedirectHandler())
            resp = opener.open(req)

            if type(resp) is list:
                if len(resp) == 2 and (resp[0] == 302 or resp[0] == 301):
                    uri = resp[1]
                    req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
                    resp = urllib2.urlopen(req)
                    #print "status code is:",f[0]
                    #print "location is:", f[1]
        else:
            req = urllib2.Request(url=uri, data=ET.tostring(xml_doc))
            resp = urllib2.urlopen(req)

        rsp = resp.read()
        if dump_xml in ImcUtils.AFFIRMATIVE_LIST:
            print '%s <==== %s' % (self.__imc, rsp)
        return rsp

    def __validate_imc(self):
        """ ValidateIMC method validates if a given host is valid IMC Server. """

        valid_models = ("R460-4640810", "C260-BASE-2646")
        model_validated = False
        rack_dn = CoreUtils.make_dn([CoreUtils.make_rn(NamingId.TOP_SYSTEM), CoreUtils.make_rn(NamingId.COMPUTE_RACK_UNIT, ServerId="1")])

        cr_dn = self.config_resolve_dn(rack_dn)
        if cr_dn.error_code == 0:
            for child in cr_dn.OutConfig.child:
                model_name = child.get_attr('Model')
                if model_name.startswith("UCSC"):
                    model_validated = True
                elif model_name.startswith("UCS-E"):
                    model_validated = True
                elif model_name in valid_models:
                    model_validated = True

            if not model_validated:
                return False

        crc = self.config_resolve_class("networkElement")
        if crc.error_code == 0:
            return False

        return True

    def login(self, name, username=None, password=None, nossl=None, port=None, proxy=None, auto_refresh=YesOrNo.FALSE, dump_xml=None, force=False):
        """
        login method authenticates and connects to IMC.

        - name         specifies the IP Address IMC Server.
        - username    specifies the username credential.
        - password    specifies the password credential.
        - nossl        specifies if the connection is made via http(True) or https(False).
                Default is False.
        - port         specifies the port. Default is 80(http) or 443(https).
        - proxy     specifies if the is made via proxy.
        - auto_refresh    specifes to True to keep the cookie alive.Default is False.
        """
        #from ImcBase import ManagedObject, CoreUtils, ImcException, ImcValidationException
        from ImcMos import FirmwareRunning
        import getpass

        if name == None:
            raise ImcValidationException('[Error]: Hostname/IP was not specified')

        if username == None:
            username = raw_input("Username: ")

        if password == None:
            password = getpass.getpass()

        #if self.__cookie != None:
        #    self.logout(dump_xml)
        if self.__cookie != None and self.__cookie != "":
            if not force:
                cr_dn = self.config_resolve_dn(ManagedObject(NamingId.TOP_SYSTEM).make_rn(), False, dump_xml)
                if cr_dn.error_code == 0:
                    if str(name).lower() == str(self.__name).lower() and str(username).lower() == str(self.__username).lower():
                        return True
                    else:
                        raise ImcValidationException("Handle has active connection with IMC %s using username %s .Create new handle to connect to IMC %s with username %s" %(self.__name,self.__username,name,username ) )           
                    
            else :
                self.logout(dump_xml)

        self.__imc = name
        self.__name = name
        self.__username = username
        self.__password = password
#        self.__nossl = nossl

        if nossl != None and port != None:
            self.__nossl = nossl
            self.__port = int(port)
        elif nossl != None and port==None:
            if nossl:
                self.__port = 80
                self.__nossl = True
            else:
                self.__port = 443
                self.__nossl = False
        elif nossl == None and port != None:
            if int(port) == 80:
                self.__nossl = True
                self.__port = 80
            elif int(port) == 443:
                self.__nossl = False
                self.__port = 443
            else:
                self.__nossl = False
                self.__port = int(port)
        else:
            self.__nossl = False
            self.__port = 443
            
#        if port != None:
#            self.__port = port
#        elif nossl == True:
#            self.__port = 80
#        else:
#            self.__port = 443

        if proxy != None:
            self.__proxy = proxy

        self.__cookie = ""

        response = self.aaa_login(username, password, dump_xml)

        if response == None:
            return False      # No Reason to throw exception.

        if response.error_code != 0:
            self.__imc = None
            self.__virtual_ipv4_address = None
            self.__name = None
            self.__username = None
            self.__password = None
            self.__nossl = False
            self.__port = 443
            raise ImcException(response.error_code, response.error_descr)

        self.__cookie = response.OutCookie
        self.__last_update_time = str(time.asctime())
        self.__domains = response.OutDomains
        self.__priv = response.OutPriv.split(',')
        self.__refresh_period = int(response.OutRefreshPeriod)
        self.__session_id = response.OutSessionId
        self.__version = ImcVersion(response.OutVersion)

        #Validate CSeries
        if not self.__validate_imc():
            self.logout()
            raise ImcValidationException('[Error]: login : Invalid IMC Server <%s>' %(self.__name))


        cr_dn = self.config_resolve_dn(ManagedObject(NamingId.TOP_SYSTEM).make_rn(), False, dump_xml)
        if cr_dn.error_code == 0:
            for top_system in cr_dn.OutConfig.child:
                self.__imc = top_system.Name
                self.__virtual_ipv4_address = top_system.Address

        if response.OutVersion == "" or response.OutVersion == None:
            firmware_obj = ManagedObject(NamingId.FIRMWARE_RUNNING)
            firmware_obj.Deployment = FirmwareRunning.CONST_DEPLOYMENT_SYSTEM
            rn_array = [ManagedObject(NamingId.TOP_SYSTEM).make_rn(), ManagedObject(NamingId.MGMT_CONTROLLER).make_rn(), firmware_obj.make_rn()]
            cr_dn = self.config_resolve_dn(CoreUtils.make_dn(rn_array), False, dump_xml)
            if cr_dn.error_code == 0:
                for firmware in cr_dn.OutConfig.child:
                    self.__version = ImcVersion(firmware.Version)

        if auto_refresh in ImcUtils.AFFIRMATIVE_LIST:
            self.__refreshable = auto_refresh
            self.__start_refresh_timer()
        else:
            self.__stop_refresh_timer()

        if self.__imc not in default_imc:
            default_imc[self.__imc] = self

        return True

    def logout(self, dump_xml=None):
        """ logout method disconnects from IMC. """
        if self.__cookie == None:
            return True

        if self.__refresh_timer:
            self.__refresh_timer.cancel()

        response = self.aaa_logout(dump_xml)
        self.__cookie = None
        self.__last_update_time = str(time.asctime())
        self.__domains = None
        self.__priv = None
        self.__session_id = None
        self.__version = None

        if self.__imc in default_imc:
            del default_imc[self.__imc]

        if response.error_code == "555":
            return True
        elif response.error_code != 0:
            raise ImcException(response.error_code, response.error_descr)

        return True

    def __start_refresh_timer(self):
        """ Internal method to support auto-refresh functionality. """
        if self.__refresh_period > 60:
            interval = self.__refresh_period-60
        else:
            interval = 60
        self.__refresh_timer = Timer(interval, self.refresh)
        self.__refresh_timer.setDaemon(True)
        self.__refresh_timer.start()

    def __stop_refresh_timer(self):
        """ Internal method to support auto-refresh functionality. """
        if self.__refresh_timer != None:
            self.__refresh_timer.cancel()
            self.__refresh_timer = None

    def refresh(self, auto_relogin=False, dump_xml=None):
        """ Internal method to support auto-refresh functionality. """
        self.__stop_refresh_timer()

        response = self.aaa_refresh(self.__username, self.__password, dump_xml)
        if response.error_code != 0:
            self.__cookie = None
            if auto_relogin:
                return self.login(self.__name, self.__username, self.__password, self.__nossl, self.__port, self.__proxy, self.__refreshable, dump_xml)
            return False

        self.__domains = response.OutDomains
        self.__priv = response.OutPriv.split(',')
        self.__refresh_period = int(response.OutRefreshPeriod)
        self.__cookie = response.OutCookie

        #re-enable the timer
        self.__start_refresh_timer()
        return True


    def get_imc_managedobject(self, in_mo=None, class_id=None, params=None, in_hierarchical=False, dump_xml=None):
        """
        Gets Managed Object from IMC.

        - in_mo, if provided, it acts as a parent for the present operation.
          It should be None unless a username wants to define a parent scope.
          It can be a single MO or a list containing multiple managed objects.
        - class_id of the managed object/s to get.
        - params contains semicolon (;) separated list of key/value pairs(key=value),
          that are used as filters for selecting specific managed objects.
          The key should be a valid property of the managed object to be retrieved.
        - in_hierarchical, Explores hierarchy if true, else returns managed objects at a single level.
        """

        if params != None:
            keys = params.keys()
        else:
            keys = []

        out_config = []
        meta_class_id = ""
        if class_id != None and class_id != "":
            #ClassId param set
            meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
            if meta_class_id == None:
                meta_class_id = class_id
                mo_meta = MoMeta(ImcUtils.word_u(class_id), ImcUtils.word_l(class_id), "", "", "InputOutput", ManagedObject.DUMMYDIRTY, [], [], [], [], [])
            else:
                mo_meta = CoreUtils.get_mo_property_meta(meta_class_id, "Meta")

            if mo_meta == None:
                raise ImcValidationException('[Error]: get_imc_managedobject: mo_meta for class_id [%s] is not valid' %(class_id))
                #return None

            if in_mo != None and isinstance(in_mo, list) and len(in_mo) > 0:
                for mo in in_mo:
                    crc = self.config_resolve_children(mo_meta.xml_attribute, mo.get_attr("Dn"), in_hierarchical, dump_xml)
                    if crc.error_code != 0:
                        raise ImcException(crc.error_code, crc.error_descr)

                    for child in crc.OutConfigs.child:
                        out_config.append(child)
            else:
                crc = self.config_resolve_class(mo_meta.xml_attribute, in_hierarchical, dump_xml)
                if crc.error_code != 0:
                    raise ImcException(crc.error_code, crc.error_descr)
                for child in crc.OutConfigs.child:
                    out_config.append(child)
        else:
            dn = ""
            for key in keys:
                if key.lower() == "dn":
                    dn = params[key]
            if not dn:
                raise ImcValidationException('[Error]: Please provide ClassId or dn')
            cr_dn = self.config_resolve_dn(dn, in_hierarchical, dump_xml)
            if cr_dn.error_code != 0:
                raise ImcException(cr_dn.error_code, cr_dn.error_descr)
            for child in cr_dn.OutConfig.child:
                out_config.append(child)

        #client side filtering starts
        for key in keys:
            prop_mo_meta = CoreUtils.is_property_in_meta_ignore_case(meta_class_id, key)
            if prop_mo_meta != None:
                attr_name = prop_mo_meta.xml_attribute
            else:
                attr_name = key
            for mo in out_config[:]:
                attr_name = attr_name[0].upper() + attr_name[1:]
                if mo.get_attr(attr_name) != params[key]:
                    out_config.remove(mo)
        #client side filtering ends

        molist = []
        current_molist = out_config
        while len(current_molist) > 0:
            child_molist = []
            for mo in current_molist:
                molist.append(mo)
                while mo.get_child_count() > 0:
                    for child in mo.child:
                        mo.remove_child(child)
                        if child.__dict__.has_key('Dn'):
                            if child.Dn == None or child.Dn == "":
                                child.set_attr("Dn", mo.Dn + '/' + child.Rn)
                                child.mark_clean()
                        else:
                            child.set_attr("Dn", mo.Dn + '/' + child.Rn)
                            child.mark_clean()
                        child_molist.append(child)
                        break
            current_molist = child_molist

        return molist

    def add_imc_managedobject(self, in_mo=None, class_id=None, params=None, dump_xml=None):
        """
        Adds a Managed Object to IMC.

        - in_mo, if provided, it acts as a parent for the present operation.
          It should be None unless a username wants to define a parent scope.
          It can be a single MO or a list containing multiple managed objects.
        - class_id of the managed object/s to be added.
        - params contains semicolon (;) separated list of key/value pairs(key=value),
          that are used as filters for selecting specific managed objects.
          The key should be a valid property of the managed object to be added.
        """

        unknown_mo = False
        if class_id == None or class_id == "":
            raise ImcValidationException('[Error]: add_imc_managedobject [Description]: class_id is Null')

        meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
        if meta_class_id != None:
            class_id = meta_class_id
            mo_meta = CoreUtils.get_mo_property_meta(class_id, "Meta")
        else:
            unknown_mo = True

        config_map = ConfigMap()
        rn = None
        dn = None
        #mo_meta = CoreUtils.get_mo_property_meta(class_id, "Meta")
        if params != None:
            keys = params.keys()
        else:
            keys = []

        if not unknown_mo:
            rn = mo_meta.rn
            for prop in CoreUtils.get_property_list(class_id):
                prop_meta = CoreUtils.get_mo_property_meta(class_id, prop)
                if prop_meta.access != MoPropertyMeta.NAMING:
                    continue
                naming_prop_found = False
                for key in keys:
                    if key.lower() == prop.lower():
                        rn = re.sub(r'\[%s\]' % prop, '%s' % params[key], rn)
                        naming_prop_found = True
                        break

                if naming_prop_found == False:
                    ImcUtils.write_imc_warning("[Warning]: add_imc_managedobject [Description]:Expected NAMING Property %s for ClassId %s not found" %(prop, class_id))
                    rn = re.sub(r'\[%s\]' % prop, '%s' % "", rn)

        obj = ManagedObject(class_id)

        for prop in keys:
            if not unknown_mo:
                prop_mo_meta = CoreUtils.is_property_in_meta_ignore_case(class_id, prop)
                if prop_mo_meta != None:
                    if prop.lower() == "rn" or prop.lower() == "dn":
                        pass
                    elif prop_mo_meta.access == MoPropertyMeta.READ_ONLY:
                        ImcUtils.write_imc_warning("[Warning]: AddManagedObject [Description]:Attempt to add non-writeable property %s in Class %s" %(prop, class_id))

                    if prop.lower() == "rn":
                        if in_mo == None or not isinstance(in_mo, list) or len(in_mo) == 0:
                            ImcUtils.write_imc_warning("[Warning]: AddManagedObject [Description]:Ignoring Rn since no parent provided")
                        if rn != params[prop]:
                            ImcUtils.write_imc_warning("[Warning]: AddManagedObject [Description]:Rn Mismatch. Provided %s Computed %s. Ignoring Computed Rn" %(params[prop], rn))
                            rn = params[prop]#bug fix. if Rn and Name are both provided by username then Rn will get preference.

                    if prop.lower() == "dn":
                        dn = params[prop]

                    obj.set_attr(prop_mo_meta.name, str(params[prop]))
                else:
                    #Known MO - Unknown Property
                    obj.set_attr(ImcUtils.word_l(prop), str(params[prop]))
            else:
                #Unknown MO
                if prop.lower() == "dn":
                    dn = params[prop]

                if prop.lower() == "rn":
                    rn = params[prop]
                if rn == None:
                    rn = ""

                obj.set_attr(ImcUtils.word_l(prop), str(params[prop]))

        obj.set_attr("Status", Status().CREATED)

        if dn != None and dn != "":
            obj.set_attr("Dn", dn)
            pair = Pair()
            #pair.set_attr("Key", obj.dn)
            pair.set_attr("Key", obj.get_attr("Dn"))
            pair.add_child(obj)
            config_map.add_child(pair)
        elif in_mo != None and isinstance(in_mo, list) and len(in_mo) > 0:
            for mo in in_mo:
                pdn = mo.get_attr("Dn")
                if pdn != None:
                    obj.set_attr("Dn", pdn + '/' +rn)
                    pair = Pair()
                    #pair.set_attr("Key", obj.dn)
                    pair.set_attr("Key", obj.get_attr("Dn"))
                    pair.add_child(obj.clone())
                    config_map.add_child(pair)

        if config_map.get_child_count() == 0:
            ImcUtils.write_imc_warning('[Warning]: AddManagedObject [Description]: Nothing to Add')
            return None

        output_molist = []
        for pair in config_map.child:
            in_config = ConfigConfig()
            for mo in pair.child:
                in_config.add_child(mo)
            ccm = self.config_conf_mo(dn=pair.Key, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
            if ccm.error_code == 0:
                molist = []
                for child in ccm.OutConfig.child:
                    if isinstance(child, Pair) == True:
                        for mo in child.child:
                            molist.append(mo)
                    elif isinstance(child, ManagedObject) == True:
                        molist.append(child)
                output_molist.extend(molist)
            else:
                raise ImcException(ccm.error_code, ccm.error_descr)

        return output_molist

    def set_imc_managedobject(self, in_mo, class_id=None, params=None, dump_xml=None):
        """
        Modifies Managed Object in IMC.

        - in_mo, if provided, it acts as the target object for the present operation.
          It should be None unless a username wants to provide an in_mo.
          It can be a single MO or a list containing multiple managed objects.
        - class_id of the managed object/s to be removed.
        - params contains semicolon (;) separated list of key/value pairs(key=value),
          that are used as filters for selecting specific managed objects.
          The key should be a valid property of the managed object to be modified.
        """

        #unknown_mo = False
        dn = None
        obj = None
        config_map = None
        dn_param_set = False

        if params != None:
            keys = params.keys()
        else:
            keys = []

        for key in keys:
            if key.lower() == "dn":
                # ClassId And dn Specified - No Parent Necessary
                dn_param_set = True
                dn = params[key]

        if in_mo == None or not isinstance(in_mo, list) or len(in_mo) == 0:
            if not dn_param_set:
                if class_id == None or class_id == "":
                    raise ImcValidationException('[Error]: set_imc_managedobject [Description]: in_mo and ClassId are both not specified')
                else:
                    raise ImcValidationException('[Error]: set_imc_managedobject [Description]: in_mo and dn are both not specified')
            else:
                if class_id == None or class_id == "":
                    raise ImcValidationException('[Error]: set_imc_managedobject [Description]: in_mo and ClassId are both not specified')
                else:
                    meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
                    if meta_class_id != None:
                        class_id = meta_class_id
                    #    mo_meta = CoreUtils.get_mo_property_meta(class_id, "Meta")
                    #else:
                    #    unknown_mo = True

                    obj = ManagedObject(class_id)
                    for prop in keys:
                        prop_mo_meta = CoreUtils.is_property_in_meta_ignore_case(class_id, prop)
                        if prop_mo_meta != None:
                            if prop.lower() == "rn" or prop.lower() == "dn":
                                pass
                            elif prop_mo_meta.access == MoPropertyMeta.READ_ONLY:
                                ImcUtils.write_imc_warning("[Warning]: SetManagedObject [Description] Attempt to set non-writable property %s in Class %s" %(prop, class_id))

                            obj.set_attr(prop_mo_meta.name, str(params[prop]))
                        else:
                            #Sets the unknown property/value as Xtra_property in obj
                            obj.set_attr(ImcUtils.word_l(prop), str(params[prop]))

                    obj.set_attr("Dn", dn)
                    obj.set_attr("Status", Status().MODIFIED)
                    pair = Pair()
                    pair.set_attr("Key", obj.get_attr("Dn"))
                    pair.add_child(obj)
                    config_map = ConfigMap()
                    config_map.add_child(pair)

        else:
            if class_id != None and class_id != "":
                ImcUtils.write_imc_warning("[Warning]: SetManagedObject [Description] ClassId <%s> is ignored with InMo input" %(class_id))

            config_map = ConfigMap()
            for mo in in_mo:
                obj = ManagedObject(mo.prop_mo_meta.name)
                dn = mo.get_attr("Dn")
                class_id = mo.prop_mo_meta.name

                for prop in keys:
                    prop_mo_meta = CoreUtils.is_property_in_meta_ignore_case(class_id, prop)
                    if prop_mo_meta != None:
                        if prop.lower() == "rn" or prop.lower() == "dn":
                            pass
                        elif prop_mo_meta.access == MoPropertyMeta.READ_ONLY:
                            ImcUtils.write_imc_warning("[Warning]: SetManagedObject [Description] Attempt to set non-writeable property %s in Class %s" %(prop, class_id))

                        obj.set_attr(prop_mo_meta.name, str(params[prop]))
                    else:
                        #Sets the unknown property/value as Xtra_property in obj
                        obj.set_attr(ImcUtils.word_l(prop), str(params[prop]))

                obj.set_attr("Dn", dn)
                obj.set_attr("Status", Status.MODIFIED)
                pair = Pair()
                pair.set_attr("Key", obj.get_attr("Dn"))
                pair.add_child(obj)
                config_map.add_child(pair)

        output_molist = []
        for pair in config_map.child:
            in_config = ConfigConfig()
            for mo in pair.child:
                in_config.add_child(mo)

            ccm = self.config_conf_mo(dn=pair.Key, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)

            if ccm.error_code == 0:
                molist = []
                for child in ccm.OutConfig.child:
                    if isinstance(child, Pair) == True:
                        for mo in child.child:
                            molist.append(mo)
                    elif isinstance(child, ManagedObject) == True:
                        molist.append(child)
                output_molist.extend(molist)
            else:
                raise ImcException(ccm.error_code, ccm.error_descr)

        return output_molist

    def remove_imc_managedobject(self, in_mo=None, class_id=None, params=None, dump_xml=None):
        """
        Removes Managed Object in IMC.

        - in_mo, if provided, it acts as the target object for the present operation.
          It should be None unless a username wants to provide an in_mo.
          It can be a single MO or a list containing multiple managed objects.
        - class_id of the managed object/s to be removed.
        - params contains semicolon (;) separated list of key/value pairs(key=value),
          that are used as filters for selecting specific managed objects.
          The key should be a valid property of the managed object to be modified.
        """

        if params != None:
            keys = params.keys()
        else:
            keys = []

        config_map = ConfigMap()
        if in_mo != None and isinstance(in_mo, list) and len(in_mo) > 0:
            for mo in in_mo:
                pair = Pair()
                pair.set_attr("Key", mo.get_attr("Dn"))
                obj = ManagedObject(mo.class_id)
                obj.set_attr("Status", Status().DELETED)
                pair.add_child(obj)

                config_map.add_child(pair)

        elif class_id != None:
            pair = Pair()
            meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
            if meta_class_id != None:
                class_id = meta_class_id
            for prop in keys:
                if prop.lower() == "dn":
                    pair.set_attr("Key", params[prop])
            if pair.get_attr("Key") == None:
                raise ImcValidationException('[Error]: remove_imc_managedobject [Description]: dn missing in propertyMap')

            obj = ManagedObject(class_id)
            obj.set_attr("Status", Status().DELETED)
            pair.add_child(obj)
            config_map.add_child(pair)

        if config_map.get_child_count() == 0:
            raise ImcValidationException('[Error]: remove_imc_managedobject [Description]: (inMO) or (ClassId and dn) missing')

        for pair in config_map.child:
            in_config = ConfigConfig()
            for mo in pair.child:
                in_config.add_child(mo)

            ccm = self.config_conf_mo(dn=pair.Key, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)

            if ccm.error_code == 0:
                molist = []
                for child in ccm.OutConfig.child:
                    if isinstance(child, Pair) == True:
                        for mo in child.child:
                            molist.append(mo)
                    elif isinstance(child, ManagedObject) == True:
                        molist.append(child)
            else:
                raise ImcException(ccm.error_code, ccm.error_descr)

        return molist

    def aaa_get_compute_auth_tokens(self, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("AaaGetComputeAuthTokens")

        method.Cookie = self.__cookie

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def aaa_keep_alive(self, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("AaaKeepAlive")

        method.Cookie = self.__cookie

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def aaa_login(self, in_name, in_password, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("AaaLogin")

        method.InName = in_name
        method.InPassword = in_password

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def aaa_logout(self, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("AaaLogout")

        method.InCookie = self.__cookie

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def aaa_refresh(self, in_name, in_password, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("AaaRefresh")

        method.InCookie = self.__cookie
        method.InName = in_name
        method.InPassword = in_password

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def config_conf_mo(self, dn, in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("ConfigConfMo")

        method.Cookie = self.__cookie
        method.Dn = dn
        method.InConfig = in_config
        method.InHierarchical = (("false", "true")[in_hierarchical in ImcUtils.AFFIRMATIVE_LIST])

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def config_resolve_children(self, class_id, in_dn, in_hierarchical=YesOrNo.FALSE, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("ConfigResolveChildren")

        meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
        if meta_class_id != None:
            class_id = ImcUtils.word_l(meta_class_id)
        else:
            class_id = ImcUtils.word_l(class_id)
        method.ClassId = class_id
        method.Cookie = self.__cookie
        method.InDn = in_dn
        method.InHierarchical = (("false", "true")[in_hierarchical in ImcUtils.AFFIRMATIVE_LIST])

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def config_resolve_class(self, class_id, in_hierarchical=YesOrNo.FALSE, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("ConfigResolveClass")

        meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
        if meta_class_id != None:
            class_id = ImcUtils.word_l(meta_class_id)
        else:
            class_id = ImcUtils.word_l(class_id)
        method.ClassId = class_id
        method.Cookie = self.__cookie
        method.InHierarchical = (("false", "true")[in_hierarchical in ImcUtils.AFFIRMATIVE_LIST])

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def config_resolve_dn(self, dn, in_hierarchical=YesOrNo.FALSE, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("ConfigResolveDn")

        method.Cookie = self.__cookie
        method.Dn = dn
        method.InHierarchical = (("false", "true")[in_hierarchical in ImcUtils.AFFIRMATIVE_LIST])

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def config_resolve_parent(self, dn, in_hierarchical=YesOrNo.FALSE, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("ConfigResolveParent")

        method.Cookie = self.__cookie
        method.Dn = dn
        method.InHierarchical = (("false", "true")[in_hierarchical in ImcUtils.AFFIRMATIVE_LIST])

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def event_subscribe(self, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("EventSubscribe")

        method.Cookie = self.__cookie

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

    def event_unsubscribe(self, dump_xml=None):
        """ Auto-generated IMC XML API Method. """
        method = ExternalMethod("EventUnsubscribe")

        method.Cookie = self.__cookie

        response = self.xml_query(method, WriteXmlOption.DIRTY, dump_xml)

        if response != None:
            return response
        return None

