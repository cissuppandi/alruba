import Login
def network_settings_change(ip):
    ##########Changing option in the Network settings########
                Login.login(ip)                
                print("##########Changing option in the Network settings########")
                output.write("\n##########Changing option in the Network settings########")
                se=driver.find_elements_by_tag_name("svg")
                se[4].click()
                time.sleep(1)
                part=driver.find_elements_by_tag_name("a")
                time.sleep(1)
                part[1].click()
                return
