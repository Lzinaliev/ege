for n in range(100):
    s = bin(n)[2:]
    s = str(s)
    if n % 3 == 0:
        s += s[-3:]
    else:
        c = (n % 3)* 3
        s += bin(c)[2:]
    R = int(s, 2)
    if R >= 76:
        print(n)
        break