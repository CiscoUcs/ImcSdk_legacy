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

# This script adds the SNMP Trap to respective host onto the next available Id.
# Usage: AddSnmpTrap.py [options]
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
#  --shostname=SNMPHOSTNAME
#                        [Mandatory]                           To Add SnmpTrap
#                        to this respective IP
#  --susername=SNMPUSERNAME
#                        [Optional]                           To Add SnmpTrap
#                        to this respective UserName
#  --sadminstate=SNMPADMINSTATE
#                        [Optional] AdminState
#  --sversion=SNMPVERSION
#                        [Optional] Version
#  --snotifytype=SNOTIFICATIONTYPE
#                        [Optional] Notification Type
# Usecase:
# AddSnmpTrap.py -i <IP Address> -u <Username> -p <Password> --shostname 45.5.5.6 --susername snmpuser4 --sadminstate enabled --sversion v3 --snotifytype traps
                        
import platform
import getpass
import optparse

from ImcSdk import *

handle_list = []
affirmative_list = ['true', 'True', 'TRUE', True, 'yes', 'Yes', 'YES']

def get_password(prompt):
    if platform.system() == "Linux":
        return getpass.unix_getpass(prompt=prompt)
    elif platform.system() == "Windows" or platform.system() == "Microsoft":
        return getpass.win_getpass(prompt=prompt)
    else:
        return getpass.getpass(prompt=prompt)
    
def do_login(ip,user,pwd):
    print "Connecting to IMC Server <%s>" %(ip)
    handle = ImcHandle()
    if handle.login(ip,user,pwd):
        print "login successful: <%s>" %(handle.name)
        handle_list.append(handle)
        return handle

def do_logout():
    for handle in handle_list:
        handle_name = handle.name
        if handle.logout():
            print "logout successful: <%s>" %(handle_name)

def get_molist_by_dn(handle,dn,in_hierarchical=False):
    return handle.get_imc_managedobject(None,
                                      None,
                                      params={"Dn":dn},
                                      in_hierarchical=in_hierarchical)

def get_molist_by_class_id(handle,class_id,params=None,in_hierarchical=False):
    return handle.get_imc_managedobject(None,
                                      class_id,
                                      params=params,
                                      in_hierarchical=in_hierarchical)

def set_mo_by_inmo(handle,in_mo,params=None,force=False):
    if not force:
        print "Are you sure you want to modify? "
        set_flag = raw_input('Enter Yes or No. (Default is "Yes") : ')
        set_flag = set_flag.strip()
        if set_flag != "" and set_flag not in affirmative_list:
            return None
    return handle.set_imc_managedobject(in_mo=in_mo,
                                      class_id=None,
                                      params=params)

if __name__ == "__main__":
    try:
        parser = optparse.OptionParser()
        parser.add_option('-i', '--ip',dest="ip",
                          help="[Mandatory] IMC IP Address")
        parser.add_option('-u', '--username',dest="username",
                          help="[Mandatory] Account Username for IMC login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC login")
        parser.add_option('--shostname',dest="snmp_hostname",
                          help="[Mandatory] \
                          To Add SnmpTrap to this respective IP")
        parser.add_option('--susername',dest="snmp_username",
                          default="None",
                          help="[Optional] \
                          To Add SnmpTrap to this respective UserName")
        parser.add_option('--sadminstate',dest="snmp_admin_state",
                          type='choice',
                          choices=['Disabled','Enabled','disabled','enabled'],
                          default=CommSnmpTrap.CONST_ADMIN_STATE_DISABLED,
                          help="[Optional] AdminState")
        parser.add_option('--sversion',dest="snmp_version",
                          type='choice',
                          choices=['v1','v2c','v3'],
                          default=CommSnmpTrap.CONST_VERSION_V3,
                          help="[Optional] Version")
        parser.add_option('--snotifytype',dest="s_notification_type",
                          type='choice',
                          choices=['informs','traps'],
                          default=CommSnmpTrap.CONST_NOTIFICATION_TYPE_TRAPS,
                          help="[Optional] Notification Type")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Please provide IMC IP Address")
        if not options.username:
            parser.print_help()
            parser.error("Please provide IMC UserName")
        if not options.snmp_hostname:
            parser.print_help()
            parser.error("Please provide HostName for SNMP Trap <--shostname>")
        if not options.password:
            options.password=get_password("IMC Password:")

        
        #Connect to IMC    
        handle=do_login(options.ip,options.username,options.password)
        #handle.SetDumpXml()
        
        HOSTNAME_DEFAULT = "0.0.0.0"
        
        #Find the next available ID.
        snmp_host_dict={}
        snmp_host_id=None
        
        current_snmp_host_list=get_molist_by_class_id(handle,NamingId.COMM_SNMP_TRAP)
       
        for host in current_snmp_host_list:
            if options.snmp_hostname == host.get_attr(CommSnmpTrap.HOSTNAME):
                raise Exception("Trap destination IP Address %s already exists"
                                %(options.snmp_hostname))
            else:
                snmp_host_dict[int(host.get_attr(CommSnmpTrap.ID))] = \
                                host.get_attr(CommSnmpTrap.HOSTNAME)
        
        for hostId in sorted(snmp_host_dict.keys()):
            if snmp_host_dict[hostId] == HOSTNAME_DEFAULT:
                snmp_host_id=str(hostId)
                break
        
        if snmp_host_id == None:
            raise Exception("No Id available to Add any more SNMP Trap.")
        
        #Add the User to respective ID
        pmo = get_molist_by_class_id(handle,
                              NamingId.COMM_SNMP_TRAP,
                              params={CommSnmpTrap.ID:snmp_host_id}
                              )
        user_properties={
                    CommSnmpTrap.USER : options.snmp_username,
                    CommSnmpTrap.HOSTNAME : options.snmp_hostname,
                    CommSnmpTrap.ADMIN_STATE : options.snmp_admin_state,
                    CommSnmpTrap.NOTIFICATION_TYPE : options.s_notification_type,
                    CommSnmpTrap.VERSION : options.snmp_version
                        }
        add_snmp_trap = set_mo_by_inmo(handle,in_mo=pmo,params=user_properties)
        
        if add_snmp_trap:
            print "Successfully added SNMP Trap."
            write_object(add_snmp_trap)

        do_logout()

    except Exception, err:
        do_logout()
        print "Exception:", str(err)
#        import traceback, sys
#        print '-'*60
#        traceback.print_exc(file=sys.stdout)
#        print '-'*60