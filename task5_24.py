for i in range(10000,1000,-1):
    s = str(i)
    c1 = int(s[0]) + int(s[1])
    c2 = int(s[1]) + int(s[2])
    c3 = int(s[2]) + int(s[3])
    f = str(c1 + c2 + c3 - max(c1, c2, c3) - min(c1, c2, c3))
    s = str(max(c1, c2, c3))
    s1 = f + s
    if s1 == '613':
        print(i)
        break