__author__ = 'vishwanath dewangan'
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from gui.basic_opr import login, logout, open_prov


def get(driver, target, user):
    local_driver = driver
    local_user = user
    local_target = target

    login(local_driver, local_user)

    open_prov(local_driver)

    local_driver.switch_to.frame(0)
    local_driver.find_element_by_xpath("//a[@name='display']").click()
    local_driver.find_element_by_xpath("//input[@id='Exact']").click()
    local_driver.find_element_by_xpath("//input[@name='targetId']").send_keys(local_target['number'])
    local_driver.find_element_by_xpath("//a[contains(.,'Submit')]").click()

    # Getting status of target
    try:
        target['status'] = local_driver.find_element_by_xpath("//table[@id='DisplayInfo']/tbody/tr/td[11]").text
    except NoSuchElementException:
        target['status'] = local_driver.find_element_by_xpath("//p[@class='info']").text

    logout(local_driver)


def verify(driver, target, user, sts):
    local_driver = driver
    local_target = target
    local_user = user
    local_status = sts

    for i in range(10):
        get(local_driver, local_target, local_user)
        get_status = local_target['status']
        print time.strftime("%Y-%m-%d %H:%M:%S"), get_status
        if get_status == local_status or get_status == "Error" or get_status == "No records found":
            break
        time.sleep(60)
    return get_status
