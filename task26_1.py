f = open('26.txt')
l = f.readlines()
count = 0
for i in range(len(l)):
    l[i] = int(l[i])
l.sort(reverse=True)
l1 = [l[1]]
for i in l:
    if l1[-1] - i >= 8:
        l1.append(i)

print(len(l1),min(l1))
