for a in range(0,1000):
    k = 0
    for x in range(0,1000):
        if (x&49 != 0) <= ((x&41 == 0) <= (x&a != 0)):
            k += 1
    if k == 1000:
        print(a)
        break

