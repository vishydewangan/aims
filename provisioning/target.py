__author__ = 'vishwanath dewangan'
import time
from selenium.webdriver.support.ui import Select
from gui.basic_opr import login, logout, open_prov, check_exists_by_xpath

# Opening Login Page
def activate(driver, target, lea):
    local_driver = driver
    local_lea = lea
    local_target = target

    login(local_driver, local_lea)
    open_prov(local_driver)
    local_driver.switch_to.frame(0)

    for key, value in local_target['input'].items():
        local_driver.find_element_by_xpath("//input[@id='%s']" %value).click()

    xpath = "//select[@name='homeTspType']"
    if check_exists_by_xpath(local_driver, xpath):
        Select(local_driver.find_element_by_xpath(xpath)).select_by_visible_text(local_target['tsp_type'])
    local_driver.find_element_by_xpath("//input[@id='%s']" %local_target['id_type']).send_keys(local_target['id'])
    local_driver.find_element_by_xpath("//a[@title='Submit']").click()

    xpath = "//td[contains(.,'Deactivated')]"
    if check_exists_by_xpath(local_driver, xpath):
        print "Target " + local_target['id'] + " is deactivated"
        xpath1 = "%s/../td[4]//a[@title='Activate target']" %xpath
        if check_exists_by_xpath(local_driver, xpath1):
            local_driver.find_element_by_xpath(xpath1).click()
        xpath2 = "%s/../td[5]//a[@title='Activate target']" %xpath
        if check_exists_by_xpath(local_driver, xpath2):
            local_driver.find_element_by_xpath(xpath2).click()

    local_driver.find_element_by_xpath("//input[@name='alias']").send_keys(local_target['alias'])
    xpath = "//td[contains(., 'Circle')]"
    if check_exists_by_xpath(local_driver, xpath):
        local_driver.find_element_by_xpath("//li[@value='%s']" %local_target['circle']).click()
        local_driver.find_element_by_xpath("//input[@id='%s']" %local_target['circle']).click()
        local_driver.find_element_by_xpath("//input[@id='%s']" %local_target['circle']).click()
        local_driver.find_element_by_xpath("//input[@id='%s']" %local_target['tsp']).click()
    Select(local_driver.find_element_by_xpath("//select[@name='monitoringGroup']")).select_by_visible_text(local_target['mongrp'])
    Select(local_driver.find_element_by_xpath("//select[@name='targetCase']")).select_by_visible_text(local_target['case'])
    local_driver.find_element_by_xpath("//img[@onclick='showCalendarControl(document.inputform.stopTime,1)']").click()
    current_day = int(time.strftime("%d"))
    stop_day = (current_day + 7) % 30
    if stop_day < current_day:
        local_driver.find_element_by_xpath("//a[contains(@href, 'javascript:changeCalendarControlMonth(1);')]").click()
    local_driver.find_element_by_xpath('//a[contains(text(), "%s")]' %stop_day).click()

    #local_driver.find_element_by_xpath("//input[@id='hourtext']").click()
    #local_driver.find_element_by_xpath("//input[@id='hourtext']").clear()
    #local_driver.find_element_by_xpath("//input[@id='hourtext']").clear()
    #print local_driver.find_element_by_xpath("//input[@id='hourtext']").get_attribute('value')
    #local_driver.find_element_by_xpath("//input[@id='hourtext']").send_keys('21')
    #local_driver.find_element_by_xpath("//input[@id='minutetext']").clear()
    #local_driver.find_element_by_xpath("//input[@id='minutetext']").clear()
    #local_driver.find_element_by_xpath("//input[@id='minutetext']").send_keys('34')
    # local_driver.find_element_by_xpath("//a[contains(@href, 'javascript:setCalendarControlDate(2015,9,15,10,34)')]").click()

    local_driver.find_element_by_xpath("//input[@name='warrant']").send_keys(local_target['warrant'])
    local_driver.find_element_by_xpath("//a[@title='Activate target']").click()
    text = time.strftime("%Y-%m-%d %H:%M:%S") + " Target " + local_target['id'] + " successfully entered for activation"
    target_in_activation_page = local_driver.find_element_by_xpath("//span[@id='highlight']").text
    #print "local_target:", local_target['number']
    #print "target_in_page:", target_in_activation_page
    assert target_in_activation_page == local_target['number']
    print text

    logout(local_driver)


