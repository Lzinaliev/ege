count = 0
f = open('task17_40.txt')
list = []
min1 = 10001
max1 = -10001
for i in f:
    list.append(int(i))
    if abs(int(i)) % 10 == 3:
        min1 = min(min1, int(i))
for i in range(len(list)-1):
    if (((list[i] < list[i+1]) and (abs(list[i]) % 10 == 3)) or ((list[i] > list[i+1]) and (abs(list[i+1]) % 10 == 3))) and (list[i]**2+list[i+1]**2 < min1**2):
        count += 1
        max1 = max(max1, list[i]**2 + list[i+1]**2)
print(count, max1)

