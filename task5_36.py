for i in range(1, 1000):
    n = i
    string = ""
    while n > 0: # перевод в троичную систему
        string += str(n % 3)
        n //= 3
    string = str(i % 3) + string
    r = 0
    for j in range(len(string)):
        r += int(string[j]) * 3 ** j
    if r > 999:
        print(r)
        break

