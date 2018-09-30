list_colors = ["blue", 'red', 'teal', 'green']
loop = True
while loop:
    print("Our color list")
    for i, list_color in enumerate(list_colors):
        print(i+1, '.', list_color) 
    loop1 = True
    while loop1 :   
        enter1 = input("Choose number or string enter N for number S for string: ")
        while enter1 != "N" and enter1 != "S":
            enter1 = input("Invalid, retry:")
        if enter1 == 'N':
            try:
               enter = int(input("Item to delete: "))
               list_colors.pop(enter)
               for j, list_colorss in enumerate(list_colors):
                  print(j+1, '.', list_colorss)
               loop1 = False
            except ValueError:
                pass
            except IndexError:
                pass
        elif enter1 == 'S':
            try:
                enter = str(input("Item to delete: "))
                if enter in list_colors:
                    list_colors.remove(enter)
                    for m, list_colorsss in enumerate(list_colors):
                        print(m+1, '.', list_colorsss)
                else:
                    loop1 = False
            except IndexError:
                pass