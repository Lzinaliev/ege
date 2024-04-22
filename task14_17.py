for i in range(1,100):
    for x in "0123456789abcdefghi":
        res = int('98' + x + '79641', 19) + int('36' + x + '14', 19) + int('73' + x + '4', 19)
        if res % 18 == 0:
            print(res//18)
