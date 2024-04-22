count = 0
max1 = -20001
list = []
f = open('17.txt')
for elem in f:
    list.append(int(elem))
for i in range(len(list) - 1):
    if list[i] % 3 == 0 or list[i+1] % 3 == 0:
        count += 1
        max1 = max(max1,list[i] + list[i+1])
print(count, max1)








