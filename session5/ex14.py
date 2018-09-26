import getpass
print("Đăng kí tài khoản")

tendangnhap = str(input("Nhập tên đăng nhập:  "))


loop = True
while loop :
    password = getpass.getpass("nhập mât khẩu:  ")
    password2 = getpass.getpass("nhập lại mât khẩu:  ")
    email = str(input("Nhập email của bạn:  "))
    if password2 != password:
       print("Nhập lại sai rồi ")
    elif len(password) < 8:
        print("bạn nhập thiếu kí tự rồi 8 cơ")
    elif password.isdigit() == True:  
        print("bạn nhập sai rồi phải có cả chữ chứ")
    elif password.isalpha() == True:
        print("bạn nhập sai rồi phải có  số chứ")
    elif email.endswith('@gmail.com') == False:
        print("Email ko hợp lệ phải kết thúc bằng @gmail.com")
    else:
        print("Đăng nhập thành công")
        loop = False
