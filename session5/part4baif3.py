import getpass
print("Đăng kí tài khoản")
tendangnhap = str(input("Nhập tên đăng nhập:  "))
email = str(input("Nhập email của bạn:  "))
loop = True
while loop :
    password = getpass.getpass("nhập mât khẩu:  ")
    password2 = getpass.getpass("nhập lại mât khẩu:  ")
    if password2 != password:
       print("Nhập lại sai rồi ")
       password2 = getpass.getpass("nhập lại mât khẩu:  ")
    elif 
    else:
        loop = False
