from random import randint
import random

print("Biểu thức đúng thì điền đúng còn sai thì sai ez game")

sign = random.choice(['+', '-'])
loop = True
while loop:
    a = randint(0, 100)
    b = randint(0, 100)
    c = randint(-100, 199)
    if sign == '+':
        d = a + b
    elif sign == '-':
        d = a - b
    ketqua = random.choice([c, d])
    
    print(a, sign, b, '=', ketqua)
    
    answer = input("T/F: ")
    if (answer == 'T' and ketqua == d  ) or (answer == 'F' and ketqua != d):
        print("Đúng rồi đó")
    else:
        print("sai rồi")
        break

