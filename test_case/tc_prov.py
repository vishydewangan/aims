#!/usr/bin/python
__author__ = 'vishwanath dewangan'
import unittest
import re
import os
from selenium import webdriver
from provisioning import approval, conf, status, target
from collections import OrderedDict


class provTestCases(unittest.TestCase):
    """
    This class is used for putting all test method of provisioning activity.
    """

    def setUp(self):
        self.profile = webdriver.FirefoxProfile('/home/vishy/.mozilla/firefox/lu9o1giq.default')
        self.driver = webdriver.Firefox(self.profile)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

def make_activation_test(target_type, lea_type):
    """
    Template function for creating provisioning activation test method.
    """
    def test(self):
        print ""
        local_driver = self.driver
        local_target = conf.get_target_detail(target_type, lea_type)
        local_lea = lea_type
        local_rmc = conf.RMC
        local_status = conf.STATUS['act']

        # Activation request by LEA
        target.activate(local_driver, local_target, local_lea)

        # Approving from RMC
        approval.approve(local_driver, local_target, local_rmc, "activation")

        # Verify the status of target
        final_status = status.verify(local_driver, local_target, local_lea, local_status)
        self.assertTrue(final_status == local_status, local_target['id'] + " not activated and its status is " + final_status)
    return test


def make_modification_test(target_type, lea_type):
    """
    Template function for creating provisioning modification test method.
    """
    def test(self):
        print ""
        local_driver = self.driver
        local_target = conf.get_target_detail(target_type, lea_type)
        local_lea = lea_type
        local_rmc = conf.RMC
        local_status = conf.STATUS['act']

        # Activation request by LEA
        target.modify(local_driver, local_target, local_lea)

        # Approving from RMC
        approval.approve(local_driver, local_target, local_rmc, "modification")

        # Verify the status of target
        final_status = status.verify(local_driver, local_target, local_lea, local_status)
        self.assertTrue(final_status == local_status, local_target['id'] + " not modified and its status is " + final_status)
    return test


def make_deactivation_test(target_type, lea_type):
    """
    Template function for creating provisioning deactivation test method.
    """
    def test(self):
        print ""
        local_driver = self.driver
        local_target = conf.get_target_detail(target_type, lea_type)
        local_lea = lea_type
        local_rmc = conf.RMC
        local_status = conf.STATUS['deact']

        #print unittest.TestCase.id(self)

        # Activation request by LEA
        target.deactivate(local_driver, local_target, local_lea)

        # Approving from RMC
        approval.approve(local_driver, local_target, local_rmc, "deactivation")

        # Verify the status of target
        final_status = status.verify(local_driver, local_target, local_lea, local_status)
        self.assertTrue(final_status == local_status, local_target['id'] + " not deactivated and its status is " + final_status)
    return test


if __name__ == "__main__":
    #Module below creates the test methods for all combination of target type and lea type.
    id=1
    ttype = ['LOCAL', 'ROAMING', 'ILD', 'IMSI', 'IMEI', 'MEID']
    action= OrderedDict([('act', make_activation_test), ('mod', make_modification_test), ('deact', make_deactivation_test) , ('react', make_activation_test)])
    ltype = ['SLEA', 'SLEMF', 'NLEA', 'NLEMF']
    for i in ttype:
        for key, value in action.items():
            for k in ltype:
                target_type = getattr(conf, i)
                lea_type=getattr(conf, k)
                tc_id = str(id).zfill(3)
                test_method = value(target_type, lea_type)
                test_method.__name__ = 'test_prov_%s_%s_%s_%s' %(tc_id, i.lower(), key, k.lower())
                setattr(provTestCases, test_method.__name__, test_method)
                id+=1

    complete_test_cases = provTestCases.__dict__.keys()
    complete_test_cases.sort()
    complete_test_cases=complete_test_cases[4:]

    #Section below select the test methods from complete set.
    selected_test_cases=[]
    for tc in complete_test_cases:
        match = re.search(".*nlemf.*",tc)
        if match:
            selected_test_cases.append(match.group(0))

    #Create the test suite of selected test method
    suite = unittest.TestSuite()
    [suite.addTest(provTestCases(x)) for x in selected_test_cases]
    print suite

    #Runs the test suite
    unittest.TextTestRunner(verbosity=2).run(suite)
