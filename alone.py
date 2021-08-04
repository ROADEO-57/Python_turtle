import turtle as t
t.bgcolor("black")
t.speed(0)
t.width(12)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color("red", "red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()

t.penup()
t.pencolor("yellow")
t.goto(0, 0)
t.write("L O V E", 'false', 'center',  font=('Cooper', 50))


t.penup()
t.goto(-270, 80)
t.setheading(0)
t.pendown()

heart()

t.penup()
t.goto(300, -70)
t.setheading(0)
t.pendown()

heart()

t.penup()
t.goto(-400, -190)
t.setheading(0)
t.pendown()


heart()

t.penup()
t.goto(-70, -200)
t.setheading(0)
t.pendown()


heart()

t.penup()
t.goto(190, 130)
t.setheading(0)
t.pendown()


heart()
t.penup()
t.pencolor("cyan")
t.goto(-150, 0)
t.write("A", 'false', 'center', font=('Cooper', 50))

t.penup()
t.pencolor("cyan")
t.goto(5, 0)
t.write("I", 'false', 'center', font=('Cooper', 50))

t.pencolor("black")
t.penup()
t.goto(0, 170)
t.pendown()

for zigzag in range(3):
    t.left(75)
    t.forward(25)
    t.right(65)
    t.forward(40)


t.done()
