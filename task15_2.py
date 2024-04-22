for a in range(0,1000):
    num = 0
    for x in range(0,1000):
        if (x&25 != 0) <= ((x&17 == 0) <= (x&a != 0)):
            num += 1
    if num == 1000:
        print(a)
        break