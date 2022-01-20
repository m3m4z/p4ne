#импорт библиотек
from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self,:
        IPv4Network.__init__(self,
              random.randint(0xb000000, 0xdf000000)
              random.randint(8, 24)
              strict=false)

    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 2)





