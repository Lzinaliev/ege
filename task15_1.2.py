p = list(range(5,31))
q = list(range(14,24))
a = list(range(-300,301))
for x in range(-300,301):
    if not(((x in p) == (x in q)) <= (x not in a)):
        a.remove(x)
print(a,9)
