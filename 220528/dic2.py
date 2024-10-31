dictionary = {"chuot": "gao", "meo": "chuot", "tho": "unknown", "chim": "ca", "soc": "unknown"}

key_list = dictionary.keys()
check = False
for i in key_list:
    if "unknown" == dictionary[i]:
        add = "Vui long nhap phan bi thieu cua " + i + ": "
        answer = input(add)
        dictionary[i] = answer
print(dictionary)
answer2 = input("Nhap 1 con vat bat ky trong danh sach: ")
check2 = False
for i in key_list:
    if answer2 == i:
        dictionary.pop(i)
        print(dictionary)
        check2 = True
        break
if check2 == False:
    print("Khong co dong vat nay ben trong danh sach")
    chuoi = "Hay them thuc an cho " + answer2 + ": "
    thuc_an = input(chuoi)
    dictionary[answer2] = thuc_an
    print("Thanh cong them con vat vao danh sach")
    print(dictionary)


