from turtle import *

left(90)
for i in range(4):
     forward(8*30)
     right(150)
     forward(8*30)
     right(30)
penup()
for x in range(0,11):
    for y in range(-11,11):
        goto(x*30,y*30)
        dot(4)
done()
