import random

random_list = []

def random_number_list(SL):
    for i in range(SL):
        random_number = random.randint(1,100)
        random_list.append(random_number)

def sum_calculator(list_name):
    sum_num = 0
    for i in range(len(list_name)):
        sum_num = sum_num + list_name[i]
    return sum_num

def sub_calculator(list_name):
    sub_num = list_name[0]
    for i in range(1, len(list_name)):
        sub_num = sub_num - list_name[i]
    return sub_num

def mul_calculator(list_name):
    mul_num = list_name[0]
    for i in range(1, len(list_name)):
        mul_num = mul_num * list_name[i]
    return mul_num

def sort(list_name):
    for i in range(len(list_name)):
        for x in range(len(list_name)):
            if list_name[i] < list_name[x]:
                list_name[i], list_name[x] = list_name[x], list_name[i]
    return list_name

def random_number(answer, list_name):
    i = 0
    check = False
    while i < len(list_name):
        if answer == list_name[i]:
            list_name.pop(i)
            check = True
        else:
            i = i + 1
    if check == False:
        list_name.append(answer)
    return list_name

if __name__ == "__main__":
    N = int(input("Nhap so luong phan tu co trong danh sach: "))
    random_number_list(N)
    print("Danh sach so ngau nhien:", random_list)
    sum_number = sum_calculator(random_list)
    print("Tong cac so trong danh sach:", sum_number)
    sub_number = sub_calculator(random_list)
    print("Hieu cac so trong danh sach:", sub_number)
    mul_num = mul_calculator(random_list)
    print("Tich cac so trong danh sach:", mul_num)
    x = int(input("Nhap 1 so bat ky: "))
    random_num = random_number(x, random_list)
    print("Danh sach da xoa/them phan tu", x, "la:", random_num)
    sort_num = sort(random_list)
    print("Danh sach theo thu tu tang dan:", sort_num)
