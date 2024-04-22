count = 0
for a in range(300,0, -1):
    k = 0
    for x in range(0,300):
        for y in range(0,300):
            if ((2*x + 3 * y) < 30) or (x + y >= a):
                k += 1
    if k == 300*300:
        count += 1
print(count)