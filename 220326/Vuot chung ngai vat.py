import turtle as t
import time
import random

far = 40
boost = 0
score = 0
score_check = 0
tracer_speed = 2
pause = False
shapesize = 3

def up():
    if p.ycor() < 450:
        y = p.ycor()
        p.sety(y+40)

def down():
    if p.ycor() > -450:
        y = p.ycor()
        p.sety(y-40)

def left():
    if p.xcor() > -400:
        x = p.xcor()
        p.setx(x-40)

def right():
    if p.xcor() < 500:
        x = p.xcor()
        p.setx(x+40)

def init_position(cnv_name):
    cnv_name.fillcolor(random.choice(color))
    x = random.randint(-400, 500)
    y = 450
    cnv_name.setpos(x, y)

def move_down(cnv_name):
    global score_check
    speed = random.uniform(0.4, 1)
    cnv_name.forward(speed + boost)
    if cnv_name.ycor() < -450:
        init_position(cnv_name)
        score_check = score_check + 1
        update_score()

def update_score():
    global score_check
    global score
    global tracer_speed
    global far
    global shapesize
    if score_check == 7:
        score_check = 0
        score = score + 1
        c.clear()
        c.write("Score: " + str(score), False, "left", ("Arial", 30, "bold"))
        tracer_speed = tracer_speed + 0.5
        if score % 10 == 0:
            vc1.shapesize(shapesize+0.5)
            vc2.shapesize(shapesize+0.5)
            vc3.shapesize(shapesize+0.5)
            vc4.shapesize(shapesize+0.5)
            vc5.shapesize(shapesize+0.5)
            vc6.shapesize(shapesize+0.5)
            vc7.shapesize(shapesize+0.5)
            far = far + 2

def loss_check():
    if p.xcor() - vc1.xcor() >= -far and p.xcor() - vc1.xcor() <= far \
    and p.ycor() - vc1.ycor() >= -far and p.ycor() - vc1.ycor() <= far:
        return True
    if p.xcor() - vc2.xcor() >= -far and p.xcor() - vc2.xcor() <= far \
    and p.ycor() - vc2.ycor() >= -far and p.ycor() - vc2.ycor() <= far:
        return True
    if p.xcor() - vc3.xcor() >= -far and p.xcor() - vc3.xcor() <= far \
    and p.ycor() - vc3.ycor() >= -far and p.ycor() - vc3.ycor() <= far:
        return True
    if p.xcor() - vc4.xcor() >= -far and p.xcor() - vc4.xcor() <= far \
    and p.ycor() - vc4.ycor() >= -far and p.ycor() - vc4.ycor() <= far:
        return True
    if p.xcor() - vc5.xcor() >= -far and p.xcor() - vc5.xcor() <= far \
    and p.ycor() - vc5.ycor() >= -far and p.ycor() - vc5.ycor() <= far:
        return True
    if p.xcor() - vc6.xcor() >= -far and p.xcor() - vc6.xcor() <= far \
    and p.ycor() - vc6.ycor() >= -far and p.ycor() - vc6.ycor() <= far:
        return True
    if p.xcor() - vc7.xcor() >= -far and p.xcor() - vc7.xcor() <= far \
    and p.ycor() - vc7.ycor() >= -far and p.ycor() - vc7.ycor() <= far:
        return True
    return False


v = t.Turtle()
v.hideturtle()
def pause_check():
    global pause
    if pause == False:
        pause = True
        v.penup()
        v.goto(0,0)
        v.pendown()
        v.pencolor("white")
        v.write("Paused!", False, "center",("Arial",50,"bold"))
        v.penup()
        v.goto(0,-50)
        v.pendown()
        v.write("Press p to continue", False, "center",("Arial",30,"bold"))
        v.penup()
    else:
        pause = False
        v.clear()



def den():
    e = t.Turtle()
    e.hideturtle()
    e.speed(0)
    for i in range(1):
        e.goto(150,350)
        e.fillcolor("yellow")
        e.begin_fill()
        e.circle(40)
        e.end_fill()
        time.sleep(1)
        e.clear()
        e.penup()
        e.goto(250, 350)
        e.pendown()
        e.fillcolor("red")
        e.begin_fill()
        e.circle(40)
        e.end_fill()
        time.sleep(1)
        e.clear()
        e.penup()
        e.goto(350, 350)
        e.pendown()
        e.fillcolor("green")
        e.begin_fill()
        e.circle(40)
        e.end_fill()
        time.sleep(1)
        e.clear()
    e.goto(250, 350)
    e.pendown()
    e.pencolor("white")
    e.write("Go!", False, "Center",("Arial",50,"bold"))
    time.sleep(1)
    e.clear()

t.bgcolor("black")
t.screensize()
t.speed(0)
screen = t.Screen()
screen.tracer(1)

# Player
p = t.Turtle()
p.shape("turtle")
p.shapesize(2)
p.fillcolor("blue")
p.penup()
p.left(90)
p.goto(0, -430)
t.onkeypress(up, "Up")
t.onkeypress(down, "Down")
t.onkeypress(left, "Left")
t.onkeypress(right, "Right")
t.onkeypress(pause_check, "p")
t.listen()

# Draw
c = t.Turtle()
c.hideturtle()
c.fillcolor("red")
c.penup()
c.goto(-550,430)
c.pencolor("cyan")
c.pendown()
c.write("Score: " + str(score), False, "left",("Arial",30,"bold"))


# Den
den()

# Tao chuong ngai vat
vc1 = t.Turtle()
vc1.hideturtle()
vc1.shape("square")
color = ("red", "blue", "skyblue", "purple", "yellow", "green", "brown")
vc1.speed(0)
vc1.shapesize(shapesize)
vc1.penup()
vc1.right(90)

vc2 = vc1.clone()
vc3 = vc1.clone()
vc4 = vc1.clone()
vc5 = vc1.clone()
vc6 = vc1.clone()
vc7 = vc1.clone()

init_position(vc1)
init_position(vc2)
init_position(vc3)
init_position(vc4)
init_position(vc5)
init_position(vc6)
init_position(vc7)

vc1.showturtle()
vc2.showturtle()
vc3.showturtle()
vc4.showturtle()
vc5.showturtle()
vc6.showturtle()
vc7.showturtle()


while True:
    if pause == False:
        screen.tracer(tracer_speed)
        move_down(vc1)
        move_down(vc2)
        move_down(vc3)
        move_down(vc4)
        move_down(vc5)
        move_down(vc6)
        move_down(vc7)
        boost = boost + 0.000001
        loss = loss_check()
        if loss == True:
            g = t.Turtle()
            g.hideturtle()
            g.penup()
            g.goto(0,0)
            g.pencolor("white")
            g.write("GAME OVER!", False, "Center",("Arial",50,"bold"))
            print("Game over")
            break
    else:
        screen.update()
