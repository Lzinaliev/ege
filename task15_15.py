p = list(range(3,38+1))
q = list(range(21,57+1))
a = list(range(-300,300))
for x in range(-300,300):
    if not(((x in q) <= (x in p)) <= (x not in a)):
        a.remove(x)
print(a)
print(57-38)