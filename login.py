import numpy as np

class Login():
    def __init__(self,database):
        self.user = None
        self.password = None
        self.database = database #luu du lieu tai  khoan mat khau
        #database dang (-1,2), cột đầu lưu tài khoản, cột hai lưu mật khẩu dạng string

    def check_pass(self,user,password):
        # hàm  nhập vào username và password, kiểm tra đúng thông tin tài khoản không
        for i in range(self.database.shape[0]): #tim tat ca cac tai khoan
            if self.database[i][0] == user and self.database[i][1] == password:
                return True
            else:
                return False

    def forgot_pass(self,user,password):
        # Hàm xử lý để đặt lại mật khẩu, trước mắt yêu cầu điền username
        index = -1
        for i in range(self.database.shape[0]):
            if self.database[i][0] == user:
                index = i
                break
        if index == -1:
            #nếu tài khoản không tồn tại thì không thể đổi mật khẩu
            print("tai khoan khong ton tai")
            return False

        #điều kiện mật khẩu gồm có: có ít nhất 8 kí tự
        #                           có ít nhất 1 ký tự viết hoa
        #                           có ít nhất 1 chữ số

        if len(password) < 8:
            print("Mật khẩu phải có ít nhất 8 ký tự")
            return False
        num = False
        cap = False
        for i in password:
            if i.isdigit():
                num = True
            if i.isupper():
                cap = True
        if not num:
            print("Mật khẩu phải có ít nhất 1 chữ số")
            return False
        if not cap:
            print("Mật khẩu phải có ít nhất 1 ký tự viết hoa")
            return False
        self.database[index][1] = password
        return True


    def create_acc(self,user,password):
        index = -1
        for i in range(self.database.shape[0]):
            if self.database[i][0] == user:
                index = i
                break

        #nếu đã tồn tại không thể thêm vào
        if index != -1:
            print("tài khoản này đã tồn tại")
            return False

        # điều kiện mật khẩu gồm có: có ít nhất 8 kí tự
        #                           có ít nhất 1 ký tự viết hoa
        #                           có ít nhất 1 chữ số
        if len(password) < 8:
            print("Mật khẩu phải có ít nhất 8 ký tự")
            return False
        num = False
        cap = False
        for i in password:
            if i.isdigit():
                num = True
            if i.isupper():
                cap = True
        if not num:
            print("Mật khẩu phải có ít nhất 1 chữ số")
            return False
        if not cap:
            print("Mật khẩu phải có ít nhất 1 ký tự viết hoa")
            return False
        self.database = np.vstack((self.database,[user,password]))
        return True

    def print_database(self):
        print(self.database)
