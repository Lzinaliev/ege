for x in '0123456789ABCDEFGHIJKL':
    t = int('63' + x + '59685',22) + int('17' + x + '53', 22) + int('36' + x + '5',22)
    if t % 21 == 0:
        print(t//21)
        break