line = set()
for i in range(-300,300):
    line.add(i)
for x in range(-300,300):
    if not(((x in line) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in line))):
        line.remove(x)
print(len(line)-1)


