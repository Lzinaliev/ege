#№5
#print("x y z")
#for x in range(0,2):
    #for y in range(0,2):
        #for z in range(0,2):
            #if not((x or y) <= (z == x)):
               # print(x,y,z)


#№5
for n in range(0,256):
    s = bin(n)[2:]
    s = str(s)
    if len(s) < 8:
        s = '0' * (8 - len(s)) + s
    s = s.replace('1','2')
    s = s.replace('0', '1')
    s = s.replace('2', '0')
    r = int(s,2)
    if r - n == 111:
        print(n)


#№6
#from turtle import *
#k = 30
#left(90)
#for i in range(4):
    #forward(12*k)
    #right(150)
    #forward(12*k)
    #right(30)
#penup()
#for x in range(0,8):
    #for y in range(-10,14):
        #goto(x*k,y*k)
        #dot()
#done()

#№8
#num = '12345'
#c = 0
#for i1 in num:
    #for i2 in num:
        #for i3 in num:
            #for i4 in num:
                #for i5 in num:
                   # x = i1 + i2 + i3 + i4 + i5
                    #if x.count('1')== 3:
                       # c += 1
#print(c)
