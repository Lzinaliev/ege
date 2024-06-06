x = 3**2020 - 3**1020 + 9**800 - 81
s = ''
while x != 0:
    s += str(x%3)
    x = x//3
s = s[::-1]
print(s.count('2'))