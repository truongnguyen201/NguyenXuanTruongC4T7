h = int(input("Nhập chiều cao: "))
w = int(input("Nhập chiều rộng: "))
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))



i = 0
while i <h:
    if i == y:
        for j in range(w):
            if j == x:
                print("x", end=(" "))
            else:
                print("-", end=(" "))
    else:
        for n in range(w):
            print("-", end=(" "))
    print()
    i = i+1
    
          