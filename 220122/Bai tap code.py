# Write your code here :-)
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.goto(0,0)
for i in range(7):
    t.right(51.42)
    t.forward(100)
t.penup()
t.forward(260)
t.pendown()
for i in range(6):
    t.forward(125)
    t.right(60)
t.penup()
t.backward(760)
t.pendown()
for i in range(5):
    t.forward(150)
    t.right(72)
