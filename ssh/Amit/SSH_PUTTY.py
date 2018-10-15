from pywinauto.application import Application
import time
import pywinauto
import getpass
import linecache
import sys
import datetime
def work_week():
         now=datetime.datetime.now()
         date=now.strftime("%Y/%m/%d")
         year,month,date=date.split("/")
         ww=datetime.date(int(date),int(month),int(16)).isocalendar()[1]                  
         return ww
    #work_week()
def putty_auto():    
    try:        
        num_lines = 0
        ip=raw_input("ENTER THE IP ADDRESS")
        port=raw_input("ENTER THE PORT TO CONNECT")     
        pwa_app = Application ().start (cmd_line=u'PuTTY')
        time.sleep(2)
        w_handle = pywinauto.findwindows.find_windows(title=u'PuTTY Configuration', class_name='PuTTYConfigBox')[0]
        window = pwa_app.window(handle=w_handle)
        ctrl = window['TreeView']  
        ctrl.get_item([u'Session']).click() 
        ctrl.get_item([u'Session', u'Logging']).click()  
        time.sleep(2)
        dlg=pwa_app['PuTTy Configuration']
        time.sleep(2)
        dlg[u'&Printable outputRadioButton'].click()
        time.sleep(2)
        dlg[u'Always overwrite itRadioButto'].click()
        time.sleep(1)
        dlg[u'Log &file name:Edit'].click()
        time.sleep(2)
        dlg[u'Log &file name:Edit'].set_text(u'')
        time.sleep(1)
        dlg[u'Log &file name:Edit'].set_text("C:/Users/"+str(getpass.getuser())+"/Downloads/putty.txt")
        time.sleep(1)
        ctrl.get_item([u'Window']).click()
        time.sleep(1)
        ctrl.get_item([u'Window',u'Behaviour']).click()
        time.sleep(1)
        dlg[u'System menu appears on A&LT aloneCheckBox'].click()
        time.sleep(1)
        dlg[u'&Ensure window is always on topCheckBox'].click()
        ctrl.get_item([u'Session']).click()
        time.sleep(1)
        dlg[u'Host &Name (or IP address)Edit'].click()
        time.sleep(1)
        dlg[u'Host &Name (or IP address)Edit'].set_text(ip)
        time.sleep(1)
        dlg[u'&PortEdit'].click()
        time.sleep(1)
        dlg[u'&PortEdit'].set_text(u'')
        time.sleep(1)
        dlg[u'&PortEdit'].set_text(port)
        time.sleep(1)
        dlg[u'&OpenButton'].click()
        time.sleep(1)
        dlg=pwa_app['PuTTy']
        time.sleep(4)
        #dlg.type_keys("{ENTER}")
        dlg.wait('ready')

        dlg.type_keys("admin")
        time.sleep(2)
        dlg.type_keys("{ENTER}")
        time.sleep(2)
        dlg.type_keys("1234567!")
        time.sleep(2)
        dlg.type_keys("{ENTER}")
        time.sleep(2)
        with open("SSH_TEST_CASE.txt", 'r') as f:
            for line in f:
                num_lines += 1
        print("THE NUMBER OF COMMAND FOUND:{}".format(num_lines))
        for i in range(num_lines+1):
            try:
                time.sleep(2)    
                a=list(linecache.getline("SSH_TEST_CASE.txt",i))
                print("SENDING THE COMMAND:{}".format(linecache.getline("SSH_TEST_CASE.txt",i)))
                for i  in a:
                    time.sleep(1)
                    if(i=="-"):
                        dlg.type_keys("{SPACE}")            
                    elif(i=="\n"):
                        dlg.type_keys("{ENTER}")
                    else:
                        dlg.type_keys(i.lower())
                if(len(a)==2):
                    print("PLEASE WAIT WHEN THE PDU REBOOT..IT MAY TAKE 20 SEC")            
                    for i in xrange(20,0,-1):
                        sys.stdout.write(str(i)+' ')
                        sys.stdout.flush()
                        time.sleep(1)
                    print("REFRESHING THE PUTTY SESSION TO CONTINUE")    
                    dlg.type_keys("{ENTER}")
                    time.sleep(2)
                    dlg=pwa_app['PuTTy Fatal Error']
                    #time.sleep(2)
                    #dlg[u'OKButton'].click()
                    time.sleep(2)
                    dlg[u'OK'].click()
                    time.sleep(2)
                    dlg=pwa_app['PuTTy']
                    time.sleep(1)
                    dlg.type_keys("%")
                    time.sleep(1)
                    dlg.type_keys("r")
                    time.sleep(5)
                    dlg.wait('ready')
                    dlg.type_keys("admin")
                    time.sleep(2)
                    dlg.type_keys("{ENTER}")
                    time.sleep(2)
                    dlg.type_keys("1234567!")
                    time.sleep(2)
                    dlg.type_keys("{ENTER}")

                    time.sleep(2)
            except:
                    print("SEEMS THE PDU GOT DISCONNECTED\n..WATING FOR 10 SECOND")
                    time.sleep(10)
                    dlg=pwa_app['PuTTy Fatal Error']
                    #time.sleep(2)
                    #dlg[u'OKButton'].click()
                    time.sleep(2)
                    dlg[u'OK'].click()
                    time.sleep(2)
                    dlg=pwa_app['PuTTy']
                    time.sleep(1)
                    dlg.type_keys("%")
                    time.sleep(1)
                    dlg.type_keys("r")
                    time.sleep(5)
                    dlg.wait('ready')
                    dlg.type_keys("admin")
                    time.sleep(2)
                    dlg.type_keys("{ENTER}")
                    time.sleep(2)
                    dlg.type_keys("1234567!")
                    time.sleep(2)
                    dlg.type_keys("{ENTER}")
        time.sleep(2)      
        dlg.type_keys("exit")
        time.sleep(1)
        dlg.type_keys("{ENTER}")        
    except Exception as e:
                    now=datetime.datetime.now()
                    print("THE SCRIPT UNABLE TO CONTINUE FOR SOME ERROR.\n**SCRIPT_ERROR FILE HAS BEEN GENERATED")                                    
                    error=open("SCRIPT_ERROR.txt",'a')
                    error.write(now.strftime("\nDATE AND TIME:"+" "+"%H:%M:%S---%d/%b/%Y"))
                    error.write("\nTHE SCRIPTS FAILED TO EXCUTE FOR THE FOLLOWING ERROR")
                    print(e)
                    error.write("\n"+str(e))
                    error.close()                
                    sys.exit() 
        
    return None 
