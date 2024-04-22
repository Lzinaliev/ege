# -*- coding: utf-8 -*-
#print("x y z w")
#for x in range(0,2):
 #   for y in range(0,2):
  #      for z in range(0,2):
   #         for w in range(0,2):
    #            if not((x and not(y)) or (x == z) or not(w)):
     #               print(x,y,z,w)


#for n in range(1,1000):
 #   s = bin(n)[2:]
  #  if n % 2 == 0:
   #     s += '10'
    #else:
    #    s += '01'
   # r = int(s,2)
   # if r < 102:
    #    print(r)

#from turtle import *
#k = 30
#left(90)
#for i in range(4):
 #   forward(7*k)
  #  right(90)
   # forward(8*k)
    #right(90)

#penup()
#for x in range(0,10):
#    for y in range(0,10):
#        goto(x*k,y*k)
#        dot(4)
#done()

#a = 'год'
#count = 0
#for i1 in a:
#    for i2 in a:
 #       for i3 in a:
  #          for i4 in a:
   #             for i5 in a:
    #                for i6 in a:
     #                   x = i1 + i2 + i3 + i4 + i5 + i6
      #                  if x[0] in 'гд' and x[5] in 'гд':
       #                     count += 1
#print(count)

x = "1" + '0'*80
while ('10' in x) or ('1' in x):
    if '10' in x:
        x = x.replace('10','001')
    else:
        if '1' in x:
            x = x.replace('1','000')
print(x.count('0'))
