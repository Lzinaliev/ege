#2
#print('x y z w')
#for x in range(0,2):
 #   for y in range(0, 2):
  #      for z in range(0, 2):
   #         for w in range(0, 2):
    #            if not(not(w <= x) or (not(z) <= (not(y))) or (z)):
     #               print(x,y,z,w)

#5
def f4(n):
    s = ''
    while n != 0:
        s += str(n % 4)
        n = n // 4
    return s[::-1]


for n in range(1,1000):
    n4 = f4(n)
    if n % 4 == 0:
        n4 += n4[-2:]
    else:
        ost = n % 4
        ost4 = f4(ost*2)
        n4 += ost4
    r = int(n4, 4)
    if r >= 1088:
        print(n)
        break

