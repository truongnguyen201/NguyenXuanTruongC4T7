items = [5, 1, 8, 92, -1, 30]


number = int(input("enter a number: "))
if number in items:
    print("Found, position: ", items.index(number+1))
elif number not in items:
    print("Not found")
