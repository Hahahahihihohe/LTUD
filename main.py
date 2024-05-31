from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QApplication, QPushButton, QStackedWidget, \
    QTableWidgetItem, QLabel, QSizePolicy, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import sys
from main_scr import Movie, Mainscreen
from movie_time import Movie_time, Booking_screen
from nddatve import xulydatve
import numpy as np
from user import User

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

        self.chuyenphim.clicked.connect(lambda: self.open_movie_page(1, self.pixmaps[0], 1))
        self.chuyenhinhanh.clicked.connect(lambda: self.open_movie_page(1, self.pixmaps[0], 1))
        self.chuyenphim_2.clicked.connect(lambda: self.open_movie_page(2, self.pixmaps[0], 2))
        self.chuyenhinhanh_2.clicked.connect(lambda: self.open_movie_page(2, self.pixmaps[0], 2))
        self.chuyenphim_3.clicked.connect(lambda: self.open_movie_page(3, self.pixmaps[5], 3))
        self.chuyenhinhanh_3.clicked.connect(lambda: self.open_movie_page(3, self.pixmaps[5], 3))
        self.chuyenphim_4.clicked.connect(lambda: self.open_movie_page(4, self.pixmaps[1], 4))
        self.chuyenhinhanh_4.clicked.connect(lambda: self.open_movie_page(4, self.pixmaps[1], 4))
        self.chuyenphim_5.clicked.connect(lambda: self.open_movie_page(5, self.pixmaps[0], 5))
        self.chuyenhinhanh_5.clicked.connect(lambda: self.open_movie_page(5, self.pixmaps[0], 5))
        self.chuyenphim_6.clicked.connect(lambda: self.open_movie_page(6, self.pixmaps[4], 6))
        self.chuyenhinhanh_6.clicked.connect(lambda: self.open_movie_page(6, self.pixmaps[4], 6))

        self.pushButton.clicked.connect(lambda: self.open_movie_page(6, self.pixmaps[4], 6))
        self.pushButton_2.clicked.connect(lambda: self.open_movie_page(3, self.pixmaps[5], 3))
        self.pushButton_3.clicked.connect(lambda: self.open_movie_page(4, self.pixmaps[1], 4))

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

    def open_movie_page(self, movie_index, pixmap, movie_id):
        page1.update_content(movie_index, pixmap, movie_id)
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

        self.current_movie_id = None
        self.current_hour = None
        self.current_id = None
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
        #self.p12.clicked.connect(self.ve)
        #self.p11.clicked.connect(self.select_hour)
        for i in range(1, 6):
            for j in range(1, 8):
                button = getattr(self, f'p{i}{j}', None)
                if button:
                    button.clicked.connect(self.select_hour)
    def getidnh(self, movie_id, hour):
        for movie_time in self.dulieu.list:
            if movie_time.movie_id == str(movie_id) and movie_time.hour == hour:
                return movie_time.id
        return None  # Trả về None nếu không tìm thấy ID
    def select_hour(self):
        sender = self.sender()
        self.current_hour = sender.text()




        # Lấy id và movie_id từ danh sách Movie_time
        self.current_id  = self.getidnh(self.current_movie_id , self.current_hour)
        page2.update_seat_status(self.current_id)
        page2.idt(self.current_movie_id , self.current_hour ,self.current_id)
        print(f"Selected hour: {self.current_hour}, Movie ID: {self.current_movie_id}, ID: {self.current_id}")
        widget.setCurrentIndex(2)
        user = User()
        user.update_info(3)

    def ve(self):

        #widget.datve.update_seat_status(self.current_movie_id, self.current_hour)
        widget.setCurrentIndex(2)
        # else:
        #     QMessageBox.warning(self, "Lỗi", "Chưa chọn phim hoặc giờ chiếu.")

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

    def update_content(self, movie, pixmap, movie_id):
        if self.mscr.Movie:
            phim1 = self.mscr.Movie[movie_id]
            self.label_2.setText(phim1.GetName())
            self.label_5.setText(phim1.GetDes())
            self.label_6.setText(phim1.GetType())
            self.label_7.setText(phim1.GetTime())
            self.label_9.setText(phim1.getAge_Res())
            self.label.setPixmap(pixmap)
            self.lichchieu(movie_id)
            self.current_movie_id = movie_id
            print(movie_id)

    def lichchieu(self, movie_id):
        movie_times = self.dulieu.ShowMovieTime(movie_id)
        schedule_by_day = {}

        for movie_time in movie_times:
            day = movie_time.day
            hour = movie_time.hour
            if day in schedule_by_day:
                schedule_by_day[day].append(hour)
            else:
                schedule_by_day[day] = [hour]

        for day, hours in schedule_by_day.items():
            schedule_by_day[day] = sorted(hours)

        self.update_day_buttons(schedule_by_day)

    def update_day_buttons(self, schedule_by_day):
        button_names = {
            '22/5': ['p11', 'p12', 'p13', 'p14', 'p15', 'p16', 'p17'],
            '23/5': ['p21', 'p22', 'p23', 'p24', 'p25', 'p26', 'p27'],
            '24/5': ['p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p37'],
            '25/5': ['p41', 'p42', 'p43', 'p44', 'p45', 'p46', 'p47'],
            '26/5': ['p51', 'p52', 'p53', 'p54', 'p55', 'p56', 'p57']
        }

        for day, buttons in button_names.items():
            if day not in schedule_by_day:
                for button_name in buttons:
                    button = getattr(self, button_name, None)
                    if button:
                        button.setText("")
                        button.setVisible(False)
            else:
                hours = schedule_by_day[day]
                for i, button_name in enumerate(buttons):
                    button = getattr(self, button_name, None)
                    if button:
                        if i < len(hours):
                            button.setText(hours[i])
                            button.setVisible(True)
                        else:
                            button.setText("")
                            button.setVisible(False)

    def trove(self):
        widget.setCurrentIndex(0)



