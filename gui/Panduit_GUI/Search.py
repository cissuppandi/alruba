import Login
#############CHECKING SEARCH FUNCTIONALITY#################
def search(ip):
                #ip=raw_input("Enter the IP address of the PDU")
                Login.login(ip)
                print("#############CHECKING SEARCH FUNCTIONALITY#################")
                output.write("\n#############CHECKING SEARCH FUNCTIONALITY#################")
                srch=driver.find_element_by_id("search_app")
                srch.click()
                time.sleep(3)
                srch.send_keys("SNMP")
                srch.send_keys(Keys.ENTER)
                check=driver.find_elements_by_tag_name("header")
                b=check[1]
                if((b.text).strip()=="SNMP Management"):
                    print("SEARCH OPERATION COMPLETED SUCCESSFULLY")
                    output.write("\nSEARCH OPERATION COMPLETED SUCCESSFULLY")
                else:
                    print("SOMETHING IS WRONG",b.text)
                    output.write("\nSOMETHING IS WRONG")
                srch.clear()
                time.sleep(3)
                print("SENDING A JUNK STRING")
                output.write("\nSENDING A JUNK STRING")
                srch.send_keys(name)
                check=driver.find_elements_by_tag_name("header")
                b=check[1]
                print(b.text)
                if((b.text).strip()=="SNMP Management"):
                    print("SEARCH OPERATION COMPLETED SUCCESSFULLY,NO CHANGE IN RESULT")
                    output.write("\nSEARCH OPERATION COMPLETED SUCCESSFULLY,NO CHANGE IN RESULT")
                else:
                    print("SOMETHING IS WRONG",b.text)
                    output.write("\nSOMETHING IS WRONG")
                output.close()
                return 
