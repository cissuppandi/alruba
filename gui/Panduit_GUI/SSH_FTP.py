import Network_Settings
def SSH_FTP_enable(ip):
                Network_Settings.network_settings_change(ip)
                print("##########CHANGING THE SSH/FTP##########")
                output.write("\n##########CHANGING THE SSH/FTP##########")
                print("ENABLING SSH/FTP Access Configuration")
                output.write("\nENABLING SSH/FTP Access Configuration")
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
                output.write("\nWATING FOR 25 SEC TO RESTART ")
                for i in xrange(26,0,-1):
                                 sys.stdout.write(str(i)+' ')
                                 sys.stdout.flush()
                                 time.sleep(1)               
                Network_Settings.network_settings_change(ip)
                output.close()
                return
def SSH_FTP_check(ip):
                Network_Settings.network_settings_change(ip)
                en=driver.find_elements_by_tag_name("svg")
                if(str(en[15].get_attribute("aria-label"))=="checkmark"):
                          print("SUCCESS!!!"+"\n"+"SSH is Enabled")
                          output.write("\nSUCCESS!!!"+"\n"+"SSH is Enabled")
                else:
                    print("ERROR!!!!"+"\n"+"SSH  is Disabled")
                if(str(en[16].get_attribute("aria-label"))=="checkmark"):
                          print("SUCCESS!!!"+"\n"+"FTP is Enabled")
                          output.write("\nSUCCESS!!!"+"\n"+"FTP is Enabled")
                else:
                    print("ERROR!!!!"+"\n"+"FTP  is Disabled")
                    output.write("\nERROR!!!!"+"\n"+"FTP  is Disabled")
                output.close()
                return
