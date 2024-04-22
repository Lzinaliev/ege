for N in range(1,1000):
    s = bin(N)[2:]
    s1 = s.count("1")
    s2 = s1 % 2
    s += str(s2)
    s1 = s.count("1")
    s2 = s1 % 2
    s += str(s2)
    R = int(s, 2)
    if R > 123:
        print(R)
        break

