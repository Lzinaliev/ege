for a in range(0,300):
    k = 0
    for x in range(0,300):
        for y in range(0,300):
            if (y + 2*x < a) or (x>30) or (y>20):
                k += 1
    if k == 300*300:
        print(a)
        break