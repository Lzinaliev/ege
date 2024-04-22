count = 0
max1 = 0
max2 = 0

f = open('task17_1323.txt')
for i in f:
    list.append(int(i))
    if int(i) % 100 == 19:
        max1 = max(max1, int(i))

