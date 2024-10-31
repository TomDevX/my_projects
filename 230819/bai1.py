x = int(input("Nhập số bất kỳ: "))
sum = 0
while not (x >= 50 and x <= 200):
    print("Please enter again")
    x = int(input("Nhập số bất kỳ: "))
for i in range(5, x+1, 5):
        sum = sum + i
print(sum)
