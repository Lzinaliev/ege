for a in range(0,200):
    k = 0
    for x in range(1, 201):
        for y in range(1, 201):
            if ((144 % x == 0) <= (x % y != 0)) or ((x + y) > 100) or ((a - x) > y):
                k += 1
    if k == 200*200:
        print(a)
        break
