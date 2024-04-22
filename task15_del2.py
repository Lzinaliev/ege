for a in range(1,1001):
    k = 0
    for x in range(1, 1001):
        if ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100):
            k += 1
    if k == 1000:
        print(a)
        break


