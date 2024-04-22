from sys import setrecursionlimit
count = 0
setrecursionlimit(2000000000)
def f(n):
    if n == 0:
        return 0
    elif n % 2 ==0:
        return f(n-1) + 1
    elif n > 0 and n % 2 != 0:
        return f(n / 2)

for n in range(50000000):
    if f(n) == 3:
        count += 1
        for n in range(50000000,1000000001):
            if f(n) == 3:
                count += 1
print(count)

