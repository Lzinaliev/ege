#$pvpv
#01234

def f(n,m,p):
    if n + m >= 77 and (p == 4 or p == 2):
        return 1
    elif n + m >= 77 and p < 4:
        return 0
    elif n + m < 77 and p == 4:
        return 0
    else:
        if p % 2 == 0:
            return f(n+1,m,p+1) and f(n,m+1,p+1) and f(n*2,m,p+1) and f(n,m*2,p+1)
        else:
            return f(n + 1, m, p + 1) or f(n, m + 1, p + 1) or f(n * 2, m, p + 1) or f(n, m * 2, p + 1)

def f1(n,m,p):
    if n + m >= 77 and p == 2:
        return 1
    elif n + m >= 77 and p < 2:
        return 0
    elif n + m < 77 and p == 2:
        return 0
    else:
        if p % 2 == 0:
            return f1(n+1,m,p+1) and f1(n,m+1,p+1) and f1(n*2,m,p+1) and f1(n,m*2,p+1)
        else:
            return f1(n + 1, m, p + 1) or f1(n, m + 1, p + 1) or f1(n * 2, m, p + 1) or f1(n, m * 2, p + 1)

for n in range(1,70):
    if f(n,7,0) == 1:
        print(n)

print('----------------------')
for n in range(1,70):
    if f1(n,7,0) == 1:
        print(n)