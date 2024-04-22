count = 0
max1 = 0
max2 = 0
f = open('task17_55.txt')
list = []
for i in f:
    list.append(int(i))
    if int(i) % 100 == 13:
        max1 = max(max1,int(i))
print(max1)
for i in range(len(list) - 2):
    s = list[i] , list[i+1] , list[i+2]
    c = 0
    for x in s:
        if 99 < x < 1000:
            c += 1
    if c == 2 and sum(s) <= max1:
        count += 1
        max2 = max(max2, list[i] + list[i + 1] + list[i + 2])
print(count, max2)


