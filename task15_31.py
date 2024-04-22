for a in range(0,200):
    k = 0
    for x in range(1, 201):
            if ((x&116 != 0) or (x&92 != 0)) <= ((x&69 == 0) <= (x&a != 0)):
                k += 1
    if k == 200:
        print(a)
        break

