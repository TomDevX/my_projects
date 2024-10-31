n = ["0","1","2","3","4"]
print("Step 1:", n)
for i in range(1,len(n)):
    n.pop(4)
    n.insert(0, "0")
    print("Step", i+1, ":", n)
