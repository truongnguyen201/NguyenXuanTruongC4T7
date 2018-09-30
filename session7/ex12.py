quan = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
danso = [150.300, 247.100, 333.300, 266.800, 420.900, 318.000]

l = len(quan)
for i in range(l):
   list_new = [quan[i], danso[i]]
   print(*list_new, sep=': ')

