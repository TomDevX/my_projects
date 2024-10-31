# Write your code here :-)
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(10)
turtle.title("o to & ngoi sao")
turtle.bgcolor("sky blue")
# Car's body
t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.backward(300)
t.right(135)
t.forward(250)
t.left(135)
t.forward(100)
t.right(90)
t.circle(60, -180)
t.right(90)
t.forward(300)
t.right(90)
t.circle(60, -180)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(77)
t.left(90)
t.forward(180)
t.end_fill()
t.fillcolor("black")
t.penup()
# Wheels
# Wheel 1
t.goto(205, -125)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(55)
t.penup()
t.goto(205, -140)
t.pendown()
t.circle(40)
t.end_fill()
# Wheel 2
t.penup()
t.goto(-216, -125)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(55)
t.penup()
t.goto(-216, -140)
t.pendown()
t.circle(40)
t.end_fill()
t.penup()
# Window
t.goto(-200, -80)
t.right(180)
t.pendown()
t.fillcolor("purple")
t.begin_fill()
for i in range(2):
    t.forward(400)
    t.left(90)
    t.forward(70)
    t.left(90)
t.end_fill()
t.fillcolor("black")
t.penup()
# Star
t.goto(400, 300)
t.color("black")
t.pensize(3)
t.pendown()

angle = 150
side = 30
pointies = 5
ROTATION = 360 / pointies

angle_left = angle
angle_right = angle
t.fillcolor("yellow")
t.begin_fill()


for p in range(pointies):
    t.forward(side)
    t.right(angle_right)
    t.forward(side)
    t.left(angle_left)
    t.right(ROTATION)

t.end_fill()
t.penup()
t.home()
#Tree
t.goto(-450,-200)
t.left(90)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-350,300)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for i in range(13):
   t.circle(30,135)
   t.right(108)
t.end_fill()
t.hideturtle()
t.penup()
t.home()
turtle.exitonclick()
