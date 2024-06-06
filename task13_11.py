
from ipaddress import *

for a in range(0,256):

    net = ip_network(f'32.0.{a}.5/255.255.240.0', strict=0)
    f = 0

    for ip in net:

        i = bin(int(ip))[2:]

        sl = i[:16]
        sr = i[16:]
        if sl.count('1') > sr.count('1'):
            f = 1

            break

    if f == 0:
        print(a,f)


