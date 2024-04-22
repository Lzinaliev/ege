def f(n):
    if n == 0:
        return  0
    elif n > 0 and n % 3 == 0:
        return f(n//3)
    elif n % 3 > 0:
        return n % 3 + f(n-(n % 3))

i = 0
while f(i) != 11:
    i += 1
print(i)



