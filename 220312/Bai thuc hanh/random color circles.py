import turtle as t
import random
import time

t.screensize()
t.speed(0)



while True:
    color = ["red", "green", "blue", "black", "cyan", "sky blue", "brown", "purple", "pink", "grey", "violet", "orange", "saddlebrown", "deepskyblue"]
    ran_color = random.choice(color)
    ran_csize = random.randint(5, 100)
    ran_x = random.randint(-500, 500)
    ran_y = random.randint(-400, 400)
    t.penup()
    t.goto(ran_x, ran_y)
    t.fillcolor(ran_color)
    t.begin_fill()
    t.pendown()
    t.circle(ran_csize)
    t.end_fill()


