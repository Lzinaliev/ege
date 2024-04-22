f = open('107_17.txt')
c = 0
min = 100001
list = []
max1 = 0
for i in f:
    list.append(int(i))
    if int(i) < min and int(i) % 21 == 0:
        min = int(i)
for a in range(len(list)-1):
    if (list[a] % min == 0) or (list[a + 1] % min == 0):
        c += 1
        max1 = max(max1, list[a] + list[a+1])

print(c,max1)



