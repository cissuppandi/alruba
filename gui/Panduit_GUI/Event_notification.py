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
def event_notification(ip):
                driver=Login.login(ip)
                ##output=File_Creation.file_create() 
                print("#######################EVENT NOTIFICATION#############")
                #output.write("\n#######################EVENT NOTIFICATION#############")
                se=driver.find_elements_by_tag_name("svg")
                se[4].click()
                time.sleep(1)
                part=driver.find_elements_by_tag_name("a")
                print("CHECKING THE EVENT NOTIFICATION PAGE")
                time.sleep(1)
                part[5].click()
                print("CHECKING EMAIL CHECK BOX")
                email=driver.find_element_by_name("allEmail")
                time.sleep(1)
                m=driver.find_elements_by_tag_name("label")
                if(email.is_selected()==True):
                        print("THE EMAIL CHECK BOX IS ALREADY ENABLED,SO DISABLING IT")
                                
                        m[0].click()
                        time.sleep(1)
                        m[0].click()       
                else:
                        print("THE EMAIL CHECK BOX IS ALREADY DISABLED,SO ENABLING IT")
                        #time.sleep(2)
                        m[0].click()        
                snmp=driver.find_element_by_name("allSnmp")
                if(snmp.is_selected()==True):
                        print("THE SNMP CHECK BOX IS ALREADY ENABLED,SO DISABLING IT")
                       # time.sleep(2)
                        m[1].click()
                        time.sleep(1)
                        m[1].click()       
                else:
                        print("THE SNMP CHECK BOX IS ALREADY DISABLED,SO ENABLING IT")
                        #time.sleep(2)
                        m[1].click()
                sys=driver.find_element_by_name("allSyslog")
                if(sys.is_selected()==True):
                        print("THE SYSLOG CHECK BOX IS ALREADY ENABLED,SO DISABLING IT")
                        #time.sleep(2)
                        m[2].click()
                        time.sleep(1)
                        m[2].click()
                        sys_count=1
                else:
                        print("THE SYSLOG CHECK BOX IS ALREADY DISABLED,SO ENABLING IT")
                        time.sleep(2)
                        m[2].click()        
                        sys_count=2
                time.sleep(1)
                #output.close()
                return driver
def event_notofication_verify(ip):
                driver=Login.login(ip)
                #output=File_Creation.file_create() 
                se=driver.find_elements_by_tag_name("svg")
                se[4].click()
                time.sleep(1)                
                print("VERIFYING THE SETTINGS AGAIN")
                time.sleep(1)
                snmp=driver.find_element_by_name("allSnmp")
                email=driver.find_element_by_name("allEmail")
                sys=driver.find_element_by_name("allSyslog")
                if(email.is_selected()==True):
                        print("SNMP_EMAIL IS ENABLE")
                        #output.write("\nSNMP_EMAIL IS ENABLE")
                else:
                     print("SNMP_EMAIL IS DISABLED")
                     #output.write("\nSNMP_EMAIL IS DISABLED")
                if(snmp.is_selected()==True):
                        print("SNMP_TRAP IS ENABLED")
                        #output.write("\nSNMP_TRAP IS ENABLED")
                else:
                     print("SNMP_TRAP IS DISABLED")
                     #output.write("\nSNMP_TRAP IS DISABLED")
                if(sys.is_selected()==True):
                        print("SYSLOG IS ENABLED")
                        #output.write("\nSYSLOG IS ENABLED")
                else:
                     print("SYSLOG IS DISABLED")
                     #output.write("\nSYSLOG IS DISABLED")
                #output.close()
                return driver
