def f(x):
    l = []
    for d in range(2,x):
        if x % d == 0:
            l.append(d)
            if len(l) > 2:
                break
    if len(l) == 2:
        print(l[0],l[1])

for i in range(174457,174505+1):
    f(i)





