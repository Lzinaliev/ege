from turtle import *

left(90)
k = 10
for i in range(7):
    seth(0)
    circle(-4*k,180)
    seth(-90)
    circle(-4 * k, 180)
    seth(-180)
    circle(-4 * k, 180)
    seth(-270)
    circle(-4 * k, 180)
penup()
for x in range(-15,6):
    for y in range(-15,10):
        goto(x*k,y*k)
        dot(3)
done()
print("ответ 153")