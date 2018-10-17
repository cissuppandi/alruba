import Login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import datetime
import os
import File_Creation
import getpass
#############CHECKING SEARCH FUNCTIONALITY#################
def search(ip):
                #ip=raw_input("Enter the IP address of the PDU")
                driver=Login.login(ip)
                #=File_Creation.file_create()
                print("#############CHECKING SEARCH FUNCTIONALITY#################")
                #.write("\n#############CHECKING SEARCH FUNCTIONALITY#################")
                srch=driver.find_element_by_id("search_app")
                srch.click()
                time.sleep(3)
                srch.send_keys("SNMP")
                srch.send_keys(Keys.ENTER)
                check=driver.find_elements_by_tag_name("header")
                b=check[1]
                if((b.text).strip()=="SNMP Management"):
                    print("SEARCH OPERATION COMPLETED SUCCESSFULLY")
                    #.write("\nSEARCH OPERATION COMPLETED SUCCESSFULLY")
                else:
                    print("SOMETHING IS WRONG",b.text)
                    #.write("\nSOMETHING IS WRONG")
                srch.clear()
                time.sleep(3)
                print("SENDING A JUNK STRING")
                #.write("\nSENDING A JUNK STRING")
                srch.send_keys(name)
                check=driver.find_elements_by_tag_name("header")
                b=check[1]
                print(b.text)
                if((b.text).strip()=="SNMP Management"):
                    print("SEARCH OPERATION COMPLETED SUCCESSFULLY,NO CHANGE IN RESULT")
                    #.write("\nSEARCH OPERATION COMPLETED SUCCESSFULLY,NO CHANGE IN RESULT")
                else:
                    print("SOMETHING IS WRONG",b.text)
                    #.write("\nSOMETHING IS WRONG")
                #.close()
                return driver
