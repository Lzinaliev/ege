#$pvp
#0123


def f(n,m,p):
    if n + m >= 46:
        return p % 2 == 0
    if p == 0:
        return 0
    l = []
    if n < m:
        for z in range(1,n+1):
            l.append(f(n+z,m,p-1))
    else:
        for z in range(1,m+1):
            l.append(f(n,m+z,p-1))
    if p % 2 == 0:
        return all(l)
    else:
        return any(l)

a = []
for n in range(1,41):
        if f(n,5,3) == 1 and f(n,5,1) != 1:
            a.append(n)

print(a)
