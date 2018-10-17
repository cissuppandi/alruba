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
def outlet_verify(ip):
                #ip=raw_input("Enter the IP address of the PDU")
                driver=Login.login(ip)
                ##output=File_Creation.file_create(
         #####################VERIFYING OUTLET FUNCTIONALITY##########
                print("#####################VERIFYING OUTLET FUNCTIONALITY##########")
                out1=driver.find_elements_by_tag_name("svg")
                ##output.write("\n#####################VERIFYING OUTLET FUNCTIONALITY##########")
                print("VERIFYING OUTLET ONE BY TURNING IT OFF")
                time.sleep(2)
                out1[11].click()
                off=driver.find_elements_by_tag_name("a")
                time.sleep(2)
                off[1].click()
                yes=driver.find_elements_by_tag_name("button")
                time.sleep(2)
                yes[1].click()
                #output.close()
                return driver
