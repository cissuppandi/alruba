import Network_Settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import datetime
import os
import getpass
import File_Creation
def SSH_FTP_enable(ip):
                driver=Network_Settings.network_settings_change(ip)
                #=File_Creation.file_create()
                print("##########CHANGING THE SSH/FTP##########")
                #.write("\n##########CHANGING THE SSH/FTP##########")
                print("ENABLING SSH/FTP Access Configuration")
                #.write("\nENABLING SSH/FTP Access Configuration")
                ssh=driver.find_elements_by_tag_name("a")
                time.sleep(2)
                ssh[3].click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[contains(text(), 'SSH Access')]").click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[contains(text(), 'FTPs Access')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Save')]").click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[contains(text(), 'Do you really want to apply changes now')]"
                ).click()
                time.sleep(1)
                driver.find_element_by_xpath(    ".//*[contains(text(), 'Apply')]").click()
                print("WATING FOR 25 SEC TO RESTART ")
                #.write("\nWATING FOR 25 SEC TO RESTART ")
                for i in xrange(26,0,-1):
                                 sys.stdout.write(str(i)+' ')
                                 sys.stdout.flush()
                                 time.sleep(1)               
                Network_Settings.network_settings_change(ip)
                #.close()
                return driver
def SSH_FTP_check(ip):
                driver=Network_Settings.network_settings_change(ip)
                #=File_Creation.file_create()
                en=driver.find_elements_by_tag_name("svg")
                if(str(en[15].get_attribute("aria-label"))=="checkmark"):
                          print("SUCCESS!!!"+"\n"+"SSH is Enabled")
                          #.write("\nSUCCESS!!!"+"\n"+"SSH is Enabled")
                else:
                    print("ERROR!!!!"+"\n"+"SSH  is Disabled")
                if(str(en[16].get_attribute("aria-label"))=="checkmark"):
                          print("SUCCESS!!!"+"\n"+"FTP is Enabled")
                          #.write("\nSUCCESS!!!"+"\n"+"FTP is Enabled")
                else:
                    print("ERROR!!!!"+"\n"+"FTP  is Disabled")
                    #.write("\nERROR!!!!"+"\n"+"FTP  is Disabled")
                #.close()
                return driver
