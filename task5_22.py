for N in range(1, 100):
    s = bin(N)[2:]
    if s.count("1") > s.count("0"):
        s += '1'
    else:
        s += '0'
    R = int(s,2)
    if R > 100:
        print(R)
        break