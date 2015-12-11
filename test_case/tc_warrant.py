__author__ = 'vishwant dewangan'
import unittest
import re
import os
from selenium import webdriver
from  warrant import warrant_conf, warrant_req, warrant_appr
from provisioning import conf, approval, target, status
from collections import OrderedDict


class warrantTestCases(unittest.TestCase):
    """
    This class is used for putting all test method of generation and approval of warrant.
    """

    def setUp(self):
        self.profile = webdriver.FirefoxProfile('/home/vishy/.mozilla/firefox/lu9o1giq.default')
        self.driver = webdriver.Firefox(self.profile)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

def make_warrant_request_test(target_type, lea_type):
    """
    Template function for creating provisioning activation test method.
    """
    def test(self):
        print ""
        local_driver = self.driver
        local_target = warrant_conf.get_target_detail(target_type, lea_type)
        local_lea = lea_type
        local_mha = warrant_conf.MHA
        local_rmc = conf.RMC
        local_status = conf.STATUS['act']

        # Activation request by LEA
        warrant_req.generate(local_driver, local_target, local_lea)

        # Approving from MHA
        warrant_appr.approve(local_driver, local_target, local_mha)

         # Approving from RMC
        approval.approve(local_driver, local_target, local_rmc, "activation")

        # Verify the status of target
        final_status = status.verify(local_driver, local_target, local_lea, local_status)
        self.assertTrue(final_status == local_status, local_target['id'] + " not activated and its status is " + final_status)
    return test

if __name__ == "__main__":
    #Module below creates the test methods for all combination of target type and lea type.
    id=1
    ttype = ['LOCAL', 'ROAMING', 'ILD', 'IMSI', 'IMEI', 'MEID']
    ltype = ['SLEA', 'SLEMF', 'NLEA', 'NLEMF']
    for i in ttype:
        for k in ltype:
                target_type = getattr(warrant_conf, i)
                lea_type=getattr(warrant_conf, k)
                tc_id = str(id).zfill(3)
                test_method = make_warrant_request_test(target_type, lea_type)
                test_method.__name__ = 'test_warrant_%s_%s_%s' %(tc_id, i.lower(), k.lower())
                setattr(warrantTestCases, test_method.__name__, test_method)
                id+=1

    complete_test_cases = warrantTestCases.__dict__.keys()
    complete_test_cases.sort()
    complete_test_cases=complete_test_cases[4:]

    #Section below select the test methods from complete set.
    selected_test_cases=[]
    for tc in complete_test_cases:
        match = re.search(".*ild*.slea.*",tc)
        if match:
            selected_test_cases.append(match.group(0))

    #Create the test suite of selected test method
    suite = unittest.TestSuite()
    [suite.addTest(warrantTestCases(x)) for x in selected_test_cases]
    print suite

    #Runs the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)