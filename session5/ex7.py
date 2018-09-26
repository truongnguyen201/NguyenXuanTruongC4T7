loop = True
while loop:
    try:
        n = int(input("Nhập 1 số:   "))
        for i in range(n+1, 0, -1):
            print(i)
        loop = False
    except ValueError:
        pass