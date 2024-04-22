cdel = 0
i = 700000
while cdel < 5:
    i += 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if i / j == i:
                break
            if (i / j + j) % 10 == 8:
                print(i, i // j + j)
                cdel += 1
            break