from ipaddress import *

k = 0

network = ip_network('211.48.136.64/255.255.255.224')

for ip in network:
    s = format(ip,"b")

    if s[-2] == '1' and s[-1] == '1':
        k += 1
print(k)
        