info = {
        "name": "",
        "birthday": "",
        "id": "",
        "math": "",
        "physics": "",
        "chemistry": ""
    }
def check_value(answer, min_value, max_value):
    while True:
        check = True
        for i in answer:
            if i < '0' or i > '9':
                check = False
                break
        if check == True:
            answer = int(answer)
            if answer > min_value and answer < max_value:
                break
        answer = input("Nhap khong hop le, vui long nhap lai: ")
    return answer

def input_info():
    ten = input("Vui long nhap ten HS: ")
    info["name"] = ten
    ngay_sinh = input("Vui long nhap ngay sinh HS: ")
    info["birthday"] = ngay_sinh
    ma_so_HS = input("Vui long nhap ma so HS: ")
    info["id"] = ma_so_HS
    toan = check_value(input("Vui long nhap diem Toan cua HS: "), -1, 11)
    info["math"] = toan
    ly = check_value(input("Vui long nhap diem Ly cua HS: "), -1, 11)
    info["physics"] = ly
    hoa = check_value(input("Vui long nhap diem Hoa cua HS: "), -1, 11)
    info["chemistry"] = hoa

def average_3_num(num_1, num_2, num_3):
    return (num_1 + num_2 + num_3) / 3

def update_info():
    while True:
        print("1: Ten")
        print("2: Ngay sinh")
        print("3: Ma HS")
        print("4: Diem Toan")
        print("5: Diem Ly")
        print("6: Diem Hoa")
        print("7: Ket thuc")
        answer = check_value(input("Vui long nhap so ban can chinh: "), 0, 8)
        if answer == 1:
            ten = input("Vui long nhap ten HS: ")
            info["name"] = ten
        elif answer == 2:
            ngay_sinh = input("Vui long nhap ngay sinh HS: ")
            info["birthday"] = ngay_sinh
        elif answer == 3:
            ma_so_HS = input("Vui long nhap ma so HS: ")
            info["id"] = ma_so_HS
        elif answer == 4:
            toan = check_value(input("Vui long nhap diem Toan cua HS: "), -1, 11)
            info["math"] = toan
        elif answer == 5:
            ly = check_value(input("Vui long nhap diem Ly cua HS: "), -1, 11)
            info["physics"] = ly
        elif answer == 6:
            hoa = check_value(input("Vui long nhap diem Hoa cua HS: "), -1, 11)
            info["chemistry"] = hoa
        elif answer == 7:
            break

def delete_info():
    while True:
        print("1: Ten")
        print("2: Ngay sinh")
        print("3: Ma HS")
        print("4: Diem Toan")
        print("5: Diem Ly")
        print("6: Diem Hoa")
        print("7: Ket thuc")
        answer = check_value(input("Vui long chon thong tin can xoa"), -1, 8)
        if answer == 1:
            info["name"] = ""
        elif answer == 2:
            info["birthday"] = ""
        elif answer == 3:
            info["id"] = ""
        elif answer == 4:
            info["math"] = ""
        elif answer == 5:
            info["physics"] = ""
        elif answer == 6:
            info["chemistry"] = ""
        elif answer == 7:
            break

def add_info():
    change_continue = True
    while change_continue:
        answer = input("Nhap key can them moi: ")
        key_list = info.keys()
        while answer in key_list:
            answer = input("Key nay da ton tai, vui long nhap key moi: ")
        value_add = "Nhap gia tri cho thong tin " + answer + " : "
        value = input(value_add)
        info[answer] = value
        change_continue = play_again()

def play_again():
    yn = ""
    while yn != "y" and yn != "n":
        yn = input("Ban co muon tiep tuc chinh sua khong? Y/N ").lower()
    if yn == "y":
        return True
    if yn == "n":
        return False


if __name__ == "__main__":
    again = True
    while again:
        print("1: Nhap thong tin")
        print("2: Them thong tin")
        print("3: Xoa thong tin")
        print("4: Cap nhat thong tin")
        print("5: Diem trung binh Toan, Ly, Hoa")
        answer = check_value(input("Vui long nhap so ban can chinh: "), 0, 6)
        if answer == 1:
            input_info()
        elif answer == 2:
            add_info()
        elif answer == 3:
            delete_info()
        elif answer == 4:
            update_info()
        elif answer == 5:
            if info["math"] == "" or info["chemistry"] == "" or info["physics"] == "":
                print("Diem chua duoc cap nhat day du")
            else:
                average = average_3_num(info["math"], info["chemistry"], info["physics"])
                print("Diem trung binh cua 3 mon la:", average)
        print(info)
        again = play_again()
