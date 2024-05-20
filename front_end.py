from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication
from PyQt5.uic import loadUi
import sys

from login import Login
#Cửa sổ đăng nhập
class login_wd(QMainWindow):
    def __init__(self):
        super(login_wd,self).__init__()
        loadUi("login_wd.ui",self)
        self.login = Login()
        self.register_0.clicked.connect(self.switch)
        self.login_btn.clicked.connect(self.check)

    #kiểm tra thông tin đăng nhập
    def check(self):
        taikhoan = self.User.text()
        matkhau = self.Pass_word.text()
        kt = self.login.check_pass(taikhoan, matkhau)
        if kt:
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
            widget.setCurrentIndex(2)

        else:
            QMessageBox.information(self, "Thông báo", "Sai tài khoản hoặc mật khẩu")
    #chuyển sang cửa sổ đăng ký
    def switch(self):
        register_f = register_wd()
        widget.addWidget(register_f)
        widget.setCurrentIndex(1)
#Cửa sổ đăng ký
class register_wd(QMainWindow):
    def __init__(self):
        self.login = Login()
        super(register_wd,self).__init__()
        loadUi("register_wd.ui",self)
        self.register_1.clicked.connect(self.check_rgt)

    def check_rgt(self):
        ten = self.name.text()
        tuoi = self.age.text()
        tk = self.account.text()
        mk = self.pw.text()
        kt_mk = self.check_pw.text()
        kt2 = self.login.create_acc(tk,mk,kt_mk,ten,tuoi)
        if kt2==1:
            QMessageBox.information(self, "Thông báo", "Tài khoản này đã tồn tại")
        elif kt2==2:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt2==3:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt2==4:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt2==5:
            QMessageBox.information(self, "Thông báo", "Mật khẩu nhập lại không đúng")
        elif kt2==6:
            QMessageBox.information(self, "Thông báo", "Đăng ký thành công")
            widget.setCurrentIndex(0)
class test(QMainWindow):
    def __init__(self):
        super(test,self).__init__()
        loadUi("test.ui",self)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

login_f = login_wd()
register_f = register_wd()
test_f = test()
widget.addWidget(login_f)
widget.addWidget(register_f)
widget.addWidget(test_f)
widget.setCurrentIndex(0)
widget.setFixedWidth(500)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
