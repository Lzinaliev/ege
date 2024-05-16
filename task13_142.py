from ipaddress import  *

network = ip_network('23.140.159.160/255.255.252.0',strict=0)
count = 0
for i in network:
    binip = format(i,"b")
    x = binip[:16]
    y = binip[16:]
    if x.count('1') >= y.count('1'):
        count += 1
print(count)