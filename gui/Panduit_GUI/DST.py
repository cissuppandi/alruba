
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import datetime
import os
import getpass
import Network_Settings
import File_Creation
def dst_enable(ip):                               
                driver=Network_Settings.network_settings_change(ip)
                #output=File_Creation.file_create()
                print("#######Enabling the DST#################")
                #output.write("\n#######Enabling the DST#################")
                print("ENABLING THE DAYLIGHT SAVING TIME")
                #output.write("\nENABLING THE DAYLIGHT SAVING TIME")
                dst=driver.find_elements_by_tag_name("a")
                dst[6].click()
                time.sleep(1)
                driver.find_element_by_xpath(    ".//*[contains(text(), 'Enable')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Save')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Do you really want to apply changes now')]"
                ).click()
                time.sleep(2)
                driver.find_element_by_xpath(    ".//*[contains(text(), 'Apply')]").click()
                print("WATING FOR 25 SEC TO RESTART ")
                #output.write("\nWATING FOR 25 SEC TO RESTART ")
                for i in xrange(26,0,-1):
                                 sys.stdout.write(str(i)+' ')
                                 sys.stdout.flush()
                                 time.sleep(1)
                #output.close()
                return driver
def dst_check(ip):
                print("\nLOGGING AGAIN TO VERIFY")
                Network_Settings.network_settings_change(ip)
                part=driver.find_elements_by_tag_name("a")
                time.sleep(1)
                part[1].click()
                time.sleep(2)
                en=driver.find_elements_by_tag_name("svg")
                if(str(en[21].get_attribute("aria-label"))=="checkmark"):
                          print("SUCCESS!!!"+"\n"+"DAYLIGHT SAVING is Enabled")
                          #output.write("\nSUCCESS!!!"+"\n"+"DAYLIGHT SAVING is Enabled")
                else:
                    print("ERROR!!!!"+"\n"+"DAYLIGHT SAVING is Disabled")
                    #output.write("\nERROR!!!!"+"\n"+"DAYLIGHT SAVING is Disabled")
                #output.close()
                return driver
