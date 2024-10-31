import turtle  as t

# Thiết lập giao diện

s = t.Screen()
s.setup(800,500)
s.setworldcoordinates(-450,-450,450,450)
s.bgcolor("black")
s.title("Game")

# Thiết lập lựa chọn
t_text = t.Turtle()
t_text.pencolor("cyan")
t_text.hideturtle()
t_text.penup()
t_text.speed(0)

t_box = t_text.clone()
t_box.pencolor("cyan")
t_box.pensize(3)

t_choice = t_text.clone()
t_choice.shape("circle")
t_choice.speed(3)
s.onscreenclick(t_choice.goto)

t_LR = t_text.clone()
t_LR.pencolor("cyan")
t_LR.pensize(3)

t_box.penup()
t_box.goto(0,-150)
t_box.pendown()
t_box.goto(0,-450)
t_box.penup()
t_box.goto(-450,-150)
t_box.pendown()
t_box.goto(450,-150)
t_box.penup()
t_box.goto(-450,-450)
t_box.pendown()
t_box.goto(450,-450)
t_box.penup()
t_box.goto(-450,-450)
t_box.pendown()
t_box.goto(-450,-150)
t_box.penup()
t_box.goto(450,-450)
t_box.pendown()
t_box.goto(450,-150)

t_LR.goto(-225, -350)
t_LR.write("LEFT", font=('', 40), align="center")
t_LR.goto(225, -350)
t_LR.write("RIGHT", font=('', 40), align="center")
