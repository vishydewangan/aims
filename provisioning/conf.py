__author__ = 'vishwanath dewangan'

from collections import OrderedDict

RMC = {
    'url': 'https://rwblbpi0.ccsrm.lab.in:8443/cms/General/index.jsp',
    'uname': 'rmc_del_nml',
    'passwd': 'password'
}


SLEA = {
    'url': 'https://rwblbpi0.ccsrm.lab.in:8443/cms/General/index.jsp',
    'uname': 'cbi_del',
    'passwd': 'password',
    'id': '1',
    'case': 'tada'
}


SLEMF = {
    'url': 'https://rlmlbpi1.ccsrm.lab.in:8443/cms/General/index.jsp',
    'uname': 'super',
    'passwd': 'password',
    'id': '2',
    'case': 'defection'
}


NLEA = {
    'url': 'https://cwblbvf0.ccsrm.lab.in:8443/cms/General/index.jsp',
    'uname': 'ib_hq',
    'passwd': 'password',
    'id': '3',
    'case': 'misbehavior'
}


NLEMF = {
    'url': 'https://llmlbra0.ccsrm.lab.in:8443/cms/General/index.jsp',
    'uname': 'super',
    'passwd': 'password',
    'id': '4',
    'case': 'national herald'
}


LOCAL = {
    'id_type': 'endDgt',
    'id_prefix': '956002222',
    'input': OrderedDict([
        ('target_type', 'E164'),
        ('region', 'NLD'),
        ('network', 'LOCAL')
    ]),
    'circle': '2',
    'tsp': '202',
}


ROAMING = {
    'id_type': 'endDgt',
    'id_prefix': '971702222',
    'input': OrderedDict([
        ('target_type', 'E164'),
        ('region', 'NLD'),
        ('network', 'ROAMING')
    ]),
    'circle': '9',
    'tsp': '804'
}


ILD = {
    'id_type': 'ildTarget',
    'id_prefix': '1234562222',
    'input': OrderedDict([
        ('target_type', 'E164'),
        ('region', 'ILD')
    ])
}


IMSI = {
    'id_type': 'imsiTarget',
    'id_prefix': '40491956002222',
    'input': OrderedDict([
        ('target_type', 'IMSI')
    ]),
    'tsp_type': 'GSM',
    'circle': '2',
    'tsp': '202'
}

IMEI = {
    'id_type': 'imeiTarget',
    'id_prefix': '3039195600222',
    'input': OrderedDict([
        ('target_type', 'IMEI')
    ]),
    'circle': '2',
    'tsp': '202',
}

MEID = {
    'id_type': 'meidTarget',
    'id_prefix': '80BCA22',
    'input': OrderedDict([
        ('target_type', 'MEID')
    ]),
    'circle': '2',
    'tsp': '212',
}

STATUS = { 'act': 'Activated', 'deact': 'Deactivated'}
TARGET = {}
def get_target_detail(target_type, lea):
    TARGET = target_type
    TARGET['id'] = TARGET['id_prefix'] + lea['id']
    TARGET['alias'] = TARGET['input']['target_type'] + lea['id']
    TARGET['warrant'] = "/cdot/war/" + lea['id']
    TARGET['mongrp'] = "DEFAULT"
    TARGET['case'] = lea['case']
    TARGET['status'] = ""
    if TARGET['input']['target_type'] == 'E164':
        if TARGET['input']['region'] == 'ILD':
            TARGET['number'] = TARGET['id']
        else:
            TARGET['number'] = "91" + TARGET['id']
    else:
        TARGET['number'] = TARGET['id']
    return TARGET