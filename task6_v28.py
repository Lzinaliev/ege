from turtle import *

left(90)

for i in range(4):
    forward(10*30)
    right(90)
right(30)
for g in range(5):
    forward(6*30)
    right(60)
    forward(6*30)
    right(120)
penup()
speed(10)
for x in range(0,12):
    for y in range(0,12):
        goto(x*30,y*30)
        dot(4)
done()
