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
def config_upload(ip):
                #ip=raw_input("Enter the IP address of the PDU")
                global driver
                driver=Login.login(ip)
                #output=File_Creation.file_create()
                print("############UPLOAD REQUIRED CONFIGURATION##########")
                #output.write("############UPLOAD REQUIRED CONFIGURATION##########")
                se=driver.find_elements_by_tag_name("svg")
                se[4].click()
                part=driver.find_elements_by_tag_name("a")
                part[2].click()
                time.sleep(4)
                driver.find_element_by_xpath(".//*[contains(text(), 'Action')]").click()
                time.sleep(3)
                driver.find_element_by_xpath(".//*[contains(text(), 'Upload Configuration')]").click()
                time.sleep(2)
                cnf=driver.find_elements_by_tag_name("input")
                time.sleep(2)
                path=os.getcwd()+"/conf.ini"
                cnf[0].send_keys(path)
                time.sleep(1)
                up=driver.find_elements_by_tag_name("button")
                time.sleep(2)
                up[1].click()
                print("PLEASE WAIT WHILE THE REQUIRED CONFIGURATION FLASH AND REBOOT THE PDU.IT MAY TAKE 40 sec .\n.PLEASE WAIT....")
                for i in xrange(40,0,-1):
                        sys.stdout.write(str(i)+' ')
                        sys.stdout.flush()                                
                        time.sleep(1)
                Login.login(ip)
                #output.close()
                return driver
