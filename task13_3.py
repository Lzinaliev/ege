from ipaddress import *
k= 0

network = ip_network('192.168.32.160/255.255.255.240')

for ip in network:
    s = format(ip,"b")
    if s.count('1') % 2 == 0:
        k += 1

print(k)