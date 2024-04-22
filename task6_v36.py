from turtle import *

left(90)
right(90)

for i in range(4):
    forward((4*5**0.5)*20)
    right(150)
    forward((4 * 5 ** 0.5) * 20)
    right(300)
penup()
for x in range(-13,10):
    for y in range(-14,13):
        goto(x*20,y*20)
        dot(3)
done()
