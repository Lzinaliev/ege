x = 49**10 + 7**30 - 49
s = ''
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]
print(s.count("6"))