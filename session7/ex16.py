quan = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
danso = [150300, 147100, 333300, 266800, 420900, 318000]

l = len(quan)
matdodancu = []
for j in range(l):
    matdodancu1 = danso[j]/dientich[j]
    matdodancu1 = round(matdodancu1, 3)
    matdodancu.append(matdodancu1)

tongmatdodancu = sum(matdodancu)
mdcutb = tongmatdodancu/l
mdcutb =round(mdcutb, 3)
print("Mật độ dân cư trung bình:")
print(mdcutb)
