import random

def list_ngau_nhien(n, a ,b):
    LN = []
    for i in range(n):
        LN.append(random.randint(a, b))
    return LN

listN = list_ngau_nhien(10, 1, 100)
print(listN)

def tim_so_lon_nhat(list_can_tim):
    so_lon_nhat = list_can_tim[0]
    for i in range(1,len(list_can_tim)):
        if list_can_tim[i] > so_lon_nhat:
            so_lon_nhat = list_can_tim[i]
    return so_lon_nhat

print("So lon nhat trong danh sach tren la:", tim_so_lon_nhat(listN))

def tim_so_nho_nhat(list_can_tim):
    so_nho_nhat = list_can_tim[0]
    for i in range(1,len(list_can_tim)):
        if list_can_tim[i] < so_nho_nhat:
            so_nho_nhat = list_can_tim[i]
    return so_nho_nhat

print("So nho nhat trong danh sach tren la:", tim_so_nho_nhat(listN))
