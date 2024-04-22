#27
from turtle import *

left(90)

for i in range(4):
    forward(12*30)
    right(90)
right(30)
for g in range(3):
    forward(8*30)
    right(60)
    forward(8*30)
    right(120)
penup()
speed(10)
for x in range(0,13):
    for y in range(0,13):
        goto(x*30,y*30)
        dot(4)
done()



