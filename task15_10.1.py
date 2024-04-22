p = list(range(10,41))
q = list(range(5,16))
r = list(range(35,51))
a = []
for x in range(-500,501):
    if not(((x in a) or (x in p)) or ((x in q) <=(x in r))):
        a.append(x)
print(len(a),a)
