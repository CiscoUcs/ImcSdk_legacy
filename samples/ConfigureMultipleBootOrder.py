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

# This script configure the boot order for multiple device in one go.
# Usage: ConfigureMultipleBootOrder.py [options]
# >python ConfigureMultipleBootOrder.py -i "XX.XX.XX.XX" 
# -u "username" --bootdict "{FDD :3 ,HDD:4}"
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
#  --bootdict=BOOTDICT   [Mandatory] Dictionary with key as device 
#                                    and value as order.
#                         Available Device <HDD,FDD,CDROM,PXE,EFI>
#                         Available Order <1,2,3,4,5>
# Usecase:
# ConfigureMultipleBootOrder.py -i <IP Address> -u <Username> -p <Password> --bootdict "{FDD:2, HDD:3}"
                 
import platform
import getpass
import optparse
import warnings
import operator

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

def set_mo_by_class_id(handle,class_id,params=None,force=True):
    if not force:
        print "Are you sure you want to modify? "
        set_flag = raw_input('Enter Yes or No. (Default is "Yes") : ')
        set_flag = set_flag.strip()
        if set_flag != "" and set_flag not in affirmative_list:
            return None

    return handle.set_imc_managedobject(None,class_id=class_id,params=params)

def convert_str_to_dict(device_order):
    device_order=device_order.strip('{}')
    mydict={}
    for boot_order_pairs in device_order.split(','):
        boot_order_pair=boot_order_pairs.split(':')
        
        key=boot_order_pair[0].strip()
        value=boot_order_pair[1].strip()
        if key == "" or value == "":
            warnings.warn(
                        "Ignoring Invalid Device:Order <%s:%s>" %(key,value)
                        )
            continue
        mydict[key]=value

    return mydict

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
        
        phy_boot_dev_list = [
                          "CDROM",
                          "FDD",
                          "PXE",
                          "EFI",
                          "HDD"                          
                          ]
        
        parser = optparse.OptionParser()
        parser.add_option('-i', '--ip',dest="ip",
                          help="[Mandatory] IMC IP Address")
        parser.add_option('-u', '--username',dest="userName",
                          help="[Mandatory] Account Username for IMC login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC login")
        parser.add_option('--bootdict',dest="bootDict",
                          help="[Mandatory] Dictionary with key as device\
                                and value as order.\
                                Available Device <HDD,FDD,CDROM,PXE,EFI>\
                                Available Order <1,2,3,4,5>)")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Please provide IMC IP Address")
        if not options.userName:
            parser.print_help()
            parser.error("Please provide IMC UserName")
        if not options.bootDict:
            parser.print_help()
            parser.error("Please provide Boot Device Dictionary")
        if not options.password:
            options.password=get_password("IMC Password:")
        
        boot_dev_dict = convert_str_to_dict(options.bootDict)
        
        for boot_dev in boot_dev_dict.keys():
            if boot_dev.upper() in phy_boot_dev_list:
                continue
            else:
                del boot_dev_dict[boot_dev]
                warnings.warn("Ignoring Invalid Device <%s>" %(boot_dev))
        
        sorted_boot_dev_dict = sorted(
                                   boot_dev_dict.iteritems(), 
                                   key=operator.itemgetter(1)
                                   )
        
        #Connect to IMC    
        handle=do_login(options.ip,options.userName,options.password)
        #handle.SetDumpXml()
        
        existing_boot_devices = get_child(handle,
                                       in_dn="sys/rack-unit-1/boot-policy")
        
        existing_boot_device_rn_list = []
        for existing_boot_device in existing_boot_devices:
            existing_boot_device_rn_list.append(existing_boot_device.Rn)
        
        for (device,order) in sorted_boot_dev_dict:
            mod_boot_dev=None
            device_obj=get_boot_obj(device.upper())
            params_dict = {
                          "Dn" : device_obj.dn,
                          "Order" : order,
                          "Access" : device_obj.access
                          }
            try:
                if device_obj.rn in existing_boot_device_rn_list:
                    mod_boot_dev = set_mo_by_class_id(handle,
                                         device_obj.class_id,
                                         params=params_dict)
                else:
                    mod_boot_dev = add_mo_by_class_id(handle,
                                        device_obj.class_id,
                                        params=params_dict)
                if mod_boot_dev:
                    write_object(mod_boot_dev)
            except Exception, err:
                print "Exception:", str(err)
        
        do_logout()

    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60