#for a in range(0,301):
#    k = 0
#    for x in range(0,301):
#        for y in range(0,301):
#            if (x>=a) or (y >= a) or (x * y <= 270):
#                k += 1
#    if k == 301*301:
#        print(a)

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n-1) * f(n-1)

print(f(123)//f(120))