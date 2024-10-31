import turtle as t
import random
import time

t.screensize()

# Rua trong tai
turtle_tai = t.Turtle()
turtle_tai.penup()
turtle_tai.goto(-580, 380)
turtle_tai.pendown()
turtle_tai.forward(1150)
turtle_tai.penup()
turtle_tai.goto(-0, 400)
turtle_tai.write("Finish!", False, "center", ("Arial", 30, "bold"))
turtle_tai.hideturtle()

# Rua do
turtle_red = t.Turtle()
turtle_red.shape("turtle")
turtle_red.fillcolor("red")
turtle_red.penup()
turtle_red.left(90)
turtle_red.goto(-450, -400)

# Rua xanh la
turtle_green = t.Turtle()
turtle_green.shape("turtle")
turtle_green.fillcolor("green")
turtle_green.penup()
turtle_green.left(90)
turtle_green.goto(-230, -400)

# Rua xanh duong
turtle_blue = t.Turtle()
turtle_blue.shape("turtle")
turtle_blue.fillcolor("blue")
turtle_blue.penup()
turtle_blue.left(90)
turtle_blue.goto(130, -400)

# Rua vang
turtle_yellow = t.Turtle()
turtle_yellow.shape("turtle")
turtle_yellow.fillcolor("yellow")
turtle_yellow.penup()
turtle_yellow.left(90)
turtle_yellow.goto(230, -400)

# Rua cam
turtle_orange = t.Turtle()
turtle_orange.shape("turtle")
turtle_orange.fillcolor("orange")
turtle_orange.penup()
turtle_orange.left(90)
turtle_orange.goto(450, -400)

# Chay!
die = [1, 2, 3, 4, 5, 6]

for i in range(30):
    if turtle_red.pos() >= (-450, 380):
        print("Player Red Wins the Race!")
        break
    elif turtle_blue.pos() >= (130, 380):
        print("Player Blue Wins the Race!")
        break
    elif turtle_green.pos() >= (-230, 380):
        print("Player Green Wins the Race!")
        break
    elif turtle_yellow.pos() >= (230, 380):
        print("Player Yellow Wins the Race!")
        break
    elif turtle_orange.pos() >= (450, 380):
        print("Player Orange Wins the Race!")
        break
    else:
        die_roll = random.choice(die)
        turtle_red.forward(30 * die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        turtle_blue.forward(30 * die_roll2)
        time.sleep(1)
        die_roll3 = random.choice(die)
        turtle_green.forward(30 * die_roll3)
        time.sleep(1)
        die_roll4 = random.choice(die)
        turtle_yellow.forward(30 * die_roll4)
        time.sleep(1)
        die_roll5 = random.choice(die)
        turtle_orange.forward(30 * die_roll5)
        time.sleep(1)




