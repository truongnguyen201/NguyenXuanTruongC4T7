import getpass
print("Đăng kí tài khoản")
tendangnhap = str(input("Nhập tên đăng nhập:  "))
password = getpass.getpass("nhập mât khẩu:  ")
email = str(input("Nhập email của bạn:  "))
loop = True
while loop :
    password2 = getpass.getpass("nhập lại mât khẩu:  ")
    if password2 != password:
       print("Nhập lại sai rồi ")
       password2 = getpass.getpass("nhập lại mât khẩu:  ")
    else:
        loop = False