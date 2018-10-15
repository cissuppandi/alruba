import linecache
num_lines=0
import pandas as pd
import Report
import shutil
import getpass
import os
import sys
import datetime
import SSH_PUTTY
def putty_check():
    try:
        src="C:/Users/"+str(getpass.getuser())+"/Downloads/putty.txt"
        dst=str(os.getcwd())+"\putty.txt"
        shutil.copy2(src,dst)
        print("FILE HAS COPIED SUCCESFULLY")
        try:
            num_lines=0
            with open("putty.txt", 'r') as f:
                for line in f:               
                    num_lines += 1
            print("THE NUMBER OF LINES FOUND:{}".format(num_lines))
            cmd=pd.read_csv("SSH_TEST.csv",header=0,index_col=False)
            for i in range(0,num_lines):
                a=linecache.getline("putty.txt",i)
                b=a.split(":")
                print(b[0].replace(" ", ""))   
                if(b[0].replace(" ", "")=="FirmwareVersion"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[0,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="BootloaderVersion"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[1,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="LANGUAGEVersion"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[2,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="WebVersion"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[3,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="IPv4Addr"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[4,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="IPv6Addr(1)"):
                    print(b[1].strip("\n)"))
                    temp=""
                    a=linecache.getline("putty.txt",i)
                    b=a.split(":")
                    for i in range(7):            
                        temp=temp+b[i]
                    temp=temp.split(" ")
                    temp=temp[2].strip("\n")        
                    cmd.iloc[5,2]=temp
                elif(b[0].replace(" ", "")=="MACAddr"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[6,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="SKU"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[7,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="SERIAL"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[8,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="FuncType"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[9,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="Rating"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[10,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="Mac"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[11,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="Tcpip"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[12,2]=b[1].strip("\n)")   
                elif(b[0].replace(" ", "")=="SSHPort"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[13,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="FTPSPort"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[14,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="HTTPPort"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[15,2]=b[1].strip("\n)")
                elif(b[0].replace(" ", "")=="HTTPSPort"):
                    print(b[1].strip("\n)"))
                    cmd.iloc[16,2]=b[1].strip("\n)")
                elif(a=="TFTP function is on\n"):
                    #print(b[1].strip("\n)"))
                    cmd.iloc[17,2]="ON"
                elif(a=="PANDUIT>net redfish\n"):
                    a=linecache.getline("putty.txt",i+2)
                    a=a.strip("\n")
                    b=a.split(":")
                    if(b[1].strip(" ")=="ON"):
                        cmd.iloc[18,2]="ON"
                    else:
                        cmd.iloc[18,2]="OFF"
                else:
                    continue
                    #print("NOT ABLE TO LOCATE THE VALUE")
            count_pass=0
            for i in range(0,cmd.shape[0]):
                if(cmd.iloc[i,1]==cmd.iloc[i,2].lstrip(" ")):
                    cmd.iloc[i,3]="PASS"
                    count_pass=count_pass+1
                else:
                    cmd.iloc[i,3]="FAIL"
                    
                    
            cmd.iloc[5,9]=i+1
            cmd.iloc[5,10]=count_pass
            cmd.iloc[5,11]=i+1-count_pass
            cmd.loc[i+1]=""
            week=SSH_PUTTY.work_week()
            cmd.iloc[i+1,0]="RESULT OF THE"+" "+str(week)
            cmd = cmd.rename(columns={'Unnamed: 2': '','Unnamed: 3': '','Unnamed: 4': '','Unnamed: 5': '', 'Unnamed: 6': '','Unnamed: 7': '','Unnamed: 8': '','Unnamed: 9': '','Unnamed: 10': '','Unnamed: 11': ''})        
            cmd.to_csv("SSH_TEST_FINAL.csv",mode='a',index=False)       
            print("GENERATIONG HTML REPORT...PLEASE WAIT\nFOR DOWNLOAD THE IMAGE COPY THE URL IN THE CHROME")
            Report.report("SSH","PASS","FAIL",count_pass,int(cmd.iloc[5,11]))
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
        
SSH_PUTTY.putty_auto()
putty_check()
