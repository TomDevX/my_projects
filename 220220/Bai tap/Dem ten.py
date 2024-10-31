# Bài tập 3: Nhập vào họ và tên của mình. Đếm có bao nhiêu ký tự trong choỗi ký tự đã nhập. VD: Nhập “Nguyen Van A” -> Số ký tự là 12
name = input("Nhap ho ten cua ban: ")
print("Ten cua ban la: ", name)
counter = 0
for i in name:
    counter = counter + 1
print("So ky tu trong ten ban la: ", counter)

