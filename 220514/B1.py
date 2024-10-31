import turtle as t

t.setup(600,600)
screen = t.Screen()
screen.setworldcoordinates(-300, -300, 300, 300)

pen = t.Turtle()
def drawTriangle(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()


def drawRectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()


def drawStar(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(5):
        pen.forward(size)
        pen.left(144)
    pen.end_fill()

def drawCloud(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("grey")
    pen.begin_fill()
    for i in range(3):
        pen.circle(size)
        pen.penup()
        pen.forward(size)
        pen.pendown()
    pen.end_fill()

def drawBird(x, y, color, size):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.pencolor(color)
    pen.left(45)
    pen.forward(size)
    pen.right(90)
    pen.forward(size*2)
    pen.left(90)
    pen.forward(size*2)
    pen.right(90)
    pen.forward(size)


def drawMoon(x, y, size):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.pencolor("white")
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    pen.penup()
    pen.forward(size)
    pen.left(90)
    pen.forward(50)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

#############################################################################################
#############################################################################################
#############################################################################################























































drawMoon(0, 0, 100)
