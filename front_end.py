from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication
from PyQt5.uic import loadUi
import sys

from login import Login
from user import User
#Cửa sổ đăng nhập
class login_wd(QMainWindow):
    def __init__(self):
        super(login_wd,self).__init__()
        loadUi("login_wd.ui",self)
        self.login = Login()

        self.register_0.clicked.connect(self.switch_register)
        self.login_btn.clicked.connect(self.check)
        self.forgot_pw_btn.clicked.connect(self.switch_forgotpw)

    #kiểm tra thông tin đăng nhập
    def check(self):
        taikhoan = self.User.text()
        matkhau = self.Pass_word.text()
        kt = self.login.check_pass(taikhoan, matkhau)
        if kt != 0:
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
            widget.setCurrentIndex(2)
            id = kt
        else:
            QMessageBox.information(self, "Thông báo", "Sai tài khoản hoặc mật khẩu")
    #chuyển sang cửa sổ đăng ký
    def switch_register(self):
        register_f = register_wd()
        widget.addWidget(register_f)
        widget.setCurrentIndex(1)
    def switch_forgotpw(self):
        forgot_f = forgot_pw()
        widget.addWidget(forgot_f)
        widget.setCurrentIndex(3)
#Cửa sổ đăng ký
class register_wd(QMainWindow):
    def __init__(self):
        super(register_wd,self).__init__()
        loadUi("register_wd.ui",self)
        self.login = Login()

        self.register_1.clicked.connect(self.check_rgt)
        self.back.clicked.connect(self.gobacklogin)
    def gobacklogin(self):
        widget.setCurrentIndex(0)
#Kiểm tra thông tin đăng ký
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
#Cửa sổ quên mật khẩu
class forgot_pw(QMainWindow):
    def __init__(self):
        super(forgot_pw,self).__init__()
        loadUi("forgot_pw.ui",self)
        self.login = Login()

        self.change_pw.clicked.connect(self.check_fgp)
        self.back.clicked.connect(self.gobacklogin)
    def gobacklogin(self):
            widget.setCurrentIndex(0)
#Kiểm tra tài khoản xem đã tồn tại hay chưa, nếu đã tồn tại thì cho phép đổi mật khẩu
    def check_fgp(self):
        taikhoan = self.User_old.text()
        mk_moi = self.pw_new.text()
        kt_mk_moi = self.pw_new2.text()
        kt3 = self.login.forgot_pass(taikhoan,mk_moi,kt_mk_moi)
        if kt3 == 1:
            QMessageBox.information(self, "Thông báo", "Tài khoản không tồn tại")
        elif kt3 == 2:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt3 == 3:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt3 == 4:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt3 == 5:
            QMessageBox.information(self, "Thông báo", "Mật khẩu nhập lại không đúng")
        elif kt3 == 6:
            QMessageBox.information(self, "Thông báo", "Đổi mật khẩu thành công")
            widget.setCurrentIndex(0)

class acc_info(QMainWindow):
    def __init__(self):
        super(acc_info,self).__init__()
        loadUi("acc_info.ui",self)

id = 0
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

login_f = login_wd()
register_f = register_wd()
test_f = test()
forgot_f = forgot_pw()
widget.addWidget(login_f)
widget.addWidget(register_f)
widget.addWidget(test_f)
widget.addWidget(forgot_f)
widget.setCurrentIndex(0)
widget.setFixedWidth(500)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
