skill = []
skill1 = {
    'Name': 'Tackle',
    'Min level': 1,
    'Damage': 5,
    'Hit rate': 0.3
}

skill2 = {
    'Name': 'Quick attack',
    'Min level': 2,
    'Damage': 3,
    'Hit rate': 0.5
}

skill3 = {
    'Name': 'Strong kick',
    'Min level': 4,
    'Damage': 7,
    'Hit rate': 0.3
}

skill.append(skill1)
skill.append(skill2)
skill.append(skill3)
i=1
for k in skill:
    print("Skill", i)
    print(k['Name'])
    i+=1

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
loop = True
while loop:
    try:
       n = int(input("Choose skill: "))
       if n == 1:
           if skill1['Min level'] <= character['level']:
              print("Skill damage: ", skill1['Damage'])
           else:
              print("No permission")
       if n == 2:
           if skill2['Min level'] <= character['level']:
              print("Skill damage: ", skill2['Damage'])
           else:
              print("No permission")
       if n ==3:
           if skill3['Min level'] <= character['level']:
              print("Skill damage: ", skill3['Damage'])
           else:
              print("No permission")
       if n >=4:
           print("Dont have that skill")
    except ValueError:
        pass
    





