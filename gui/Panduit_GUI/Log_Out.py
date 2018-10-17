def log_out():
                print("############################LOGOUT FROM THE GUI#############")
                driver.find_element_by_xpath(".//*[contains(text(), 'admin')]").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[contains(text(), 'Log Out')]").click()
                time.sleep(2)
                driver.close()
                return
