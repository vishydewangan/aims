#!/usr/bin/python
__author__ = 'vishwanath dewangan'
import time
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from provisioning import status
from gui.basic_opr import login, logout, open_prov, check_exists_by_xpath


def approve(driver, target, rmc, req_type):
    local_driver = driver
    local_rmc = rmc
    local_target = target

    for i in range(10):
        login(local_driver, local_rmc)
        open_prov(local_driver)
        local_driver.switch_to.frame(0)
        local_driver.find_element_by_xpath("//a[@name='display']").click()
        if req_type == "activation":
            local_driver.find_element_by_xpath("//select[@id='status']").send_keys("Pending for Approval")
        elif req_type == "modification":
            local_driver.find_element_by_xpath("//select[@id='status']").send_keys("Pending Approval for Modification")
        elif req_type == "deactivation":
            local_driver.find_element_by_xpath("//select[@id='status']").send_keys("Pending Approval for Deactivation")
        local_driver.find_element_by_xpath("//input[@id='Exact']").click()
        local_driver.find_element_by_xpath("//input[@name='targetId']").send_keys(local_target['number'])
        local_driver.find_element_by_xpath("//a[contains(text(),'Submit')]").click()
        try:
            target['status'] = local_driver.find_element_by_xpath("//table[@id='DisplayInfo']/tbody/tr/td[11]").text
        except NoSuchElementException:
            target['status'] = local_driver.find_element_by_xpath("//p[@class='info']").text
        print time.strftime("%Y-%m-%d %H:%M:%S"), target['status']
        if local_target['status'] == "Pending for Approval" or local_target['status'] == "Modification pending for Approval" or local_target['status'] == "Deactivation pending for Approval":
            break
        logout(local_driver)
        time.sleep(30)
    assert local_target['status'] == "Pending for Approval" or local_target['status'] == "Modification pending for Approval" or local_target['status'] == "Deactivation pending for Approval", "No Approval request received by RMC"

    local_driver.find_element_by_xpath("//img[@alt='Edit']").click()
    local_driver.find_element_by_xpath("//input[@id='tidCheck']").click()
    local_driver.find_element_by_xpath("//input[@id='ttCheck']").click()
    local_driver.find_element_by_xpath("//input[@id='leaCheck']").click()
    local_driver.find_element_by_xpath("//input[@id='stateCheck']").click()
    xpath = "//input[@id='tspTypeCheck']"
    if check_exists_by_xpath(local_driver, xpath):
        local_driver.find_element_by_xpath("%s" %xpath).click()
    xpath = "//input[@id='tspCheck']"
    if check_exists_by_xpath(local_driver, xpath):
        local_driver.find_element_by_xpath("%s" %xpath).click()
    local_driver.find_element_by_xpath("//input[@id='provTypeCheck']").click()
    local_driver.find_element_by_xpath("//input[@id='startTimeCheck']").click()
    local_driver.find_element_by_xpath("//input[@id='stopTimeCheck']").click()
    local_driver.find_element_by_xpath("//input[@id='contentCheck']").click()
    local_driver.find_element_by_xpath("//input[@id='warrantCheck']").click()
    xpath = "//input[@id='warrantFileCheck']"
    if check_exists_by_xpath(local_driver, xpath):
        local_driver.find_element_by_xpath("%s" %xpath).click()
    local_driver.find_element_by_xpath("//input[@id='warrantDateCheck']").click()
    local_driver.find_element_by_xpath("//a[@id='approve']").click()
    local_driver.switch_to_alert().accept()
    try:
        local_driver.switch_to_alert().accept()
    except NoAlertPresentException:
        pass
    text = time.strftime("%Y-%m-%d %H:%M:%S") + " Target " + local_target['id'] + " successfully approved"
    assert "successfully approved" or "To be modified" in local_driver.page_source, local_target['id'] + " Target approval failed"
    assert local_target['id'] in local_driver.page_source, local_target['id'] + " Target approval failed"
    print text

    logout(local_driver)