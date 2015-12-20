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
""" This  module contains the additional utility apart Generic Get,Set,Add and Remove. """

import os
import re
import time
import xml.dom
from xml.dom.minidom import Node

import ImcUtils
from ImcConstants import YesOrNo, NamingId, Status
from Imc import ConfigConfig, ConfigMap, Pair
from ImcCoreMeta import MoPropertyMeta, MoMeta, ImcValidationException, ImcException, WriteXmlOption
from ImcCore import ManagedObject, GenericMO, CoreUtils
from ImcHandle import default_imc, ImcHandle
from ImcUtilityCore import ImcConstant

def export_imc_session(file_path, key, merge=YesOrNo.FALSE):
    """
    Stores the credential of currently logged in IMC in current session to a file. Password will be stored in encrypted format using key.

    - file_path specifies the path of the credential file.
    - key specifies any string used for secure encryption.
    - merge should be set as False unless username wants to append the existing credential file with new credential.
    """
    from ImcUtilityCore import _ImcLoginXml

    if file_path is None:
        raise ImcValidationException('[Error]: Please provide file_path')

    if key is None:
        raise ImcValidationException('[Error]: Please provide key')

    doc = xml.dom.minidom.Document()
    node_list = None

    if merge in ImcUtils.AFFIRMATIVE_LIST and os.path.isfile(file_path):#isfile() checks for file. exists() return true for directory as well
        doc = xml.dom.minidom.parse(file_path)
        node_list = doc.documentElement.childNodes
    else:
        doc.appendChild(doc.createElement(_ImcLoginXml.IMC_HANDLES))

    h_imc_array = default_imc.values()

    if h_imc_array != None:
        for h_imc in h_imc_array:
            updated = False
            if node_list != None:
                for child_node in node_list:
                    if child_node.nodeType != Node.ELEMENT_NODE:
                        continue

                    elem = child_node
                    if not elem.hasAttribute(_ImcLoginXml.NAME) or not elem.hasAttribute(_ImcLoginXml.USER_NAME):
                        continue
                    if elem.getAttribute(_ImcLoginXml.NAME) != h_imc.name or elem.getAttribute(_ImcLoginXml.USER_NAME) != h_imc.username:
                        continue

                    if h_imc.nossl:
                        elem.setAttribute(_ImcLoginXml.NO_SSL, h_imc.nossl)
                    elif elem.hasAttribute(_ImcLoginXml.NO_SSL):
                        elem.removeAttribute(_ImcLoginXml.NO_SSL)

                    if (h_imc.nossl and h_imc.port != 80) or (not h_imc.nossl and h_imc.port != 443):
                        elem.setAttribute(_ImcLoginXml.PORT, h_imc.port)
                    elif elem.hasAttribute(_ImcLoginXml.PORT):
                        elem.removeAttribute(_ImcLoginXml.PORT)

                    #elem.setAttribute(_ImcLoginXml.PASSWORD, p3_encrypt(h_imc.__password,key))
                    elem.setAttribute(_ImcLoginXml.PASSWORD, ImcUtils.encrypt_password(h_imc.password, key))
                    updated = True
                    break

            if updated:
                continue

            node = doc.createElement(_ImcLoginXml.IMC)
            attr = doc.createAttribute(_ImcLoginXml.NAME)
            attr.value = h_imc.name
            node.setAttributeNode(attr)
            attr = doc.createAttribute(_ImcLoginXml.USER_NAME)
            attr.value = h_imc.username
            node.setAttributeNode(attr)

            if h_imc.nossl:
                attr = doc.createAttribute(_ImcLoginXml.NO_SSL)
                attr.value = h_imc.nossl
                node.setAttributeNode(attr)

            if (h_imc.nossl and h_imc.port != 80) or (not h_imc.nossl and h_imc.port != 443):
                attr = doc.createAttribute(_ImcLoginXml.PORT)
                attr.value = h_imc.port
                node.setAttributeNode(attr)

            attr = doc.createAttribute(_ImcLoginXml.PASSWORD)
            #attr.value = p3_encrypt(h_imc.__password,key)
            attr.value = ImcUtils.encrypt_password(h_imc.password, key)
            node.setAttributeNode(attr)

            doc.documentElement.insertBefore(node, doc.documentElement.lastChild)

    xml_new = doc.toprettyxml(indent=" ")
    xml_new = re.sub(r"^.*?xml version.*\n", "", xml_new)
    xml_new = re.sub(r"\n[\s]*\n", "\n", xml_new)
    xml_new = re.sub(r"^(.*)", r"\1", xml_new, re.MULTILINE)

    f_handle = open(file_path, 'w')
    f_handle.write(xml_new)
    f_handle.close()

