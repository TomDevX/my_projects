# Write your code here :-)
import turtle as t
t.bgcolor("Black")
t.pencolor("white")
t.speed(0)
name = (t.textinput("Tên", "Nhập họ và tên"))

sides = int(t.numinput("Số cạnh xoắn ốc", "Nhập số cạnh xoắn ốc", 5, 2, 6))
for x in range(100):
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(name, False, "center", ("Arial", int((x+4)/4), "bold"))
    t.left(360/sides +2)
t.exitonclick()
