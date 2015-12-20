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
""" This  module contains the supporting methods for ImcSdk package. """

import httplib
import os
import socket
import ssl
import sys
import types
import urllib2

from ImcCoreMeta import ImcValidationException

AFFIRMATIVE_LIST = ('true', 'True', 'TRUE', True, 'yes', 'Yes', 'YES')

class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
    """ Class to handle connection to IMC via redirection. """
    #def http_error_301(self, req, fp, code, msg, headers):
    def http_error_301(self, req, fp, code, msg, headers):
        #result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        resp_status = [code, headers.dict["location"]]
        return resp_status

    def http_error_302(self, req, fp, code, msg, headers):
        #result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        resp_status = [code, headers.dict["location"]]
        return resp_status


class TLS1Connection(httplib.HTTPSConnection):
    """Like HTTPSConnection but more specific"""
    def __init__(self, host, **kwargs):
        httplib.HTTPSConnection.__init__(self, host, **kwargs)

    def connect(self):
        """Overrides HTTPSConnection.connect to specify TLS version"""
        # Standard implementation from HTTPSConnection, which is not
        # designed for extension, unfortunately
        if sys.version_info >= (2, 7):
            sock = socket.create_connection((self.host, self.port),
                                            self.timeout, self.source_address)
        elif sys.version_info >= (2, 6):
            sock = socket.create_connection((self.host, self.port),
                                            self.timeout)
        else:
            sock = socket.create_connection((self.host, self.port))

        if getattr(self, '_tunnel_host', None):
            self.sock = sock
            self._tunnel()

        # This is the only difference; default wrap_socket uses SSLv23
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
                                    ssl_version=ssl.PROTOCOL_TLSv1)


class TLS1Handler(urllib2.HTTPSHandler):
    """Like HTTPSHandler but more specific"""
    def __init__(self):
        urllib2.HTTPSHandler.__init__(self)

    def https_open(self, req):
        return self.do_open(TLS1Connection, req)


def write_imc_warning(string):
    """ Method to throw warnings. """
    import warnings
    warnings.warn(string)
    
def str_to_class(s):
    """Convert String to Class Type"""
    if s in globals() and isinstance(globals()[s], types.ClassType):
        return globals()[s]
    return None

def word_l(word):
    """ Method makes the first letter of the given string as lower case. """
    return word[0].lower() + word[1:]

def word_u(word):
    """ Method makes the first letter of the given string as upper case. """
    return word[0].upper() + word[1:]

def check_registry_key(java_key):
    """ Method checks for the java in the registry entries. """
    from _winreg import ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKey, QueryValueEx
    path = None
    try:
        a_reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        rk = OpenKey(a_reg, java_key)
        for i in range(1024):
            current_version = QueryValueEx(rk, "CurrentVersion")
            if current_version != None:
                key = OpenKey(rk, current_version[0])
                if key != None:
                    path = QueryValueEx(key, "JavaHome")
                    return path[0]
    except Exception:
        write_imc_warning("Not able to access registry.")
        return None

def get_java_installation_path():
    """ Method returns the java installation path in the windows or Linux environment. """
    import platform

    # Get JavaPath for Ubuntu
    #if os.name == "posix":
    if platform.system() == "Linux":
        path = os.environ.get('JAVA_HOME')
        if not path:
            raise ImcValidationException("Please make sure JAVA is installed and variable JAVA_HOME is set properly.")
        else:
            path = os.path.join(path, 'bin')
            path = os.path.join(path, 'javaws')
            if not os.path.exists(path):
                raise ImcValidationException("javaws is not installed on System.")
            else:
                return path

    # Get JavaPath for Windows
    #elif os.name == "nt":
    elif platform.system() == "Windows" or platform.system() == "Microsoft":

        path = os.environ.get('JAVA_HOME')

        if path == None:
            path = check_registry_key(r"SOFTWARE\\JavaSoft\\Java Runtime Environment\\")

        if path == None:#Check for 32 bit Java on 64 bit machine.
            path = check_registry_key(r"SOFTWARE\\Wow6432Node\\JavaSoft\\Java Runtime Environment")

        if not path:
            raise ImcValidationException("Please make sure JAVA is installed.")
        else:
            path = os.path.join(path, 'bin')
            path = os.path.join(path, 'javaws.exe')
            if not os.path.exists(path):
                raise ImcValidationException("javaws.exe is not installed on System.")
            else:
                return path

def get_sha_hash(input_string):
    """ Method returns the sha hash digest for a given string. """
    import sha
    return sha.new(input_string).digest()

def expand_key(key, clen):
    """ Internal method supporting encryption and decryption functionality. """
    import sha
    from string import join
    from array import array

    blocks = (clen+19)/20
    xkey = []
    seed = key
    for i in xrange(blocks):
        seed = sha.new(key+seed).digest()
        xkey.append(seed)
    j = join(xkey, '')
    return array('L', j)

def encrypt_password(password, key):
    """ Encrypts the password using the given key. """
    from array import array
    import hmac
    import sha
    import base64
    from time import time

    H = get_sha_hash

    uhash = H(','.join(str(x) for x in [`time()`, `os.getpid()`, `len(password)`, password, key]))[:16]

    k_enc, k_auth = H('enc'+key+uhash), H('auth'+key+uhash)
    n = len(password)
    password_stream = array('L', password+'0000'[n&3:])
    xkey = expand_key(k_enc, n+4)

    for i in xrange(len(password_stream)):
        password_stream[i] = password_stream[i] ^ xkey[i]

    ct = uhash + password_stream.tostring()[:n]
    auth = hmac.new(ct, k_auth, sha).digest()

    encrypt_str = ct + auth[:8]
    encoded_str = base64.encodestring(encrypt_str)
    encrypted_password = encoded_str.rstrip('\n')
    return encrypted_password

def decrypt_password(cipher, key):
    """ Decrypts the password using the known key. """
    import base64
    import hmac
    import sha
    from array import array

    H = get_sha_hash

    cipher = cipher+"\n"
    cipher = base64.decodestring(cipher)
    n = len(cipher)-16-8

    uhash = cipher[:16]
    password_stream = cipher[16:-8] + "0000"[n&3:]
    auth = cipher[-8:]

    k_enc, k_auth = H('enc'+key+uhash), H('auth'+key+uhash)
    vauth = hmac.new(cipher[-8:], k_auth, sha).digest()[:8]

    password_stream = array('L', password_stream)
    xkey = expand_key(k_enc, n+4)

    for i in xrange(len(password_stream)):
        password_stream[i] = password_stream[i] ^ xkey[i]

    decrypted_password = password_stream.tostring()[:n]
    return decrypted_password