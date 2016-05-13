__author__ = 'vishwanath dewangan'
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def login(driver, user):
    local_driver = driver
    local_url = user['url']
    local_uname = user['uname']
    local_passwd = user['passwd']
    local_driver.get(local_url)
    local_driver.find_element_by_name("username").send_keys(local_uname)
    local_driver.find_element_by_name("j_password").send_keys(local_passwd)
    local_driver.find_element_by_xpath("//a[@title='Submit form']").click()

def logout(driver):
    local_driver = driver
    local_driver.switch_to.default_content()
    local_driver.find_element_by_xpath("//a[@title='Log out']").click()
    local_driver.switch_to_alert().accept()

def open_prov(driver):
    local_driver = driver
    local_driver.find_element_by_xpath("//span[contains(text(),'Provisioning Management')]").click()
    local_driver.find_element_by_xpath("//span[contains(text(), 'TSP Target Provisioning')]").click()

def open_warrant(driver):
    local_driver = driver
    local_driver.find_element_by_xpath("//span[contains(text(),'Warrant Management')]").click()

def check_exists_by_xpath(driver, xpath):
    try:
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    except TimeoutException:
       return False
    return True

def HelloWorld():
    print "Hello World"