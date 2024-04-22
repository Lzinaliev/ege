a = set()
for x in range(0,10):
    for y in range(0,10000):
        s = '3' + str(x) + '1' + str(y)[1:] + '57'
        if int(s) % 1991 == 0 and int(s) < 10**8:
            a.add(s)

for x in range(0,10):
        s = '3' + str(x) + '1' + '57'
        if int(s) % 1991 == 0 and int(s) < 10**8:
            a.add(s)

l = list(a)
for i in range(len(l)):
    l[i] = int(l[i])
l = sorted(l)
for i in range(len(l)):
    print(l[i],int(l[i]/1991))

