x = 0
y = 0

for x in range(801):
    for y in range(801):
        if (1.15*x+1.2*y == 945) and (x + y == 800):
            print(x)
            print(y)

