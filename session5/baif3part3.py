loop = True
while loop :
    try:
        n = int(input("Nhập 1 số:  "))
        while loop:
            if n not in [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12]:
               print("Ko có tháng này ")
               n = int(input("Nhập cho đúng tháng vào đm"))
            elif n in [1, 3, 5, 7, 8, 10, 12]:
                print("tháng có 31 ngày")
                loop = False
            elif n in [4, 6, 9, 11]:
                print("Tháng có 30 ngày")
                loop = False
            elif n == 2:
                a = int(input("Nhập vào năm đi đm: "))
                if a%4 == 0:
                    print("Năm nhuận đó đồ ngu có 29 ngày")
                    loop = False
                else:
                    print("ko ph năm nhuận thì có 28 ngày")
                    loop = False
                
        break
    except ValueError:
        pass
     