from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication, QPushButton, QStackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from chuyenhinh import slidebar
from main_scr import Mainscreen
from nddatve import xulydatve
import ndphim,trangchu
#mainw = Mainscreen()
ui = ''
#appp = QtWidgets.QApplication(sys.argv)
app = QtWidgets.QApplication(sys.argv)

window1 = xulydatve()
window = slidebar()

mainwindow = QMainWindow()
#class inhinh(QMainWindow, hi.Ui_MainWindow)
def home():
    window1.show()

window.show()
sys.exit(app.exec_())