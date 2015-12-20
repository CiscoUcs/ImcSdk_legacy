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
""" This is an auto-generated module containing ExternalMethod Meta information. """

from ImcCoreMeta import MethodPropertyMeta, MethodMeta

_METHOD_FACTORY_META = {

	"AaaGetComputeAuthTokens": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"OutTokens":MethodPropertyMeta("OutTokens", "outTokens", "Xs:string", "Version142b", "Output", False),
		"Meta":MethodMeta("AaaGetComputeAuthTokens", "aaaGetComputeAuthTokens", "Version142b")
	},

	"AaaKeepAlive": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"Meta":MethodMeta("AaaKeepAlive", "aaaKeepAlive", "Version142b")
	},

	"AaaLogin": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"InName":MethodPropertyMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
		"InPassword":MethodPropertyMeta("InPassword", "inPassword", "Xs:string", "Version142b", "Input", False),
		"OutChannel":MethodPropertyMeta("OutChannel", "outChannel", "Xs:string", "Version142b", "Output", False),
		"OutCookie":MethodPropertyMeta("OutCookie", "outCookie", "Xs:string", "Version142b", "Output", False),
		"OutDomains":MethodPropertyMeta("OutDomains", "outDomains", "Xs:string", "Version142b", "Output", False),
		"OutEvtChannel":MethodPropertyMeta("OutEvtChannel", "outEvtChannel", "Xs:string", "Version142b", "Output", False),
		"OutPriv":MethodPropertyMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
		"OutRefreshPeriod":MethodPropertyMeta("OutRefreshPeriod", "outRefreshPeriod", "Xs:unsignedInt", "Version142b", "Output", False),
		"OutSessionId":MethodPropertyMeta("OutSessionId", "outSessionId", "Xs:string", "Version142b", "Output", False),
		"OutVersion":MethodPropertyMeta("OutVersion", "outVersion", "Xs:string", "Version142b", "Output", False),
		"Meta":MethodMeta("AaaLogin", "aaaLogin", "Version142b")
	},

	"AaaLogout": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"InCookie":MethodPropertyMeta("InCookie", "inCookie", "StringMin0Max47", "Version142b", "Input", False),
		"OutStatus":MethodPropertyMeta("OutStatus", "outStatus", "Xs:string", "Version142b", "Output", False),
		"Meta":MethodMeta("AaaLogout", "aaaLogout", "Version142b")
	},

	"AaaRefresh": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"InCookie":MethodPropertyMeta("InCookie", "inCookie", "StringMin0Max47", "Version142b", "Input", False),
		"InName":MethodPropertyMeta("InName", "inName", "Xs:string", "Version142b", "Input", False),
		"InPassword":MethodPropertyMeta("InPassword", "inPassword", "Xs:string", "Version142b", "Input", False),
		"OutChannel":MethodPropertyMeta("OutChannel", "outChannel", "Xs:string", "Version142b", "Output", False),
		"OutCookie":MethodPropertyMeta("OutCookie", "outCookie", "Xs:string", "Version142b", "Output", False),
		"OutDomains":MethodPropertyMeta("OutDomains", "outDomains", "Xs:string", "Version142b", "Output", False),
		"OutEvtChannel":MethodPropertyMeta("OutEvtChannel", "outEvtChannel", "Xs:string", "Version142b", "Output", False),
		"OutPriv":MethodPropertyMeta("OutPriv", "outPriv", "Xs:string", "Version142b", "Output", False),
		"OutRefreshPeriod":MethodPropertyMeta("OutRefreshPeriod", "outRefreshPeriod", "Xs:unsignedInt", "Version142b", "Output", False),
		"OutSessionId":MethodPropertyMeta("OutSessionId", "outSessionId", "Xs:string", "Version142b", "Output", False),
		"OutVersion":MethodPropertyMeta("OutVersion", "outVersion", "Xs:string", "Version142b", "Output", False),
		"Meta":MethodMeta("AaaRefresh", "aaaRefresh", "Version142b")
	},

	"ConfigConfMo": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"Dn":MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
		"InConfig":MethodPropertyMeta("InConfig", "inConfig", "ConfigConfig", "Version142b", "Input", True),
		"InHierarchical":MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
		"OutConfig":MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
		"Meta":MethodMeta("ConfigConfMo", "configConfMo", "Version142b")
	},

	"ConfigResolveChildren": {
		"ClassId":MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "Input", False),
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"Dn":MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "Output", False),
		"InDn":MethodPropertyMeta("InDn", "inDn", "ReferenceObject", "Version142b", "Input", False),
		"InHierarchical":MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
		"OutConfigs":MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
		"Meta":MethodMeta("ConfigResolveChildren", "configResolveChildren", "Version142b")
	},

	"ConfigResolveClass": {
		"ClassId":MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"InHierarchical":MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
		"OutConfigs":MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
		"Meta":MethodMeta("ConfigResolveClass", "configResolveClass", "Version142b")
	},

	"ConfigResolveDn": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"Dn":MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
		"InHierarchical":MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
		"OutConfig":MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
		"Meta":MethodMeta("ConfigResolveDn", "configResolveDn", "Version142b")
	},

	"ConfigResolveParent": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"Dn":MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
		"InHierarchical":MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
		"OutConfig":MethodPropertyMeta("OutConfig", "outConfig", "ConfigConfig", "Version142b", "Output", True),
		"Meta":MethodMeta("ConfigResolveParent", "configResolveParent", "Version142b")
	},

	"EventSubscribe": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
		"Meta":MethodMeta("EventSubscribe", "eventSubscribe", "Version142b")
	},

	"EventUnsubscribe": {
		"Cookie":MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "Input", False),
		"Meta":MethodMeta("EventUnsubscribe", "eventUnsubscribe", "Version142b")
	},

}

