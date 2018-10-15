#import socket
#import getpass
#import sys
#import telnetlib
#import time
#import datetime
#import socket
#import threading
#import os
#import datetime
#from pyasn1.type import univ
#from pyasn1.codec.ber import encoder, decoder

#base_oid = "1.3.6.1.4.1.19536.10.1"
#outlet_object = 5
#outlet_control = '5.2.1'
#ocStatus = 1
#from pysnmp.entity.rfc3413.oneliner import cmdgen

class define:
    off = 1
    on = 2
    pendingOff = 3
    pendingOn = 4
    reboot = 5
    lastState = 3
    # Sensor types
    none = 0
    temperature = 1
    humidity = 2
    door = 3
    dry = 4
    spot = 5
    rope = 6
    smoke = 7
    beacon = 8
    hid = 9

