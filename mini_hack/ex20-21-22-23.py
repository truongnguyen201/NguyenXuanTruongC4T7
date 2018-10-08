character = {
    'Name' : 'Tackle',
    'Age': 17,
    'Strength' : 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ["shield", 'bread loaf'], 
    'Gold': 100,
    'level': 2
}

character['Gold'] +=50
print(character)

Backpack = character['Backpack']
Backpack.append("FlintStone")
print(character)

character['Pocket'] = ['MonsterDex', 'Flashlight']
print(character)