import time
#import mydefines
#from mydefines import define as defs
import mysnmp
from mysnmp import snmpClient


base_oid = "1.3.6.1.4.1.19536.10.1"

#pdug5IdentTable
pdug5Model = '3.1'
pdug5Manufacturer = '4.1'
pdug5FirmwareVersion = '5'


#Sensors
sensorObject = '4'
#Common Sensors
sensorbase = '1.2.1'
pdug5TemperatureScale = '1'
pdug5TemperatureCount = '2'
pdug5HumidityCount = '3'

#Temperature/Humidity
temperatureBase = '4.2.1'
humidityBase = '4.3.1'
temperatureOid = '4.2.1'
humidityOid = '4.3.1'
pdug5SensorValue = '4'
pdug5SensorName = '2'

HOST = "192.168.0.8"
defReadString = "public"
defWriteString = "private"

def getPduCountJones(HOST, defReadString, defWriteString):
        snmp = snmpClient(HOST, defReadString, defWriteString)

        #testoid = base_oid + '.' + '1.1.0'
        testoid = base_oid + '.' + sensorbase + '.' + '9' + '.' + pdug5TemperatureScale

        status, pduCount = snmp.getCmdInteger(testoid);

        return status, pduCount
    
    
def getPduSnmpStringData(HOST, defReadString, defWriteString, myoid):
        snmp = snmpClient(HOST, defReadString, defWriteString)
        status, value = snmp.getCmdString(myoid);
        return status, value
    
def getPduSnmpIntData(HOST, defReadString, defWriteString, myoid):
        snmp = snmpClient(HOST, defReadString, defWriteString)
        status, value = snmp.getCmdInteger(myoid);
        return status, value