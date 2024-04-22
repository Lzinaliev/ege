p = list(range(130,172))
q = list(range(150,186))
a = []
for x in range(-300,300):
    if not((x in p) <= (((x in q) and (x not in a)) <= (x not in p))):
        a.append(x)
print(a)

