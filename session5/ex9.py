loop = True
while loop :
    try:
        n = int(input("Nhập 1 số:  "))
        if n > 13:
            print("yes")
        elif n < 13:
            print("no")
        elif n == 13:
            print("equal")
    except ValueError:
        pass
     