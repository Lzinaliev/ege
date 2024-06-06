for a in range(1,301):
    k = 0
    for x in range(1,301):
        if (x%a != 0) <= ((x % 26 == 0) <= (x % 169 !=0)):
            k += 1
    if k == 300:
        print(a)
