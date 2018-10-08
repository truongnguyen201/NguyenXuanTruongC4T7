price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS' : 400,
    'TOSHIBA': 600,
    'FUJISU': 900,
    'ALIENWARE': 1000
}

computer = {
    'HP' : 20,
    "DELL" : 50,
    "MACBOOK": 12,
    "ASUS": 30,
    'TOSHIBA': 10,
    'FUJISU':15  ,
    'ALIENWARE': 5   
}
tong = 0
for k in price.keys():
    a = price[k]*computer[k]
    tong = tong + a
print(tong)
        