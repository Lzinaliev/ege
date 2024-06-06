count = 0
for i in range(800000, -1,-1):
    delit = set()

    for d in range(2, round(i ** 0.5) + 1):
        if i % d == 0:
            delit.add(d)
            delit.add(i // d)

    if delit:
        m = (max(delit) - min(delit))

        if m % 17 == 0:
            print(i, m)
            count += 1
        if count == 5:
            break