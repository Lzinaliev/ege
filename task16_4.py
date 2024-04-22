def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return f(n-2) + f(n-1)

print(f(8))