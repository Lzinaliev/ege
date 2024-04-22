from turtle import *

left(90)
for i in range(6):
    forward(300)
    right(60)
penup()
speed(10)
for x in range(0,19):
    for y in range(-5,19):
        goto(x*30,y*30)
        dot(4)
done()