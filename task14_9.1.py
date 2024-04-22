for x in '12345678':
    for y in '012345678':
        s = int('2' + y + '66' + x, 9) + int(x + '0' + y + '1', 12)
        if s % 170 == 0:
            print(s // 170)