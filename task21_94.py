#$pvpv
#01234


def f(n,p):
    if n >= 84 and (p == 4 or p ==2):
        return 1
    elif n >= 84 and p < 4:
        return 0
    elif n < 84 and p == 4:
        return 0
    else:
        if p%2 == 0:
            if n % 2 == 0:
                return f(n+1,p+1) and f(int(n*1.5),p+1)
            else:
                return f(n+1,p+1) and f(n*2,p+1)
        else:
            if n % 2 == 0:
                return f(n+1,p+1) or f(int(n*1.5),p+1)
            else:
                return f(n+1,p+1) or f(n*2,p+1)

def f1(n,p):
    if n >= 84 and p == 2:
        return 1
    elif n >= 84 and p < 2:
        return 0
    elif n < 84 and p == 2:
        return 0
    else:
        if p%2 == 0:
            if n % 2 == 0:
                return f1(n+1,p+1) and f1(int(n*1.5),p+1)
            else:
                return f1(n+1,p+1) and f1(n*2,p+1)
        else:
            if n % 2 == 0:
                return f1(n+1,p+1) or f1(int(n*1.5),p+1)
            else:
                return f1(n+1,p+1) or f1(n*2,p+1)

for n in range(1,84):
    if f(n,0) == 1:
        print(n)

print('============')

for n in range(1,108):
    if f1(n,0) == 1:
        print(n)


