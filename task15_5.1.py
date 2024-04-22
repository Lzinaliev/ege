count = 0
for a in range(0,300):
    k = 0
    for x in range(0,300):
        for y in range(0,300):
                if ((x < a) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= a)):
                    k += 1
    if k == 300*300:
        count += 1
print(count)
        