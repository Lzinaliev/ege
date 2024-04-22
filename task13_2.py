from ipaddress import *

k = 0

network = ip_network('192.168.0.0/255.255.128.0')

for i in network:
    if int(i) % 4 == 0:
        k += 1

print(k)