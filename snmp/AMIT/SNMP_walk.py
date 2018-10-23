from pysnmp.hlapi import *
import time
def snmp_walk(ip,port):
    i=0
    ques=raw_input("DO YOU WANT TO START WITH THE DEFAULT OID VALUE,WRITE Y/N")
    if(ques.lower()=='y'):
        OID='1.3.6.1.2.1.1.1.0'
        start_time=time.time()
    else:    
        OID=raw_input("ENTER THE OID TO START")
        start_time=time.time()
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),CommunityData('public'),
                              UdpTransportTarget((ip,port)),
                              ContextData(),
                              ObjectType(ObjectIdentity(OID))):

        i=i+1
        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            break
        else:
            for varBind in varBinds:
                              
                print(' = '.join([x.prettyPrint() for x in varBind]))
        
    print("TIME TAKEN  FOR THE FETCHING"+" "+str(i)+" "+"NUMBERS OF"+" "+"OID IS"+" " +str(time.time()-start_time)+" "+"sec")         
               

