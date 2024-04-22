from sys import setrecursionlimit

setrecursionlimit(3000)
def f(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + f(n-1)

print(f(2204) - f(2202))