loop = True
while loop :
    try:
        n = int(input("Nhập 1 số:  "))
        if n%2 == 0:
            print("số chẵn") 
        elif n%2 !=0:
            print("Ko phải số chẵn")
        break
    except ValueError:
        pass
     