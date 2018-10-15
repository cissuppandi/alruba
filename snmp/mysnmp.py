import socket
import getpass
import sys
import telnetlib
import time
import datetime
import socket
import threading
import os
import datetime
from pyasn1.type import univ
from pyasn1.codec.ber import encoder, decoder
from pysnmp.entity.rfc3413.oneliner import cmdgen
import mydefines
from mydefines import define

HOST = "10.20.90.237"
defReadString = "public"
defWriteString = "private"

class snmpClient:
    ipAddr = 0
    readString = 0
    writeString = 0
 
    def __init__(self, host=HOST, rdStr=defReadString, wrStr=defWriteString):
        snmpClient.ipAddr=host 
        snmpClient.readString=rdStr
        snmpClient.writeString=wrStr

    def getCmdInteger(self, oid):
        value = 0
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
              cmdgen.CommunityData(snmpClient.readString),
              cmdgen.UdpTransportTarget((snmpClient.ipAddr, 161), timeout=1, retries=0), oid)

        if errorIndication:
            print(errorIndication)
            status = -1 
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            status = -1
        else:
            value = int (varBinds[0][1])
            status = 0

        return status,value

    def setCmdInteger(self, oid, value):
        cmdGen = cmdgen.CommandGenerator()

        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.setCmd(
                  cmdgen.CommunityData(snmpClient.writeString),
                  cmdgen.UdpTransportTarget((snmpClient.ipAddr, 161), timeout=1, retries=0),
                  cmdgen.ObjectType(cmdgen.ObjectIdentity(oid), cmdgen.Integer(value)))

        if errorIndication:
            print(errorIndication)
            status = -1
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            status = -1
        else:
            status = 0

        return status

    def getCmdString(self, oid):
        value = " "
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
              cmdgen.CommunityData(snmpClient.readString),
              cmdgen.UdpTransportTarget((snmpClient.ipAddr, 161), timeout=1, retries=0), oid)

        if errorIndication:
            print(errorIndication)
            status = -1
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            status = -1
        else:
            value = varBinds[0][1]
            status = 0

        return status,value

