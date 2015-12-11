__author__ = 'vishwanath dewangan'
import time
import re
from selenium.webdriver.support.ui import Select
from gui.basic_opr import login, logout, open_warrant, check_exists_by_xpath

def generate(driver, target, lea):
    local_driver = driver
    local_lea = lea
    local_target = target

    login(local_driver, local_lea)
    open_warrant(local_driver)
    local_driver.switch_to.frame(0)
    Select(local_driver.find_element_by_xpath("//select[@name='targetType']")).select_by_visible_text(local_target['input']['target_type'])

    xpath = "//select[@name='tspType']"
    if check_exists_by_xpath(local_driver, xpath):
        Select(local_driver.find_element_by_xpath(xpath)).select_by_visible_text(local_target['tsp_type'])

    local_driver.find_element_by_xpath("//input[@id='%s']" %local_target['id_type']).send_keys(local_target['id'])

    xpath = "//tr[@class= 'tspRow']"
    #xpath = "//li[@value='%s']" %local_target['circle']
    if check_exists_by_xpath(local_driver, xpath):
        local_driver.find_element_by_xpath("//li[@value='%s']" %local_target['circle']).click()
        local_driver.find_element_by_xpath("//input[@id='%s']" %local_target['tsp']).click()

    local_driver.find_element_by_xpath("//input[@class='supFile']").send_keys("/media/vishy/download/warrant.pdf")
    local_driver.find_element_by_xpath("//a[@title='Submit Request']").click()
    msg = local_driver.switch_to.alert
    print msg.text
    warrant_id = re.search('([0-9].*[0-9])', msg.text).group(1)
    msg.accept()
    local_target['warrant'] = warrant_id
    print "Request generated successfully with warrant-id ", local_target['warrant']

    logout(local_driver)