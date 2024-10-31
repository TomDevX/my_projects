# Bài tập 4: Nhập họ và tên của mình và in ra màn hình hiển thị turtle graphics với kích cỡ 30 và màu đỏ.
import turtle as t
t.bgcolor("Black")
t.pencolor("red")
name = (t.textinput("Tên", "Nhập họ và tên"))

t.write(name, False, "center", ("Arial", 30, "bold"))
t.hideturtle()
t.exitonclick()

