# Write your code here :-)
import turtle
t = turtle.Turtle()
#Triangle
t.fillcolor("yellow")
t.begin_fill()
for i in range(3):
    t.forward(300)
    t.left(120)
t.end_fill()
t.fillcolor("black")

