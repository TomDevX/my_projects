import random

random_list = []
def random_number():
    for i in range(10):
        randomN = random.randint(1,100)
        random_list.append(randomN)

def max_number(list_name):
    max_num = list_name[0]
    for i in range(len(list_name)):
        if max_num < list_name[i]:
            max_num = list_name[i]
    return max_num

def min_number(list_name):
    min_num = list_name[0]
    for i in range(len(list_name)):
        if min_num > list_name[i]:
            min_num = list_name[i]
    return min_num



if __name__ == "__main__":
    random_number()
    print("Danh sach so ngau nhien la:", random_list)
    max_number = max_number(random_list)
    print("So lon nhat trong danh sach la:", max_number)
    min_number = min_number(random_list)
    print("So nho nhat trong danh sach la:", min_number)
