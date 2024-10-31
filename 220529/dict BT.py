market = {"trung" : 10, "rau muong": 1, "bap": 5, "ca chep": 1, "hanh la": 1}

length = len(market)
add = "Co tat ca " + str(length) + " mon do can mua:"
print(add)
key_list = market.keys()
for i in key_list:
    print(i)

print("")

check = False
for i in key_list:
    if i == "rau cai":
            print("Me cua Nhi can mua rau cai")
            check = True
else:
    print("Me cua Nhi khong can mua rau cai")
trung = market["trung"]
for i in key_list:
    if i == "trung":
        print("So trung can mua la:", trung)

print("")

market["trung"] = 5
print("Nha con trung nen me Nhi da giam so trung con:", trung)
market["bo rau thom"] = 1
so_luong_bo_rau = market["bo rau thom"]
adddd = "Me Nhi da quyet dinh mua them bo rau xanh, voi so luong la: " + str(so_luong_bo_rau)
print(adddd)

print("")

print("Vi hang xom da cho rau muong nen me Nhi khong can mua nua")
for i in key_list:
    if i == "rau muong":
       market.pop("rau muong")
       break
print("Danh sach do an me Nhi can mua hien tai:")
for i in key_list:
    print(i)
