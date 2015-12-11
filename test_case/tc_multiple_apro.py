#!/usr/bin/python
__author__ = 'vishwanath dewangan'
import unittest
import os
from selenium import webdriver
from provisioning import conf, target, approval



class provMultipleTargetApproval(unittest.TestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile(os.path.expanduser("/home/vishy/.mozilla/firefox/bbteei4s.selenium"))
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(2)

    def test_prov_multiple_t1_by_state_lea(self):
        local_driver = self.driver
        local_target = conf.get_target_detail(conf.LOCAL, conf.SLEA)
        local_lea = conf.SLEA
        local_rmc = conf.RMC
        for i in range(0,1000):
            local_target['id'] = str(9818100000 + i)
            local_target['number'] = '91'+local_target['id']
            print local_target['id'], local_target['number']
            #target.activate(local_driver, local_target, local_lea)
            approval.approve(local_driver, local_target, local_rmc, "activation")


    def test_prov_multiple_t2_by_state_lemf(self):
        local_driver = self.driver
        local_target = conf.get_target_detail(conf.LOCAL, conf.SLEMF)
        local_lea = conf.SLEMF
        local_rmc = conf.RMC
        for i in range(0,1000):
            local_target['id'] = str(9818200000 + i)
            local_target['number'] = '91'+local_target['id']
            print local_target['id'], local_target['number']
            #target.activate(local_driver, local_target, local_lea)
            approval.approve(local_driver, local_target, local_rmc, "activation")

    def test_prov_multiple_t3_by_national_lea(self):
        local_driver = self.driver
        local_target = conf.get_target_detail(conf.LOCAL, conf.NLEA)
        local_lea = conf.NLEA
        local_rmc = conf.RMC
        for i in range(0,1000):
            local_target['id'] = str(9818300000 + i)
            local_target['number'] = '91'+local_target['id']
            print local_target['id'], local_target['number']
            #target.activate(local_driver, local_target, local_lea)
            approval.approve(local_driver, local_target, local_rmc, "activation")

    def test_prov_multiple_t4_by_national_lemf(self):
        local_driver = self.driver
        local_target = conf.get_target_detail(conf.LOCAL, conf.NLEMF)
        local_lea = conf.NLEMF
        local_rmc = conf.RMC
        for i in range(0,1000):
            local_target['id'] = str(9818400000 + i)
            local_target['number'] = '91'+local_target['id']
            print local_target['id'], local_target['number']
            #target.activate(local_driver, local_target, local_lea)
            approval.approve(local_driver, local_target, local_rmc, "activation")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
