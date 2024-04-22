count = 0
max1 = -10001
min1 = 100001
f = open('task17_42.txt')
list = []
for i in f:
    list.append(int(i))
    if i[-2] == i[-3]:
        min1 = min(min1, int(i))
for i in range(len(list)-1):
    if (abs(list[i]) % 13 == 0 and abs(list[i+1]) % 13 != 0) or (abs(list[i]) % 13 != 0 and abs(list[i+1]) % 13 == 0):
        if (list[i]**2 + list[i+1]**2 <= min1**2):
            if (str(list[i])[-1] == str(list[i+1])[-2]) or (str(list[i])[-2] == str(list[i+1])[-1]):
                count += 1
                max1 = max(max1, list[i]**2 + list[i+1]**2)
print(count, max1)



