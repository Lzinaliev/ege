a = set()
for i in range(-300,300):
    a.add(i)
for x in range(-300,300):
    for y in range(-300,300):
            if not(((x in a) <= (x**2 <= 81)) and ((y**2 <= 36) <= (y in a))) :
                a.remove(x)

print(len(a)-1)
