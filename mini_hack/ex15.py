price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA': 600,
    'FUJISU': 900,
    'ALIENWARE': 1000
}

hang = input("Nhập hãng: ")
so_luong = int(input("Nhập số lượng: "))
tong = so_luong*price[hang]
print(tong)