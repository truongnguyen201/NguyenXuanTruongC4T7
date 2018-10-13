i = 0
while i <5:
    if i == 3:
        for j in range(6):
            if j == 1:
                print("x", end=(" "))
            else:
                print("-", end=(" "))
    else:
        for n in range(6):
            print("-", end=(" "))
    print()
    i = i+1
    
          