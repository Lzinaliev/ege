from fnmatch import *

c = set()
b = []
for i in range(1,30):
    b.append(2**i)
for n in range(0,10**9,31*2031):
    if fnmatch(str(n), '*31*65?'):
        a = set()
        for d in range(1,round(n**0.5)+1):

            if n % d == 0:
                a.add(d)
                a.add(n//d)
        if len(a) in b:
            c.add(n)

l = sorted(list(c))
for i in range(len(c)):
    print(l[i],l[i]//2031)



