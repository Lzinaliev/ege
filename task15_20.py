count = 0
for a in range(0,300,):
    k = 0
    for m in range(0,300):
        for n in range(0,300):
            if ((2*m + 3 *n) > 40) or ((m < a) and (n <= a)):
                k += 1
    if k == 300*300:
        print(a)
        break