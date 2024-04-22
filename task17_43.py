count = 0
f = open('task17_43.txt')
list = []
min1 = 100001
min2 = 100001
for i in f:
    list.append(int(i))
    if (int(i) > 99 and int(i) < 1000) and int(i) % 10 == 5:
        min1 = min(min1, int(i))
for i in range(len(list) - 1):
    if (99< list[i] <1000) != (99 < list[i+1] <1000) and ((list[i]+list[i+1]) % min1 == 0):
        count += 1
        min2 = min(min2, list[i] + list[i + 1])
print(count, min2)

