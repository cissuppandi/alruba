import Login
import Identification_Dump
def upload_firmware(ip):
                Login.login(ip)
    ###########################UPLOAD FIRMWARE####################################
                print("###########################UPLOAD FIRMWARE####################################")
                output.write("\n###########################UPLOAD FIRMWARE####################################")
                print("PLEASE KEEP THE PANDUIT FIRMWARE IN THE SAME DIRECTORY")
                se=driver.find_elements_by_tag_name("svg")
                se[4].click()
                part=driver.find_elements_by_tag_name("a")
                part[2].click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Action')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Upload Firmware')]").click()
                time.sleep(2)
                fw=driver.find_element_by_name("file")
                time.sleep(2)
                fw.send_keys(os.getcwd()+"/Panduit.FW")
                time.sleep(1)
                up=driver.find_elements_by_tag_name("button")
                time.sleep(1)
                up[1].click()
                print("PLEASE WAIT WHILE THE FIRMWARE FLASH AND REBOOT THE PDU.IT MAY TAKE 4-5 MINS.\n.PLEASE WAIT....")
                for i in xrange(300,0,-1):
                        sys.stdout.write(str(i)+' ')
                        sys.stdout.flush()
                        #print("\n"*50)        
                        time.sleep(1)
                        
                driver.get(ip)
                time.sleep(1)
                Identification_Dump.iden(ip)
                driver.find_element_by_xpath(".//*[contains(text(), 'admin')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Log Out')]").click()
                return
