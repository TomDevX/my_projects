food = {
'chuot': 'gao',
'meo': 'chuot',
'tho': 'unknown',
'chim': 'ca',
'soc': 'unknown'
}

food["tho"] = "carrot"
food["soc"] = "hat de"

for keys in food.keys():
    print("Thuc an cua", key, "la", food[key])
