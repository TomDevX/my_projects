def find_max(a,b,c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max

def find_min(a,b,c):
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    return min

a = int(input("Nhap gia tri a: "))
b = int(input("Nhap gia tri b: "))
c = int(input("Nhap gia tri c: "))

lonnhat = find_max(a,b,c)
nhonhat = find_min(a,b,c)
print("So lon nhat la:", lonnhat)
print("So nho nhat la:", nhonhat)
