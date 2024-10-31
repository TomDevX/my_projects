import random

'''n = int(input("Nhập số : "))
diction = {}
for i in range(1,n+1):
    diction[i]=i**3

print(diction)'''

x = random.randint(1,100)

def nguyento(k):
    dem = 0
    if k <= 1:
        return False
    else:
        for i in range(2,k):
            if k%i == 0:
                dem+=1
        if dem == 0:
            return True
        else:
            return False

def DS(x):
    ds=[]
    for i in range(0, x+1):
        if nguyento(i):
            ds.append(i)
    return ds
print(DS(x))
