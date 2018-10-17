import Login
def event_dump(ip):
    ####################EVENT LOG AND DATA LOG#################
                #ip=raw_input("Enter the IP address of the PDU")
                Login.login(ip)                
                print("####################EVENT LOG AND DATA LOG#################")
                output.write("\n####################EVENT LOG AND DATA LOG#################")
                data_event=driver.find_elements_by_tag_name("svg")
                data_event[3].click()
                time.sleep(1)
                data=driver.find_elements_by_tag_name("a")
                for i in range(1,3):
                    data=driver.find_elements_by_tag_name("a")
                    print("CLICKING ON THE"+" "+data[i].text)
                    output.write("\nCLICKING ON THE"+" "+data[i].text)
                    time.sleep(5)
                    data[i].click()    
                    data_event[3].click()
                time.sleep(20)
                data_event=driver.find_elements_by_tag_name("svg")
                data_event[3].click()
                data=driver.find_elements_by_tag_name("a")
                print("CLICKING ON THE"+" "+data[4].text)
                output.write("\nCLICKING ON THE"+" "+data[4].text)
                data[4].click()
                time.sleep(3)
                output.close()
                return
