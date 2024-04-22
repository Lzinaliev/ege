#print('x y z w')
#for x in range(0,2):
  #  for y in range(0, 2):
   #     for z in range(0, 2):
        #    for w in range(0, 2):
         #       if not(y<=x) or (z<=w) or not(z):
            #        print(x,y,z,w)


for n in range(0,100):
    s = bin(n)[2:]
    sum1 = 0
    for i in s:
        sum1 = sum1 + int(i)
        if sum1 % 2 == 0:
            s = s + '0'
