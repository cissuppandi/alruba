import Login
def outlet_verify(ip):
                #ip=raw_input("Enter the IP address of the PDU")
                Login.login(ip)
         #####################VERIFYING OUTLET FUNCTIONALITY##########
                print("#####################VERIFYING OUTLET FUNCTIONALITY##########")
                out1=driver.find_elements_by_tag_name("svg")
                output.write("\n#####################VERIFYING OUTLET FUNCTIONALITY##########")
                print("VERIFYING OUTLET ONE BY TURNING IT OFF")
                time.sleep(2)
                out1[11].click()
                off=driver.find_elements_by_tag_name("a")
                time.sleep(2)
                off[1].click()
                yes=driver.find_elements_by_tag_name("button")
                time.sleep(2)
                yes[1].click()
                output.close()
                return
