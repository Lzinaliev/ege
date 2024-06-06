
from ipaddress import *

for a in range(0,256):

    net = ip_network(f'126.255.{a}.100/255.255.240.0', strict=0)
    flag = 0

    for ip in net:

        i = format(ip,'b')
        sl = i[:16]
        sr = i[16:]
        if sl.count('1') < sr.count('1'):
            flag = 1

            break

    if flag == 0:
        print(a)


