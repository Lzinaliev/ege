for n in range(95632,95701):
    c = 0
    d = []
    for j in range(1,n+1):
        if n % j == 0:
            if j % 2 == 0:
                c += 1
                d.append(j)
    if c == 6:
        print(d)