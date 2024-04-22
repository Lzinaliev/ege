#12
from turtle import *

left(90)
for i in range(4):
    forward(300)
    right(60)
    forward(300)
    right(120)
penup()
for x in range(17):
    for y in range(17):
        goto(x*30,y*30)
        dot()
done()