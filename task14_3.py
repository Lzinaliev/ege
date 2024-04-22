x = 9**8 + 3**5 - 9
s = ''
while x != 0:
    s += str(x % 3)
    x //= 3
s = s[::-1]
print(s.count("2"))