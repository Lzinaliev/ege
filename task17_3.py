count = 0
max1 = 0
list = []
f = open('12345.txt')
for el in f:
    list.append(int(el))
for i in range(len(list) - 1):
    if (list[i] - list[i + 1]) % 2 == 0 and (list[i] % 31 == 0 or list[i + 1] % 31 == 0):
        count += 1
        max1 = max(max1, list[i] + list[i + 1])
print(count, max1)