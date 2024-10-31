diem_lop = {
    "A" : 9.5,
    "B" : 8.7,
    "C" : 7.6,
    "D" : 10.0,
    "C" : 8.0
}

print("Lop co", len(diem_lop), "HS")
print("Ten cua cac ban trong lop la:", diem_lop.keys())
Sum = 0
for diem in diem_lop.values():
    Sum = Sum + diem
DTB = Sum / len(diem_lop)
print("Diem trung binh cua cac ban trong lop la:", DTB)
