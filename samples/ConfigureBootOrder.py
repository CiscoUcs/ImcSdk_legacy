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

# This script configure the boot order for respective device.
# Usage: ConfigureBootOrder.py [options]
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
#  --bootdevice=BOOTDEVICE
#                        [Mandatory] Type of Boot Device
#  --bootorder=BOOTORDER
#                        [Optional] Boot Order for respective device
# Usecase:
# ConfigureBootOrder.py  -i <IP Address> -u <Username> -p <Password> --bootdevice FDD --bootorder 3
# ConfigureBootOrder.py  -i <IP Address> -u <Username> -p <Password> --bootdevice FDD
                        
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

def get_molist_by_dn(handle,dn,in_hierarchical=False):
    return handle.get_imc_managedobject(None,
                                      None,
                                      params={"Dn":dn},
                                      in_hierarchical=in_hierarchical)

def get_molist_by_class_id(handle,in_mo,class_id,params=None,in_hierarchical=False):
    return handle.get_imc_managedobject(in_mo=in_mo,
                                      class_id=class_id,
                                      params=params,
                                      in_hierarchical=in_hierarchical)
    
def add_mo_by_class_id(handle,class_id,params=None):
    return handle.add_imc_managedobject(None,class_id=class_id,params=params)

def set_mo_by_inmo(handle,in_mo,params=None,force=False):
    if not force:
        print "Are you sure you want to modify? "
        setFlag = raw_input('Enter Yes or No. (Default is "Yes") : ')
        setFlag = setFlag.strip()
        if setFlag != "" and setFlag not in affirmative_list:
            return None
    return handle.set_imc_managedobject(in_mo=in_mo,
                                      class_id=None,
                                      params=params)
    
class BootDevMap:
    def __init__(self,dn,rn,access,class_id):
        self.dn = dn
        self.rn = rn
        self.access = access
        self.class_id = class_id
    
def get_boot_obj(boot_dev):
    if boot_dev == "CDROM":
        boot_obj=BootDevMap(
                         'sys/rack-unit-1/boot-policy/vm-read-only',
                         'vm-read-only',
                         'read-only',
                         'LsbootVirtualMedia'                    
                         )
    elif  boot_dev == "FDD":
        boot_obj=BootDevMap(
                         'sys/rack-unit-1/boot-policy/vm-read-write',
                         'vm-read-write',
                         'read-write',
                         'LsbootVirtualMedia' 
                         )
    elif  boot_dev == "PXE":
        boot_obj=BootDevMap(
                         'sys/rack-unit-1/boot-policy/lan-read-only',
                         'lan-read-only',
                         'read-only',
                         'LsbootLan' 
                         )
    elif  boot_dev == "EFI":
        boot_obj=BootDevMap(
                         'sys/rack-unit-1/boot-policy/efi-read-only',
                         'efi-read-only',
                         'read-only',
                         'LsbootEfi' 
                         )
    elif  boot_dev == "HDD":
        boot_obj=BootDevMap(
                         'sys/rack-unit-1/boot-policy/storage-read-write',
                         'storage-read-write',
                         'read-write',
                         'LsbootStorage' 
                         )
    else:
        boot_obj=None
    
    return boot_obj
    
        

if __name__ == "__main__":
    try:
        
        phy_boot_device_list = [
                          "CDROM",
                          "FDD",
                          "PXE",
                          "EFI",
                          "HDD"                          
                          ]
        
        parser = optparse.OptionParser()
        parser.add_option('-i', '--ip',dest="ip",
                          help="[Mandatory] IMC IP Address")
        parser.add_option('-u', '--username',dest="username",
                          help="[Mandatory] Account Username for IMC login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC login")
        parser.add_option('--bootdevice',dest="boot_device",
                          type='choice',
                          choices=phy_boot_device_list,
                          help="[Mandatory] Type of Boot Device")
        parser.add_option('--bootorder',dest="bootOrder",
                          type='choice',
                          choices=['1','2','3','4','5'],
                          help="[Optional] Boot Order for respective device")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Please provide IMC IP Address")
        if not options.username:
            parser.print_help()
            parser.error("Please provide IMC UserName")
        if not options.boot_device:
            parser.print_help()
            parser.error("Please provide Boot Device")
        if not options.password:
            options.password=get_password("IMC Password:")
        
        boot_dev = options.boot_device
        boot_ord = options.bootOrder
        mod_boot_dev = None
        boot_dev_obj = get_boot_obj(boot_dev)
        
        #Connect to IMC    
        handle=do_login(options.ip,options.username,options.password)
        #handle.SetDumpXml()
        
        boot_device = get_molist_by_dn(handle,boot_dev_obj.dn)
        write_object(boot_device)
        
        if boot_ord:
            params_dict = {
                          "Dn" : boot_dev_obj.dn,
                          "Order" : boot_ord,
                          "Access" : boot_dev_obj.access
                          }
        else:
            params_dict = {
                          "Dn" : boot_dev_obj.dn,
                          "Access" : boot_dev_obj.access
                          }

        if boot_device:
            if not boot_ord:
                print "Device already exist."
                boot_ord=raw_input(
                "Please specify boot order if you wish to change[1-5]:")
                boot_ord=boot_ord.strip()
                if boot_ord:
                    params_dict["Order"] = boot_ord
                    mod_boot_dev = set_mo_by_inmo(handle,
                                             in_mo=boot_device,
                                             params=params_dict)
            else:
                mod_boot_dev = set_mo_by_inmo(handle,
                                         in_mo=boot_device,
                                         params=params_dict)
        else:
            mod_boot_dev = add_mo_by_class_id(handle,
                                        boot_dev_obj.class_id,
                                        params=params_dict)
        
        if mod_boot_dev:
            write_object(mod_boot_dev)
        
        do_logout()

    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60