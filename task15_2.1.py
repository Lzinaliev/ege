count = 0
for a in range(0,300):
    num = 0
    for x in range(0,300):
        for y in range(0,300):
            if ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6)):
                num += 1
    if num == 300*300:
        count += 1
print(count)    