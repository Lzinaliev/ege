#print("x y z w")
#for x in range(0,2):
    #for y in range(0,2):
        #for z in range(0,2):
            #for w in range(0,2):
                #if not((x and not(y)) or (y==z) or not(w)):
                    #print(x,y,z,w)


#for n in range(0,100):
    #s = bin(n)[2:]
    #s = str(s)
    #s += str(s.count('1') % 2)
    #s += str(s.count('1') % 2)
    #if int(s, 2) > 97:
        #print(n)
        #break

from turtle import *


k = 30
left(90)
for i in range(4):
    forward(10*k)
    right(270)
penup()
forward(3*k)
right(270)
forward(5*k)
right(90)
pendown()
for i in range(2):
    forward(10*k)
    right(270)
    forward(12*k)
    right(270)
penup()
for x in range(-20,11):
    for y in range(0,15):
        goto(x*k,y*k)
        dot()

done()

#c = 0
#numbers = "1234"
#for i1 in numbers:
    #for i2 in numbers:
        #for i3 in numbers:
            #for i4 in numbers:
               # for i5 in numbers:
                  #  x = i1 + i2 + i3 + i4 +i5
                  #  if x.count("1") == 2:
                  #      c += 1
#print(c)
