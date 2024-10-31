import random
TP = "Tokyo", "Kyoto", "NewYork", "London", "HCM", "HaNoi", "VungTau", "NhaTrang", "DaLat", "DaNang", "Dubai", "Seoul", "Paris"


for i in range(random.randint(1, 3)):
    print("Thanh pho noi tieng ngau nhien: ", random.choice(TP))
