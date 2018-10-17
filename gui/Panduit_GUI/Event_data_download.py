import Login
def event_data_download(ip):
    ######VERIFY THE DATA LOG AND EVENT LOG DOWNLOAD####
                Login.login(ip)
                print("######VERIFY THE DATA LOG AND EVENT LOG DOWNLOAD####")
                output.write("######VERIFY THE DATA LOG AND EVENT LOG DOWNLOAD####")
                time.sleep(3)
                os_user=getpass.getuser()
                print("CHECKING THE DOWNLOAD FOLDER FOR THE EVENT LOG")
                time.sleep(1)
                
                if(os.path.isfile("C:\Users/" + str(os_user)+"/Downloads/logs.csv")==True):
                        print("THE EVENT FILE HAS DOWNLOADED SUCCESFULLY")
                        output.write("THE EVENT FILE HAS DOWNLOADED SUCCESFULLY")
                else:
                        print("ERROE!!THE EVENT DOWNLOAD WAS UNSUCCESSFULL")
                        output.write("ERROE!!THE EVENT DOWNLOAD WAS UNSUCCESSFULL")
                time.sleep(1)
                if(os.path.isfile("C:\Users/" + str(os_user)+"/Downloads/logs.csv")==True):
                        print("THE DATALOG FILE HAS DOWNLOADED SUCCESFULLY")
                        output.write("THE DATALOG FILE HAS DOWNLOADED SUCCESFULLY")
                else:
                        print("ERROE!!THE DATALOG DOWNLOAD WAS UNSUCCESSFULL")
                        output.write("ERROE!!THE DATALOG DOWNLOAD WAS UNSUCCESSFULL")
                output.close()
                return
