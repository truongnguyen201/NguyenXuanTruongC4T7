import random

print("GAME")
print("")
print("Guess word")
print("")
print("Rule:We've got a list")
print("We'll choose a word and shuffle its character randomly")
print("Your mission : predict that word after shuffling")
print("GUD LUCK")
print("")

country = ['Vietnam', 'Japan', 'China', 'United States', 'United Kingdom', 'India', 'Russia', 'Germany', 'Switzerland', 'Netherland']
print("Name of country:", *country, sep=', ')
word = random.choice(country)
word2 = word.swapcase()
character = list(word2)
random.shuffle(character)
print(*character, sep='')

loop = True
while loop:
    nguoidungnhap = str(input("Please enter corrcet word: "))
    if nguoidungnhap != word:
        nguoidungnhap = str(input("Wrong, ahihi =))), too hard for you :)), retry: "))
    else:
        print("correct")
        loop = False

