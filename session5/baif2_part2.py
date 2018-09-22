loop = True
while loop:
    try:
        n = int(input("Nhập 1 số:   "))
        for i in range(0, n+1):
            print(i)
        loop = False
    except ValueError:
        pass