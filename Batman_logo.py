import turtle as t
import math
t.fillcolor("yellow")
t.begin_fill()
t.speed(500)
t.bgcolor("#000000")
t.color("yellow")

roadeo = 20

t.left(90)
t.penup()
t.goto(-7*roadeo, 0)
t.pendown()

for a in range(7*roadeo, -3*roadeo, 1):
    x = a/roadeo
    rel = math.fabs(x)
    y = 1.5*math.sqrt((-math.fabs(rel-1))*math.fabs(3-rel)/ ((rel-1)*(3-rel)))*(
            1+math.fabs(rel-3)/(rel-3))*math.sqrt(1-(x/7)**2)+(
                4.5+0.75*(math.fabs(x-0.5)+math.fabs(x+0.5))-2.75*(
                    math.fabs(x-0.75)+math.fabs(x+0.75)))*(1+math.fabs(1-rel)/(1-rel))
    t.goto(a, y*roadeo)

for a in range(-3*roadeo, -1*roadeo-1, 1):
    x = a/roadeo
    rel = math.fabs(x)
    y = (2.71052+1.5-0.5*rel-1.35526*math.sqrt(4-(rel-1)**2))*math.sqrt(
        math.fabs(rel-1)/(rel-1))
    t.goto(a, y*roadeo)

t.goto(-1*roadeo, 3*roadeo)
t.goto(int(-0.5*roadeo), int(2.2*roadeo))
t.goto(int(0.5*roadeo), int(2.2*roadeo))
t.goto(1*roadeo, 3*roadeo)
print("Batman Logo With Python")

for a in range(1*roadeo+1, 3*roadeo+1, 1):
    x = a/roadeo
    rel = math.fabs(x)
    y = (2.71052+1.5-0.5*rel-1.35526*math.sqrt(4- (rel-1)**2))*math.sqrt(
        math.fabs(rel-1)/(rel-1))
    t.goto(a, y*roadeo)

for a in range(7*roadeo, 4*roadeo, -1):
    x = a/roadeo
    rel = math.fabs(x)
    y = (-3)*math.sqrt(1-(x/7)**2)*math.sqrt(math.fabs(rel-4)/(rel-4))
    t.goto(a, y*roadeo)

for a in range(4*roadeo, -4*roadeo, -1):
    x = a/roadeo
    rel = math.fabs(x)
    y = math.fabs(x/2)-0.0913722*x**2-3+math.sqrt(1-(math.fabs(rel-2)-1)**2)
    t.goto(a, y*roadeo)

for a in range(-4*roadeo-1, -7*roadeo-1, -1):
    x = a/roadeo
    rel = math.fabs(x)
    y = (-3)*math.sqrt(1-(x/7)**2)*math.sqrt(math.fabs(rel-4)/(rel-4))
    t.goto(a,y*roadeo)
t.end_fill()
t.penup()
t.goto(300, 300)
t.done()
