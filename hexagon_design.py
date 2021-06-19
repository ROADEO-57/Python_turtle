import turtle as t
from random import randint
# x for the expected circle value 1
x = 20
# variable for the expected gajurel circle 2
gajurel = 10

# the speed of the pen value 3
t.speed(40000)
t.colormode(255)

def move(l, a):
        t.right(a)
        t.forward(l)

def hex():
        t.pendown()
        t.color(randint(0, 255), randint(0, 255), randint(0, 255))
        t.begin_fill()
        for i in range(6):
                move(x, -60)
        t.end_fill()
        t.penup()

t.penup()

for roadeo in range(gajurel):
        if roadeo == 0:
                hex()
                move(x,-60)
                move(x, -60)
                move(x,-60)
                move(0, 180)
        for i in range(6):
                move(0, 60)
                for j in range(roadeo+1):
                        hex()
                        move(x, -60)
                        move(x, 60)
                move(-x, 0)
        move(-x, 60)
        move(x, -120)
        move(0, 60)

t.exitonclick()
