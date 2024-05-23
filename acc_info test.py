from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication,QStackedWidget
from PyQt5.uic import loadUi
import sys

from user import User
from front_end import id

class acc_info(QMainWindow):
    def __init__(self):
        super(acc_info,self).__init__()
        loadUi("acc_info.ui",self)
        self.acc_info.clicked.connect(self.switch_user)
        self.trading_history.clicked.connect(self.switch_his)
        self.add_money.clicked.connect(self.switch_money)

    def switch_user(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_his(self):
        self.stackedWidget.setCurrentIndex(1)
    def switch_money(self):
        self.stackedWidget.setCurrentIndex(2)
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

acc_info_f = acc_info()
widget.addWidget(acc_info_f)
widget.setCurrentIndex(0)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())