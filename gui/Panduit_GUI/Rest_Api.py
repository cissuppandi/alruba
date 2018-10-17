import Network_Settings               
def rest_api_enable(ip):
                Network_Settings.network_settings_change(ip)
                print("##########ENABLING REST API FEATURE############")
                output.write("\n##########ENABLING REST API FEATURE############")
                print("Enabling WEB/RESTapi Access Configuration")
                output.write("\nEnabling WEB/RESTapi Access Configuration")
                rest=driver.find_elements_by_tag_name("a")
                rest[2].click()
                time.sleep(1)
                en=driver.find_element_by_id("restaccess")
                en.send_keys("Enable")
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Save')]").click()
                time.sleep(1)
                driver.find_element_by_xpath(".//*[contains(text(), 'Do you really want to apply changes now')]"
                ).click()
                time.sleep(1)
                driver.find_element_by_xpath(    ".//*[contains(text(), 'Apply')]").click()
                print("WATING FOR 25 SEC TO RESTART ")           
                for i in xrange(26,0,-1):
                                 sys.stdout.write(str(i)+' ')
                                 sys.stdout.flush()
                                 time.sleep(1)
                print("\n\nLOGGiNG AGAIN TO VERIFY")
                output.write("\n\n\nLOGGING AGAIN TO VERIFY")                           
                Network_Settings.network_settings_change(ip)
                output.close()
                return
def rest_api_check(ip):
                Network_Settings.network_settings_change(ip)                
                en=driver.find_elements_by_tag_name("svg")
                
                if(str(en[13].get_attribute("aria-label"))=="checkmark"):
                          print("SUCCESS!!!"+"\n"+"RESTapi Access is Enabled")
                          output.write("\nSUCCESS!!!"+"\n"+"RESTapi Access is Enabled")
                else:
                    print("ERROR!!!!"+"\n"+"RESTapi Access  is Disabled")
                    output.write("\nERROR!!!!"+"\n"+"RESTapi Access  is Disabled")
                output.close()
                return 
