from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication, QPushButton, QStackedWidget, QTableWidgetItem, QLabel, QSizePolicy,QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import sys
from main_scr import Movie, Mainscreen
from movie_time import Movie_time, Booking_screen
from nddatve import xulydatve

# Trang chủ
class SlideBar(QMainWindow):
    def __init__(self):
        super(SlideBar, self).__init__()
        loadUi("hi.ui", self)

        self.setWindowTitle("SlideBar Menu")
        self.trangchu.clicked.connect(self.switch_trangchu_page)
        self.lichchieu.clicked.connect(self.switch_lichchieu)
        self.tintuc.clicked.connect(self.switch_tintuc)
        self.thanhvien.clicked.connect(self.switch_thanhvien)
        self.trai.clicked.connect(self.switch_truot)
        self.phai.clicked.connect(self.switch_truot)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.switch_truot)
        self.timer.start(3000)

        self.mainscreen = Mainscreen()
        self.ketnoidb()

        self.pushButton_6.clicked.connect(self.chuyen_anh1)
        self.pushButton_7.clicked.connect(self.chuyen_anh2)
        self.pushButton_13.clicked.connect(self.chuyen_anh3)

        # Đường dẫn tới các hình ảnh
        image_paths = [
            "D:/LTUD/pythonProject5/Quỷ Ám Tín Đồ.png",
            "D:/LTUD/pythonProject5/tải xuống (2).jpg",
            "D:/LTUD/pythonProject5/Nhóc Trùm Nối Nghiệp Gia Đình.png",
            "D:/LTUD/pythonProject5/Wolfoo Và Hòn Đảo Kỳ Bí.png",
            "D:/LTUD/pythonProject5/tải xuống.jpg",
            "D:/LTUD/pythonProject5/tải xuống (1).jpg",
            "D:/LTUD/pythonProject5/Thám Tử Lừng Danh Conan Tàu Ngầm Sắt Màu Đen.png",
            "D:/LTUD/pythonProject5/tải xuống (4).jpg",
            "D:/LTUD/pythonProject5/Học Thuyết.png"
        ]

        self.pixmaps = [QPixmap(path) for path in image_paths]

        self.update_images()

        self.chuyenphim.clicked.connect(lambda: self.open_movie_page(1,self.pixmaps[0]))
        self.chuyenhinhanh.clicked.connect(lambda: self.open_movie_page(1,self.pixmaps[0]))
        self.chuyenphim_2.clicked.connect(lambda: self.open_movie_page(2,self.pixmaps[0]))
        self.chuyenhinhanh_2.clicked.connect(lambda: self.open_movie_page(2,self.pixmaps[0]))
        self.chuyenphim_3.clicked.connect(lambda: self.open_movie_page(3,self.pixmaps[5]))
        self.chuyenhinhanh_3.clicked.connect(lambda: self.open_movie_page(3,self.pixmaps[5]))
        self.chuyenphim_4.clicked.connect(lambda: self.open_movie_page(4,self.pixmaps[1]))
        self.chuyenhinhanh_4.clicked.connect(lambda: self.open_movie_page(4,self.pixmaps[1]))
        self.chuyenphim_5.clicked.connect(lambda: self.open_movie_page(5,self.pixmaps[0]))
        self.chuyenhinhanh_5.clicked.connect(lambda: self.open_movie_page(5,self.pixmaps[0]))
        self.chuyenphim_6.clicked.connect(lambda: self.open_movie_page(6,self.pixmaps[4]))
        self.chuyenhinhanh_6.clicked.connect(lambda: self.open_movie_page(6,self.pixmaps[4]))

        self.pushButton.clicked.connect(lambda : self.open_movie_page(6,self.pixmaps[4]))
        self.pushButton_2.clicked.connect(lambda: self.open_movie_page(3, self.pixmaps[5]))
        self.pushButton_3.clicked.connect(lambda: self.open_movie_page(4, self.pixmaps[1]))
    def update_images(self):
        self.anh1.setPixmap(self.pixmaps[0])
        self.label_7.setPixmap(self.pixmaps[1])
        self.anh1_5.setPixmap(self.pixmaps[2])
        self.anh2.setPixmap(self.pixmaps[3])
        self.label_5.setPixmap(self.pixmaps[1])
        self.label.setPixmap(self.pixmaps[4])
        self.label_13.setPixmap(self.pixmaps[4])
        self.label_14.setPixmap(self.pixmaps[1])
        self.label_15.setPixmap(self.pixmaps[4])
        self.label_12.setPixmap(self.pixmaps[5])
        self.label_6.setPixmap(self.pixmaps[5])
        self.label_16.setPixmap(self.pixmaps[5])
        self.anh1_2.setPixmap(self.pixmaps[6])
        self.anh1_3.setPixmap(self.pixmaps[7])
        self.anh1_4.setPixmap(self.pixmaps[8])

    def open_movie_page(self, movie_index, pixmap):
        page1.update_content(movie_index,pixmap)
        widget.setCurrentIndex(1)

    def switch_trangchu_page(self):
        self.stackedWidget.setCurrentIndex(0)

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
        else:
            print("No movies found")

