#print('x y z w')
#for x in range(0,2):
 #   for y in range(0,2):
  #      for z in range(0, 2):
   #         for w in range(0, 2):
        #           if not(not(x) and not(y) or (y == z) or not(w)):
    #            print(x,y,z,w)


for n in range(1,100):
    s = str(bin(n)[2:])
    for i in range(len(s)):
        sum = s[i] + s[i+1]
        print(sum)


