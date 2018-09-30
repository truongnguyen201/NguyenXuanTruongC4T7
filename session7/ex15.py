quan = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
danso = [150300, 147100, 333300, 266800, 420900, 318000]

print("Diện tích quận:")
l = len(quan)
for i in range(l):
   list_new = [quan[i], dientich[i]]
   print(*list_new, sep=': ')

matdodancu = []
for j in range(l):
    matdodancu1 = danso[j]/dientich[j]
    matdodancu1 = round(matdodancu1, 3)
    matdodancu.append(matdodancu1)

print("Mật độ dân cư:")
for x in range(l):
    list_new1 = [quan[x], matdodancu[x]]
    print(*list_new1, sep=': ')