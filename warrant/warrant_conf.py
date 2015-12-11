___author__ = 'vishwanath dewangan'

from collections import OrderedDict

MHA = {
    'url': 'https://cnmlbxx2.ccsrm.lab.in:8443/warrant/General/index.jsp',
    'uname': 'mha_super',
    'passwd': 'password'
}


SLEA = {
    'url': 'https://cnmlbxx2.ccsrm.lab.in:8443/warrant/General/index.jsp',
    'uname': 'doe_del_super',
    'passwd': 'password',
    'id': '1'
}


SLEMF = {
    'url': 'https://cnmlbxx2.ccsrm.lab.in:8443/warrant/General/index.jsp',
    'uname': 'ib_del_super',
    'passwd': 'password',
    'id': '2'
}


NLEA = {
    'url': 'https://cnmlbxx2.ccsrm.lab.in:8443/warrant/General/index.jsp',
    'uname': 'ib_hq_super',
    'passwd': 'password',
    'id': '3'
}


NLEMF = {
    'url': 'https://cnmlbxx2.ccsrm.lab.in:8443/warrant/General/index.jsp',
    'uname': 'raw_hq_super',
    'passwd': 'password',
    'id': '4'
}


LOCAL = {
    'id_type': 'endDgt',
    'id_prefix': '956002222',
    'input': OrderedDict([
        ('target_type', 'E.164'),
        ('network', 'LOCAL')
    ]),
    'circle': '2',
    'tsp': '202',
}


ROAMING = {
    'id_type': 'endDgt',
    'id_prefix': '971702222',
    'input': OrderedDict([
        ('target_type', 'E.164'),
        ('network', 'ROAMING')
    ]),
    'circle': '9',
    'tsp': '804'
}


ILD = {
    'id_type': 'ildTarget',
    'id_prefix': '1234562222',
    'input': OrderedDict([
        ('target_type', 'ILD')
    ]),
    'circle': '2'
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
        ('target_type', 'ESN/MEID')
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
    TARGET['status'] = ""
    if TARGET['input']['target_type'] == 'E.164':
        TARGET['number'] = "91" + TARGET['id']
    else:
        TARGET['number'] = TARGET['id']
    return TARGET