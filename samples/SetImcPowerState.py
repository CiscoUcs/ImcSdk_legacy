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

# This script sets the power state to on or off.
#
# Usage: SetImcPowerState.py [options]
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
#  --on                  Set the Powerstate to ON
#  --off                 Set the Powerstate to OFF

import platform
import getpass
import optparse

from ImcSdk import *

handle_list = []
affirmative_list = ['true', 'True', 'TRUE', True, 'yes', 'Yes', 'YES']

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

def get_molist_by_dn(handle,dn,in_hierarchical=False):
    return handle.get_imc_managedobject(None, 
                                      None, 
                                      params={"Dn":dn},
                                      in_hierarchical=in_hierarchical)

def set_mo_by_class_id(handle,class_id,params=None,force=False):
    if not force:
        print "Are you sure you want to modify? "
        set_flag = raw_input('Enter Yes or No. (Default is "Yes") : ')
        set_flag = set_flag.strip()
        if set_flag != "" and set_flag not in affirmative_list:
            return None
    
    return handle.set_imc_managedobject(None, 
                                      class_id=class_id, 
                                      params=params, 
                                      )

if __name__ == "__main__":
    try:
        parser = optparse.OptionParser()
        parser.add_option('-i', '--ip',dest="ip",
                          help="[Mandatory] IMC IP Address")
        parser.add_option('-u', '--username',dest="username",
                          help="[Mandatory] Account Username for IMC login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC login")
        parser.add_option('--on',dest="state",
                          action='store_const',
                          const=ComputeRackUnit.CONST_OPER_POWER_ON,
                          help="Set the Powerstate to ON")
        parser.add_option('--off', dest="state",
                          action='store_const',
                          const=ComputeRackUnit.CONST_OPER_POWER_OFF,
                          help="Set the Powerstate to OFF")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Provide IMC IP Address")
        if not options.username:
            parser.print_help()
            parser.error("Provide Username for IMC login")
        if not options.state:
            parser.print_help()
            parser.error("Provide --on OR --off")
        if not options.password:
            options.password=get_password()
        
        #Connect to IMC    
        handle=do_login(options.ip,options.username,options.password)
        
        #Get Firmware Details
        rack_unit=get_molist_by_dn(handle,"sys/rack-unit-1")
        current_power_state=rack_unit[0].get_attr("OperPower")
        
        if options.state == current_power_state:
            print "Current Power Status is already <%s>." %(current_power_state)
        else:
            if options.state == ComputeRackUnit.CONST_OPER_POWER_ON:
                updated_rack_unit=set_mo_by_class_id(
            handle,
            class_id="ComputeRackUnit",
            params={
            ComputeRackUnit.ADMIN_POWER:ComputeRackUnit.CONST_ADMIN_POWER_UP,
            ComputeRackUnit.DN:"sys/rack-unit-1"}
            )
            elif options.state == ComputeRackUnit.CONST_OPER_POWER_OFF:
                updated_rack_unit=set_mo_by_class_id(
            handle,
            class_id="ComputeRackUnit",
            params={
            ComputeRackUnit.ADMIN_POWER:ComputeRackUnit.CONST_ADMIN_POWER_DOWN,
            ComputeRackUnit.DN:"sys/rack-unit-1"}
            )
            if updated_rack_unit:
                update_power_state=updated_rack_unit[0].get_attr("OperPower")
                print "Modified Power Status changed to <%s>." %(
                                                            update_power_state)
            
        do_logout()

    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
