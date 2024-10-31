# Write your code here :-)
import turtle as t
t.bgcolor("Black")
t.pencolor("yellow")
name = (t.textinput("Tên", "Nhập họ và tên"))
add = ("Chúc một ngày tốt lành")
t.write((add + ", " + name), False, "center", ("Arial", 50, "bold"))
t.hideturtle()
t.exitonclick()
