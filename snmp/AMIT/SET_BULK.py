import pandas as pd
from pysnmp.hlapi import *
import time
import Report
def snmp_set_bulk(ip,port):
        pas=0
        fail=0
        count=0
        test=pd.read_csv("SNMP_SET.csv",header=0,index_col=False)
        week=raw_input("ENTER THE WORK WEEK")  
        for j in range(0,test.shape[0]):
                 new_value=test.iloc[j,2]
                 new_oid=test.iloc[j,0]
                 test.iloc[4,8]=j
                 
                 print("SETTING THE VALUE FOR OID :",new_oid)
                 time.sleep(2)
                 g = setCmd(SnmpEngine(),
                            CommunityData('private'),
                            UdpTransportTarget((ip,port),timeout=2, retries=2),
                            ContextData(),
                            ObjectType(ObjectIdentity(new_oid),new_value))
                 next(g)
                 print("PLEASE WAIT TO WRITE IT TO CSV")
                 time.sleep(2)
                
                 iterator = getCmd(SnmpEngine(),
                                      CommunityData('public'),
                                      UdpTransportTarget((ip,port),timeout=1,retries=2),
                                      ContextData(),
                                      ObjectType(ObjectIdentity(new_oid)))

                 errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

                 if errorIndication:  # SNMP engine errors
                        print(errorIndication)
                        
                 else:
                        if errorStatus:  # SNMP agent errors
                            test.iloc[j,3]="DEVICE NOT AVAILABLE"
                            count=count+1
                            test.iloc[4,11]=count 
                            print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
                        else:
                            for varBind in varBinds:  # SNMP response contents
                                #print(' = '.join([x.prettyPrint() for x in varBind]))
                                test.iloc[j,3]=' = '.join([x.prettyPrint() for x in varBind])
                                c=test.iloc[j,3].split('=')                
                                test.iloc[j,3]=c[1].strip()
                                if(unicode(test.iloc[j,2])==test.iloc[j,3]):
                                    test.iloc[j,4]="PASS"
                                    pas=pas+1
                                    test.iloc[4,9]=pas
                                    
                                else:
                                   fail=fail+1
                                   test.iloc[4,10]=fail
                                   test.iloc[j,4]="FAIL"
        print("THE CSV FILE NAME *OID_Set_Test* has created in the same directory")
        test = test.rename(columns={'Unnamed: 5': '', 'Unnamed: 6': '','Unnamed: 7': '','Unnamed: 8': '','Unnamed: 9': '','Unnamed: 10': '','Unnamed: 11': ''})
        test.loc[j+1]=""
        test.iloc[j+1,0]="RESULT OF THE"+" "+week
        test.to_csv("Result_SNMP_SET.csv",index=False,mode='a')
        print("PLEASE WAIT TO GENERATE THE GRAPH")
        
        Report.report("SET","PASS","FAIL",pas,fail)
        time.sleep(1)
        print("GRAPH HAS BEEN GENERATED, FOR DOWNLOAD PLEASE OPEN THE LINK IN CHROME")
        return 0    


