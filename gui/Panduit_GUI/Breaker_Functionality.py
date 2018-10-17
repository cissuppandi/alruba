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
###############CHANGING BREAKER NAME#########
def breaker_function(breaker_1,breaker_2,ip):
                global driver
                driver=Login.login(ip)
                time.sleep(2)
                home=driver.find_elements_by_tag_name("svg")
                home[0].click()
                dash=driver.find_elements_by_css_selector("a.grommetux-anchor")
                a=dash[2]
                a.click()
                #ip=raw_input("Enter the IP address of the PDU")                
                ##output=File_Creation.file_create()
                print("###############CHANGING BREAKER NAME#########")
                #output.write("\n###############CHANGING BREAKER NAME#########")
                print("CHANGING THE BREAKER NAME")
                #output.write("\nCHANGING THE BREAKER NAME")
                time.sleep(7)
                edit=driver.find_elements_by_tag_name("svg")
                edit[10].click()
                time.sleep(1)
                bk=driver.find_elements_by_tag_name("input")
                bk[0].clear()
                time.sleep(1)
                bk[0].send_keys(breaker_1)
                time.sleep(1)
                bk[1].clear()
                time.sleep(1)
                bk[1].send_keys(breaker_2)
                time.sleep(2)
                save=driver.find_elements_by_tag_name("button")
                save[1].click()
                time.sleep(2)
                save=driver.find_elements_by_tag_name("button")
                save[3].click()                
                ##########CHEKING THE BREAKER NAME#########
                print("##########CHEKING THE BREAKER NAME#########")
                #output.write("\n##########CHEKING THE BREAKER NAME#########")
                time.sleep(2)
                tab_select=driver.find_elements_by_tag_name("li")
                print("THE CHANGED NAME OF THE BREAKER_1:{}".format(tab_select[1].text)+"\n"+"THE CHANGED NAME OF THE BREAKER_2:{}".format(tab_select[2].text))
                #output.write("\nTHE CHANGED NAME OF THE BREAKER_1:{}".format(tab_select[1].text)+"\n"+"THE CHANGED NAME OF THE BREAKER_2:{}".format(tab_select[2].text))
                if(str(tab_select[1].text)==breaker_1 and str(tab_select[2].text)==breaker_2):
                             print("BOTH THE NAME HAS BEEN CHANGED")
                             #output.write("\nBOTH THE NAME HAS BEEN CHANGED")
                else:
                    print("NAME HAS NOT BEEN CHANGED")
                    #output.write("\nNAME HAS NOT BEEN CHANGED")
                #output.close()    
                return  driver  
