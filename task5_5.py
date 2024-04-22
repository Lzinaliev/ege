for N in range(1,1000):
    s = bin(N)[2:]
    if s.count("1") % 2 == 1:
        s += "11"
    else:
        s += "00"
    R = int(s,2)
    if R > 114:
        print(R)
        break