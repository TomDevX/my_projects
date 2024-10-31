lop_9A = ["Hoang Manh Dung", "Tran Van An", "Nguyen Thi Man", "Huynh Thai Son"]

for i in range(len(lop_9A)):
    print(lop_9A[i])

HSG = lop_9A[2]
print("Ban HS", HSG, "la HS gioi cua lop")

vi_tri = lop_9A.index("Tran Van An")
print("Vi tri cua HS Tran Van An la:", vi_tri)

test = False
nhap = input("Nhap 1 ten bat ky: ")
for i in range(len(lop_9A)):
    if lop_9A[i] == nhap:
        lop_9A.remove(nhap)
        test = True
        break
if test == False:
    lop_9A.append(nhap)
print("Danh sach HSG lop 9A:", lop_9A)
