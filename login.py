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

    def forgot_pass(self,user):
        # Hàm xử lý để đặt lại mật khẩu, trước mắt yêu cầu điền username
        index = -1
        for i in range(self.database.shape[0]):
            if self.database[i][0] == user:
                index = i
                break
        if index == -1:
            return "tai khoan khong ton tai"
        else:
            flag = False
            while ~flag:
                flag = True
                new_pass = input()
                if len(new_pass) < 8:
                    #kiem tra dieu kien do dai
                    flag = False
                # se them mot vai dieu kien khac sau
            self.database[index][1] = new_pass
            return "sua mat khau thanh cong"

