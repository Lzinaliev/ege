max = 0
min = 0

for i in range(568023,569230):
    k = 0
    for deli in range(2,int(i**0.5)+1):
        if i % deli == 0:
            k += 2
    if k>max:
        max=k
        min=i
print(max,min)