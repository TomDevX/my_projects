dictionary = {"house": "ngoi nha", "table": "cai ban", "flower": "bong hoa", "tree": "cai cay", "chair": "cai ghe"}
answer = input("Tra tu dien: ")

key_list = dictionary.keys()
check = False
for i in key_list:
    if answer == i:
        check = True
        break
if check == True:
    print(answer, ":", dictionary[answer])
else:
    print("Tu ngu khong ton tai")
