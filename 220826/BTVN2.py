tu_dien = {
    "book" : "cuon sach",
    "pencil": "but chi",
    "pen" : "but bi",
    "eraser" : "gom",
    "ruler" : "cay thuoc"
}

word = input().lower()
check = False
for i in tu_dien.keys():
    if i == word:
        print("Nghia cua tu", word, "la", tu_dien[word]+".")
        check = True
if not check:
    print("Tu", word, "khong co trong tu dien.")
