import time
import mydefines
from mydefines import define as defs
import mysnmp
from mysnmp import snmpClient


base_oid = "1.3.6.1.4.1.19536.10.1"

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

HOST = "10.20.90.198"
defReadString = "public"
defWriteString = "private"

def getPduCountJones(HOST, defReadString, defWriteString):
        snmp = snmpClient(HOST, defReadString, defWriteString)

        #testoid = base_oid + '.' + '1.1.0'
        testoid = base_oid + '.' + sensorbase + '.' + '9' + '.' + pdug5TemperatureScale

        status, pduCount = snmp.getCmdInteger(testoid);

        return status, pduCount

class g5pduTotal(object):
    ipAddr = 0
    readString = 0
    writeString = 0

    #
    # Constructor
    # 
    def __init__(self, host=HOST, rdStr=defReadString, wrStr=defWriteString):
        self.ipAddr=host 
        self.readString=rdStr
        self.writeString=wrStr

    #
    # Get the PDU count
    #
    def getPduCount(self):
        snmp = snmpClient(self.ipAddr, self.readString, self.writeString)

        testoid = base_oid + '.' + '1.1.0'

        status, pduCount = snmp.getCmdInteger(testoid);

        return status, pduCount

    def getTemperatureCount(self, pdu):
        status, value = self.getEnviroValue(pdu, pdug5TemperatureCount)
        return status, value

    def getHumidityCount(self, pdu):
        status, value = self.getEnviroValue(pdu, pdug5HumidityCount)
        return status, value

    ####
    def getSensorValue(self, sensorType, pdu, sensor):
        status, typeBaseOid = self.convertSensorTypeToOidBase(sensorType)
        if (status != 0):
            return status, 0
        if sensorType == defs.hid:
            oid = typeBaseOid + "." + pdug5HidSensorValue
        else:
            oid = typeBaseOid + "." + pdug5SensorValue
        status, value = self.getSensorIntValue(pdu, sensor, oid)
        return status, value

    def convertSensorTypeToOidBase(self, sensorType):
        if (sensorType == defs.temperature):
            return 0, temperatureBase
        elif (sensorType == defs.humidity):
            return 0, humidityBase
        elif (sensorType == defs.door):
            return 0, doorBase
        elif (sensorType == defs.dry):
            return 0, dryBase
        elif (sensorType == defs.spot):
            return 0, spotBase
        elif (sensorType == defs.rope):
            return 0, ropeBase
        elif (sensorType == defs.smoke):
            return 0, smokeBase
        elif (sensorType == defs.beacon):
            return 0, beaconBase
        elif (sensorType == defs.hid):
            return 0, hidStatusBase
        else:
            return -1, 0

    def getEnviroValue(self, pdu, param):
        snmp = snmpClient(self.ipAddr, self.readString, self.writeString)
        testoid = base_oid + '.' + sensorbase + '.' + param + '.' + str(pdu)
        status, value = snmp.getCmdInteger(testoid);
        return status, value

    def getSensorIntValue(self, pdu, sensor, param):
        snmp = snmpClient(self.ipAddr, self.readString, self.writeString)
        if pdu == 0:
            testoid = base_oid + '.' + param + '.' + str(sensor)
        else:
            testoid = base_oid + '.' + param + '.' + str(pdu) + '.' + str(sensor)
        status, value = snmp.getCmdInteger(testoid);
        return status, value

    def getSensorName(self, sensorType, pdu, sensor):
        status, typeBaseOid = self.convertSensorTypeToOidBase(sensorType)
        if (status != 0):
            return status, 0
        oid = typeBaseOid + "." + pdug5SensorName
        status, value = self.getSensorStringValue(pdu, sensor, oid)
        return status, value
    
    def getSensorStringValue(self, pdu, sensor, param):
        snmp = snmpClient(self.ipAddr, self.readString, self.writeString)
        if pdu == 0:
            testoid = base_oid + '.' + param + '.' + str(sensor)
        else:
            testoid = base_oid + '.' + param + '.' + str(pdu) + '.' + str(sensor)
        status, value = snmp.getCmdString(testoid);
        return status, value