def import_imc_session(file_path, key):
    """
    This operation will do a login to each IMC which is present in credential file.

    - file_path specifies the path of the credential file.
    - key specifies string used for secure encryption while export_imc_session operation.
    """
    from ImcUtilityCore import _ImcLoginXml

    if file_path is None:
        raise ImcValidationException('[Error]: Please provide file_path')

    if key is None:
        raise ImcValidationException('[Error]: Please provide key')

    if not os.path.isfile(file_path) or not os.path.exists(file_path):
        raise ImcValidationException('[Error]: File <%s> does not exist ' %(file_path))

    doc = xml.dom.minidom.parse(file_path)
    top_node = doc.documentElement
    #print top_node.localName

    if top_node is None or top_node.localName != _ImcLoginXml.IMC_HANDLES:
        return None

    if top_node.hasChildNodes():
        child_list = top_node.childNodes
        child_count = len(child_list)
        for count in range(child_count):
            child_node = child_list.item(count)
            if child_node.nodeType != Node.ELEMENT_NODE:
                continue

            if child_node.localName != _ImcLoginXml.IMC:
                continue

            lname = None
            lusername = None
            lpassword = None
            lnossl = False
            lport = None

            if child_node.hasAttribute(_ImcLoginXml.NAME):
                lname = child_node.getAttribute(_ImcLoginXml.NAME)
            if child_node.hasAttribute(_ImcLoginXml.USER_NAME):
                lusername = child_node.getAttribute(_ImcLoginXml.USER_NAME)
            if child_node.hasAttribute(_ImcLoginXml.PASSWORD):
                #lpassword = p3_decrypt(child_node.getAttribute(_ImcLoginXml.PASSWORD), key)
                lpassword = ImcUtils.decrypt_password(child_node.getAttribute(_ImcLoginXml.PASSWORD), key)
            if child_node.hasAttribute(_ImcLoginXml.NO_SSL):
                lnossl = child_node.getAttribute(_ImcLoginXml.NO_SSL)
            if child_node.hasAttribute(_ImcLoginXml.PORT):
                lport = child_node.getAttribute(_ImcLoginXml.PORT)

            # Process login
            if lname is None or lusername == None or lpassword == None:
                ImcUtils.write_imc_warning("[Warning] Insufficient information for login ...")
                continue
            try:

                handle = ImcHandle()
                handle.login(name=lname, username=lusername, password=lpassword, nossl=lnossl, port=lport)

            except Exception, err:
                ImcUtils.write_imc_warning("[Connection Error<%s>] %s" %(lname, str(err)))

