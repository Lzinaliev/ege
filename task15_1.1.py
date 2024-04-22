for a in range(300,0,-1):
    num = 0
    for x in range(0,300):
        for y in range(0,300):
            if ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9)):
                num += 1
    if num == 300*300:
        print(a)
        break