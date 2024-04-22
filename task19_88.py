#$pv
#012

def f(n,p):
    if n >= 43 and p == 2:
        return 1
    if n < 43 and p == 2:
        return 0
    if n >= 43 and p < 2:
        return 0
    else:
        if p % 2 == 0:
            return f(n+1,p+1) and f(n+4,p+1) and f(n*3,p+1)
        else:
            return f(n + 1, p + 1) or f(n + 4, p + 1) or f(n * 3, p + 1)

for n in range(1,43):
    if f(n,0) == 1:
        print(n)