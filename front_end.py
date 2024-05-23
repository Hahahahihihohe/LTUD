from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication, QStackedWidget
from PyQt5.uic import loadUi
import sys

from login import Login
from user import User

# Cửa sổ đăng nhập(0)
class login_wd(QMainWindow):
    def __init__(self):
        super(login_wd, self).__init__()
        loadUi("login_wd.ui", self)
        self.login = Login()

        self.register_0.clicked.connect(self.switch_register)
        self.login_btn.clicked.connect(self.check)
        self.forgot_pw_btn.clicked.connect(self.switch_forgotpw)

    # Kiểm tra thông tin đăng nhập
    def check(self):
        taikhoan = self.User.text()
        matkhau = self.Pass_word.text()
        kt = self.login.check_pass(taikhoan, matkhau)
        if kt != 0:
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
            acc_info_f.user.update_info(kt)  # Cập nhật thông tin người dùng
            acc_info_f.show()  # Hiển thị cửa sổ thông tin tài khoản
            widget.setCurrentIndex(2)
        else:
            QMessageBox.information(self, "Thông báo", "Sai tài khoản hoặc mật khẩu")

    # Chuyển sang cửa sổ đăng ký
    def switch_register(self):
        widget.setCurrentIndex(1)

    def switch_forgotpw(self):
        widget.setCurrentIndex(3)

# Cửa sổ đăng ký(1)
class register_wd(QMainWindow):
    def __init__(self):
        super(register_wd, self).__init__()
        loadUi("register_wd.ui", self)
        self.login = Login()

        self.register_1.clicked.connect(self.check_rgt)
        self.back.clicked.connect(self.gobacklogin)

    def gobacklogin(self):
        widget.setCurrentIndex(0)

    # Kiểm tra thông tin đăng ký
    def check_rgt(self):
        ten = self.name.text()
        tuoi = self.age.text()
        tk = self.account.text()
        mk = self.pw.text()
        kt_mk = self.check_pw.text()
        kt2 = self.login.create_acc(tk, mk, kt_mk, ten, tuoi)
        if kt2 == 1:
            QMessageBox.information(self, "Thông báo", "Tài khoản này đã tồn tại")
        elif kt2 in [2, 3, 4]:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt2 == 5:
            QMessageBox.information(self, "Thông báo", "Mật khẩu nhập lại không đúng")
        elif kt2 == 6:
            QMessageBox.information(self, "Thông báo", "Đăng ký thành công")
            widget.setCurrentIndex(0)

# Cửa sổ thông tin cá nhân(2)
class acc_info(QMainWindow):
    def __init__(self):
        super(acc_info, self).__init__()
        loadUi("acc_info.ui", self)
        self.acc_info.clicked.connect(self.switch_user)
        self.trading_history.clicked.connect(self.switch_his)
        self.add_money.clicked.connect(self.switch_money)
        self.user = User()
        self.change_pw.clicked.connect(self.switch_changepw_wd)

    def switch_user(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_his(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_money(self):
        self.stackedWidget.setCurrentIndex(2)

    def show(self):
        # Hiển thị thông tin người dùng trên giao diện
        self.user_name_2.setText(self.user.GetName())
        self.user_age_2.setText(str(self.user.GetAge()))
        self.user_money_2.setText(str(self.user.GetMoney()))

        # Hiển thị cửa sổ
        super().show()

    def switch_changepw_wd(self):
        widget.setCurrentIndex(4)

# Cửa sổ quên mật khẩu(3)
class forgot_pw(QMainWindow):
    def __init__(self):
        super(forgot_pw, self).__init__()
        loadUi("forgot_pw.ui", self)
        self.login = Login()

        self.change_pw.clicked.connect(self.check_fgp)
        self.back.clicked.connect(self.gobacklogin)

    def gobacklogin(self):
        widget.setCurrentIndex(0)

    # Kiểm tra tài khoản xem đã tồn tại hay chưa, nếu đã tồn tại thì cho phép đổi mật khẩu
    def check_fgp(self):
        taikhoan = self.User_old.text()
        mk_moi = self.pw_new.text()
        kt_mk_moi = self.pw_new2.text()
        kt3 = self.login.forgot_pass(taikhoan, mk_moi, kt_mk_moi)
        if kt3 == 1:
            QMessageBox.information(self, "Thông báo", "Tài khoản không tồn tại")
        elif kt3 in [2, 3, 4]:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt3 == 5:
            QMessageBox.information(self, "Thông báo", "Mật khẩu nhập lại không đúng")
        elif kt3 == 6:
            QMessageBox.information(self, "Thông báo", "Đổi mật khẩu thành công")
            widget.setCurrentIndex(0)

# Cửa sổ đổi mật khẩu (4)
class change_password(QMainWindow):
    def __init__(self):
        super(change_password, self).__init__()
        loadUi("change_password.ui", self)
        self.chg_pw.clicked.connect(self.change_pw)
        self.back.clicked.connect(self.switch_accinfo)
    def change_pw(self):
        mk = self.pw_new.text()
        mkm = self.pw_new2.text()
        kt = acc_info_f.user.change_pass(mk, mkm)  # Truyền ID người dùng
        if kt in [2, 3, 4]:
            QMessageBox.information(self, "Thông báo", "Mật khẩu không hợp lệ (mật khẩu của bạn phải có ít nhất 8 ký tự bao gồm ít nhất 1 chữ số và 1 chữ cái in hoa)")
        elif kt == 5:
            QMessageBox.information(self, "Thông báo", "Mật khẩu nhập lại không đúng")
        elif kt == 6:
            QMessageBox.information(self, "Thông báo", "Đổi mật khẩu thành công")
            widget.setCurrentIndex(2)
    def switch_accinfo(self):
        widget.setCurrentIndex(2)

app = QApplication(sys.argv)
widget = QStackedWidget()

login_f = login_wd()
register_f = register_wd()
acc_info_f = acc_info()
forgot_f = forgot_pw()
change_password_f = change_password()
widget.addWidget(login_f)
widget.addWidget(register_f)
widget.addWidget(acc_info_f)
widget.addWidget(forgot_f)
widget.addWidget(change_password_f)

widget.setCurrentIndex(0)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
