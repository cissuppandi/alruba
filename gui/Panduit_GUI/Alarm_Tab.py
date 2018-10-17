import Login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import datetime
import os
import getpass
def alarm(ip):
                #ip=raw_input("Enter the IP address of the PDU")
                driver=Login.login(ip)
     #########################VERIFYING ALARM##########################
                print("#########################VERIFYING ALARM##########################")
                #output.write("\n#########################VERIFYING ALARM##########################")
                print("VERIGYING THE ALARM FUNCTIONALITY")
                #output.write("\nVERIGYING THE ALARM FUNCTIONALITY")
                alarm=driver.find_elements_by_tag_name("svg")
                time.sleep(1)
                alarm[1].click()
                AA=driver.find_elements_by_tag_name("a")
                print(str(AA[1].text+"\n"+AA[2].text))
                #output.write(str(AA[1].text+"\n"+AA[2].text))
                time.sleep(1)
                AA[1].click()
                alarm=driver.find_elements_by_tag_name("svg")
                time.sleep(1)
                alarm[1].click()
                time.sleep(1)
                AA=driver.find_elements_by_tag_name("a")
                time.sleep(1)
                AA[2].click()
                #output.close()
                return driver
