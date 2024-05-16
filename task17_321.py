f = open('task17_321.txt')
count = 0
min1 = 100001
l = []
max1 = -1
for i in f:
    l.append(int(i))
    if int(i) < min1 and int(i) % 19 == 0:
        min1 = int(i)
for j in range(len(l)-1):
    if (l[j] % min1 == 0) or (l[j+1] % min1 == 0):
        count += 1
        max1 = max(max1,l[j]+l[j+1])
print(count,max1)