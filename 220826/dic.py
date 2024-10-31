market = {
    'trung': 10,
    'rau muong': 1,
    'bap ngo': 5,
    'ca chep': 1,
    'hanh la': 0.5
    }

print("So luong do an can mua la:", len(market))
print("Cac mon hang can mua la:", market.keys())
hang_hoa = "trung"
if hang_hoa in market.keys():
    print("Co mua", hang_hoa)
else:
    print("Ko mua", hang_hoa)
market["trung"] = 5
print(market)
market.pop("rau muong")
print(market)
market["rau thom"] = 2
print(market)
