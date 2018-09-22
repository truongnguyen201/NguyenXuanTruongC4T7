import math

question = input("Please choose the conversion (press C for Celcius to Farenheit and press F for Farenheit to Celcius) ")

loop = True

while loop == True :
    
    if question == "C" or question == "c":
        try :
            t_c = float(input("Please enter the temperature in Celcius: "))
            t_f = t_c * 1.8 + 32
            print(t_c,"(C) =", t_f, "(F)")
            ask = input("Press E to exit or another key to continue ")
            if ask == "e" or ask == "E":
                loop = False
            else:
                question = input("Please choose the conversion (press C for Celcius to Farenheit and press F for Farenheit to Celcius) ")
        except ValueError:
            pass

    elif question == "F" or question == "f":
        try :
            t_f = float(input("Please enter the temperature in Farenheit: "))
            t_c = (t_f - 32)/ 1.8
            t_c_round = round(t_c, 2)
            print(t_f, "(F) =", t_c_round, "(C)")
            ask = input("Press E to exit or another key to continue ")
            if ask == "e" or ask == "E":
                loop = False
            else:
                question = input("Please choose the conversion (press C for Celcius to Farenheit and press F for Farenheit to Celcius) ")
        except ValueError:
            pass

    else :
        question = input("Please choose the conversion again (press C for Celcius to Farenheit and press F for Farenheit to Celcius) ")