list_color = ["blue", 'red', 'teal', 'green']
print("Our color list:")
print(*list_color, sep=", ")
new_color = str(input("enter new color:"))
list_color.append(new_color)
print(*list_color, sep=', ')

loop = True
while loop:
    try:
        i = int(input("Enter position: "))
        print("Color at position", i, ":", list_color[i])
    except ValueError:
        pass
    except IndexError:
        pass