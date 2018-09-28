fa_vờ_rít1 = ["spiderman", "game", "idk", "dragonball"]
print(*fa_vờ_rít1, sep=',  ')

loop = True
while loop :
    try:
        i = int(input("Enter index, pleasee enter number from -4 to 3: "))
        fa_vờ_rít1[i] = str(input("Nhập j đó: "))
        print(*fa_vờ_rít1, sep=', ')
        break
    except ValueError:
        pass
    except IndexError:
        pass

if 'LOL' in fa_vờ_rít1:
    fa_vờ_rít1.remove('LOL')
    print(*fa_vờ_rít1, sep=', ')
else:
    print("Ko có LOL")
    print(*fa_vờ_rít1, sep=', ')