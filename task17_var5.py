f = open('17var05.txt')
l = []
max1 = 0
max2 = 0
count = 0
for i in f:
    l.append(int(i))
    max1 = max(max1,int(i))
print(max1)
for j in range(len(l)-1):
    if (l[j] + l[j+1]) == max1:
        count += 1
        print(l[j],l[j+1])
        max2 = max(max2,l[j]**2 + l[j+1]**2)
print(count,max2)

