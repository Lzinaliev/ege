from ipaddress import *

network = ip_network('252.67.33.87/255.252.0.0',strict=0)

for ip in network:
    binip = format(ip,'b')
    print(bin(252)[2:], bin(67)[2:], bin(169)[2:], bin(231)[2:])
    print(binip)
    print(bin(int(ip))[2:])
    break
print(len('1111100010000111000001111100010'))