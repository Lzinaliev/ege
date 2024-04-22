a = set()
b = []
c = set()
for i in range(0,20):
    b.append(2**i)
for x in range(0,10):
    for y in range(0,10000):
        for z in range(0,1000):
            s = str(y)[1:] + '31' + str(z)[1:] + '65' + str(x)
            if int(s) % 31 == 0 and int(s) % 2031 == 0 and int(s) <= 10**9:
                for d in range(1,int(int(s)**0.5)):
                    if int(s) % d == 0:
                        c.add(d)
                        c.add(int(s)//d)
                if len(c) in b:
                    a.add(int(s))



print(a)
l = sorted(list(a))

for i in range(len(l)):
    print(l[i],int(l[i] / 2031))


