from turtle import *

left(90)
for i in range(6):
    right(36)
    forward(10*30)
    right(36)
penup()
speed(10)
for x in range(0,19):
    for y in range(-10,10):
        goto(x*30,y*30)
        dot(3)
done()
    