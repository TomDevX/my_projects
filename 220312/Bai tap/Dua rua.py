import turtle as t
import random
import time

t.screensize()
t.speed(0)

# Rua khan gia
t_gia1 = t.Turtle()
t_gia2 = t.Turtle()
t_gia3 = t.Turtle()
t_gia4 = t.Turtle()
t_gia5 = t.Turtle()
t_gia6 = t.Turtle()
t_gia1.fillcolor("brown")
t_gia2.fillcolor("violet")
t_gia3.fillcolor("skyblue")
t_gia4.fillcolor("pink")
t_gia5.fillcolor("cyan")
t_gia6.fillcolor("magenta")
t_gia1.penup()
t_gia2.penup()
t_gia3.penup()
t_gia4.penup()
t_gia5.penup()
t_gia6.penup()
t_gia1.shape("turtle")
t_gia2.shape("turtle")
t_gia3.shape("turtle")
t_gia4.shape("turtle")
t_gia5.shape("turtle")
t_gia6.shape("turtle")
t_gia1.goto(-500, 200)
t_gia2.goto(-500, 150)
t_gia3.left(180)
t_gia3.goto(500, 200)
t_gia4.left(180)
t_gia4.goto(500, 150)
t_gia5.left(90)
t_gia5.goto(500, -400)
t_gia6.left(90)
t_gia6.goto(-500, -400)


# Rua trong tai
t.hideturtle()
turtle_tai = t.Turtle()
turtle_tai.penup()
turtle_tai.goto(-580, 380)
turtle_tai.pendown()
turtle_tai.forward(1150)
turtle_tai.penup()
turtle_tai.goto(-0, 400)
turtle_tai.pendown()
turtle_tai.write("Finish!", False, "center", ("Arial", 30, "bold"))
turtle_tai.penup()
turtle_tai.goto(-470, 380)
turtle_tai.right(90)
turtle_tai.pendown()
turtle_tai.forward(1000)
turtle_tai.penup()
turtle_tai.goto(470, 380)
turtle_tai.pendown()
turtle_tai.forward(1000)
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
turtle_orange.goto(430, -400)

cuoc = t.numinput("Turtle Bet", "Choose number to bet (1-5): 1=red; 2=green; 3=blue; 4=yellow; 5=orange", "choose", 1, 5)

# Dem
tdem = t.Turtle()
tdem.shape("turtle")
tdem.penup()
tdem.goto(0, 0)
tdem.pendown()
tdem.write("3", False, "center", ("Arial", 100, "bold"))
time.sleep(1)
tdem.clear()
tdem.write("2", False, "center", ("Arial", 100, "bold"))
time.sleep(1)
tdem.clear()
tdem.write("1", False, "center", ("Arial", 100, "bold"))
time.sleep(1)
tdem.clear()
tdem.write("Go!", False, "center", ("Arial", 100, "bold"))
time.sleep(1)
tdem.clear()
tdem.hideturtle()

# Chay!
die = [1, 2, 3, 4, 5, 6]

while True:
    if turtle_red.ycor() >= 380:
        time.sleep(1)
        print("Turtle Red Wins the Race!")
        break
    elif turtle_blue.ycor() >= 380:
        time.sleep(1)
        print("Turtle Blue Wins the Race!")
        break
    elif turtle_green.ycor() >= 380:
        time.sleep(1)
        print("Turtle Green Wins the Race!")
        break
    elif turtle_yellow.ycor() >= 380:
        time.sleep(1)
        print("Turtle Yellow Wins the Race!")
        break
    elif turtle_orange.ycor() >= 380:
        time.sleep(1)
        print("Turtle Orange Wins the Race!")
        break
    else:
        turtle_red.forward(random.choice(die))
        turtle_blue.forward(random.choice(die))
        turtle_green.forward(random.choice(die))
        turtle_yellow.forward(random.choice(die))
        turtle_orange.forward(random.choice(die))

#Cuoc rua
if turtle_red.ycor() >= 380:
    if cuoc == 1:
        print("It means You win the bet!")
    else:
        print("It means You lose the bet!")
elif turtle_green.ycor() >= 380:
    if cuoc == 2:
        print("It means You win the bet!")
    else:
        print("It means You lose the bet!")
elif turtle_blue.ycor() >= 380:
    if cuoc == 3:
        print("It means You win the bet!")
    else:
        print("It means You lose the bet!")
elif turtle_yellow.ycor() >= 380:
    if cuoc == 4:
        print("It means You win the bet!")
    else:
        print("It means You lose the bet!")
elif turtle_orange.ycor() >= 380:
    if cuoc == 5:
        print("It means You win the bet!")
    else:
        print("It means You lose the bet!")

