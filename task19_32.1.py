#$p
#01
list = []
def f(n,m,p):
    if n +m > 39 and p == 1:
        return 1
    if n + m <= 39 and p == 1:
        return 0
    if n + m > 39 and p < 1:
        return 0
    else:
        if n < m:
            return f(n+n,m,p+1)
        else:
            return f(n,m + m,p + 1)

for n in range(1,20):
    for m in range(1,20):
        if f(n,m,0) == 1:
            list.append(n+m)
print(min(list))


