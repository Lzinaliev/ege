for x in '0123456789ABCDE':
    t = int('98' + x + '79641', 22) + int('25' + x + '49', 22) + int('63' + x + '5',22)
    if t % 21 == 0:
        print(t // 21)
        break