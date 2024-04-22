for a in range(1,100):
    for x in "0123456789ab":
        m = '49' + x + '26'
        n = '49' + x + '70'
        if (int(m,12) + a) % int(n,12) == 0:
            print(a)
            exit