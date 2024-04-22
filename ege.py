#Текстовый файл состоит не более чем из 106 символов L, D и R. Определите длину самой длинной последовательности, состоящей из символов D.

a = "DLRLDRLRDRLDRLLDDDRLDDDDL"
count = 0
max_count = 0
for s in a:
    if s == "D":
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
print(max_count)

#Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

b = "XXYYXYZ"
count = 0
max_count = 0
for i in range(len(b)-1):
    if b[i] != b[i+1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
print(max_count)

#