f = open('27A.txt')



s = f.readline()
n,k = s.split()
n = int(n)
k = int(k)

road = [0]*k
for s1 in f:
    km, benz = s1.split()
    km = int(km)
    benz = int(benz)
    reis = benz // 11
    if benz % 11 != 0:
        reis += 1
    road[km] = reis
result = 0
min_result = 10**100
result =    