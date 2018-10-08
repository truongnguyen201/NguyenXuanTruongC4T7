import random
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

loop = True
while loop:
    try:
       n = int(input("Choose skill: "))
       if n == 1:
           a = random.uniform(0,1)
           if a < skill1["Hit rate"]:
               print("Damage:", skill1['Damage'])
           else:
               print("not hit the target")
       if n == 2:
           b = random.uniform(0,1)
           if b < skill2["Hit rate"]:
               print("Damage:", skill2['Damage'])
           else:
               print("not hit the target")
       if n ==3:
           c = random.uniform(0,1)
           if c < skill3["Hit rate"]:
               print("Damage:", skill3['Damage'])
           else:
               print("not hit the target")
       if n >=4:
           print("Dont have that skill")
    except ValueError:
        pass

