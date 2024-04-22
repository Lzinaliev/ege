for n in range(2, 100):
    s = bin(n)[2:]
    s += s[-2]
    s += s[1]
    r = int(s, 2)
    if r > 150:
        print(n)
        break