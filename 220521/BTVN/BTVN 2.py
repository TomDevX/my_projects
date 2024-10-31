animals = ["tiger", "snake", "rabbit", "elephant", "eagle", "monkey", "lizard", "crocodile", "dinosaur", "whale"]
print("Dong vat duoc yeu thich:", animals)

check = False
for i in range(len(animals)):
    if animals[i] == "rabbit":
        print("")
        print("Rabbit co trong danh sach dong vat duoc yeu thich")
        check = True
        break
if check == False:
    print("")
    print("Rabbit khong co trong danh sach dong vat duoc yeu thich", "  ", "haha")

