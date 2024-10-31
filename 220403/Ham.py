import turtle as t

screen = t.Screen()

def up():
    print("ban dang an phim up")
def down():
    print("ban dang an phim down")
def left():
    print("ban dang an phim left")
def right():
    print("ban dang an phim right")

t.onkeypress(up, "Up")
t.onkeypress(down, "Down")
t.onkeypress(left, "Left")
t.onkeypress(right, "Right")
t.listen()





