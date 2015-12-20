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

# This script gets the current boot order.
# Usage: GetBootOrder.py [options]
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
# UseCases:
# GetBootOrder.py -i <IP Address> -u <Username> -p <Password>
                        
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
        print "login successful: <%s>\n" %(handle.name)
        handle_list.append(handle)
        return handle

def do_logout():
    for handle in handle_list:
        handle_name = handle.name
        if handle.logout():
            print "\nLogout successful: <%s>" %(handle_name)

def get_molist_by_class_id(handle,in_mo,class_id,params=None,in_hierarchical=False):
    return handle.get_imc_managedobject(in_mo=in_mo,
                                      class_id=class_id,
                                      params=params,
                                      in_hierarchical=in_hierarchical)
    
def get_child(handle,in_dn,class_id=None):
    from ImcSdk.ImcCore import ExternalMethod
    
    method = ExternalMethod("ConfigResolveChildren")
    method.ClassId = class_id
    method.Cookie = handle.cookie
    method.InDn = in_dn
    method.InHierarchical = "false"

    response = handle.xml_query(method, WriteXmlOption.DIRTY, handle.dump_xml)

    if (response != None):
        if (response.error_code != 0):
            raise Exception('[Error]: get_child [Code]:' + response.error_code +\
                            ' [Description]:' + response.error_descr)
        
        return response.OutConfigs.child
       
    return None

if __name__ == "__main__":
    try:
        
        phy_boot_dev_map = {
                         "vm-read-only" : "CD-ROM",
                         "vm-read-write" : "FDD",
                         "lan-read-only" : "PXE",
                         "storage-read-write": "HDD",
                         "efi-read-only": "EFI"
                         }
        
        parser = optparse.OptionParser()
        parser.add_option('-i', '--ip',dest="ip",
                          help="[Mandatory] IMC IP Address")
        parser.add_option('-u', '--username',dest="username",
                          help="[Mandatory] Account Username for IMC login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC login")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Provide IMC IP Address")
        if not options.username:
            parser.print_help()
            parser.error("Provide IMC UserName")
        if not options.password:
            options.password=get_password("IMC Password:")
        
        #Connect to IMC    
        handle=do_login(options.ip,options.username,options.password)
        #handle.SetDumpXml()
        
        bootDevices = get_child(handle,in_dn="sys/rack-unit-1/boot-policy")
        #WriteObject(bootDevices)
        
        bootOrderDict = {}
        for bootDevice in bootDevices:
            bootOrderDict[str(bootDevice.get_attr("Order"))] = \
            bootDevice
        
        print "Current BootOrder :"
        print "###################"
        for bootOrder in sorted(bootOrderDict.keys()):
            print bootOrder +") "+ \
            phy_boot_dev_map[bootOrderDict[bootOrder].get_attr("Rn")] + \
                " (" + bootOrderDict[bootOrder].get_attr("Dn") +")" 
        
        do_logout()

    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60