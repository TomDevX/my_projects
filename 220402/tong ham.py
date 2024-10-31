def tinh_tong(N):
    sum = 0
    for i in range(N+1):
        sum = sum + i
    return sum
N = int(input("Nhap gia tri N: "))

tong = tinh_tong(N)
print("Tong ", tong)
