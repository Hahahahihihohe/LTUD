from database import db
import numpy as np
class User():
    #class set nguoi dung
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None
        self.money = None

    def update_info(self,id):
        id = int(id)
        if id > 17:
            id += 1
        # ham khoi tao
        sql = "select * from user_info where id = %s"
        res = db.fetchone(sql, [id])
        self.id = res[0]
        self.name = res[1]
        self.age = res[2]
        self.money = res[3]

    def SetName(self,name):
        self.name = name

    def SetAge(self,age):
        self.age = age


    def SetMoney(self,money):
        self.money = money

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age


    def GetMoney(self):
        return self.money


    def ShowALl(self):
        print(self.id,self.name,self.age,self.money)

    def change_info(self,name, age):
        sql = "update user_info set name = %s , age = %s where id = %s"
        db.execute(sql, [name, age, self.id])
        db.mydb.commit()
        self.SetName(name)
        self.SetAge(age)

    def stonks(self,amount):
        self.SetMoney(self.GetMoney() + amount)
        sql = "update user_info set money = %s where id = %s"
        db.execute(sql, [self.GetMoney(), self.id])
        db.mydb.commit()
        print("nap thanh cong")
        return True

    def stinks(self,amount):
        if self.GetMoney() < amount:
            return False
        self.SetMoney(self.GetMoney() - amount)
        return True

    def Getorder(self):
        sql = """
        SELECT movie_name, price, time from order_history where user_id = %s
        """
        res = db.fetchall(sql,[self.id])
        if not res:
            return False
        else:
            res = np.array(res)
        return res

    def change_pass(self,password, con_pass):
        id = int(self.id)
        if id > 17:
            id -= 1

        if len(password) < 8:
            print("Mật khẩu phải có ít nhất 8 ký tự")
            return 2
        num = False
        cap = False
        for i in password:
            if i.isdigit():
                num = True
            if i.isupper():
                cap = True
        if not num:
            print("Mật khẩu phải có ít nhất 1 chữ số")
            return 3
        if not cap:
            print("Mật khẩu phải có ít nhất 1 ký tự viết hoa")
            return 4
        if con_pass != password:
            print("Mật khẩu nhập lại không đúng")
            return 5

        sql = "update customers set password = %s where id = %s"
        db.execute(sql, [password, id])
        db.mydb.commit()
        return 6


