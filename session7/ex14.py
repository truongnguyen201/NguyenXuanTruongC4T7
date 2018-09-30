quan = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
danso = [150300, 247100, 333300, 266800, 420900, 318000]

l = len(quan)
for i in range(l):
   list_new = [quan[i], danso[i]]
   print(i+1, '.', *list_new, sep=' ')

numb = max(danso)
i = danso.index(numb)
print("Quận có số dân đông nhất: ", quan[i] )
numb2 = min(danso)
j = danso.index(numb2)
print("Quận có số dân ít nhất: ", quan[j])
