a = set()

def f(x, a):
    return ((x in a) <= (x**2 <= 81)) and ((x**2 <= 36) <= (x in a))
for x in range(-1000, 1000):
    if not f(x, a):
        a.add(x)

print(len(a) - 1)