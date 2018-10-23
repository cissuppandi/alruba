from pysnmp.hlapi import *
def set_cmd(ip,port,new_oid,new_value):
    
    g = setCmd(SnmpEngine(),
                CommunityData('private',mpModel=1),
                UdpTransportTarget((ip, port),timeout=2, retries=2, tagList=''),
                ContextData(),
                ObjectType(ObjectIdentity(new_oid),new_value))
    print(next(g))
    print("PLEASE WAIT ONCE TO VERIFY THE VALUE")
    
    return 
    

def set_check(ip,port,OID):
        print("GETIING THE NEW VALUE FROM SNMP SERVER")
        iterator = getCmd(SnmpEngine(),
                          CommunityData('public',mpModel=1),
                          UdpTransportTarget((ip,port),timeout=1,retries=2),
                          ContextData(),
                          ObjectType(ObjectIdentity(OID)))

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:  # SNMP engine errors
            print(errorIndication)
            return errorIndication
           
        else:
            if errorStatus:  # SNMP agent errors
                print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
                return'%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?')
            else:
                for varBind in varBinds:  # SNMP response contents
                    print(' = '.join([x.prettyPrint() for x in varBind]))
                    return ' = '.join([x.prettyPrint() for x in varBind])
      
