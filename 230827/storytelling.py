import turtle as t


#set up
s = t.Screen()
s.setup(900,900)
s.setworldcoordinates(-450,-450,450,450)
s.bgcolor("Black")
s.title("Game kinh dị")
t_text = t.Turtle()
t_text.penup()
t_text.speed(0)
t_text.pencolor("cyan")
t_text.hideturtle()
t_box = t.Turtle()
t_LR = t.Turtle()

t_box = t.Turtle()
t_box.pencolor("cyan")
t_box.pensize(3)

t_choice = t.Turtle()
t_choice.shape("circle")
t_choice.pencolor("cyan")
t_choice.speed(3)
t_choice.penup()
s.onscreenclick(t_choice.goto)

t_LR = t.Turtle()
t_LR.pencolor("cyan")
t_LR.pensize(3)

t_box.speed(0)
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
t_box.hideturtle()

t_LR.speed(0)
t_LR.penup()
t_LR.goto(-225, -350)
t_LR.pendown()
t_LR.write("1", font=('', 40), align="center")
t_LR.penup()
t_LR.goto(225, -350)
t_LR.pendown()
t_LR.write("2", font=('', 40), align="center")
t_LR.hideturtle()

def YN(answer):
    while answer != "1" and answer != "2":
        print("Vui lòng chỉ nhập câu trả lời 1 hoặc 2")
        answer = str(input())
    return answer
def choice():
    if t_choice.ycor() < -150:
        if t_choice.xcor() < 0:
            t_choice.goto(0,0)
            return "1"
        elif t_choice.xcor() > 0:
            t_choice.goto(0,0)
            return "2"
    else:
        t_choice.goto(0,0)

def start():
    global a
    t_text.clear()
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Đây là game nhập vai kinh dị được làm rất dảk", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("TRÒ CHƠI BẮT ĐẦU", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("Bạn vào ngôi nhà ma ám, sau khi đi vào, cánh cửa đột nhiên đóng lại. Bạn sẽ vào thám hiểm hay tìm cách ra khỏi nhà? 1 = thám hiểm, 2 = tìm cách trốn thoát", font = ("Arial",30), align = "center")
    a = choice()
    while a == None:
        a = choice()
    t_text.clear()
    return a
    YN(a)
def first1():
    global b
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn đi vào căn phòng đầu tiên và thấy có các hung khí như: dao, súng, kiếm, vv... Chọn 1 = cầm một trong những hung khí theo, 2 = Đi thám hiểm các phòng khác.", font = ("Arial",30), align = "center")
    b = choice()
    while b == None:
        b = choice()
    t_text.clear()
    return b
    YN(b)
def second1():
    global c
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn đi vào căn phòng khác và thấy tờ ghi chú. Bạn sẽ đọc hay lờ nó? 1 = đọc, 2 = kệ", font = ("Arial",30), align = "center")
    c = choice()
    while c == None:
        c = choice()
    t_text.clear()
    return c
    YN(c)
def third1():
    global d
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Tờ ghi chú nói: 'Look behind you'. Bạn có nhìn phía sau ko? 1 = có, 2 = không", font = ("Arial",30), align = "center")
    d = choice()
    while d == None:
        d = choice()
    return d
    t_text.clear()
    YN(d)
def four1():
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Khi bạn nhìn về phía sau, bạn bị jumpscare và đầu độc bởi bóng đen", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("BAD ENDING", font = ("Arial",30), align = "center")
def five1():
    global e
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn đi ra khỏi phòng và tới cuối hành lang", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn thấy một cánh cửa thoát hiểm", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = mở cánh cửa; 2 = tiếp tục khám phá", font = ("Arial",30), align = "center")
    e = choice()
    while e == None:
        e = choice()
    return e
    t_text.clear()
    YN(e)
def six1():
    global d
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn rời khỏi phòng và đột nhiên thấy bóng đen", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = Tới chỗ bóng đen nói chuyện; 2 = Chạy", font = ("Arial",30), align = "center")
    d = choice()
    while d == None:
        d = choice()
    return d
    t_text.clear()
    YN(d)
def seven1():
    global d
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn không quan tâm đến và đi vào hành lang", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn thấy có một cái cửa sổ và nó có trèo ra được", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = trốn thoát bằng cửa sổ; 2 = tiếp tục thám hiểm", font = ("Arial",30), align = "center")
    d = choice()
    while d == None:
        d = choice()
    return d
    t_text.clear()
    YN(d)
def eight1():
    global d
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn không quan tâm đến và đi vào hành lang", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn thấy có một cái cửa sổ và nó có trèo ra được", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = trốn thoát bằng cửa sổ; 2 = tiếp tục thám hiểm", font = ("Arial",30), align = "center")
    d = choice()
    while d == None:
        d = choice()
    return d
    t_text.clear()
    YN(d)
def nine1():
    global e
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn đi tiếp và thấy được cầu thang để đi lên lầu", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = đi lên lầu; 2 = đi tìm đường khác để thám hiểm", font = ("Arial",30), align = "center")
    e = choice()
    while e == None:
        e = choice()
    return e
    t_text.clear()
    YN(e)
