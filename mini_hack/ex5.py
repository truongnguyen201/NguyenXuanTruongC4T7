computer = {
    'HP' : 20,
    "DELL" : 50,
    "MACBOOK": 12,
    "ASSUS": 30 
}
enter = input("Nhập hãng:")
n = int(input("Số lượng:"))
computer[enter] = n 
print(computer)