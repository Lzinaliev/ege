#$pvp
#0123

def f(n,p):
    if n >= 108 and p == 3:
        return 1
    elif n >= 108 and p < 3:
        return 0
    elif n < 108 and p == 3:
        return 0
    else:
        if p%2 == 0:
            if n % 2 == 0:
                return f(n+1,p+1) or f(int(n*1.5),p+1)
            else:
                return f(n+1,p+1) or f(n*2,p+1)
        else:
            if n % 2 == 0:
                return f(n+1,p+1) and f(int(n*1.5),p+1)
            else:
                return f(n+1,p+1) and f(n*2,p+1)

for n in range(1,108):
    if f(n,0) == 1:
        print(n)