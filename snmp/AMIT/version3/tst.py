import time
from pysnmp.hlapi import *
import getpass
username=raw_input("ENTER THE USER NAME")
authkey=getpass.getpass("ENTER THE AUTHENTICATION PASSWORD")
privkey=getpass.getpass("ENTER THE PRIVATE KEY")
ip=raw_input("ENTER THE IP ADDRESS")
def key(count):
    authkey="123456789"
    privkey="123456789"
    if(count==0):
        authkey=authkey
        privkey=privkey          
    elif(count==1):
        authkey=None
        privkey=None
    return authkey,privkey

count_pass=0
for i in range(2):
    authkey,privkey=key(i)
    print("VERYFYING WITH AUTHKEY:{} AND PRIVACY KEY:{}".format(authkey,privkey))
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               UsmUserData(username,authKey=authkey,privKey=privkey,authProtocol=(1, 3, 6, 1, 6, 3, 10, 1, 1, 2),privProtocol=(1, 3, 6, 1, 6, 3, 10, 1, 2, 2)),
               UdpTransportTarget((ip, 161),timeout=30),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.4.1.19536.10.1.5.1.1.18.1.2')))
    )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
            
            count_pass=count_pass+1
if(count_pass==1):
    print("THE TEST CASE IS PASSED")
else:
    print("THE TEST CASE IS FAILED.")
            
