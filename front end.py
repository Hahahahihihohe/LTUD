from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sys
import mysql.connector

from login import Login
from test import Second_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.login = Login()

        self.setObjectName("MainWindow")
        self.resize(653, 650)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.setFont(font)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setStyleSheet("")


        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 301, 471))
        self.widget.setStyleSheet("background: rgb(79, 228, 242);\n"
                                  "border-radius: 20px;\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(15, 170, 91, 31))
        self.label.setStyleSheet("background: rgba(0,0,0,0);\n"
                                 "border-radius: 2px solid rgba(0,0,0,0);\n"
                                 "color: rgb(20, 43, 36);\n"
                                 "padding-bottom: 5px;\n"
                                 "")
        self.label.setObjectName("label")
        self.User = QtWidgets.QLineEdit(self.widget)
        self.User.setGeometry(QtCore.QRect(114, 170, 171, 28))
        self.User.setStyleSheet("background: rgb(255,255,255);\n"
                                "border-radius: 7px;\n"
                                "color: rgb(20, 43, 36);\n"
                                "padding-bottom: 5px;\n"
                                "")
        self.User.setObjectName("User")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(15, 220, 91, 31))
        self.label_2.setStyleSheet("background: rgba(0,0,0,0);\n"
                                   "border-radius: 2px solid rgba(0,0,0,0);\n"
                                   "color: rgb(20, 43, 36);\n"
                                   "padding-bottom: 5px;\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.Pass_word = QtWidgets.QLineEdit(self.widget)
        self.Pass_word.setGeometry(QtCore.QRect(114, 220, 171, 28))
        self.Pass_word.setStyleSheet("background: rgb(255,255,255);\n"
                                     "border-radius: 7px;\n"
                                     "color: rgb(20, 43, 36);\n"
                                     "padding-bottom: 5px;\n"
                                     "")
        self.Pass_word.setText("")
        self.Pass_word.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass_word.setObjectName("Pass_word")
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.clicked.connect(self.tkmk)
        self.login_btn.setGeometry(QtCore.QRect(15, 280, 270, 35))
        font = QtGui.QFont()
        font.setPointSize(11)

        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("QPushButton#login_btn{\n"
                                     "background-color: rgba(61, 157, 201, 0.851);\n"
                                     "border-radius: 10px;\n"
                                     "color: rgb(20, 43, 36);\n"
                                     "}\n"
                                     "QPushButton#login_btn:hover{\n"
                                     "background-color : rgba(50, 119, 217, 0.851);\n"
                                     "}\n"
                                     "QPushButton#login_btn:pressed{\n"
                                     "padding-left : 4px;\n"
                                     "padding-bottom : 4px;\n"
                                     "background-color : rgba(23, 107, 145, 0.851);\n"
                                     "}")
        self.login_btn.setObjectName("login_btn")

        self.forgot_pw = QtWidgets.QPushButton(self.widget)
        self.forgot_pw.setGeometry(QtCore.QRect(15, 320, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.forgot_pw.setFont(font)
        self.forgot_pw.setStyleSheet("QPushButton#forgot_pw{\n"
                                     "background-color: rgba(0,0,0,0);\n"
                                     "color: rgb(20, 43, 36);\n"
                                     "}\n"
                                     "QPushButton#forgot_pw:hover{\n"
                                     "text-decoration: underline;\n"
                                     "}\n"
                                     "")
        self.forgot_pw.setObjectName("forgot_pw")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(15, 380, 121, 31))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setStyleSheet("background: rgba(0,0,0,0);\n"
                                   "border-radius: 2px solid rgba(0,0,0,0);\n"
                                   "color: rgb(20, 43, 36);\n"
                                   "padding-bottom: 5px;\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.register_0 = QtWidgets.QPushButton(self.widget)
        self.register_0.setGeometry(QtCore.QRect(150, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.register_0.setFont(font)
        self.register_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_0.setStyleSheet("QPushButton#register_0{\n"
                                      "background-color: rgba(92, 99, 232, 0.851);\n"
                                      "border-radius: 10px;\n"
                                      "color: rgb(20, 43, 36);\n"
                                      "}\n"
                                      "QPushButton#register_0:hover{\n"
                                      "background-color : rgba(50, 119, 217, 0.851);\n"
                                      "}\n"
                                      "QPushButton#register_0:pressed{\n"
                                      "padding-left : 4px;\n"
                                      "padding-top : 4px;\n"
                                      "background-color : rgba(23, 107, 145, 0.851);\n"
                                      "}")
        self.register_0.setObjectName("register_0")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def tkmk(self):
        taikhoan = self.User.text()
        matkhau = self.Pass_word.text()
        kt = self.login.check_pass(taikhoan, matkhau)
        if kt:
            self.second_window = Second_MainWindow()
            self.second_window.show()
            self.close()

        else:
            QMessageBox.information(self, "Thông báo", "Sai tài khoản hoặc mật khẩu")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tài khoản"))
        self.User.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Mật khẩu"))
        self.Pass_word.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Đăng nhập"))
        self.forgot_pw.setText(_translate("MainWindow", "Quên mật khẩu?"))
        self.label_3.setText(_translate("MainWindow", "Chưa có tài khoản?"))
        self.register_0.setText(_translate("MainWindow", "Đăng ký"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
