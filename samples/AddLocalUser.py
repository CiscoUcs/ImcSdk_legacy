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

# This script adds the local user to the next available Id in IMC server.
# Usage: AddLocalUser.py [options]
#
# Options:
#  -h, --help            show this help message and exit
#  -i IP, --ip=IP        [Mandatory] IMC IP Address
#  -u USERNAME, --username=USERNAME
#                        [Mandatory] Account Username for IMC Login
#  -p PASSWORD, --password=PASSWORD
#                        [Mandatory] Account Password for IMC Login
#  --lusername=LOCALUSERNAME
#                        [Mandatory] Username for Local User
#  --lpasswd=LOCALUSERPASSWORD
#                        [Mandatory] Password for Local User
#  --lpriv=LOCALUSERPRIVILEGE
#                        [Optional] Privilege for Local User
#  --lstatus=LOCALUSERSTATUS
#                        [Optional] Account Status for Local User
# Usecase:
# AddLocalUser.py -i <IP Address> -u <Username> -p <Password> --lusername <LocalUserName> --lpasswd <LocalUserPassword>

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
        print "Login successful: <%s>" %(handle.name)
        handle_list.append(handle)
        return handle

def do_logout():
    for handle in handle_list:
        handle_name = handle.name
        if handle.logout():
            print "Logout successful: <%s>" %(handle_name)

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
                          help="[Mandatory] Account Username for IMC Login")
        parser.add_option('-p', '--password',dest="password",
                          help="[Mandatory] Account Password for IMC Login")
        parser.add_option('--lusername',dest="local_username",
                          help="[Mandatory] Username for Local User")
        parser.add_option('--lpasswd',dest="local_user_password",
                          help="[Mandatory] Password for Local User")
        parser.add_option('--lpriv',dest="local_user_privilege",
                          type='choice',
                          choices=['admin', 'read-only', 'user'],
                          default=AaaUser.CONST_PRIV_READ_ONLY,
                          help="[Optional] Privilege for Local User")
        parser.add_option('--lstatus',dest="local_user_status",
                          type='choice',
                          choices=['active', 'inactive'],
                          help="[Optional] Account Status for Local User")
        
        (options, args) = parser.parse_args()
        
        if not options.ip:
            parser.print_help()
            parser.error("Please provide IMC IP Address")
        if not options.username:
            parser.print_help()
        if not options.local_username:
            parser.print_help()
            parser.error("Please provide Local UserName <--lusername>")
        if not options.password:
            options.password=get_password("IMC Password:")
        if not options.local_user_password:
            options.local_user_password=get_password("Local User Password:")
        
        #Connect to IMC    
        handle=do_login(options.ip,options.username,options.password)
        
        #Find the next available ID.
        user_id_dict={}
        local_user_id=None
        current_user_list=get_molist_by_class_id(handle,NamingId.AAA_USER)
       
        for user in current_user_list:
            user_id_dict[int(user.get_attr(AaaUser.ID))] = user.get_attr(
                                                                AaaUser.NAME)
        
        for user_id in sorted(user_id_dict.keys()):
            if not user_id_dict[user_id]:
                local_user_id=str(user_id)
                break
        
        if local_user_id == None:
            raise Exception("No Id available to Add any more user.")
        
        #Add the User to respective ID
        pmo = get_molist_by_class_id(handle,
                              NamingId.AAA_USER,
                              params={AaaUser.ID:local_user_id}
                              )
        user_properties={
                        AaaUser.NAME    : options.local_username,
                        AaaUser.PWD     : options.local_user_password,
                        AaaUser.PRIV    : options.local_user_privilege,
                        AaaUser.STATUS  : options.local_user_status                   
                        }
        new_local_user = set_mo_by_inmo(handle,in_mo=pmo,params=user_properties)
        if new_local_user:
            print "Successfully added Local User."
            write_object(new_local_user)

        do_logout()

    except Exception, err:
        do_logout()
        print "Exception:", str(err)
        import traceback, sys
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
