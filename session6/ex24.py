import random
word = str(input("Enter a word: "))
character = list(word)
random.shuffle(character)
print(*character, sep=', ')