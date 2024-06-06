for n in range(1,1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = str(s) + '0'

    else:
        s = str(s) + '1'
    d = s[2:]

    if s.count('1') % 3 == 0:
        s = '11' + d
    else:
        s = '10' + d
    R = int(s,2)
    if R > 26:
        print(n)
        break