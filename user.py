class user():
    #class set nguoi dung
    def __init__(self, name = 'None', age = 0, gender = 'M', money = 0 ):
        #ham khoi tao
        self.name = name
        self.age = age
        self.gender = gender
        self.money = money

    def set_name(self,name):
        #set name
        self.name = name

    def get_name(self):
        #get name
        return self.name

    def set_gender(self, gender):
        # set giới tính
        self.gender = gender

    def get_gender(self):
        # get gioi tinh
        return self.gender

    def set_age(self, age):
        # set tuoi
        self.age = age

    def get_age(self):
        # get age
        return self.age

    def set_money(self, money):
        # set money
        self.money = money

    def get_money(self):
        # get name
        return self.money