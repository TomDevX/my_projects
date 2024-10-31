import turtle as t
import time
import random

t.screensize()
t.speed(0)
t.shape("turtle")
c = t.Turtle()

t.hideturtle()
c.hideturtle()

# mau ngau nhien
mau = "red", "yellow", "green"
ranco = random.choice(mau)
ranco2 = random.choice(mau)
ranco3 = random.choice(mau)

# ve khung
c.penup()
c.goto(-180,-10)
c.fillcolor("black")
c.begin_fill()
c.pendown()
c.forward(360)
c.left(90)
c.forward(100)
c.left(90)
c.forward(360)
c.left(90)
c.forward(100)
c.end_fill()

so = t.numinput("So lan nhap nhay", "Nhap so lan nhap nhay (1-100)", 10, 1, 100)



for i in range(int(so)):
    t.goto(-100, 0)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    time.sleep(1)
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    time.sleep(1)
    t.clear()
    t.penup()
    t.goto(100,0)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    time.sleep(1)
    t.clear()



t.goto(-200, 0)
t.fillcolor("green")
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.goto(200,0)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(40)
t.end_fill()
