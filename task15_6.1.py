p = list(range(20,50))
q = list(range(30,66))
a = []
for x in range(-500,501):
    if not((x not in a) <= ((x in p) <= (x not in q))):
        a.append(x)
print(len(a),a)
