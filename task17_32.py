f = open('17.txt')
s = 0
maxsum = 0
count = 0
g = 0
list = []
for i in f:
    list.append(int(i))
    if int(i) % 2 != 0:
        s += int(i)
        count += 1
avr = s / count
for a in range(len(list) -1):
    if ((list[a] % 5 == 0) or (list[a + 1] % 5 == 0)) and ((list[a] < avr) or (list[a + 1] < avr)):
        g += 1
        maxsum = max(maxsum, list[a] + list[a + 1])
print(g , maxsum)


