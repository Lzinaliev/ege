count1 = 0
f = open('task17_57.txt')
list = []
max1 = 0
max2 = 0
for i in f:
    list.append(int(i))
    if int(i) % 100 == 17:
        max1 = max(max1, int(i))
for i in range(len(list)-2):
    s = list[i] , list[i+1] , list[i+2]
    c = 0
    delt = 0
    for t in s:
        if 999 < t < 10000:
            c += 1
        if t % 5 == 0:
            delt += 1
    if c == 2 and delt >= 1 and (list[i] + list[i + 1] + list[i + 2]) > max1:
        count1 += 1
        max2 = max(max2, list[i] + list[i + 1] + list[i + 2])
print(count1, max2)
