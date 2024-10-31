import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()

t.pencolor("yellow")
t.fillcolor("yellow")
def star(size, x, y):
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.setheading(0)

for i in range(20):
    size = random.randint(10, 500)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    star(size, x, y)
