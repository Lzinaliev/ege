count = 0
m = 0

with open('task17_5.txt') as f:
    lst = [int(i) for i in f]

length = len(lst)
for i in range(length - 1):
    for j in range(i + 1, length):
        if lst[i] * lst[j] % 10 == 0:
            count += 1
            m = max(m, lst[i] + lst[j])

print(count, m)