def backup_imc(handle, remotehost, remotefile, protocol, username, password, passphrase=None, timeout_sec=ImcConstant.TIME_OUT_IN_SEC, dump_xml=None):
    """
    Creates and downloads the backup of IMC.

    - remotehost    specifies the host where username need to download the backup.
    - remotefile    specifies the path on remotehost where username need to download the backup.
    - protocol        specifies the protocol used for transferring the file to remotehost.
    - username        specifies the username credential to login to remotehost.
    - password        specifies the password credential to login to remotehost.
    - timeout_sec     specifies the time in seconds for which method waits for the backUp file
                    to generate else exit. Default is 600 Seconds.
    """
    from ImcMos import MgmtBackup

    if timeout_sec == None or timeout_sec == "" or timeout_sec < 1:
        timeout_sec = ImcConstant.TIME_OUT_IN_SEC
        ImcUtils.write_imc_warning('[Warning]: Inappropriate <timeoutsec>. Chosen default value is 600 Seconds')

    #dn = "sys/export-config"
    #dn = ImcUtils.make_dn([ManagedObject(NamingId.TOP_SYSTEM).make_rn(),ManagedObject(NamingId.MGMT_BACKUP).make_rn()])
    dn = CoreUtils.make_dn([CoreUtils.make_rn(NamingId.TOP_SYSTEM), CoreUtils.make_rn(NamingId.MGMT_BACKUP)])

    mgmt_backup = ManagedObject(NamingId.MGMT_BACKUP)

    mgmt_backup.Hostname = remotehost
    mgmt_backup.User = username
    mgmt_backup.Pwd = password
    mgmt_backup.Proto = protocol
    mgmt_backup.RemoteFile = remotefile
    mgmt_backup.dn = dn
    mgmt_backup.AdminState = MgmtBackup.CONST_ADMIN_STATE_ENABLED
    mgmt_backup.Status = Status.MODIFIED
    mgmt_backup.Passphrase = passphrase

    in_config = ConfigConfig()
    in_config.add_child(mgmt_backup)
    response = handle.config_conf_mo(dn, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
    if response.error_code != 0:
        raise ImcException(response.error_code, response.error_descr)
        #raise Exception('[Error]: backup_imc [Code]:' + ccm.error_code + ' [Description]:' + ccm.error_descr)

    time.sleep(10) #Wait for 10 seconds before start checking.

    duration = timeout_sec
    poll_interval = ImcConstant.POLL_INTERVAL_IN_SEC

    cr_dn = None
    status = False

    while True:
        cr_dn = handle.config_resolve_dn(dn, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
        if cr_dn.error_code == 0:
            for each_mgmt_dn in cr_dn.OutConfig.child:
                if each_mgmt_dn.AdminState == MgmtBackup.CONST_ADMIN_STATE_DISABLED:
                    if each_mgmt_dn.FsmStageDescr == "Completed successfully":
                        status = True
                    if each_mgmt_dn.FsmStageDescr == "Error":
                        raise ImcValidationException("Failed to export the CIMC configuration file." + "Error Code: " + each_mgmt_dn.FsmRmtInvErrCode + " Error Description: " + each_mgmt_dn.FsmRmtInvErrDescr)

        else:
            raise ImcException(cr_dn.error_code, cr_dn.error_descr)

        if status:
            break

        time.sleep(min(duration, poll_interval))
        duration = max(0, (duration-poll_interval))

        if duration == 0:
            raise ImcValidationException('Backup operation in progress but utility backup_imc timed out. Exiting Method backup_imc')

    return cr_dn.OutConfig.child

def import_imc_backup(handle, remotehost, remotefile, protocol, username, password, passphrase=None, dump_xml=None):
    """
    Imports backUp.
    This operation will upload the IMC backup taken earlier via GUI or backup_imc operation.
    User can perform an import while the system is up and running.

    - remotehost    specifies the host where username need to download the backup.
    - remotefile    specifies the path on remotehost where username need to download the backup.
    - protocol        specifies the protocol used for transferring the file to remotehost.
    - username        specifies the username credential to login to remotehost.
    - password        specifies the password credential to login to remotehost.
    """
    from ImcMos import MgmtImporter

    dn = CoreUtils.make_dn([CoreUtils.make_rn(NamingId.TOP_SYSTEM), CoreUtils.make_rn(NamingId.MGMT_IMPORTER)])
    mgmt_importer = ManagedObject(NamingId.MGMT_IMPORTER)
    mgmt_importer.dn = dn
    mgmt_importer.AdminState = MgmtImporter.CONST_ADMIN_STATE_ENABLED
    mgmt_importer.Hostname = remotehost
    mgmt_importer.User = username
    mgmt_importer.Pwd = password
    mgmt_importer.RemoteFile = remotefile
    mgmt_importer.Proto = protocol
    mgmt_importer.AdminState = MgmtImporter.CONST_ADMIN_STATE_ENABLED
    mgmt_importer.Status = Status.MODIFIED
    mgmt_importer.Passphrase = passphrase
    
    in_config = ConfigConfig()
    in_config.add_child(mgmt_importer)
    ccm = handle.config_conf_mo(dn=dn, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
    if ccm.error_code != 0:
        raise ImcException(ccm.error_code, ccm.error_descr)

    time.sleep(10) #Wait for 10 seconds before start checking.
    status = False
    while True:
        cr_dn = handle.config_resolve_dn(dn, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
        if cr_dn.error_code == 0:
            if cr_dn.OutConfig.get_child_count() > 0:
                for cimc_backup in cr_dn.OutConfig.child:
                    if cimc_backup.AdminState == MgmtImporter.CONST_ADMIN_STATE_DISABLED:
                        if cimc_backup.FsmStageDescr == "Completed successfully":
                            status = True
                        if cimc_backup.FsmStageDescr == "Error":
                            raise ImcValidationException("Failed to import the CIMC configuration file." + "Error Code: " + cimc_backup.FsmRmtInvErrCode + " Error Description: " + cimc_backup.FsmRmtInvErrDescr)
            else:
                raise ImcValidationException("Failed to  import the CIMC configuration file.")
        else:
            raise ImcException(cr_dn.error_code, cr_dn.error_descr)
        if status:
            break

    return ccm.OutConfig.child

def update_imc_firmware_huu(handle, remote_share, share_type, remote_ip, username, password, update_component, stop_on_error=None, timeout=None, verify_update=None, cimc_secure_boot=None, dump_xml=None):
    """
    Uploads the HUU Firmware image to IMC Server.

    - remoteip        specifies the IP address of host containing firmware image.
    - username        specifies the Username login credential of host containing firmware image.
    - password        specifies the Password login credential of host containing firmware image.
    - remoteshare        specifies the path of firmware image on remoteip server.
    - sharetype        specifies the share type.
    - update_component    specifies the respective component to update or "all".
    - stop_on_error        specifies the action on error. "yes" or "no".
    - timeout        specifies the timeout in minute to exit the operation.
    - verify_update        speifies if IMC verify after update. "yes" or "no".
    """
    from ImcMos import HuuFirmwareUpdater

    dn = CoreUtils.make_dn([CoreUtils.make_rn(NamingId.TOP_SYSTEM), CoreUtils.make_rn(NamingId.HUU_CONTROLLER), CoreUtils.make_rn(NamingId.HUU_FIRMWARE_UPDATER)])
    huu_firmware_updater = ManagedObject(NamingId.HUU_FIRMWARE_UPDATER)
    huu_firmware_updater.dn = dn
    huu_firmware_updater.RemoteShare = remote_share
    huu_firmware_updater.MapType = share_type
    huu_firmware_updater.RemoteIp = remote_ip
    huu_firmware_updater.Username = username
    huu_firmware_updater.Password = password
    huu_firmware_updater.UpdateComponent = update_component
    huu_firmware_updater.AdminState = HuuFirmwareUpdater.CONST_ADMIN_STATE_TRIGGER
    huu_firmware_updater.StopOnError = stop_on_error
    huu_firmware_updater.TimeOut = timeout
    huu_firmware_updater.VerifyUpdate = verify_update
    huu_firmware_updater.CimcSecureBoot = cimc_secure_boot

    in_config = ConfigConfig()
    in_config.add_child(huu_firmware_updater)
    ccm = handle.config_conf_mo(dn=dn, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
    if ccm.error_code != 0:
        raise ImcException(ccm.error_code, ccm.error_descr)

    return ccm.OutConfig.child

def update_imc_firmware(handle, in_mo, admin_state, protocol, share_type, remote_server, remote_path, username, password, secure_boot=None, dump_xml=None):
    """
    Uploads the Firmware image to IMC Server.

    - in_mo            specifies the respective Managed Object to upload image.
    - remoteserver        specifies the IP address of host containing firmware image.
    - username        specifies the Username login credential of host containing firmware image.
    - password        specifies the Password login credential of host containing firmware image.
    - remotepath        specifies the path of firmware image on remoteserver.
    - protocol            specifies the protocol used for transferring the file to remotehost.
    - sharetype            specifies the share type.
    - admin_state        specifies the admin state.
    """
    from ImcMos import FirmwareUpdatable
    dn = None

    if in_mo != None:
        if str(ImcUtils.word_u(in_mo.class_id)) == "FirmwareUpdatable":
            dn = in_mo.get_attr("Dn")
        elif str(ImcUtils.word_u(in_mo.class_id)) == "BiosUnit":
            dn = CoreUtils.make_dn([in_mo.get_attr("Dn"), CoreUtils.make_rn("FirmwareUpdatable")])
        elif str(ImcUtils.word_u(in_mo.class_id)) == "MgmtController":
            dn = CoreUtils.make_dn([in_mo.get_attr("Dn"), CoreUtils.make_rn("FirmwareUpdatable")])
        else:
            raise ImcValidationException("Please provide correct Managed Object. Valid MOs <FirmwareUpdatable or BiosUnit or MgmtController")
    else:
        raise ImcValidationException("Please provide correct Managed Object. Valid MOs <FirmwareUpdatable or BiosUnit or MgmtController")

#        if updatetype == FirmwareUpdatable.CONST_TYPE_BLADE_CONTROLLER:
#            dn = "sys/rack-unit-1/mgmt/fw-updatable"
#        if updatetype == FirmwareUpdatable.CONST_TYPE_BLADE_BIOS:
#            dn = "sys/rack-unit-1/bios/fw-updatable"
#        if updatetype == FirmwareUpdatable.CONST_TYPE_ADAPTOR:
#            dn = "sys/rack-unit-1/adaptor-1/mgmt/fw-updatable"

    firmware_updater = ManagedObject(NamingId.FIRMWARE_UPDATABLE)
    firmware_updater.dn = dn
    firmware_updater.Status = Status.MODIFIED
    #firmware_updater.AdminState = FirmwareUpdatable.CONST_ADMIN_STATE_TRIGGER
    firmware_updater.AdminState = admin_state
    firmware_updater.Protocol = protocol
    firmware_updater.RemoteServer = remote_server
    firmware_updater.RemotePath = remote_path
    firmware_updater.User = username
    firmware_updater.Pwd = password
    firmware_updater.Type = share_type
    firmware_updater.SecureBoot = secure_boot

    in_config = ConfigConfig()
    in_config.add_child(firmware_updater)

    ccm = handle.config_conf_mo(dn=dn, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)

    if ccm.error_code != 0:
        raise ImcException(ccm.error_code, ccm.error_descr)

    return ccm.OutConfig.child

def get_imc_techsupport(handle, remotehost, remotefile, protocol, username, password, timeout_sec=ImcConstant.TIME_OUT_IN_SEC, dump_xml=None):
    """
    Creates and downloads the technical support data of IMC server.

    - remotehost    specifies the host where username need to download the technical support data.
    - remotefile    specifies the path on remotehost where username need to download the technical support data.
    - protocol        specifies the protocol used for transferring the file to remotehost.
    - username        specifies the username credential to login to remotehost.
    - password        specifies the password credential to login to remotehost.
    - timeout_sec     specifies the time in seconds for which method waits for the technical support data file
            to generate else exit.Default is 600 Seconds.
    """
    from ImcMos import MgmtImporter

    if timeout_sec == None or timeout_sec == "" or timeout_sec < 1:
        timeout_sec = ImcConstant.TIME_OUT_IN_SEC
        ImcUtils.write_imc_warning('[Warning]: Inappropriate <timeoutsec>. Chosen default value is 600 Seconds')

    #dn = "sys/rack-unit-1/tech-support"
    dn = CoreUtils.make_dn([CoreUtils.make_rn(NamingId.TOP_SYSTEM), CoreUtils.make_rn(NamingId.COMPUTE_RACK_UNIT, ServerId="1"), CoreUtils.make_rn(NamingId.SYSDEBUG_TECH_SUPPORT_EXPORT)])
    sysdebug_techsupport = ManagedObject(NamingId.SYSDEBUG_TECH_SUPPORT_EXPORT)
    sysdebug_techsupport.DN = dn
    sysdebug_techsupport.AdminState = MgmtImporter.CONST_ADMIN_STATE_ENABLED
    sysdebug_techsupport.RemoteFile = remotefile
    sysdebug_techsupport.Protocol = protocol
    sysdebug_techsupport.Status = Status.MODIFIED
    sysdebug_techsupport.Hostname = remotehost
    sysdebug_techsupport.User = username
    sysdebug_techsupport.Pwd = password

    in_config = ConfigConfig()
    in_config.add_child(sysdebug_techsupport)
    ccm = handle.config_conf_mo(dn=dn, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
    time.sleep(10) #Wait for 10 seconds before start checking.

    #TODO: CHECK THE FIELD fsmStageDescr
    duration = timeout_sec
    poll_interval = ImcConstant.POLL_INTERVAL_IN_SEC
    crd = None
    if ccm.error_code == 0:
        ImcUtils.write_imc_warning('Waiting for the Tech Support file to become available (this may take several minutes).')
        status = False
        while True:
            crd = handle.config_resolve_dn(dn, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
            if crd.error_code == 0:
                if crd.OutConfig.get_child_count() > 0:
                    for tech_support in crd.OutConfig.child:
                        if tech_support.AdminState == MgmtImporter.CONST_ADMIN_STATE_DISABLED: #TODO: replace the hard-coded string after schema change
                            if tech_support.FsmStatus == "success":
                                status = True
                            else:
                                raise ImcValidationException('Failed to create the TechSupport file.' + tech_support.FsmStatus)
                else:
                    raise ImcValidationException('Failed to create the TechSupport file.')
            else:
                raise ImcException(crd.error_code, crd.error_descr)
            if status:
                break
            time.sleep(min(duration, poll_interval))
            duration = max(0, (duration-poll_interval))
            if duration == 0:
                raise ImcValidationException('TechSupport generation in progress but get_imc_techsupport process timed out. Exiting Method get_imc_techsupport')
    else:
        raise ImcException(ccm.error_code, ccm.error_descr)

    return crd.OutConfig.child

def start_imc_iod_snapshot(handle, iso_share_ip, iso_share, iso_share_type, username, password, timeout, remote_share_ip, remote_share_path, remote_share_file, remote_share_type, remote_share_username, remote_share_password, admin_state="trigger", dump_xml=None):
    """ This method starts the IOD Snapshot."""
    #dn = "sys/iod/snapshotStart"
    #dn = ImcUtils.make_dn([ManagedObject(NamingId.TOP_SYSTEM).make_rn(), ManagedObject(NamingId.IOD_CONTROLLER).make_rn(), ManagedObject(NamingId.IOD_SNAPSHOT_START).make_rn()])
    dn = CoreUtils.make_dn([CoreUtils.make_rn(NamingId.TOP_SYSTEM), CoreUtils.make_rn(NamingId.IOD_CONTROLLER), CoreUtils.make_rn(NamingId.IOD_SNAPSHOT_START)])
    iod_snapshot = ManagedObject(NamingId.IOD_SNAPSHOT_START)
    iod_snapshot.dn = dn
    #iod_snapshot.AdminState = iod_snapshot.CONST_ADMIN_STATE_TRIGGER
    iod_snapshot.AdminState = admin_state
    iod_snapshot.IsoShare = iso_share
    iod_snapshot.IsoShareIp = iso_share_ip
    iod_snapshot.IsoShareType = iso_share_type
    iod_snapshot.Username = username
    iod_snapshot.Password = password
    iod_snapshot.TimeOut = timeout
    iod_snapshot.RemoteShareIp = remote_share_ip
    iod_snapshot.RemoteSharePath = remote_share_path
    iod_snapshot.RemoteShareFile = remote_share_file
    iod_snapshot.RemoteShareType = remote_share_type
    iod_snapshot.RemoteShareUsername = remote_share_username
    iod_snapshot.RemoteSharePassword = remote_share_password

    in_config = ConfigConfig()
    in_config.add_child(iod_snapshot)
    ccm = handle.config_conf_mo(dn=dn, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
    if ccm.error_code != 0:
        raise ImcException(ccm.error_code, ccm.error_descr)

    return ccm.OutConfig.child

def stop_imc_iod_snapshot(handle, timeout, admin_state="trigger", dump_xml=None):
    """ This method stops the IOD Snapshot."""
    #dn = "sys/iod/snapshotStart"
    #dn = ImcUtils.make_dn([ManagedObject(NamingId.TOP_SYSTEM).make_rn(), ManagedObject(NamingId.IOD_CONTROLLER).make_rn(), ManagedObject(NamingId.IOD_SNAPSHOT_CANCEL).make_rn()])
    dn = CoreUtils.make_dn([CoreUtils.make_rn(NamingId.TOP_SYSTEM), CoreUtils.make_rn(NamingId.IOD_CONTROLLER), CoreUtils.make_rn(NamingId.IOD_SNAPSHOT_CANCEL)])
    iod_snapshot = ManagedObject(NamingId.IOD_SNAPSHOT_CANCEL)
    iod_snapshot.dn = dn
    #iod_snapshot.AdminState = iod_snapshot.CONST_ADMIN_STATE_TRIGGER
    iod_snapshot.AdminState = admin_state
    iod_snapshot.TimeOut = timeout

    in_config = ConfigConfig()
    in_config.add_child(iod_snapshot)
    ccm = handle.config_conf_mo(dn=dn, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)

    if ccm.error_code != 0:
        raise ImcException(ccm.error_code, ccm.error_descr)

    return ccm.OutConfig.child

def sync_imc_managedobject(handle, difference, delete_not_present=False, no_version_filter=True, dump_xml=None):
    """
    Syncs Managed Object.

    Method takes the difference object (output of compare_imc_managedobject) and applies the differences
    on reference Managed Object.
    - difference specifies the Difference object (output of compare_imc_managedobject) which has
      differences of the properties of two or more Managed Objects.
    - delete_not_present, if set as True, any missing MOs in reference Managed Object set will be deleted.
    - no_version_filter, If set as True, minversion for Mos or properties to be added in reference
      Managed Object will not be checked.
    """
    from ImcUtilityCore import _ImcMoDiff

    if difference == None or (isinstance(difference, list) and len(difference) == 0):
        raise ImcValidationException("[Error]: sync_imc_managedobject: Difference Object can not be Null")

    config_map = ConfigMap()

    for mo_diff in difference:
        mo = mo_diff.input_object
        class_id = mo.class_id
        gmo_diff = None
        meta_class_id = CoreUtils.find_class_id_in_mo_meta_ignore_case(class_id)
        if meta_class_id == None:
            ImcUtils.write_imc_warning("Ignoring [%s]. Unknown ClassId [%s]." %(mo_diff.input_object.get_attr("dn"), class_id))
            continue

        #Removes Difference Object.
        if mo_diff.side_indicator == _ImcMoDiff.REMOVE and delete_not_present:
            gmo_diff = ManagedObject(class_id)
            gmo_diff.set_attr("dn", mo.get_attr("dn"))
            gmo_diff.set_attr("Status", Status().DELETED)
            gmo_diff = GenericMO(gmo_diff, WriteXmlOption.ALL_CONFIG)#gmo_diff should be generic object

        if mo_diff.side_indicator == _ImcMoDiff.ADD_MODIFY:
            gmo_diff = ManagedObject(class_id)
            add_exists = False
            mo_meta = CoreUtils.is_property_in_meta_ignore_case(class_id, "Meta")

            if mo_meta != None and 'Add' in mo_meta.verbs:
                add_exists = True

            #Add Difference Object.
            if add_exists and (mo_diff.diff_property == None or len(mo_diff.diff_property) == 0):
                for prop in mo.__dict__:
                    prop_mo_meta = CoreUtils.is_property_in_meta_ignore_case(class_id, prop)
                    if prop_mo_meta != None:
                        if prop.lower() == "rn" or prop.lower() == "dn" or prop_mo_meta.access == MoPropertyMeta.READ_ONLY:
                            continue
                        gmo_diff.set_attr(prop_mo_meta.name, mo.get_attr(prop))

                gmo_diff.set_attr("Dn", mo.get_attr("Dn"))
                gmo_diff.set_attr("Status", Status().CREATED)

                gmo_diff = GenericMO(gmo_diff, WriteXmlOption.ALL_CONFIG)#gmo_diff should be generic object
                if not no_version_filter:
                    h_reference = mo.get_handle()
                    if h_reference != None and h_reference.version != None:
                        gmo_diff.filter_version(h_reference.version)

            #Modify the Managed Object
            else:
                if mo_diff.diff_property == None or len(mo_diff.diff_property) == 0:
                    ImcUtils.write_imc_warning('Add not supported for class_id ' + class_id +'. Reverting to modify.')
                    continue

                final_diff_props = mo_diff.diff_property
                gmo_diff = ManagedObject(class_id)
                for prop in final_diff_props:
                    prop_mo_meta = CoreUtils.is_property_in_meta_ignore_case(class_id, prop)
                    if prop_mo_meta != None:
                        #if (prop.lower() == "rn" or prop.lower() == "dn" or prop_mo_meta.access == MoPropertyMeta.ReadOnly):
                        if prop.lower() == "rn" or prop.lower() == "dn":
                            continue
                        gmo_diff.set_attr(prop_mo_meta.name, mo.get_attr(prop))

                gmo_diff.set_attr("Dn", mo.get_attr("Dn"))
                gmo_diff.set_attr("Status", Status().MODIFIED)
                gmo_diff = GenericMO(gmo_diff, WriteXmlOption.ALL_CONFIG)#gmo_diff should be generic object to apply filter_version on it.

        #TODO: NoversionFilter functionality discussion.

        if gmo_diff != None and not no_version_filter:
            gmo_meta = CoreUtils.get_mo_property_meta(gmo_diff.class_id, "Meta")
            if gmo_meta != None and handle.version != None:
                if handle.version < gmo_meta.version:
                    ImcUtils.write_imc_warning('Ignoring unsupported class_id %s for dn %s.'  %(gmo_diff.class_id, gmo_diff.get_attr("dn")))
                    gmo_diff = None

                if gmo_diff != None and handle.version != None:
                    gmo_diff.filter_version(h_reference.version)

            if gmo_diff.__dict__.has_key("_exclude_prop_list"):
                for prop in gmo_diff.excludePropList:
                    if prop == "Xtra_property":
                        gmo_diff.__dict__[prop] = {}
                        continue
                    gmo_diff.__dict__[prop] = None

        if gmo_diff != None:
            pair = Pair()
            pair.set_attr("Key", gmo_diff.get_attr("Dn"))
            pair.add_child(gmo_diff)
            config_map.add_child(pair)

    if config_map.get_child_count() == 0:
        return None

    output_molist = []
    for pair in config_map.child:
        in_config = ConfigConfig()
        for mo in pair.child:
            in_config.add_child(mo)

        ccm = handle.config_conf_mo(dn=pair.Key, in_config=in_config, in_hierarchical=YesOrNo.FALSE, dump_xml=dump_xml)
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

def compare_imc_managedobject(reference_object, difference_object, exclude_different=YesOrNo.FALSE, include_equal=YesOrNo.FALSE, no_version_filter=YesOrNo.FALSE, include_operational=YesOrNo.FALSE, xlate_map=None):
    """
    Compares managed objects.

    - reference_object specifies objects used as a reference for comparison.
    - difference_object specifies objects that are compared to the reference objects.
    - exclude_different, if set as True then displays only the properties of compared objects that are equal.
    - include_equal, set as True to display properties of compared objects that are equal. By default, only properties that differ between the
      reference and difference objects are displayed.
    - no_version_filter, set as True to ignore minimum version in properties.
    - include_operational, set as True to include operational properties.
    - xlate_map specifies translation map with DNs of entities that needs to be translated.
    """
    from ImcUtilityCore import _ImcMoDiff, _compare, _CompareStatus, _translate_imc_managedobject
    reference_dict = {}
    difference_dict = {}

    if reference_object != None and isinstance(reference_object, list) and len(reference_object) > 0:
        for mo in reference_object:
            if mo == None:
                continue

            mo_meta = CoreUtils.is_property_in_meta_ignore_case(mo.prop_mo_meta.name, "Meta")

            if mo_meta != None:
                if mo_meta.io == MoMeta.ACCESS_TYPE_OUTPUTONLY:
                    ImcUtils.write_imc_warning('[Warning]: Ignoring [%s]. Non-configurable class [%s]' %(mo.Dn, mo.prop_mo_meta.name))
                    continue
                if mo_meta.io == MoMeta.ACCESS_TYPE_IO and len(mo_meta.access) == 1 and mo_meta.access[0] == "read-only":
                    ImcUtils.write_imc_warning('[Warning]: Ignoring read-only MO  [%s]. Class [%s]' %(mo.Dn, mo.prop_mo_meta.name))
                    continue

            reference_dict[mo.Dn] = mo

    if difference_object != None and isinstance(difference_object, list) and len(difference_object) > 0:
        for mo in difference_object:
            if mo == None:
                continue

            mo_meta = CoreUtils.is_property_in_meta_ignore_case(mo.prop_mo_meta.name, "Meta")
            if mo_meta != None:
                if mo_meta.access == MoMeta.ACCESS_TYPE_OUTPUTONLY:
                    ImcUtils.write_imc_warning('[Warning]: Ignoring [%s]. Non-configurable class [%s]' %(mo.Dn, mo.prop_mo_meta.name))
                    continue
                if mo_meta.access == MoMeta.ACCESS_TYPE_IO and len(mo_meta.access) == 1 and mo_meta.access[0] == "read-only":
                    ImcUtils.write_imc_warning('[Warning]: Ignoring read-only MO  [%s]. Class [%s]' %(mo.Dn, mo.prop_mo_meta.name))
                    continue
            if xlate_map in ImcUtils.AFFIRMATIVE_LIST:
                translated_mo = _translate_imc_managedobject(mo, xlate_map)
                difference_dict[translated_mo.Dn] = translated_mo
            else:
                difference_dict[mo.Dn] = mo

    dn_list = []
    for key in reference_dict:
        dn_list.append(key)
    for key in difference_dict:
        if key not in reference_dict:
            dn_list.append(key)
    dn_list = sorted(dn_list)
    diff_output = []

    for dn in dn_list:
        if dn not in difference_dict:
            if exclude_different not in ImcUtils.AFFIRMATIVE_LIST:
                mo_diff = _ImcMoDiff(reference_dict[dn], _ImcMoDiff.REMOVE)
                diff_output.append(mo_diff)
        elif dn not in reference_dict:
            if exclude_different not in ImcUtils.AFFIRMATIVE_LIST:
                mo_diff = _ImcMoDiff(difference_dict[dn], _ImcMoDiff.ADD_MODIFY)
                diff_output.append(mo_diff)
        else:
            diff_props = []
            option = WriteXmlOption.ALL_CONFIG
            if include_operational in ImcUtils.AFFIRMATIVE_LIST:
                option = WriteXmlOption.ALL
            gmo_reference = GenericMO(reference_dict[dn], option)
            gmo_difference = GenericMO(difference_dict[dn], option)
            if not no_version_filter:
                handle = gmo_reference.get_handle()
                if handle != None and handle.version != None:
                    gmo_reference.filter_version(handle.version)

                handle = gmo_difference.get_handle()
                if handle != None and handle.version != None:
                    gmo_difference.filter_version(handle.version)

            diff_status = _compare(gmo_reference, gmo_difference, diff_props)
            if diff_status == _CompareStatus.EQUAL and include_equal in ImcUtils.AFFIRMATIVE_LIST:
                mo_diff = _ImcMoDiff(reference_dict[dn], _ImcMoDiff.EQUAL)
                diff_output.append(mo_diff)
            elif diff_status == _CompareStatus.TYPES_DIFFERENT and exclude_different not in ImcUtils.AFFIRMATIVE_LIST:
                mo_diff = _ImcMoDiff(reference_dict[dn], _ImcMoDiff.REMOVE)
                diff_output.append(mo_diff)
                mo_diff = _ImcMoDiff(reference_dict[dn], _ImcMoDiff.ADD_MODIFY)
                diff_output.append(mo_diff)
            elif diff_status == _CompareStatus.PROPS_DIFFERENT and exclude_different not in ImcUtils.AFFIRMATIVE_LIST:
                ref_values = {}
                diff_values = {}
                for prop in diff_props:
                    ref_values[prop] = gmo_reference.get_attr(prop)
                    diff_values[prop] = gmo_difference.get_attr(prop)
                mo_diff = _ImcMoDiff(difference_dict[dn], _ImcMoDiff.ADD_MODIFY, diff_props, ref_values, diff_values)
                diff_output.append(mo_diff)

    return diff_output
