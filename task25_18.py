for i in range(1000000,2000001):
    raz = []
    for d in range(1,int(i**0.5)+1):
        if i%d == 0:
            if abs(i//d - d) <= 100:
                raz.append(d)

                if len(raz) > 2:
                    print(i)
                    break


