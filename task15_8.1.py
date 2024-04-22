a = []
for x in range(-300,301):
    if not(((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))):
        a.append(x)
print(len(a)-1)