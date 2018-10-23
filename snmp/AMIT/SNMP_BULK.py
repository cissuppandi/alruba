from pysnmp.entity.rfc3413.oneliner import cmdgen
import time
def snmp_bulk(ip,port):
    oid=[]
    myoid=[]
    ln=raw_input("ENTER THE OID TO VERIFY FOLLOWED BY SPACE")
    oid.append(ln.split(" "))
    for i in oid[0]:
        myoid.append(i) 

    errorIndication, errorStatus, errorIndex, \
    varBindTable = cmdgen.CommandGenerator().bulkCmd(  
                cmdgen.CommunityData('public'), 
                cmdgen.UdpTransportTarget((ip,port)),  
                0, 
                10, *myoid)
    start_time=time.time()
    if errorIndication:
       print errorIndication
       stop_time=time.time()
    else:
        if errorStatus:
            print '%s at %s\n' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                )
            stop_time=time.time()
        else:
            stop_time=time.time()
            for varBindTableRow in varBindTable:            
                for name, val in varBindTableRow:
                   if(val.prettyPrint()=="No more variables left in this MIB View"):
                      print("")
                   else:
                      print '%s = %s' % (name, val.prettyPrint())

    print("TIME TAKEN  FOR THE FETCHING BULK"+str(time.time()-stop_time)+" "+"ms")
    return
snmp_bulk("10.20.90.139","161")
