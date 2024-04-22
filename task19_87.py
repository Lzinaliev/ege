#$pv
#012


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
for n in range(1,46):
    for m in range(1,46):
        if f(n,m,1) == 1:
            a.append(n+m)
print(min(a))

