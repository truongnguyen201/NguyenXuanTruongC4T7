try:
    a = [int(x) for x in input("Enter a list of numbers, separated by space: ").split(' ')]
except ValueError:
    pass

b = sum(a)
print(b)