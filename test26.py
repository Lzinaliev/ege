f = open('26.txt')
l = f.readlines()
for i in range(len(l)):
    l[i] = int(l[i])
l1 = [l[i]]
l.sort(reverse=True)
count = 0
for i in range(len(l)-1):
    if l[i] >= int(l[i+1])-8:
        l1.append(l[i+1])
for j in range(len(l1)-1):
    if l[j] != l[j+1]:
        print(l1)
        count += 1
print(count)