# Trang đặt chỗ xem phim
class datve(QMainWindow):
    def __init__(self):
        super(datve, self).__init__()
        loadUi("2.ui", self)
        self.setWindowTitle("DATVE")
        self.pushButton_19.clicked.connect(self.vechonngay)
        self.selected_seats = []
        self.current_movie_id = None
        self.current_hour = None
        self.current_id = None
        self.dulieu = Booking_screen()
        self.connect_seat_buttons()
        img = "D:/LTUD/pythonProject5/images.png"
        p = QPixmap(img)
        self.pushButton_pay.clicked.connect(self.pay)
        self.lblB6_38.setPixmap(p)
        self.update_price()
        #self.idt()

    def vechonngay(self):
        xacnhan = QMessageBox.question(self, "Xác nhận hủy vé", "Bạn có muốn hủy vé đã chọn?",QMessageBox.Yes | QMessageBox.No)
        if xacnhan == QMessageBox.Yes:
            # Xóa thông tin vé đã chọn
            self.selected_seats = []
            # Cập nhật lại trạng thái ghế
            self.update_seat_status(self.current_movie_id)
            self.update_price()
            widget.setCurrentIndex(1)
        else:
            return
        #widget.setCurrentIndex(1)
    def idt(self, movie_id ,hour, id):
        self.current_movie_id = movie_id
        self.current_hour = hour
        self.current_id = id
    def connect_seat_buttons(self):
        for i in range(10):
            for j in range(10):
                button_name = f"p{i + 1}{chr(97 + j)}"
                button = getattr(self, button_name, None)
                if button:
                    button.clicked.connect(lambda _, b=button_name: self.handle_seat_selection(b))

    def handle_seat_selection(self, button_name):
        button = getattr(self, button_name, None)
        if button and button.isEnabled():
            if button_name in self.selected_seats:
                self.selected_seats.remove(button_name)
                button.setStyleSheet("background-color: white")  # Reset style
            else:
                self.selected_seats.append(button_name)
                button.setStyleSheet("background-color: yellow")  # Highlight selected seat
                print("Ghế được chọn:", button_name)
                # row = int(button_name[1:]) - 1  # Lấy số hàng từ tên nút
                # col = ord(button_name[0]) - ord('p')  # Lấy số cột từ tên nút
                # print("Vị trí:", row, col)

        self.update_price()

    def update_price(self):
        price_per_seat = 55000
        total_price = price_per_seat * len(self.selected_seats)
        self.label_price.setText(f"Giá tiền: {total_price} VND")
        #total_price = 0
    def update_seat_status(self, id):
        x = self.dulieu.GetMovie(id)
        seat_matrix = x.GetBookingState()

        print("Seat matrix:", seat_matrix)  # In ra dãy seat_matrix để kiểm tra

        for i in range(10):
            for j in range(10):
                button_name = f"p{i + 1}{chr(97 + j)}"
                button = getattr(self, button_name, None)
                if button:
                    if seat_matrix[i, j] == 1:  # Sử dụng số nguyên 1 thay vì chuỗi '1'
                        button.setEnabled(False)
                        button.setStyleSheet("background-color: red")  # Highlight booked seat
                    else:
                        button.setEnabled(True)
                        button.setStyleSheet("background-color: white")  # Reset style for available seat

    def pay(self):
        if not self.selected_seats or not self.current_movie_id or not self.current_hour:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ghế và đặt giờ chiếu.")
            return

        confirmation = QMessageBox.question(self, "Xác nhận thanh toán", "Bạn có muốn thanh toán cho các vé đã chọn?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.No:
            return
        else :
        # movie_time = self.dulieu.GetMovie(self.current_movie_id, self.current_hour)
        # seat_coords = []
        # for seat in self.selected_seats:
        #     row = int(seat[1]) - 1
        #     col = ord(seat[2]) - 97
        #     seat_coords.append([row, col])
        #
        # seat_array = np.array(seat_coords)
        # success = movie_time.Update(seat_array)

        #if success:
            QMessageBox.information(self, "Thành công", "Đặt vé thành công!")
            #self.update_seat_status(self.current_id)  # Cập nhật trạng thái ghế sau khi đặt vé thành công
            #self.selected_seats = []  # Đặt lại danh sách ghế đã chọn
            widget.setCurrentIndex(1)
        # else:
        #     QMessageBox.warning(self, "Thất bại", "Đặt vé thất bại. Vui lòng thử lại sau.")


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
