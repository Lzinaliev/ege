from t import *

left(90)
for i in range(7):
    forward(300)
    right(120)
penup()
for x in range(-11,10):
    for y in range(-11, 10):
        goto(x*30,y*30)
        dot()


done()