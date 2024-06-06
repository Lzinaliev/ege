from ipaddress import *

for a in (0,128,192,224,240,248,252,254,255):
    net = ip_network(f'252.63.194.3/255.255.{a}.0',strict=0)
    for ip in net:
        i = bin(int(ip))[2:]
        s1 = i[:16]
        s2 = i[16:]
    if s1.count('1') >= s2.count('1'):
        print(a)
        break