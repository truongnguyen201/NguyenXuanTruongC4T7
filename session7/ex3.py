list_color = ["blue", 'red', 'teal', 'green']
print("Our color list:")
print(*list_color, sep=", ")
new_color = str(input("enter new color:"))
list_color.append(new_color)
print(*list_color, sep=', ')