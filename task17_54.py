count = 0
max1 = -1000001
max2 = -1000001
list = []
f = open('task17_54.txt')
for i in f:
    list.append(int(i))
    if abs(int(i)) % 100 == 29:
        max1 = max(max1, int(i))
for i in range(len(list)-2):
    s = list[i], list[i+1], list[i+2]
    c = 0
    for x in s:
        if 9999 < abs(x) < 100000:
            c += 1
    if c == 2 and sum(s) < max1:
        count += 1
        max2 = max(max2, sum(s))
print(count, max2)