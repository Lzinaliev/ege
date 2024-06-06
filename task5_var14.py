for n in range(0,10000):
    s = n - int(n//4)
    sbin = bin(s)[2:]
    sbin = sbin + str(bin(sbin.count('1')//2)[2:])
    print(n,sbin)