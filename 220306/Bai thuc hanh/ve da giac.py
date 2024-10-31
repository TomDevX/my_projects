import turtle as t
import time

t.screensize()
t.shape("turtle")

# Ve hinh ngu giac
t.pensize(5)
t.pencolor("yellow")
t.fillcolor("red")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.left(72)
    time.sleep(2)
t.end_fill()
t.hideturtle()
t.exitonclick()