def ten1():
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn đi lên lầu và thấy có vật đang phát sáng", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("TO BE CONTINUE", font = ("Arial",30), align = "center")
def eleven1():
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn đi lại cái bàn gần đó và thấy một tờ giấy do chủ căn nhà để lại", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Tờ ghi chú nói: Nơi này rất nguy hiểm, tuy nhiên nó có một kho báu rất có giá trị", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("TO BE CONTINUE", font = ("Arial",30), align = "center")
def twelve1():
    global c
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn đi vào một căn phòng khác", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn gặp một xác người", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("Bạn sẽ lục soát cái xác đó hay kệ?. 1 = lục soát, 2 = kệ", font = ("Arial",30), align = "center")
    c = choice()
    while c == None:
        c = choice()
    return c
    t_text.clear()
    YN(c)

def thirteen1():
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn đã trốn thoát và còn sống nhưng không khám phá được gì", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("Neutral ending", font = ("Arial",30), align = "center")
def fourteen1():
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn đã trốn thoát và còn sống nhưng không khám phá được gì", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("Neutral ending", font = ("Arial",30), align = "center")

def first2():
    global b
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn vô một căn phòng và tìm thấy tờ giấy chỉ chỗ giấu đồ cạy cửa", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("Sau khi đi theo chỉ dẫn, bạn thấy một quả bom, có 1 dây đỏ và 1 dây xanh. Chọn 1 = cắt dây đỏ, 2 = cắt dây xanh", font = ("Arial",30), align = "center")
    b = choice()
    while b == None:
        b = choice()
    return b
    t_text.clear()
    YN(b)
def second2():
    global c
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn cắt dây đỏ và sống sót", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("Có một cánh cửa mở ra, bạn có vào ko? 1 = vào; 2 = nope", font = ("Arial",30), align = "center")
    c = choice()
    while c == None:
        c = choice()
    return c
    t_text.clear()
    YN(c)
def third2():
    global d
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn đi vào phòng và thấy đầy kho báu", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Tuy nhiên, chuông báo động reo lên và bạn đang bị truy lùng bởi 1 tên sát nhân", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = lấy thùng kho báu và chạy; 2 = kệ kho báu và chạy", font = ("Arial",30), align = "center")
    d = choice()
    while d == None:
        d = choice()
    return d
    t_text.clear()
    YN(d)
def four2():
    t_text.clear()
    t_text.goto(0,350)
    t_text.write("Bạn lấy thùng kho báu và chạy", font = ("Arial",30), align = "center")
    t_text.goto(0,400)
    t_text.write("Trong thùng kho báu có thiết bị định vị nên tên sát nhân đã sớm dí kịp bạn", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn mang đồ nặng quá nên ko chạy đc và bị giết", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("BAD ENDING", font = ("Arial",30), align = "center")
def five2():
    global e
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn chạy thật nhanh khỏi căn phòng", font = ("Arial",30), align = "center")
    t_text.goto(0,350)
    t_text.write("Bạn thấy phòng giám sát của tên sát nhân", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Trong đó toàn là những camera trong nhà", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = đập nát nó; 2 = nghiên cứu cách để thoát ra thông qua các nút bấm", font = ("Arial",30), align = "center")
    e = choice()
    while e == None:
        e = choice()
    return e
    t_text.clear()
    YN(e)
def six2():
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Bạn đập nó và cổ máy tự hủy và bạn bị chôn vùi trong toà nhà", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("BAD ENDING", font = ("Arial",30), align = "center")
def seven2():
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn thấy nút báo cháy và ấn nó", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Tất cả cửa đều mở ra và bạn trốn thoát thành công", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("GOOD ENDING", font = ("Arial",30), align = "center")
def eight2():
    t_text.goto(0,400)
    t_text.write("Bạn đi ra khỏi phòng và đi tới cuối hành lang", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn thấy cái điện thoại", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("1 = gọi cho người tới cứu; 2 = tiếp tục tìm đường thoát", font = ("Arial",30), align = "center")
    e = choice()
    while e == None:
        e = choice()
    return e
    t_text.clear()
    YN(e)
def nine2():
    t_text.clear()
    t_text.goto(0,300)
    t_text.write("Có người tới cứu bạn và bạn bình an vô sự rời khỏi đó", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("GOOD ENDING", font = ("Arial",30), align = "center")
def ten2():
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn đi tìm đường khác để trốn thoát nhưng bị tên sát nhân tìm thấy", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn bị bắt và bị nhốt", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("TO BE CONTINUE", font = ("Arial",30), align = "center")
def eleven2():
    t_text.clear()
    t_text.goto(0,400)
    t_text.write("Bạn đi tìm đường khác để trốn thoát nhưng bị tên sát nhân tìm thấy", font = ("Arial",30), align = "center")
    t_text.goto(0,300)
    t_text.write("Bạn bị bắt và bị nhốt", font = ("Arial",30), align = "center")
    t_text.goto(0,200)
    t_text.write("TO BE CONTINUE", font = ("Arial",30), align = "center")

start()
if a == "1":
    first1()
    if b == "1":
        second1()
        if c == "1":
            third1()
            if d == "1":
                four1()
            elif d == "2":
                five1()
                if e == "1":
                    thirteen1()
                elif e == "2":
                    fourteen1()
            elif c == "2":
                six1()
        elif c == "2":
            seven1()
            if d == "1":
                eight1()
            elif d == "2":
                nine1()
                if e == "1":
                    ten1()
                elif e == "2":
                    eleven1()
    elif b == "2":
            twelve1()
elif a == "2":
    first2()
    if b == "1":
        second2()
        if c == "1":
            third2()
            if d == "1":
                four2()
            elif d == "2":
                five2()
                if e == "1":
                    six2()
                if e == "2":
                    seven2()
        elif c == "2":
            eight2()
            if e == "1":
                nine2()
            elif e == "2":
                ten2()
    elif b == "2":
        eleven2()


