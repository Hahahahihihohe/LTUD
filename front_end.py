from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget,QVBoxLayout, QApplication
from PyQt5.uic import loadUi
import sys
import mysql.connector

from login import Login
class login_wd(QMainWindow):
    def __init__(self):
        super(login_wd,self).__init__()
        loadUi("login_wd.ui",self)
        self.login = Login()
        self.register_0.clicked.connect(self.switch)
        self.login_btn.clicked.connect(self.check)
    def check(self):
        taikhoan = self.User.text()
        matkhau = self.Pass_word.text()
        kt = self.login.check_pass(taikhoan, matkhau)
        if kt:
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
            widget.setCurrentIndex(2)

        else:
            QMessageBox.information(self, "Thông báo", "Sai tài khoản hoặc mật khẩu")
    def switch(self):
        register_f = register_wd()
        widget.addWidget(register_f)
        widget.setCurrentIndex(1)
class register_wd(QMainWindow):
    def __init__(self):
        super(register_wd,self).__init__()
        loadUi("register_wd.ui",self)

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
