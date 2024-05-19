from database import db

class User():
    #class set nguoi dung
    def __init__(self, id):
        #ham khoi tao
        sql = "select * from user_info where id = %s"
        res = db.fetchone(sql,[id])
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
