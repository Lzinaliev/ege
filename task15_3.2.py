p = list(range(10,30))
q = list(range(13,19))
a = list(range(-300,301))
for x in range(-300,301):
    if not(((x in a) <= (x in p)) or (x in q)):
        a.remove(x)
print(a,19)
