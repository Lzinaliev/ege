from ipaddress import *
k = 0
net = ip_network('23.140.159.160/255.255.252.0',0)

for ip in net:
    s = bin(int(ip))[2:]
    sl = s[:16]
    sr = s[16:]
    if sl.count('1') < sr.count('1'):
        k += 1
print(k)