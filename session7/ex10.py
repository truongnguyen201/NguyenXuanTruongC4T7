list_numbs = [5, 1, 8, 92, 7, 30]
print(*list_numbs, sep=', ')
l = len(list_numbs)
print("All even numbers: ")

for i in range(l):
    if list_numbs[i] %2 == 0:
       print(list_numbs[i], end =" ")