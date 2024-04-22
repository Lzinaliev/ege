for n in range(100, 1000):
    s = str(n)
    c1 = int(s[0]) * int(s[1])
    c2 = int(s[1]) * int(s[2])

    if c1 < c2:
        f = str(c1)
        s = str(c2)
    else:
        f = str(c2)
        s = str(c1)

    s1 = f + s
    if s1 == '621':
        print(n)
        break
