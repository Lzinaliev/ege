#$pv
#012

def f(n,m,p):
    if n + m <= 20 and p == 2:
        return 1
    elif n + m > 20 and p == 2:
        return 0
    elif n+m <= 20 and p < 2:
        return 0
    else:
        if p % 2 == 0:
            return f(n - 1, m, p + 1) or f(n, m - 1, p + 1) or f(n // 2 + n % 2, m, p + 1) or f(n, m // 2 + m % 2, p + 1)
        else:
            return f(n - 1, m, p + 1) or f(n, m - 1, p + 1) or f(n // 2 + n % 2, m, p + 1) or f(n, m // 2 + m % 2, p + 1)


for n in range(100, 10,-1):
    if f(n, 10, 0) == 1:
        print(n)
        break

