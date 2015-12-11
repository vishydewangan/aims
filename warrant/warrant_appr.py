__author__ = 'vishwanath dewangan'
import time
import re
from selenium.webdriver.support.ui import Select
from gui.basic_opr import login, logout, open_warrant, check_exists_by_xpath

def approve(driver, target, mha):
    local_driver = driver
    local_mha = mha
    local_target = target

    login(local_driver, local_mha)
    open_warrant(local_driver)
    local_driver.switch_to.frame(0)
    local_driver.find_element_by_xpath("//a[contains(text(),'Display')]").click()
    xpath = "//td[contains(@onclick,'%s')]"%local_target['warrant']
    if check_exists_by_xpath(local_driver, xpath):
        local_driver.find_element_by_xpath("%s" %xpath).click()
    else:
        print "Warrant not exists"
        logout(local_driver)
    local_driver.find_element_by_xpath("//input[@id='fileLoc']").send_keys("/media/vishy/download/warrant.pdf")
    local_driver.find_element_by_xpath("//a[contains(@onclick,'checkForm')]").click()
    local_driver.switch_to_alert().accept()
    print "Warrant approved successfully with warrant-id ", local_target['warrant']

    logout(local_driver)