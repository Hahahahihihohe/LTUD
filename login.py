import numpy as np
from database import db
class Login():
    def __init__(self):
        self.user = None
        self.password = None

    def check_pass(self,user,password):
        # hàm  nhập vào username và password, kiểm tra đúng thông tin tài khoản không
        sql = "select * from customers where user = %s"
        res = db.fetchone(sql,(user,))
        if res:
            if res[2] == password and res[1] == user:
                return True
            else:
                return False
        else:
            return False

    def forgot_pass(self,user,password):
        # Hàm xử lý để đặt lại mật khẩu, trước mắt yêu cầu điền username
        sql = "SELECT * from customers where user = %s"
        res = db.fetchone(sql, [user])
        if not res:
            print("Tai khoan nay khong ton tai")
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
        sql = "update customers set password = %s where user = %s"
        db.execute(sql,[password,user])
        db.mydb.commit()
        return True


    def create_acc(self,user,password, name, age):
        sql = "SELECT * from customers where user = %s"
        res = db.fetchone(sql,[user])
        if res:
            print("Tai khoan nay da ton tai")
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
        sql = "INSERT INTO customers (user, password) VALUES (%s, %s)"
        db.execute(sql,[user,password])
        db.mydb.commit()
        sql = "INSERT INTO user_info (name, age, money) VALUES (%s, %s,0)"
        db.execute(sql, [name, age])
        db.mydb.commit()
        print("Tạo tài khoản thành công")
        return True

    def show_database(self):
        sql = "select * from customers"
        res = np.array(db.fetchall(sql))
        print(res)

