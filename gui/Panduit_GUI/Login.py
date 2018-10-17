import File_Creation
ip=raw_input("Enter the IP address of the PDU")
def login(ip):
    #########OPENING WEBROWSER WITH WEBDRIVER#######
                print("#########OPENING WEBROWSER WITH WEBDRIVER#######")        
                driver = webdriver.Chrome()
                driver.get(ip)
                time.sleep(1)
                ##############LOGIN THROUGH WEBDRIVER##########
                print("##############LOGIN THROUGH WEBDRIVER##########")
                username=driver.find_element_by_name("username")
                #WebDriverWait(driver, timeout).until(username)
                time.sleep(1)
                username.send_keys("admin")
                time.sleep(1)
                password=driver.find_element_by_name("password")
                #WebDriverWait(driver, timeout).until(password)
                time.sleep(1)
                password.send_keys("1234567!")
                time.sleep(1)
                submit=driver.find_element_by_xpath('//button')
                submit.click()
                time.sleep(2)
                try:
                        if(driver.find_element_by_tag_name("p").text=="User is already logged in. Do you really want to continue?"):
                                driver.find_element_by_xpath(".//*[contains(text(), 'OK')]").click()
                                time.sleep(2)
                except:
                        print("LOGGED IN SUCCESFULLY")
                        time.sleep(4)
                return 
