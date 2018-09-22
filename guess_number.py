from random import randint

print("GUESSING GAME")
print("Rules")
print("Think about a number and i wil guess that")
print("Let me know the difference if my guessing number is wrong ")
print("Lets start the game")


n = int(input("enter a number: "))




print("I will guess your number from 0 to n")
print("Hmm... Lets me see")

a = int((0+n)/2)
print(a)
b = n
guess1 = 1
loop = True

while loop:
    ask = str(input("Is my number Correct or Wrong?, enter C for Correct and W for Wrong:  ",))
    if ask == 'C':
        print("So easy =)))")
        loop = False
    elif ask == 'W':
        ask_2 = str(input("Is your number higher or lower than that number ?, enter H for higher and L for lower: ")) 
        if ask_2 == 'H' :
            c = a
            a = int((c + b)/2)
            print(a)
        elif ask_2 == 'L' :
            b = a
            a = int((b + c)/2)
            print(a)
            
    
                   
    
        
             




