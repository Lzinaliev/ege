p = list(range(17,47))
q = list(range(22,58))
a = []
for x in range(-500,501):
    if not((x not in a) <= (((x in p) and (x in q)) <= (x in a))):
        a.append(x)
print(len(a)-1, a)
