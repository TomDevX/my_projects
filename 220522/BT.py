# Nhập vào số lượng phần tử của một mảng từ bàn phím trong đoạn [5,20].
# Các phần tử của mảng được random trong đoạn -100,100.
# 1/ Tính tổng các số chẵn
# 2/ In ra tất cả các số nguyên tố có trong mảng.
# 3/ Sắp xếp mảng trên theo thứ tự tăng dần.
# Lấy 1 phần tử để so sánh các phần tử còn lại, nếu nhỏ hơn thì đổi giá trị cho nhau (sử dụng 2 dòng for lòng ghép).
# 4/ Nếu trong mảng có từ 2 phần tử trở lên trùng nhau thì xoá các phần tử trùng nhau phía sau.
# Dùng 2 dòng for và biến check
#       [1, -10, -5, 2, 1, 5, 1]
#       [-10, -5, 1, 1, 1, 2, 5]
import random

def user_input():
    num = int(input("Nhap vao so N bat ky trong doan [5,20]: "))
    while num < 5 or num > 20:
        num = int(input("Vui long nhap lai so N bat ky trong doan [5,20]: "))
    return num

def random_element(list_name, length):
    for i in range(length):
        ran_num = random.randint(-100 , 100)
        list_name.append(ran_num)

def total_even(list_name):
    sum = 0
    for i in range(len(list_name)):
        if list_name[i] % 2 == 0:
            sum = sum + list_name[i]
    return sum


def prime_number(list_name):
    prime_list = []
    for i in range(len(list_name)):
        if list_name[i] < 2:
            # print("Gia tri", list_name[i], "khong phai la so nguyen to")
            continue
        elif list_name[i] == 2:
            # print("Gia tri", list_name[i], "la so nguyen to")
            prime_list.append(list_name[i])
        else:
            check = True
            for x in range(2 , list_name[i]):
                if list_name[i] % x == 0:
                    # print("Gia tri", list_name[i], "khong phai la so nguyen to")
                    check = False
                    break
            if check == True:
                # print("Gia tri", list_name[i], "la so nguyen to")
                prime_list.append(list_name[i])
    return prime_list

def sort(list_name):
    for i in range(len(list_name)):
        for j in range(i, len(list_name)):
            if list_name[i] > list_name[j]:
                list_name[i], list_name[j] = list_name[j], list_name[i]
    return list_name


if __name__ == "__main__":
    N = user_input()
    random_list = []
    random_element(random_list, N)
    print(random_list)

    total = total_even(random_list)
    print("Tong cac so chan trong list:", total)

    prime_list = prime_number(random_list)
    print("Danh sach so nguyen to co trong mang tren la:", prime_list)

    sort_list = sort(random_list)
    print("Danh sach da duoc sap xep theo thu tu tang dan:", sort_list)
