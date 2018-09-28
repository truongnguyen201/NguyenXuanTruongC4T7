menu_deserts = ["cake", "cocktail", "crepe", "ice cream"]
print("MENU_DESERTS:", *menu_deserts, sep=",")


#lựa chọn CRUD

loop = True
while loop:
    choose = input("enter c or C for create, r or R for read, u or U for update, D or d for delete: ")
    while choose not in ['c', 'C', 'R', 'r', 'd', 'D', 'u', 'U' ]:
        choose = input("invalid, retry: ")

    if choose in ['C', 'c']:
        add = str(input("Add desert: "))
        menu_deserts.append(add)
        print(*menu_deserts, sep=", ")
    
    elif choose in ['R', 'r']:
        for i, menu_desert in enumerate(menu_deserts):
            print(i+1, '.', menu_desert.capitalize())
    
    elif choose in ['U', 'u']:
        loop1 = True
        while loop1:
            try:
                n = int(input("menu_index: "))
                jdo = str(input("update new dish: "))
                l = len(menu_deserts)
                while n > l-1:
                    n = int(input("Dont have that index, retry: "))
                menu_deserts[n-1] = jdo
                print(*menu_deserts, sep=", ")
                loop1 = False
            except ValueError:
                pass
    
    elif choose in ['D', "d"]:
        loop1 = True
        while loop1:
            try:
                i = int(input("menu_index: "))
                l = len(menu_deserts)
                while i > l-1:
                    i = int(input("Dont have that index, retry: "))
                menu_deserts.pop(i-1)
                print(*menu_deserts, sep=', ')
                loop1 = False
            except ValueError:
                pass

