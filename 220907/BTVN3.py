def so_may_man(so):
    print(so, "chia cho", 100, "du", so % 100)
    if so % 100 == 24:
        print("Day la so may man")
    else:
        print("Day khong phai la so may man")

num = int(input("Nhap so N bat ky: "))
so_may_man(num)
