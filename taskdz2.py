x = 2*216**6 + 3*36**9 - 432
s = ''
while x != 0:
    s += str(x%6)
    x = x//6
s = s[::-1]
print(s.count('5'))