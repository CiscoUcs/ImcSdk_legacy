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

# This script retrieves faults from the respective IMC.
# Usage: GetFaults.py [options]
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC login
#  --severity=FAULTSEVERITY
#                        [Optional] Fault Severity
# UseCases:
# GetFaults.py -i <IP Address> -u <Username> -p <Password>
# GetFaults.py -i <IP Address> -u <Username> -p <Password> --classid ComputeRackUnit
# GetFaults.py -i <IP Address> -u <Username> -p <Password> --severity info
                        
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

def get_molist_by_class_id(handle,in_mo,class_id,params=None,in_hierarchical=False):
    return handle.get_imc_managedobject(in_mo=in_mo,
                                      class_id=class_id,
                                      params=params,
                                      in_hierarchical=in_hierarchical)

if __name__ == "__main__":
    try:
        
        severity_type = [
                        FaultInst.CONST_SEVERITY_CRITICAL,
                        FaultInst.CONST_SEVERITY_MAJOR,
                        FaultInst.CONST_SEVERITY_MINOR,
                        FaultInst.CONST_SEVERITY_WARNING,
                        FaultInst.CONST_SEVERITY_INFO,
                        FaultInst.CONST_SEVERITY_CONDITION,
                        FaultInst.CONST_SEVERITY_CLEARED,
                        ]
        
        parser = optparse.OptionParser()
        parser.add_option('-i', '--ip',dest="ip",
                          help="[Mandatory] IMC IP Address")
        parser.add_option('-u', '--username',dest="userName",
                          help="[Mandatory] Account Username for IMC login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC login")
        parser.add_option('--classid',dest="class_id",
                          help="[Optional] Faults under respective MO")
        parser.add_option('--severity',dest="fault_severity",
                          type='choice',
                          choices=severity_type,
                          help="[Optional] Fault Severity")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Provide IMC IP Address")
        if not options.userName:
            parser.print_help()
            parser.error("Provide IMC UserName")
        if not options.password:
            options.password=get_password("IMC Password:")
        
        #Connect to IMC    
        handle=do_login(options.ip,options.userName,options.password)
        #handle.SetDumpXml()
        
        if options.fault_severity:
            param_dict={FaultInst.SEVERITY:options.fault_severity}
        else:
            param_dict=None
        
        if options.class_id:
            pmo = get_molist_by_class_id(handle,None,options.class_id)
        else:
            pmo=None
        
        if not pmo:
            pmo=None
        
        faults=get_molist_by_class_id(handle,pmo,
                               NamingId.FAULT_INST,
                               params=param_dict
                               )
        if faults:
            write_object(faults)
        else:
            print "No Faults Present."
        
        do_logout()

    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60