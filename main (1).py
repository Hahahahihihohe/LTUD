from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication, QPushButton, QStackedWidget,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import mysql.connector
from main_scr import Movie
from main_scr import Mainscreen
# from ndphim import Ui_MainWindow1
# from nddatve import xulydatve

import sys
class slidebar(QMainWindow):
    def __init__(self):
        super(slidebar, self).__init__()
        loadUi("trangchu.ui", self)

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
        self.pushButton_13.clicked.connect(self.chuyen_anh3)

        image_path = "C:/Pycharm/ltud/Quỷ Ám Tín Đồ.png"
        image1 = "C:/Pycharm/ltud/tải xuống (2).jpg"
        img2 = "C:/Pycharm/ltud/Nhóc Trùm Nối Nghiệp Gia Đình.png"
        img3 = "C:/Pycharm/ltud/Wolfoo Và Hòn Đảo Kỳ Bí.png"
        img4 = "C:/Pycharm/ltud/tải xuống.jpg"
        img5 = "C:/Pycharm/ltud/tải xuống (1).jpg"
        img6 = "C:/Pycharm/ltud/Thám Tử Lừng Danh Conan Tàu Ngầm Sắt Màu Đen.png"
        img7 = "C:/Pycharm/ltud/tải xuống (4).jpg"
        img8 = "C:/Pycharm/ltud/Học Thuyết.png"

        p8 = QPixmap(img8)
        p3 = QPixmap(img3)
        p1 = QPixmap(image1)
        p = QPixmap(image_path)
        p4 = QPixmap(img4)
        p2 = QPixmap(img2)
        p5 = QPixmap(img5)
        p6 = QPixmap(img6)
        p7 = QPixmap(img7)
        #self.chuyenphim.clicked.connect(self.open)
        # Lấy QLabel có tên là 'anh1' từ giao diện
        #self.anh1 = self.findChild(QLabel, 'anh1')
        self.chuyenphim.clicked.connect(self.open)
        # Đặt hình ảnh vào QLabel 'anh1'
        self.kt = 0


        self.anh1.setPixmap(p)
        self.label_7.setPixmap(p1)
        self.anh1_5.setPixmap(p2)
        self.anh2.setPixmap(p3)
        self.label_5.setPixmap(p1)
        self.label.setPixmap(p4)
        self.label_13.setPixmap(p4)
        self.label_14.setPixmap(p1)
        self.label_15.setPixmap(p4)
        self.label_12.setPixmap(p5)
        self.label_6.setPixmap(p5)
        self.label_16.setPixmap(p5)
        self.anh1_2.setPixmap(p6)
        self.anh1_3.setPixmap(p7)
        self.anh1_4.setPixmap(p8)
        #self.chuyenphim.clicked.connect(self.emit_chuyenphim_clicked)



    def open(self):
        widget.setCurrentIndex(1)


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

    def chuyen_anh3(self):
        self.stackedWidget_3.setCurrentIndex(2)
    def ketnoidb(self):
        if self.mainscreen.Movie:
            p1 = self.mainscreen.Movie[1]
            self.phim1.setText(p1.GetName())
            self.phim1_2.setText(p1.GetType())
            p2 = self.mainscreen.Movie[2]
            self.phim2.setText(p2.GetName())
            self.phim2_1.setText(p2.GetType())
            p3 = self.mainscreen.Movie[3]
            self.phim1_3.setText(p3.GetName())
            self.phim1_4.setText(p3.GetType())
            p4 = self.mainscreen.Movie[4]
            self.phim1_5.setText(p4.GetName())
            self.phim1_6.setText(p4.GetType())
            p5 = self.mainscreen.Movie[5]
            self.phim1_7.setText(p5.GetName())
            self.phim1_8.setText(p5.GetType())
            p6 = self.mainscreen.Movie[6]
            self.phim1_9.setText(p6.GetName())
            self.phim1_10.setText(p6.GetType())
            #self.anh1.pick_movie(1)
            #pixmap1 = self.mainscreen.load_cover(1)
            # self.anh1.setPixmap(pixmap1)
            #self.label_movie_description.setText(first_movie.GetDes())  # Assuming you have a label to show movie description
        else:
            print("No movies found")

class xulydatve(QMainWindow):
    def __init__(self):
        super(xulydatve, self).__init__()
        loadUi("noidungphim.ui", self)
        self.setWindowTitle("NOIDUNG")
        self.mainscreen1 = Mainscreen()
        self.ketnoidb1()
        self.pushButton_3.clicked.connect(self.trove)

    def trove(self):
        widget.setCurrentIndex(0)
    def ketnoidb1(self):
        if self.mainscreen1.Movie:
            phim1 = self.mainscreen1.Movie[1]
            self.label_2.setText(phim1.GetName())


app = QApplication(sys.argv)
widget = QStackedWidget()
main_window = slidebar()
page1 = xulydatve()
widget.addWidget(main_window)
widget.addWidget(page1)
widget.setFixedWidth(1040)
widget.setFixedHeight(600)
widget.setCurrentIndex(0)
widget.show()
sys.exit(app.exec_())