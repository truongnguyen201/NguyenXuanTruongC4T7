print("We will help you to find your body mass index")
a = float(input("Please enter your height(m):   "))
b = float(input("Please enter your weight(kg):  "))
c = float (b/(a*a))

if c < 16:
    print("Serverly Underweight")
elif c < 18.5:
    print("Underweight")
elif c < 25:
    print("Normal")
elif c < 30:
    print("Overweight")
else:
    print("Obese")