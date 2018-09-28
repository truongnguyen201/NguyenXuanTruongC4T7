favourites = str(input("Nhập sở thích mỗi sở thích cách nhau 1 dấu phẩy: "))
favourite = favourites.split(',')
print("Sở thích:")
l = len(favourite)
for i in range(0, l):
   print(favourite[i])
