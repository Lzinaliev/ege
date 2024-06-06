for n in range(4,10000):
    x = '1' + '2'*n
    while ('12' in x) or ('5522' in x) or ('2222' in x):
        if '12' in x:
            x = x.replace('12','55',1)
        if '2222' in x:
            x = x.replace('2222','1',1)
        if '5522' in x:
            x = x.replace('5522','21',1)
    sum1 = 0
    for i in range(len(x)):
        sum1 += int(x[i])
    if sum1 == 142:
       print(n)
       break

#13
from ipaddress import *

network = ip_network('116.29.0.0/255.255.255.0')
count = 0
for ip in network:
    ip = bin(int(ip))[2:]
    print(ip)