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
def outlet_dump(ip):
 ########VERIFYING OUTLET NAME###############
                #ip=raw_input("Enter the IP address of the PDU")
                driver=Login.login(ip)
                ##output=File_Creation.file_create()
                #driver.refresh()
                time.sleep(10)   
                print("########VERIFYING OUTLET NAME###############")
                #output.write("\n########VERIFYING OUTLET NAME###############")
                OD=driver.find_elements_by_tag_name("span")
                time.sleep(2)
                OD[14].click()
                time.sleep(3)
                OD=driver.find_elements_by_tag_name("td")
                i=4
                for i in  range(4,len(OD),7):
                                time.sleep(2)
                                OUTLET_NAME=OD[i]                
                                on_delay=OD[i+2]
                                off_delay=OD[i+3]
                                reboot_duration=OD[i+5]
                                #output.write("\nOUTLET NAME:{}".format(OUTLET_NAME.text)+"\n"+"On_delay:{}".format(on_delay.text)+"\n"+"Off_delay:{}".format(off_delay.text)+"\n"+"Reboot_duration:{}".format(reboot_duration.text))
                                print("OUTLET NAME:{}".format(OUTLET_NAME.text)+"\n"+"On_delay:{}".format(on_delay.text)+"\n"+"Off_delay:{}".format(off_delay.text)+"\n"+"Reboot_duration:{}".format(reboot_duration.text))
                #output.close()
                return driver
