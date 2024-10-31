# Bài tập 5: Trong màn hình hiển thị turtle graphics, vẽ cây hoặc nhà tuỳ theo người dùng chọn. VD: người dùng điền “tree” thì vẽ cây, điền “house” thì vẽ nhà, nếu điền bất cứ điều gì khác thì vẽ cả 2.


import turtle as t

while True:
    player = input("Draw a tree or a house? (or exit). "). lower()
    t.Turtle()
    if player == "tree":
        t.speed(10)
        t.clear()
        t.home()
        print("Drawing trees")
        t.penup()
        t.goto(0,-200)
        t.pendown()
        t.fillcolor("brown")
        t.begin_fill()
        for i in range(2):
            t.forward(100)
            t.left(90)
            t.forward(300)
            t.left(90)
        t.end_fill()
        t.penup()
        t.goto(150,130)
        t.pendown()
        t.fillcolor("green")
        t.begin_fill()
        for i in range(13):
            t.circle(30,135)
            t.right(108)
        t.end_fill()
        t.penup()
    if player == "house":
        t.speed(10)
        t.clear()
        t.home()
        print("Drawing house")
        #House
        #house body
        t.penup()
        t.goto(-560,-500)
        t.pendown()
        t.forward(250)
        t.left(90)
        t.fillcolor("blue")
        t.begin_fill()
        for i in range(3):
            t.forward(600)
            t.right(90)
        t.end_fill()
        t.penup()
        #roof
        t.goto(-310,100)
        t.right(135)
        t.pendown()
        t.fillcolor("green")
        t.begin_fill()
        for i in range(2):
            t.forward(424)
            t.right(90)
        t.end_fill()
        t.penup()
        #door
        t.goto(-50,-450)
        t.right(135)
        t.pendown()
        t.fillcolor("red")
        t.begin_fill()
        for i in range(2):
            t.forward(200)
            t.right(90)
            t.forward(100)
            t.right(90)
        t.end_fill()
        #door bell
        t.penup()
        t.goto(40,-350)
        t.pendown()
        #t.fillcolor("yellow")
        #t.begin_fill()
        for i in range(1):
            t.circle(10)
            t.penup()
            t.goto(35,-350)
            t.pendown()
        t.end_fill()
        t.hideturtle()
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.clear()
    if player == "exit":
        print("Draw has ended")
        break
