def f(x):
    l = 0
    for d in range(2,x):
         if x % d == 0:
             l = 1
             break
    if l == 0:
        return True
    else:
        return False

k = 1
for i in range(245690,245756+1):
    if f(i) == True:
        print(k,i)
    k += 1


