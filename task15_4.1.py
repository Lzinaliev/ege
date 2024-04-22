p = list(range(4,16))
q = list(range(12,21))
a = []
for x in range(-500,501):
    if not(((x in p) and (x in q)) <= (x in a)):
        a.append(x)
print(a,3)
