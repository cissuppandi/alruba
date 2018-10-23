import os
import time
#os.chdir("C:/Python27/PYTHON_SNMP")
import SNMP_GET
import sys
import set_snmp
import SNMP_walk
import SET_BULK
import Report

ip=raw_input("ENTER THE IP ADDRESS TO CONNECT")
port=raw_input("ENTER THE PORT")

def welcome_verify(ip):

    
    print("VERIFYING THE IP ADDRESS TO CONNECT",ip)
    time.sleep(2)
    check= os.system("ping"+" " + ip +" "+"-n 2")
    print(check)
    if(check==0):
        
        print("IP IS GOOD TO GO")
        print("\n  ")
        print("ENTER THE CHOISE FROM THE BELOW TO PROCEED FURTHER")
        print("         1.SNMP GET FUNCTIONALITY FOR ONE VARIABLE")
        print("         2.SNMP SET FUNCTIONALITY FOR ONE VARIABLE")
        print("         3.SNMP GET FROM THE CSV FILE")
        print("         4.SNMP SET FROM A CSV FILE")
        print("         5.SNMP WALK FUNCTIONALITY")
        sel_one=input("")
        if(sel_one==1):
            
            SNMP_GET.SNMP(ip,port)
            
        elif(sel_one==2):
             print("YOU ARE ABOUT TO SET A VALUE")
             time.sleep(2)
             new_oid=raw_input("THE OID IS NEED TO BE SET")
             new_value=raw_input("PROVIDE THE VALUE TO SET")
             set_snmp.set_cmd(ip,port,new_oid,new_value)
             time.sleep(2)
             set_snmp.set_check(ip,port,new_oid)
             
             
        elif(sel_one==3):
             print("YOU ARE ABOUT GET THE VALUE FROM SNMP SERVER.PLEASE CHGECK THE CSV FILE CREATED FOR FINAL RESULT")
             time.sleep(2)
             SNMP_GET.save_to_csv(ip,port)
             
             
             
        elif(sel_one==4):
             print("THE VALUE IS GETTING SET FROM CSV FILE")
             time.sleep(2)
             SET_BULK.snmp_set_bulk(ip,port)
        elif(sel_one==5):
             print("PERFORMING SNMP WALK FUNCTIONALITY")
             time.sleep(2)
             SNMP_walk.snmp_walk(ip,port)    
        else:
            print("WRONG CHOISE.EXITING FROMT THE SCRIPT")
            time.sleep(2)
            sys.exit()
             
    else:
        print("PLEASE VERIFY THE IP AGAIN.NOT ABLE TO CONNECT")
    return 0
    


welcome_verify(ip)

