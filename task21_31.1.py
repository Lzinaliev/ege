#$pvpv
#01234


def f(n, m, p):
    if (p == 2 or p == 4) and n + m >= 47:
        return 1
    if p == 4 and n + m < 47:
        return 0
    if (p == 1 or p == 3) and n + m >= 47:
        return 0
    else:
        if p % 2 != 0:
            if n > m:
                return f(n + 1, m, p + 1) or f(n + 2, m, p + 1) or f(n + 3, m, p + 1) or f(n, m * 2, p + 1)
            elif n < m:
                return f(n, m + 1, p + 1) or f(n, m + 2, p + 1) or f(n, m + 3, p + 1) or f(n * 2, m, p + 1)
            elif n == m:
                return f(n + 1, m, p + 1) or f(n + 2, m, p + 1) or f(n + 3, m, p + 1) or f(n, m + 1, p + 1) or f(n, m + 2, p + 1) or f(n, n + 3, p + 1)
        else:
            if n > m:
                return f(n + 1, m, p + 1) and f(n + 2, m, p + 1) and f(n + 3, m, p + 1) and f(n, m * 2, p + 1)
            elif n < m:
                return f(n, m + 1, p + 1) and f(n, m + 2, p + 1) and f(n, m + 3, p + 1) and f(n * 2, m, p + 1)
            elif n == m:
                return f(n + 1, m, p + 1) and f(n + 2, m, p + 1) and f(n + 3, m, p + 1) and f(n, m + 1, p + 1) and f(n, m + 2, p + 1) and f(n, n + 3, p + 1)
l = set()
for n in range(1, 24):
    if f(n, 22, 0) == 1:
        print(n)
        break