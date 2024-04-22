from turtle import *
pensize(5)
left(90)
right(180)
forward(2*10)
right(90)
forward(40*10)
right(90)
forward(2*10)
for i in range(4):
    circle(-5*10,180)
    seth(90)
penup()
for x in range(-40,11):
    for y in range(-2,7):
        goto(x*10,y*10)
        dot(4)
done()