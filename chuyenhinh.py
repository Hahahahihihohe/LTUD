from trangchu import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication, QPushButton, QStackedWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import mysql.connector
from main_scr import Movie
from main_scr import Mainscreen
from ndphim import Ui_MainWindow1
from nddatve import xulydatve

import sys
class slidebar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setCentralWidget(self.ui)
        self.setWindowTitle("SlideBar Menu")
       # self.icon_name_widget.setHidden(True)
        self.trangchu.clicked.connect(self.switch_trangchu_page)
        self.trai.clicked.connect(self.switch_truot)
        self.phai.clicked.connect(self.switch_truot)
        self.lichchieu.clicked.connect(self.switch_lichchieu)
        self.tintuc.clicked.connect(self.switch_tintuc)
        self.thanhvien.clicked.connect(self.switch_thanhvien)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.switch_truot)
        self.timer.start(3000)
        self.mainscreen = Mainscreen()
        self.ketnoidb()
        self.pushButton_6.clicked.connect(self.chuyen_anh1)
        self.pushButton_7.clicked.connect(self.chuyen_anh2)
        image_path = "D:/LTUD/pythonProject5/Quỷ Ám Tín Đồ.png"
        pixmap = QPixmap(image_path)
        self.current_window = None
        self.chuyenphim.clicked.connect(self.open)
        # Lấy QLabel có tên là 'anh1' từ giao diện
        #self.anh1 = self.findChild(QLabel, 'anh1')

        # Đặt hình ảnh vào QLabel 'anh1'
        self.anh1.setPixmap(pixmap)

    def open(self):
        if self.current_window:
            self.current_window.close()

        self.current_window = QtWidgets.QMainWindow()
        self.ui = xulydatve()
        self.ui.setupUi(self.current_window)
        self.current_window.show()

    def switch_trangchu_page(self):
        self.stackedWidget.setCurrentIndex(0)
        #self.stackedWidget_2.setCurrentIndex(0)
    def switch_lichchieu(self):
        self.stackedWidget.setCurrentIndex(1)
    def switch_tintuc(self):
        self.stackedWidget.setCurrentIndex(2)
    def switch_thanhvien(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_truot(self):
        current_index = self.stackedWidget_2.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget_2.count()
        self.stackedWidget_2.setCurrentIndex(next_index)
    def chuyen_anh1(self):
        self.stackedWidget_3.setCurrentIndex(0)

    def chuyen_anh2(self):
        self.stackedWidget_3.setCurrentIndex(1)
    def ketnoidb(self):
        if self.mainscreen.Movie:
            p1 = self.mainscreen.Movie[1]
            self.phim1.setText(p1.GetName())
            self.phim1_2.setText(p1.GetType())
            p2 = self.mainscreen.Movie[2]
            self.phim2.setText(p2.GetName())
            self.phim2_1.setText(p2.GetType())


            #self.anh1.pick_movie(1)
            #pixmap1 = self.mainscreen.load_cover(1)
            # self.anh1.setPixmap(pixmap1)
            #self.label_movie_description.setText(first_movie.GetDes())  # Assuming you have a label to show movie description
        else:
            print("No movies found")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = slidebar()
    main_window.show()
    sys.exit(app.exec_())