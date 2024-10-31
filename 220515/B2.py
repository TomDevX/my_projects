n = int(input("Nhập số n: "))
i = 2
ok = True

while i < n:
    if n%i == 0:
        ok = False
        break
    else:
        i = i + 1
if ok == True:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")