# Trang nội dung thông tin phim
class xulydatve(QMainWindow):
    def __init__(self):
        super(xulydatve, self).__init__()
        loadUi("noidungphim.ui", self)
        self.setWindowTitle("NOIDUNG")
        self.mscr = Mainscreen()
        self.dulieu = Booking_screen()

        self.back.clicked.connect(self.trove)
        self.pushButton_9.clicked.connect(self.ve)
        self.pushButton_10.clicked.connect(self.ve)
        self.pushButton_11.clicked.connect(self.ve)
        self.pushButton_12.clicked.connect(self.ve)
        self.pushButton_13.clicked.connect(self.ve)
        self.pushButton_15.clicked.connect(self.ve)
        self.pushButton_17.clicked.connect(self.ve)
        self.pushButton.clicked.connect(self.thuhai)
        self.pushButton_3.clicked.connect(self.thuba)
        self.pushButton_4.clicked.connect(self.thutu)
        self.pushButton_7.clicked.connect(self.thunam)
        self.pushButton_5.clicked.connect(self.thusau)
        self.pushButton_6.clicked.connect(self.thubay)
        self.pushButton_8.clicked.connect(self.chunhat)

    #Hiện thông tin phim
    def update_content(self, movie,pixmap):
        if self.mscr.Movie:
            phim1 = self.mscr.Movie[movie]
            self.label_2.setText(phim1.GetName())
            self.label_5.setText(phim1.GetDes())
            self.label_6.setText(phim1.GetType())
            self.label_7.setText(phim1.GetTime())
            self.label_9.setText(phim1.getAge_Res())
            self.label.setPixmap(pixmap)


    def trove(self):
        widget.setCurrentIndex(0) #trở về trang đầu

    #lịch chiếu
    def thuhai(self):
        self.stackedWidget.setCurrentIndex(0)
    def thuba(self):
        self.stackedWidget.setCurrentIndex(1)
    def thutu(self):
        self.stackedWidget.setCurrentIndex(2)
    def thunam(self):
        self.stackedWidget.setCurrentIndex(3)
    def thusau(self):
        self.stackedWidget.setCurrentIndex(4)
    def thubay(self):
        self.stackedWidget.setCurrentIndex(5)
    def chunhat(self):
        self.stackedWidget.setCurrentIndex(6)

    def ve(self):
        widget.setCurrentIndex(2) #sang trang đặt vé

# Trang đặt chỗ xem phim
class datve(QMainWindow):
    def __init__(self):
        super(datve, self).__init__()
        loadUi("2.ui", self)
        self.setWindowTitle("DATVE")
        self.pushButton_19.clicked.connect(self.vechonngay)

    def vechonngay(self):
        widget.setCurrentIndex(1)


app = QApplication(sys.argv)
widget = QStackedWidget()
main_window = SlideBar()
page1 = xulydatve()
page2 = datve()
widget.addWidget(main_window)
widget.addWidget(page1)
widget.addWidget(page2)
widget.setFixedWidth(1100)
widget.setFixedHeight(650)
widget.setCurrentIndex(0)
widget.show()
sys.exit(app.exec_())
