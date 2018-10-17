import Login
def iden(ip):
 ############GETTING INFORMATION FROM IDENTIFICATION TAB#####
                #ip=raw_input("Enter the IP address of the PDU")
                Login.login(ip)
                print("############GETTING INFORMATION FROM IDENTIFICATION TAB#####")
                output.write("\n############GETTING INFORMATION FROM IDENTIFICATION TAB#####")
                print("GETTING ALL THE INFORMATION FROM THE IDENTIFICATION TAB")
                output.write("\nGETTING ALL THE INFORMATION FROM THE IDENTIFICATION TAB")
                time.sleep(2)
                home=driver.find_elements_by_tag_name("svg")
                home[0].click()
                dash=driver.find_elements_by_css_selector("a.grommetux-anchor")
                time.sleep(1)
                dash[1].click()
                time.sleep(3)
                iden_info=driver.find_elements_by_tag_name("tr")
                for i in range(0,len(iden_info)):
                    time.sleep(1)
                    print(iden_info[i].text+"\n")
                    output.write(iden_info[i].text+"\n")
                output.close()    
                return
