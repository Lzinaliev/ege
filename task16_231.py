def f(n):
    if n <= 15:
        return 2*n*n + 4*n + 3
    elif n > 15 and n%3 == 0:
        return f(n-1) + n*n + 3
    elif n > 15 and n%3 != 0:
        return f(n-2) + n-6
count = 0
for n in range(1,1001):
    x = str(f(n))
    m = 1
    for i in range(len(x)):
        if int(x[i]) % 2 == 0:
            m = 0
            break
    if m == 1:
        count += 1
print(count)







