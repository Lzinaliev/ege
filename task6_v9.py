from turtle import *

left(90)
for i in range(4):
    forward(70)
    right(90)
    forward(80)
    right(90)
penup()
for x in range(11):
    for y in range(11):
        goto(x*10,y*10)
        dot()
done()
print(42)