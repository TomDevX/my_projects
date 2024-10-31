hello = {
    "race" : "dua",
    "popular" : "pho bien",
    "hi" : "chao",
    "bye" : "tam biet",
    "great" : "tuyet voi",
    "food" : "do an",
    "fruit" : "trai cay",
    "drinks" : "do uong"
}

key = input("Tu ban can tra: ").lower()
if key in hello.keys():
    print("Nghia cua tu", key, "la", hello[key])
else:
    print("Tu nay khong co trong tu dien")
