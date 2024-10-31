a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a<b+c or b<a + c or c<a+b:
    print("Có thể vẽ được hình tam giác với 3 số này")
    if a == b and a == c:
        print("Tam giác này là tam giác đều")
    elif b == c or a == b or a == c:
        print("Tam giác này là tam giác cân")
    elif a**2 == b**2+c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
        print("Tam giác này là tam giác vuông")
    else:
        print("Tam giác này là tam giác thường")
else:
    print("Không thể vẽ hình tam giác bằng 3 số này")

