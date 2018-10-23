import pandas as pd
import time
import Report
from pysnmp.hlapi import *
import time
#a=[]
def SNMP(ip,port):
        
        OID=raw_input("ENTER THE OID TO VERIFY")
        time.sleep(2)
        print("GETIING THE VALUE FROM SNMP SERVER")
        iterator = getCmd(SnmpEngine(),
                          CommunityData('public'),
                          UdpTransportTarget((ip,port),timeout=1,retries=2),
                          ContextData(),
                          ObjectType(ObjectIdentity(OID)))
        start_time=time.time()
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:  # SNMP engine errors
            print(errorIndication)
           
        else:
            if errorStatus:  # SNMP agent errors
                print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
            else:
                for varBind in varBinds:  # SNMP response contents
                     print(' = '.join([x.prettyPrint() for x in varBind]))
        print("TIME TAKEN  FOR THE FETCHING"+str(time.time()-start_time)+" "+"ms")         
        return 0


def save_to_csv(ip,port):
    week=raw_input("ENTER THE WORK WEEK")    
    count_pass=0
    count_fail=0
    count_not_able=0
    test=pd.read_csv("SNMP_GET.csv",header=0,index_col=False)
    test.iloc[7,11]=count_not_able
    for j in range(0,test.shape[0]):
        #time.sleep(2)
        OID=test.iloc[j,0]
        test.iloc[7,8]=j+1
        print(OID)
        start_time=time.time()
        iterator = getCmd(SnmpEngine(),
                          CommunityData('public'),
                          UdpTransportTarget((ip,port),timeout=1,retries=2),
                          ContextData(),
                          ObjectType(ObjectIdentity(OID)))

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        
        if errorIndication:  # SNMP engine errors
            print(errorIndication)
            #print(OID)
        else:
            if errorStatus:  # SNMP agent errors
                test.iloc[j,1]="DEVICE NOT AVAILABLE"
                count_not_able=count_not_able+1
                test.iloc[7,11]=count_not_able
                #print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
            else:
                for varBind in varBinds:  # SNMP response contents
                    #print(' = '.join([x.prettyPrint() for x in varBind]))
                    print("TIME TAKEN  FOR THE FETCHING"+str(time.time()-start_time)+"ms") 
                    test.iloc[7,9]=count_pass
                    test.iloc[j,2]=' = '.join([x.prettyPrint() for x in varBind])
                    c=test.iloc[j,2].split('=')
                    print(c)
                    #test.iloc[j,0]=test.iloc[j,3]
                    test.iloc[j,2]=c[1].strip()
                    c.append(test.iloc[j,1])
                    test.iloc[j,1]=c[2].strip()
                    
                    
                    if(test.iloc[j,1]==test.iloc[j,2]):
                                    test.iloc[j,3]="PASS"
                                    count_pass=count_pass+1
                                    test.iloc[7,9]=count_pass
                                    
                    else:
                                   count_fail=count_fail+1
                                   test.iloc[7,10]=count_fail
                                   test.iloc[j,3]="FAIL"
                    print("Count =",j)
                    
    
    test = test.rename(columns={'Unnamed: 2': '','Unnamed: 3': '','Unnamed: 4': '','Unnamed: 5': '', 'Unnamed: 6': '','Unnamed: 7': '','Unnamed: 8': '','Unnamed: 9': '','Unnamed: 10': '','Unnamed: 11': ''})
    test.loc[j+1]=""
    test.iloc[j+1,0]="RESULT OF THE"+" "+week
    test.to_csv("Result_SNMP_GET.csv",mode='a',index=False)
    print("PLEASE WAIT TO GENERATE THE GRAPH")
    
    Report.report("GET","PASS","FAIL","NOT-PRESENT",count_pass,count_fail,count_not_able)
    time.sleep(1)
    print("GRAPH HAS BEEN GENERATED, FOR DOWNLOAD PLEASE OPEN THE LINK IN CHROME")
    
    return 0
