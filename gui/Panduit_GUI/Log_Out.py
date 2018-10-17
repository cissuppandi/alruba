from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import datetime
import os
import getpass
import Login
def log_out(ip):
                driver = Login.login(ip)
                print("############################LOGOUT FROM THE GUI#############")
                driver.find_element_by_xpath(".//*[contains(text(), 'admin')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Log Out')]").click()
                time.sleep(2)
                driver.close()
                return driver
