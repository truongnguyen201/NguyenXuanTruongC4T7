loop = True
while loop :
    try:
        n = float(input("Nhập 1 số:  "))
        a = n*n 
        print(a)
    except ValueError:
        pass
     
