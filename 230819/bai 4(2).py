import turtle as t

t.speed(0)
t.bgcolor("black")
color = ["yellow", "red", "pink", "blue", "green", "orange"]
for z in range(250):
    t.pencolor(color[z%6])
    t.forward(z)
    t.left(59)
