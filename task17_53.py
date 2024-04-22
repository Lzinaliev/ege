count = 0
max1 = -10001
list = []
min1 = 10001
f = open('task17_53.txt')
for i in f:
    list.append(int(i))
    if abs(int(i)) % 100 == 24:
        max1 = max(max1, int(i))
for i in range(len(list) -2 ):
    s = list[i], list[i+1], list[i + 2]
    c = 0
    for x in s:
        if 99 < abs(x) < 1000:
            c += 1
    if c == 1 and sum(s) > max1:
        count += 1
        min1 = min(min1, sum(s))
print(count, min1)