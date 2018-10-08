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