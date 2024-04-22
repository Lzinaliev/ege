#$pvp
#0123


def f(n,p):
    if n >= 96:
        return p % 2 == 0
    if p == 0:
        return 0
    l = [f(n+1,p-1)]
    if n % 2 == 0:
        l.append(f(n*3//2,p-1))
    if n % 3 == 0:
        l.append(f(n*4//3,p-1))
    if n %2 != 0 and n%3 != 0:
        l.append(f(n*2,p-1))
    if p % 2 == 0:
        return all(l)
    else:
        return any(l)

for n in range(1,96):
    if (f(n,3) == 1) and (f(n,1) == 0):
        print(n)

