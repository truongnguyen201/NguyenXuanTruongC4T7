fa_vờ_rít1 = ["spiderman", "game", "idk", "dragonball"]
print(*fa_vờ_rít1, sep=',  ')

loop = True
while loop :
    try:
        n = int(input("thích xóa j thì xóa: "))
        fa_vờ_rít1.pop(n)
        print(fa_vờ_rít1)
        break
    except ValueError:
        pass
    except IndexError:
        pass

