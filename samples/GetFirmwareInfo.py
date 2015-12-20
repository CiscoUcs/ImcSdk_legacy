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

# This script returns the firmware information for a respective IMC server.
#
# Usage: GetFirmwareInfo.py [options]
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
# UseCases:
# GetFirmwareInfo.py -i <IP Address> -u <Username> -p <Password>

import platform
import getpass
import optparse

from ImcSdk import *

handle_list = []

def get_password():
    if platform.system() == "Linux":
        return getpass.unix_getpass()
    elif platform.system() == "Windows" or platform.system() == "Microsoft":
        return getpass.win_getpass()
    else:
        return getpass.getpass()
    
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

def get_molist_by_class_id(handle,class_id,in_hierarchical=False):
    return handle.get_imc_managedobject(None, 
                                      class_id, 
                                      params=None,
                                      in_hierarchical=in_hierarchical)

if __name__ == "__main__":
    
    try:
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
            parser.error("Provide Username for IMC login")
        if not options.password:
            options.password=get_password()
        
        #Connect to IMC    
        handle=do_login(options.ip,options.username,options.password)
        
        #Get Firmware Details
        firmwareList=get_molist_by_class_id(handle,"firmwareRunning")
        write_object(firmwareList)
        
        do_logout()
    
    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
