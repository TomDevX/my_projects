#Bài tập 1: Nhập số tự nhiên N từ bàn phím. Tính Sum = 2 + 4 + 6 + …. + (2*N)
N = input("Nhap so N= ")
sum = 0
for i in range(2, 2*int(N) + 1, 2):
    sum = sum + i
print("Ket qua la: ", sum)
