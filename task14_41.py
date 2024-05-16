for x in '0123456789ABCDEFG':
    t = int('8' + x + '5678',25) + int('457' + x + '69',25) + int('145' + x + '1',25)
    if t % 23 == 0:
        print(t//23)
        break