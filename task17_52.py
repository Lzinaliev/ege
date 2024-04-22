count = 0
max1 = -1000001
min1 = 0
f = open('task17_52.txt')
list = []
for i in f:
    list.append(int(i))
    if abs(int(i)) % 100 == 13:
        max1 = max(max1, int(i))
for i in range(len(list)-2):
    s = list[i], list[i+1], list[i+2]
    c = 0
    for x in s:
        if 99 < abs(x) < 1000:
            c += 1
    if c == 2 and sum(s) < max1:
        count += 1
        min1 = min(min1, sum(s))
print(count,min1)