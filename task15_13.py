for a in range(1000,0,-1):
    k = 0
    for x in range(1000,0,-1):
        if (x&a != 0) <= ((x & 36 == 0) <= (x & 6 != 0)):
            k += 1
    if k == 1000:
        print(a)
        break