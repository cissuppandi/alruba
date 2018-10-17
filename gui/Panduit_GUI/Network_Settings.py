import Login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import datetime
import os
import getpass
import File_Creation
def network_settings_change(ip):
    ##########Changing option in the Network settings########
                driver=Login.login(ip)
                ##output=File_Creation.file_create()
                print("##########Changing option in the Network settings########")
                #output.write("\n##########Changing option in the Network settings########")
                time.sleep(2)
                se=driver.find_elements_by_tag_name("svg")
                se[4].click()
                time.sleep(1)
                part=driver.find_elements_by_tag_name("a")
                time.sleep(1)
                part[1].click()
                return driver
