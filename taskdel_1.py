n = int(input())
a = set()
for d in range(2,int(n**(0.5))+1):
    if n % d == 0:
        d2 = n // d
        if d2 % 3 == 0:
            a.add(d2)
        if d % 3 == 0:
            a.add(d)
if n % 3 == 0:
    a.add(n)
print(a)
