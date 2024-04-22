for n in range(100, 1000):
    s = bin(n)[2:]
    s = str(s)
    for i in range(3):
        if s.count("1") == s.count("0"):
            s += s[-1]
        elif s.count("1") > s.count("0"):
            s += "0"
        else:
            s += "1"
    R = int(s, 2) # перевод в десятичную систему
    if R % 4 == 0:
        print(n)
        break
