#$pv
#012

def f(n,p):
    if p == 2 and n >= 96:
        return 1
    elif p == 2 and p < 96:
        return 0
    elif p < 2 and n >= 96:
        return 0
    else:
        if p % 2 == 0:
            if n % 2 == 0:
                return f(n+1,p+1) and f(n+n*0.5,p+1)
            elif n % 3 == 0:
                return f(n + 1, p + 1) and f(n + n * 1/3, p + 1)
            else:
                return f(n+1,p+1) and f(n*2,p+1)
        else:
            if n % 2 == 0:
                return f(n + 1, p + 1) or f(n + n * 0.5, p + 1)
            elif n % 3 == 0:
                return f(n + 1, p + 1) or f(n + n * 1 / 3, p + 1)
            else:
                return f(n + 1, p + 1) or f(n * 2, p + 1)

for n in range(1,96):
    if f(n,0) == 1:
        print(n)
        break
