from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication, QPushButton, QStackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import mysql.connector
from main_scr import Movie
from main_scr import Mainscreen
import sys
from ndphim import Ui_MainWindow1


class xulydatve(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("NOIDUNG")
        self.mainscreen1 = Mainscreen()
        self.ketnoidb1()

    def open(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        self.window.show()

    def ketnoidb1(self):
        if self.mainscreen1.Movie:
            phim1 = self.mainscreen1.Movie[1]
            self.label_2.setText(phim1.GetName())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = xulydatve()
    window1.show()
    sys.exit(app.exec_())
