for x in '0123456789abcde':
    num1 = '123'+ x + '5'
    num2 = '1'+ x + '233'
    res = int(num1,15) + int(num2,15)
    if res % 14 == 0:
        print(res // 14)
        break