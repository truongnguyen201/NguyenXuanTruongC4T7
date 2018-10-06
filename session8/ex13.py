person = {
    "bộ phim yêu thích" : "hậu duệ the sun",
    "tên ca sỹ yêu thích" : "bảo hưng miền tây",
    "tên bài hát yêu thích" : "cô y tá phê đá:<<<)))", 
}
key1 = input("Nhập tên bạn muốn xóa: ")
if key1 in person:
   del person[key1]
   print(person)
elif key1 not in person:
    print("dont exist")

