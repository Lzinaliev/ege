a = set()
for i in range(-300,300):
    a.add(i)
for x in range(-300,300):
    if not((x in a) <= (x**2 <= 100) and ((x**2 <= 64) <= (x in a))):
        a.remove(x)
print(len(a)-1)

