for N in range(1, 10000):
    string = bin(N)[2:]
    string = str(string)
    string = string.replace('0','2').replace('1','0').replace('2','1')
    string.strip("0")
    string = int(string,2)  ##перевод в десятичную
    if N-string == 999:
        print(N)
        break