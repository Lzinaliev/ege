
f = open('26_59821.txt')
l = f.readlines()
l1 = []
for i in range(len(l)):
    x,y = l[i].split()
    l1.append([int(x),i,1])
    l1.append([int(y),i,2])
l1.sort()
det = 0
count = 0
mark = [1] * len(l1)
for i in range(len(l1)):
    if mark[l1[i][1]] == 1:
        det = l1[i][1]
        if l1[i][2] == 1:
            count += 1
        mark[l1[i][1]] = 2
print(det+1,count-1)









