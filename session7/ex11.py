try:
    a = [int(x) for x in input("Enter a list of numbers, separated by space: ").split(' ')]
except ValueError:
    pass

for numb in a:
    if numb %2 == 0:
        print("Even numb: ", numb)