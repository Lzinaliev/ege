
for a in range(1,1001):
    k = 0
    for x in range(1,1001):
        if (x % a != 0) <= ((x % 14 == 0) <= (x % 4 != 0)):
            k += 1
    if k == 1000:
        print(a)
