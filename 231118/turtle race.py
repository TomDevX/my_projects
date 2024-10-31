from turtle import *
import random as ran
import time as tim
Random11=0
Random12=0
Random13=[]
Random14=0
tgtong=[0,0,0,0,0]
t1=Pen()
t2=Pen()
t3=Pen()
t4=Pen()
t5=Pen()
sc=Screen()
sc.bgcolor('black')
colors=["red","blue","yellow","green","white"]
sc.setworldcoordinates(-2000,-2000,2000,2000)
sc.title('đua rùa')
l=[t1,t2,t3,t4,t5]
tu=Pen()
tu.hideturtle()
tu.up()
tu.sety(900)
tu.color('white')
tu.write('đua rùa',move=False,align='center',font=('Arial',20,'normal'))
tu.clear()
tu.speed(0)
for i in range(len(l)):
    l[i].lt(90)
def re(x,y):
    #setup
    t=tim.time()
    hang=1
    L2=[0,0,0,0,0]
    for i in range(len(l)):
        l[i].clear()
        l[i].speed(0)
        l[i].shape("turtle")
        l[i].color(colors[i])
        l[i].pu()
        l[i].goto(-1950+(i*800),-1800)
        l[i].showturtle()
    for i in range(5,0,-1):
        tu.write(i,move=False,align='center',font=('Arial',20,'normal'))
        tim.sleep(1)
        tu.clear()
    tu.goto(0,1900)
    tu.clear()
        #chạy
    for _ in range(2801):
        if _%50==0:
            tu.clear()
            Random13=[]
            Random11=ran.randint(0,4)
            Random14=ran.randint(1,4)
            for j in range(Random14):
                Random12=ran.randint(0,4)
                Random13.append(Random12)
            while l[Random11].isvisible()==False:
                Random11=ran.randint(0,4)
            tu.color(colors[Random11])
            tu.pd()
            tu.begin_fill()

tu.circle
(50)
            tu.end_fill()
            #xét xem có đến đích chưa
        for i in range(len(l)):
            for j in range(len(Random13)):
                if i==Random13[j]:
                    if l[i].ycor()>-1800:
                        l[i].bk(ran.randint(1,3))
            if i==Random11:
                l[i].fd(ran.randint(12,16))
            for j in range(len(l)):
                if l[i].ycor()>=1800 and L2[i]==0:
                    l[i].write(('thời gian',format(tim.time()-t,".5f")),move=False,align='center',font=('Arial',10,'normal'))
                    tgtong[i]+=tim.time()-t
                    l[i].fd(200)
                    l[i].write(('hạng:',hang,),move=False,align='center',font=('Arial',10,'normal'))
                    hang+=1
                    L2[i]+=1
                    l[i].hideturtle()
            if hang==6:
                return
asd=int(input())
for jiij in range(asd):
    re(1,1)
print(*tgtong)
tgcopy=[]
for i in tgtong:
    tgcopy.append(i)
tgcopy.sort()
for i in range(5):
    print("top",i+1 ,colors[tgtong.index(tgcopy[i])],"với",format(tgcopy[i],".5f"),"giây")
