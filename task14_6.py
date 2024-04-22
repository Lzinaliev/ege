for x in "0123456789abcdefghi":
    num1 = '321' + x + '4'
    num2 = '498' + x + '9'
    res = int(num1,19) + int(num2,19)
    if res % 23 == 0:
        print(res//23)