def modify(driver, target, lea):
    local_driver = driver
    local_lea = lea
    local_target = target

    login(local_driver, local_lea)

    open_prov(local_driver)

    local_driver.switch_to.frame(0)
    local_driver.find_element_by_xpath("//a[@name='display']").click()
    local_driver.find_element_by_xpath("//input[@id='Exact']").click()
    local_driver.find_element_by_xpath("//input[@name='targetId']").send_keys(local_target['number'])
    local_driver.find_element_by_xpath("//a[contains(.,'Submit')]").click()
    local_driver.find_element_by_xpath("//img[@alt='Edit']").click()

    # Change the input
    local_driver.find_element_by_xpath("//img[@onclick='showCalendarControl(document.inputform.stopTime,1)']").click()

    # Generating new Stop Time
    stop_time = local_driver.find_element_by_xpath("//input[@id = 'provStopTime']").get_attribute("value")
    stop_day = int(stop_time[:2])
    mod_day = (stop_day + 7) % 30
    if mod_day < stop_day:
        local_driver.find_element_by_xpath("//a[contains(@href, 'javascript:changeCalendarControlMonth(1);')]").click()
    local_driver.find_element_by_xpath('//a[contains(text(), "%s")]' % mod_day).click()

    # Generating new warrant
    old_warrant = local_driver.find_element_by_xpath("//input[@name='warrant']").get_attribute("value")
    new_warrant = old_warrant + "/new"
    if len(new_warrant) > 25:
        new_warrant = new_warrant[:11]
    local_driver.find_element_by_xpath("//input[@name='warrant']").clear()
    local_driver.find_element_by_xpath("//input[@name='warrant']").send_keys(new_warrant)

    local_driver.find_element_by_xpath("//a[@title='Modify the target']").click()
    local_driver.switch_to_alert().accept()

    text = time.strftime("%Y-%m-%d %H:%M:%S") + " Target " + local_target['id'] + " successfully entered for modification"
    target_in_modification_page =  local_driver.find_element_by_xpath("//table[@id='form-table']/tbody/tr/td[2]").text
    assert target_in_modification_page == local_target['number']
    print text

    # Logout from GUI
    logout(local_driver)


def deactivate(driver, target, lea):
    local_driver = driver
    local_lea = lea
    local_target = target

    login(local_driver, local_lea)

    open_prov(local_driver)

    local_driver.switch_to.frame(0)
    local_driver.find_element_by_xpath("//a[@name='display']").click()
    local_driver.find_element_by_xpath("//input[@id='Exact']").click()
    local_driver.find_element_by_xpath("//input[@name='targetId']").send_keys(local_target['number'])
    local_driver.find_element_by_xpath("//a[contains(.,'Submit')]").click()
    xpath = "//img[@alt='Edit']"
    if check_exists_by_xpath(local_driver, xpath):
        local_driver.find_element_by_xpath(xpath).click()
    else:
        print local_target['id'] + " not activated " + local_driver.find_element_by_xpath("//p[@class='info']").text
        logout(local_driver)
        return
    local_driver.find_element_by_xpath("//img[@onclick='showCalendarControl(document.inputform.stopTime,1)']").click()
    local_driver.find_element_by_xpath("//a[@title='Deactivate the target']").click()
    target_in_deactivation_page = local_driver.find_element_by_xpath("//span[@id='highlight']").text
    text = time.strftime("%Y-%m-%d %H:%M:%S") + " Target " + local_target['id'] + " successfully entered for deactivation"
    assert target_in_deactivation_page == local_target['number']
    print text

    logout(local_driver)