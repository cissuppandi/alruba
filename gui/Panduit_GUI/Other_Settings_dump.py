import Login
def verify_other_settings(ip):
                Login.login(ip)
                print("########VERIFYING THE OTHER SETTINGS############")
                output.write("\n########VERIFYING THE OTHER SETTINGS############")
                se=driver.find_elements_by_tag_name("svg")
                se[4].click()

                for i in range(1,9):
                    part=driver.find_elements_by_tag_name("a")
                    print("CLICKING ON THE"+" "+str(part[i].text))
                    output.write("\nCLICKING ON THE"+" "+str(part[i].text))
                    time.sleep(5)
                    part[i].click()
                    time.sleep(1)
                    se[4].click()
                    
                time.sleep(1)
                part=driver.find_elements_by_tag_name("a")
                part[1].click()
                time.sleep(2)
                en=driver.find_elements_by_tag_name("svg")
                if(str(en[10].get_attribute("aria-label"))=="checkmark"):
                    print("IPv6 Access is Enabled")
                    output.write("\nIPv6 Access is Enabled")
                else:
                    print("IPv6 Access is Disabled")
                    output.write("\nIPv6 Access is Disabled")
                if(str(en[11].get_attribute("aria-label"))=="checkmark"):
                          print("IPv6 DHCP is Enabled")
                          output.write("\nIPv6 DHCP is Enabled")
                else:
                    print("IPv6 DHCP is Disabled")
                    output.write("\nIPv6 DHCP is Disabled")
                if(str(en[13].get_attribute("aria-label"))=="checkmark"):
                          print("RESTapi Access is Enabled")
                          output.write("\nRESTapi Access is Enabled")
                else:
                    print("RESTapi Access  is Disabled")
                    output.write("\nRESTapi Access  is Disabled")
                if(str(en[15].get_attribute("aria-label"))=="checkmark"):
                          print("SSH Access is Enabled")
                          output.write("\nSSH Access is Enabled")
                else:
                    print("SSH Access is Disabled")
                    output.write("\nSSH Access is Disabled")
                if(str(en[16].get_attribute("aria-label"))=="checkmark"):
                          print("FTPs Access is Enabled")
                          output.write("\nFTPs Access is Enabled")
                else:
                    print("FTPs Access is Disabled")
                    output.write("\nFTPs Access is Disabled")
                if(str(en[18].get_attribute("aria-label"))=="checkmark"):
                          print("Network Time Protocol(NTP) is Enabled")
                          output.write("\nNetwork Time Protocol(NTP) is Enabled")
                else:
                    print("Network Time Protocol(NTP) is Disabled")
                    output.write("\nNetwork Time Protocol(NTP) is Disabled")
                if(str(en[21].get_attribute("aria-label"))=="checkmark"):
                          print("Daylight Saving is Enabled")
                          output.write("\nDaylight Saving is Enabled")
                else:
                    print("Daylight Saving is Disabled")
                    output.write("\nDaylight Saving is Disabled")
                output.close()    
                return
