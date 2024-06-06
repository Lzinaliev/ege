from ipaddress import *
count = 0
network = ip_network('252.67.33.87/255.252.0.0',strict=0)

for ip in network:
    ip = bin(int(ip))[2:]
    s1 = ip[:16]
    s2 = ip[16:]
    if s1.count('1')*2 < s2.count('1'):
        count += 1
print(count)
