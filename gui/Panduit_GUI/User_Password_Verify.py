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
def pass_policy_check():
                driver=Login.login(ip)
                #=File_Creation.file_create()
                driver.find_element_by_xpath(".//*[contains(text(), 'admin')]").click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[contains(text(), 'User Accounts')]").click()      
                def password_checking(count):
                        global username,password
                        if(count==0):
                                username="admin"
                                password="12345"
                        elif(count==1):
                                username="admin"
                                password="1234567"
                        elif(count==2):
                                username="admin"
                                password="TEST"
                        elif(count==3):
                                username="admin"
                                password="12567!"
                        elif(count==4):
                                username="admin"
                                password="5687"
                             
                        return username,password

                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(),'Session Management')]").click()
                time.sleep(2)
                print("VERYFYING THE SETTINGS OF SIGN IN RETRIES")
                if(driver.find_element_by_name("chkuserblocking").is_selected()==True):
                        print("SIGN IN RETRIES ARE ENABLED")
                        time.sleep(1)
                        print("CHANGING THE NUMBER OF RETRIES")
                        time.sleep(1)        
                        driver.find_element_by_name("maxnumfailedlogins").send_keys("4")
                        print("CHANGING THE LOCKOUT TIME TO 1 MIN")
                        time.sleep(1)
                        driver.find_element_by_name("blocktimeout").send_keys("1 min")
                        time.sleep(1)
                        driver.find_element_by_xpath(".//*[contains(text(), 'Save')]").click()
                        time.sleep(1)
                        driver.find_element_by_xpath(".//*[contains(text(), 'OK')]").click()
                        time.sleep(1)
                        driver.find_element_by_xpath(".//*[contains(text(), 'admin')]").click()
                        time.sleep(1)
                        driver.find_element_by_xpath(".//*[contains(text(), 'Log Out')]").click()
                        print("VERYFYING WITH THE DIFFERENT USERNAME AND PASSWORD COMBINATION")
                        #.write("\nVERYFYING WITH THE DIFFERENT USERNAME AND PASSWORD COMBINATION")
                        for i in range(5):
                                time.sleep(3)
                                username1,password1=password_checking(i)                
                                print("USERNAME:{},PASSWORD:{}".format(username,password))
                                #.write("\nUSERNAME:{},PASSWORD:{}".format(username,password))
                                time.sleep(3)
                                username=driver.find_element_by_name("username")
                                username.clear()
                                #WebDriverWait(driver, timeout).until(username)
                                time.sleep(1)
                                username.send_keys(username1)
                                time.sleep(1)
                                password=driver.find_element_by_name("password")
                                password.clear()
                                #WebDriverWait(driver, timeout).until(password)
                                time.sleep(1)
                                password.send_keys(password1)
                                time.sleep(1)
                                submit=driver.find_element_by_xpath('//button')
                                submit.click()                
                                time.sleep(2)
                                try:
                                      a=driver.find_elements_by_tag_name("span")
                                      if(str(a[6].text)=="Invalid Username or Password"):
                                              print("SUCCESS!!PASSWORD IS NOT WORKING")
                                              #.write("\nSUCCESS!!PASSWORD IS NOT WORKING")
                                      elif(str(a[6].text)=="User is blocked, Please try after some time"):
                                              print("USER BLOCKING SUCCESFULLY DONE\n WAITING FOR 1 MIN\n..PLEASE WAIT")                              
                                              import sys
                                              import time
                                              for i in xrange(61,0,-1):
                                                       sys.stdout.write(str(i)+' ')
                                                       sys.stdout.flush()
                                                       time.sleep(1)
                                              Login.login(ip)
                                              print("OPERATION IS SUCCESFULLL")
                                              #.write("\nOPERATION IS SUCCESFULLL")
                                      else:
                                                print("ERROR!!!!SOMETHING IS WRONG...EXTING FROM THE SCRIPT.\n..PLEASE RUN AGIAN")
                                                #.write("\nERROR!!!!SOMETHING IS WRONG...EXTING FROM THE SCRIPT.\n..PLEASE RUN AGIAN")
                                                #.close()
                                                sys.exit()
                                              
                                except:
                                        print("SOMETHING WRONG...EXITING FROM THE SCRIPT")
                                        #.write("\nSOMETHING WRONG...EXITING FROM THE SCRIPT")
                                        #.close()
                                        sys.exit()
                        
                else:
                        print("SIGN IN RETRIES ARE DISABLED SO ENABLING IT")
                        time.sleep(1)        
                        driver.find_element_by_xpath(".//*[contains(text(), 'Sign-In retries allowed')]").click()
                        time.sleep(1)        
                        driver.find_element_by_xpath(".//*[contains(text(), 'Save')]").click()
                        time.sleep(2)        
                        driver.find_element_by_xpath(".//*[contains(text(), 'OK')]").click()
                        print("\nLOGGING OUT AND RUN AGAIN")
                        driver.find_element_by_xpath(".//*[contains(text(), 'admin')]").click()
                        time.sleep(2)
                        driver.find_element_by_xpath(".//*[contains(text(), 'Log Out')]").click()
                #.close()
                return driver
