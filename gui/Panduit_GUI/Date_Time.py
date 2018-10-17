import Network_Settings

def date_time(ip):
                Network_Settings.network_settings_change(ip)
                print("##############SETTINGS DATE AND TIME################")
                output.write("\n##############SETTINGS DATE AND TIME################")
                time.sleep(2)
                part=driver.find_elements_by_tag_name("a")
                part[5].click()
                time.sleep(3)
                print("CHANGING THE DATE")
                date_time=driver.find_element_by_id("date")
                time.sleep(2)
                date_time.clear()
                now=datetime.datetime.now()
                cdt=now.strftime("%Y/%m/%d")
                time.sleep(4)
                date_time.send_keys(cdt)
                time.sleep(1)
                date_time.send_keys(cdt)
                time.sleep(1)
                for i in range(10):
                        date_time.send_keys(Keys.ARROW_LEFT)
                time.sleep(1)    
                for i in range(18):
                   date_time.send_keys(Keys.BACKSPACE)
                print("CHANGING THE TIME")
                date_time=driver.find_element_by_id("time")
                time.sleep(2)
                date_time.clear()
                now=datetime.datetime.now()
                cdt=now.strftime("%H:%M:%S")
                date_time.send_keys(cdt)
                time.sleep(1)
                date_time.send_keys(cdt)
                for i in range(8):
                        date_time.send_keys(Keys.ARROW_LEFT)
                time.sleep(1)    
                for i in range(12):
                        date_time.send_keys(Keys.BACKSPACE)
                time.sleep(3)        
                driver.find_element_by_xpath(".//*[contains(text(), 'Save')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Do you really want to apply changes now')]"
                ).click()
                time.sleep(2)
                driver.find_element_by_xpath(    ".//*[contains(text(), 'Apply')]").click()
                print("WATING FOR 25 SEC TO RESTART ")           
                for i in xrange(26,0,-1):
                                 sys.stdout.write(str(i)+' ')
                                 sys.stdout.flush()
                                 time.sleep(1)
                ouyput.close()
                return
def date_time_verify(ip):
                print("\nLOGGING AGAIN TO VERIFY")
                Network_Settings.network_settings_change(ip)
                now=datetime.datetime.now()
                cdt=now.strftime("%Y/%m/%d")               
                print("VERIFYING THE DATE AND TIME")
                time.sleep(2)
                dt=driver.find_elements_by_tag_name("td")
                if(str(dt[41]==now.strftime("%Y/%m/%d"))):
                    print("DATE HAS BEEN CHANGED SUCCESFULLY")
                    output.write("\nDATE HAS BEEN CHANGED SUCCESFULLY")
                else:
                   print("ERROR!!!!DATE IS NOT CHANGED")
                   output.write("\nERROR!!!!DATE IS NOT CHANGED")
                time_test=str(dt[43].text).split(":")
                if(int(time_test[1])-int(now.strftime("%M"))==1):
                   print("TIME HAS SUCCESFULLY CHANGED")
                   output.write("\nTIME HAS SUCCESFULLY CHANGED")
                else:
                   print("ERROR!!!!TIME IS NOT CHANGED")
                   output.write("\nERROR!!!!TIME IS NOT CHANGED")
                output.close()
                return
