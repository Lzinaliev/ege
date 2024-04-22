count1 = 0
f = open('task17_51.txt')
list = []
min1 = 100000000
max2 = 0
for i in f:
    list.append(int(i))
    if abs(int(i)) % 100 == 15:
        max2 = max(max2, int(i))
for i in range(len(list) - 2):
    count2 = 0
    x = list[i], list[i+1], list[i+2]
    for t in x:
        if 1000 <= abs(t) < 10000:
            count2 += 1
    if count2 == 1 and ((list[i] + list[i+1] + list[i+2]) < max2):
        count1 += 1
        min1 = min(min1, list[i] + list[i + 1] + list[i + 2])
print(count1, min1)

