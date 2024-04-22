from turtle import *

left(90)
right(180)
forward(5*10)
right(90)
forward(50*10)
right(90)
forward(5*10)
for i in range(5):
    circle(-50,180)
    seth(90)
penup()
for x in range(-50,10):
    for y in range(-5,10):
        goto(x*10,y*10)
        dot(4)
done()