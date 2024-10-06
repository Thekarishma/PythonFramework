
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import config
local = threading.local()


def open_url_in_chrome(url):
    local.driver = webdriver.Chrome()
    local.driver.get(url)
    local.driver.implicitly_wait(config.IMPLICIT_WAIT_TIME)
    print("driver="+local.driver.session_id)
    return local.driver


def quit_chrome(driver):
    driver.quit()

def click(xpath,driver):
    driver.find_element(By.XPATH,xpath).click()

def input(xpath,value,driver):
    driver.find_element(By.XPATH,xpath).send_keys(value)