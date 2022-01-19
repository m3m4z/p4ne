from pysnmp.hlapi import *


snmp_object1 = snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object2 = snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')


result= getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('10.31.70.107', 161)),
               ContextData(),
               ObjectType(snmp_object1))

for r in result:
    for r2 in r[3]:
            print(r2)

result2= nextCmd(SnmpEngine(),
              CommunityData('public', mpModel=0),
              UdpTransportTarget(('10.31.70.107', 161)),
              ContextData(),
              ObjectType(snmp_object2),
              lexicographicMode=False)

for r in result2:
    for r2 in r[3]:
            print(r2)
