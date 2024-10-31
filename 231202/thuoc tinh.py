class square:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def print_info(self):
        print("Dien tich hcn:", self.chieudai*self.chieurong)
        print("Chu vi hcn:", (self.chieudai+self.chieurong)*2)

hcn1 = square(10, 10)
hcn2 = square(15, 10)

hcn1.print_info()
hcn2.print_info()

class phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def nhan(self, tu2, mau2):
        print("Nhan 2 phan so la:", self.tu*tu2, "/", self.mau*mau2)
    def chia(self, tu2, mau2):
        print("Chia 2 mau so:", self.tu*mau2, "/", self.mau*tu2)

phanso1 = phanso(2, 3)

phanso1.nhan(1, 2)
phanso1.chia(2,3)


