import Login
def tab_verification(ip):
    #######GETTING THE TAB FROM HOME ICON######
                #ip=raw_input("Enter the IP address of the PDU")
                Login.login(ip)
                print("#######GETTING THE TAB FROM HOME ICON######")
                output.write("\n#######GETTING THE TAB FROM HOME ICON######")
                tab_select=driver.find_elements_by_tag_name("li")
                for i in range(0,3):
                    tab=tab_select[i]
                    name=tab.text
                    print("CLICKING THE "+" "+name+"TAB")
                    output.write("\n\nCLICKING THE "+" "+name+"TAB")
                    tab.click()
                    time.sleep(2)
                tab_select[0].click()
                time.sleep(2)
                ###########TAB FROM THE PDU TAB######
                print("###########TAB FROM THE PDU TAB######")
                output.write("\n\n\n###########TAB FROM THE PDU TAB######")
                tab_select=driver.find_elements_by_tag_name("li")
                for i in range(3,len(tab_select)):
                    tab=tab_select[i]
                    name=tab.text
                    print("CLICKING THE "+" "+name+"TAB")
                    output.write("\n\nCLICKING THE "+" "+name+"TAB")
                    time.sleep(2)
                    tab.click()

                time.sleep(2)
                tab_select=driver.find_elements_by_tag_name("li")
                for i in range(5,len(tab_select)):
                    time.sleep(2)
                    tab=tab_select[i]
                    name=tab.text
                    print("CLICKING THE "+" "+name+" "+"TAB")
                    output.write("\nCLICKING THE "+" "+name+" "+"TAB")
                    tab.click()
                tab_select[0].click()
                home=driver.find_elements_by_tag_name("svg")
                home[0].click()
                dash=driver.find_elements_by_css_selector("a.grommetux-anchor")
                print("GETIING THE MENU NAME FROM HOME ")
                output.write("\nGETIING THE MENU NAME FROM HOME ")
                for i in range(0,3):
                    a=[]
                    time.sleep(1)
                    a=dash[i].get_attribute("href").split("/")
                    output.write(a[4])
                    print(a[4])
                    
                print("checking all the menu items of home")
                output.write("\nchecking all the menu items of home")
                menu=['DASHBOARD','IDENTIFICATION','CONTROL&MANAGE']
                for i in range(0,3):
                    dash=driver.find_elements_by_css_selector("a.grommetux-anchor")
                    print("Checking the tab"+" "+"**"+menu[i]+"**")
                    output.write("\nChecking the tab"+" "+"**"+menu[i]+"**")
                    a=dash[i]
                    a.click()
                    time.sleep(6)
                    home[0].click()
                 output.close()  
                 return    
