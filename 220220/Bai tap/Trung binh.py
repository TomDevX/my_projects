# Bài tập 2: Nhập số tự nhiên N từ bàn phím. Tính trung bình cộng của N số tự nhiên. VD: N=5 -> (1 + 2 + 3 + 4 + 5) / 5
N = int(input("Nhap vao N = "))
sum = 0
for i in range(N+1):
    sum = sum + i

TB = sum/N
print("Gia tri trung binh la: ", TB)
