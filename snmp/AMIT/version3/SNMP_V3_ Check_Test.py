import time
from pysnmp.hlapi import *
import getpass
 #print(authkey,privkey)
# print("VERYFYING WITH AUTHKEY:{} AND PRIVACY KEY:{}".format(authkey,privkey))
errorIndication, errorStatus, errorIndex, varBinds = next(
           getCmd(SnmpEngine(),
                   UsmUserData('amit',authKey='123456789',privKey='123456789',authProtocol=(1, 3, 6, 1, 6, 3, 10, 1, 1, 2),privProtocol=(1, 3, 6, 1, 6, 3, 10, 1, 2, 2)),
                   UdpTransportTarget(('10.20.90.232', 161),timeout=30),
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
                
                
