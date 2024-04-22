#$pvp
#0123

def f(n,m,p):
    if n + m >= 84 and p == 3:
        return 1
    elif n + m < 84 and p == 3:
        return 0
    elif n+m >= 84 and p < 3:
        return 0
    else:
        if p % 2 == 0:
            return f(n + 1, m, p + 1) or f(n, m + 1, p + 1) or f(n, m * 2, p + 1) or f(n * 3, m,p + 1)
        else:
            return f(n + 1, m, p + 1) and f(n, m + 1, p + 1) and f(n, m * 2, p + 1) and f(n * 3, m, p + 1)


for n in range(1, 68):
    if f(n, 16, 0) == 1:
        print(n)
