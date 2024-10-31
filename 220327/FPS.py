import turtle as t

screen = t.Screen()
screen.tracer(0)
t.penup()
t.hideturtle()
t.goto(0,400)
t.right(90)

for i in range(99999):
    t.penup()
    t.forward(0.2)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()
    screen.update()
    t.clear()



