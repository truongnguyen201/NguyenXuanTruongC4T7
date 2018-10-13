import requests
import json
r = requests.get('https://jsonplaceholder.typicode.com/users', auth=('user','pass'))
d = r.json()
print(d)

i = 0
loop = True
while loop:
    if "Delphine" in d[i]['Username']:
        print(d[i])
    i+=1

Username = input("Nhập: ")
Username = Username.capitalize()
loop1 = True
while loop1:
    if Username in d[i]['Username']:
        print(d[i])
    else:
        print("Ko có")
    i+=1
