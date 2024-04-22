count = 0
m = 0

with open('task17_5.txt') as f:
    l = [int(i) for i in f]

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        pr = l[i] * l[j]
        if pr % 34 != 0:
            count += 1
            m = max(m, l[i] + l[j])

print(count, m)
