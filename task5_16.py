a = []
for x in range(10,1001):
    i = int(bin(x)[3:], 2 )
    if x - i not in a:
        a.append(x-i)
print(len(a))