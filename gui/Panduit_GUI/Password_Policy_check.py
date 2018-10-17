import Login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import datetime
import os
import getpass
import Config_Upload
import User_Settings
def password_policy_check(ip):                
                driver=User_Settings.user_settings_addition(ip)
                #driver=Login.login(ip)
                #output=File_Creation.file_create()
                print("\n############################PASWWORD POLICY VERIFICATION########################")
                #output.write("\n############################PASWWORD POLICY VERIFICATION########################")
                time.sleep(3)
                driver.find_element_by_xpath(".//*[contains(text(), 'admin')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'User Accounts')]").click()
                time.sleep(5)
                pas=driver.find_element_by_xpath(".//*[contains(text(), 'Password Policy')]").click()
                time.sleep(2)
                a=driver.find_element_by_name("minpwdlen")
                a.clear()
                time.sleep(2)
                print("CHANGING THE MINIMUM PASSWORD LENGTH TO 10")
                #output.write("CHANGING THE MINIMUM PASSWORD LENGTH TO 10")
                time.sleep(2)
                a.send_keys("10")
                time.sleep(2)
                a=driver.find_element_by_name("maxpwdlen")
                a.clear()
                time.sleep(1)
                a.send_keys("25")
                time.sleep(2)
                print("ENABLING ATLEAST ONE LOWER CASE CHARACTER")
                #output.write("ENABLING ATLEAST ONE LOWER CASE CHARACTER")
                a=driver.find_elements_by_tag_name("label")
                time.sleep(1)
                a[4].click()
                print("ENABLING ATLEAST ONE UPPER CASE CHARACTER")
                #output.write("ENABLING ATLEAST ONE UPPER CASE CHARACTER")
                time.sleep(1)
                a[6].click()
                print("ENABLING ATLEAST ONE SPECIAL CHARACTER")
                #output.write("ENABLING ATLEAST ONE SPECIAL CHARACTER")
                time.sleep(1)
                a[10].click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Save')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'OK')]").click()
                time.sleep(1)
                print("VERIFYING THE SETTINGS AGAIN")
                driver.refresh()
                time.sleep(5)
                a=driver.find_elements_by_tag_name("svg")
                time.sleep(2)
                if(str(a[28].get_attribute("aria-label"))=="checkmark"):
                        print("**ENFORCE AT LEAST ONE SPECIAL CHARACTER**IS ENABLED")
                        #output.write("**ENFORCE AT LEAST ONE SPECIAL CHARACTER**IS ENABLED")
                else:
                        print("ERROR!!!**ENFORCE AT LEAST ONE SPECIAL CHARACTER**IS NOT ENABLED")
                        #output.write("ERROR!!!**ENFORCE AT LEAST ONE SPECIAL CHARACTER**IS NOT ENABLED")
                time.sleep(1)        
                if(str(a[27].get_attribute("aria-label"))=="checkmark"):
                        print("**ENFORCE AT LEAST ONE NUMERIC CHARACTER**IS ENABLED")
                        #output.write("**ENFORCE AT LEAST ONE NUMERIC CHARACTER**IS ENABLED")
                else:
                        print("ERROR!!!**ENFORCE AT LEAST ONE NUMERIC CHARACTER**IS NOT ENABLED")
                        #output.write("ERROR!!!**ENFORCE AT LEAST ONE NUMERIC CHARACTER**IS NOT ENABLED")
                time.sleep(2)         
                if(str(a[26].get_attribute("aria-label"))=="checkmark"):
                        print("**ENFORCE AT LEAST ONE UPPER CASE CHARACTER**IS ENABLED")
                        #output.write("**ENFORCE AT LEAST ONE UPPER CASE CHARACTER**IS ENABLED")
                else:
                        print("ERROR!!!**ENFORCE AT LEAST ONE UPPER CASE CHARACTER**IS NOT ENABLED")
                        print(str(a[24].get_attribute("aria-label")))
                        #output.write("ERROR!!!**ENFORCE AT LEAST ONE UPPER CASE CHARACTER**IS NOT ENABLED")
                time.sleep(1)         
                if(str(a[25].get_attribute("aria-label"))=="checkmark"):
                        print("**ENFORCE AT LEAST ONE LOWER CASE CHARACTER**IS ENABLED")
                        #output.write("**ENFORCE AT LEAST ONE LOWER CASE CHARACTER**IS ENABLED")
                else:
                        print("ERROR!!!**ENFORCE AT LEAST ONE LOWER CASE CHARACTER**IS NOT ENABLED")
                        #output.write("ERROR!!!**ENFORCE AT LEAST ONE LOWER CASE CHARACTER**IS NOT ENABLED")
                time.sleep(2)
                user=""
                password=""
                cpassword=""
                def policy_check(count):
                        global user
                        global password,cpassword
                        if(count==0):
                                user="test"
                                password="123456789"
                                cpassword="123456789"
                        elif(count==1):
                                user="test"
                                password="12345678910"
                                cpassword="12345678910"
                        elif(count==2):
                                user="test"
                                password="123456789a"
                                cpassword="123456789a"
                        elif(count==3):
                                user="test"
                                password="123456789A"
                                cpassword="123456789A"
                        elif(count==4):
                                user="test"
                                password="1234!56789"
                                cpassword="1234!56789"
                        elif(count==5):
                                user="test"
                                password="123456789!!"
                                cpassword="123456789!!"
                        elif(count==6):
                                user="test"
                                password="abcdefghijklmnop"
                                cpassword="abcdefghijklmnop"
                        elif(count==7):
                                user="test"
                                password="ABCDEFGHIJKLMNOP"
                                cpassword="ABCDEFGHIJKLMNOP"
                        elif(count==8):
                                user="test"
                                password="abcdEFGHIJklMNOP33"
                                cpassword="abcdEFGHIJklMNOP33"
                        elif(count==9):
                                user="amit"
                                password="abcdEFGHIJkl@@MNOP33"
                                cpassword="abcdEFGHIJkl@@MNOP33"
                       
                        return user,password,cpassword
                driver.find_element_by_xpath(    ".//*[contains(text(), 'Actions')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(    ".//*[contains(text(), 'Add User')]").click()
                num=len(driver.find_elements_by_tag_name("span"))
                for i in range(10):
                        user1,password,cpassword1=policy_check(i)
                        time.sleep(2)
                        un=driver.find_element_by_name("username")
                        un.clear()
                        un.send_keys(user1)
                        time.sleep(1)
                        un=driver.find_element_by_name("password")
                        un.clear()
                        un.send_keys(password)
                        un=driver.find_element_by_name("cpassword")
                        un.clear()
                        un.send_keys(cpassword1)
                        a=driver.find_elements_by_tag_name("label")
                        a[4].click()
                        driver.find_element_by_xpath(".//*[contains(text(),'Add User')]").click()
                        time.sleep(3)
                        if(i==9):
                            driver.find_element_by_xpath(    ".//*[contains(text(), 'OK')]").click()
                        num=len(driver.find_elements_by_tag_name("span"))
                        if(num>85):
                                print("PASSWORD POLICY VERIFIED FOR THE PASSWORD COMBINATION:{}".format(password))
                                #output.write("PASSWORD POLICY VERIFIED FOR THE PASSWORD COMBINATION:{}".format(password))
                        elif(num==71):
                                time.sleep(2)
                                print("USER HAS SUCCESFULLY ADDED..WITH REQUIRED COMBINATION")
                                #output.write("USER HAS SUCCESFULLY ADDED..WITH REQUIRED COMBINATION")
                                driver.find_element_by_xpath(".//*[contains(text(),'OK')]").click()
                        else:
                               print("SOMETHING WENT WORNG....EXITING FROM THE SCRIPT")
                               #output.write("SOMETHING WENT WORNG....EXITING FROM THE SCRIPT")
                               #output.close()
                               sys.exit()
                #output.close()
                return driver
