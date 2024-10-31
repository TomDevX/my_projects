# Write your code here :-)
import turtle
b = turtle.Turtle()

b.shape("turtle")
b.speed(0)

#soil
b.penup()
b.goto(-560,-400)
b.pendown()
b.fillcolor("brown")
b.begin_fill()
for i in range(2):
    b.forward(1110)
    b.right(90)
    b.forward(100)
    b.right(90)
b.end_fill()
b.fillcolor("black")
#House
#house body
b.forward(250)
b.left(90)
b.fillcolor("blue")
b.begin_fill()
for i in range(3):
    b.forward(600)
    b.right(90)
b.end_fill()
b.fillcolor("black")
b.penup()
#roof
b.goto(-310,200)
b.right(135)
b.pendown()
b.fillcolor("green")
b.begin_fill()
for i in range(2):
    b.forward(424)
    b.right(90)
b.end_fill()
b.fillcolor("black")
b.penup()
#door
b.goto(-50,-400)
b.right(135)
b.pendown()
b.fillcolor("red")
b.begin_fill()
for i in range(2):
    b.forward(200)
    b.right(90)
    b.forward(100)
    b.right(90)
b.end_fill()
b.fillcolor("black")
#door bell
b.penup()
b.goto(40,-300)
b.pendown()
b.fillcolor("yellow")
b.begin_fill()
for i in range(1):
    b.circle(10)
    b.penup()
    b.goto(35,-300)
    b.pendown()

b.end_fill()
b.hideturtle()
b.fillcolor("yellow")
b.begin_fill()
b.circle(5)
b.end_fill()
