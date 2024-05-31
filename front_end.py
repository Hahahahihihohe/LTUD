from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QHeaderView, QApplication, QStackedWidget,QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from main_scr import Mainscreen
import sys
from login import Login
from user import User
from main_scr import Movie, Mainscreen
from movie_time import Movie_time, Booking_screen

import numpy as np

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
            acc_info_f.stackedWidget.setCurrentIndex(0)
            widget.setCurrentIndex(6)
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
        self.setWindowTitle("Register Window")  # Đặt tiêu đề cho cửa sổ đăng ký

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
        self.change_info.clicked.connect(self.switch_changeinfo_wd)
        self.logout.clicked.connect(self.switch_login)
        self.combo_box = QtWidgets.QComboBox()
        self.connect_combo_box()
        self.nt_btn.clicked.connect(self.nap_tien)
        self.back.clicked.connect(self.gobackmainmenu)
    def switch_user(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_his(self):
        self.update_order_history()  # Cập nhật lịch sử giao dịch
        self.stackedWidget.setCurrentIndex(1)

    def switch_money(self):
        self.stackedWidget.setCurrentIndex(2)
        self.cur_money.setText(str(self.user.GetMoney()))



    def gobackmainmenu(self):
        widget.setCurrentIndex(6)

    def show(self):
        # Hiển thị thông tin người dùng trên giao diện
        self.user_name_2.setText(self.user.GetName())
        self.user_age_2.setText(str(self.user.GetAge()))
        self.user_money_2.setText(str(self.user.GetMoney()))



    def switch_changepw_wd(self):
        widget.setCurrentIndex(4)
    def switch_changeinfo_wd(self):
        widget.setCurrentIndex(5)
    def switch_login(self):
        widget.setCurrentIndex(0)

    def connect_combo_box(self):
        self.combo_box.currentIndexChanged.connect(self.handle_combo_box_change)

    def handle_combo_box_change(self, index):
        selected_value = self.nt.currentText()

        #Xử lý từng giá trị của Combobox
        if selected_value == "50000":
            self.stonks(50000)
        elif selected_value == "100000":
            self.stonks(100000)
        elif selected_value == "200000":
            self.stonks(200000)
        elif selected_value == "100000":
            self.stonks(500000)
        elif selected_value == "500000":
            self.stonks(1000000)
        else:
            self.stonks(2000000)

    def update_money_display(self):
        self.user_money_2.setText(str(self.user.GetMoney()))  # Cập nhật số tiền ở stackedwidget 1
        self.cur_money.setText(str(self.user.GetMoney()))  # Cập nhật số tiền ở stackedwidget 3
    def nap_tien(self):
        # Xác định số tiền cần nạp từ combobox hoặc text box
        amount = self.nt.currentText()

        amount = int(amount)

        # Gọi phương thức stonks() với số tiền cần nạp
        self.user.stonks(amount)

        QMessageBox.information(self, "Thông báo", "Nạp tiền thành công")

        # Cập nhật giao diện người dùng
        self.update_money_display()

    def update_order_history(self):
        column_count = 3
        self.tableWidget.setColumnCount(column_count)

        # Xóa sạch bảng trước khi cập nhật dữ liệu mới
        self.tableWidget.setRowCount(0)
        order_history = self.user.Getorder()
        if order_history is False:
            QMessageBox.information(self, "Thông báo", "Không có lịch sử giao dịch")
            return

        # Đặt số hàng cho tableWidget
        self.tableWidget.setRowCount(len(order_history))
        # Duyệt qua các giao dịch và điền vào bảng
        for row_num, order in enumerate(order_history):
            for col_num, data in enumerate(order):
                item = QTableWidgetItem(str(data))
                item.setBackground(QColor(255, 255, 255))
                self.tableWidget.setItem(row_num, col_num, item)
        # Thay đổi kích thước cột để vừa với nội dung và không gian có sẵn
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Đảm bảo bảng không vượt quá chiều rộng của widget
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Tùy chọn: Thay đổi kích thước hàng để vừa với nội dung
        self.tableWidget.resizeRowsToContents()

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

#Cửa sổ thay đổi thông tin (5)
class change_info_wd(QMainWindow):
    def __init__(self):
        super(change_info_wd, self).__init__()
        loadUi("change_info_wd.ui", self)
        self.save_btn.clicked.connect(self.save_info)
        self.back.clicked.connect(self.switch_accinfo)

    def save_info(self):
        name = self.change_name_2.text()
        age_text = self.change_age_2.text()

        acc_info_f.user.change_info(name,age_text)
        # Hiển thị thông báo và chuyển đổi sang cửa sổ thông tin cá nhân
        QMessageBox.information(self, "Thông báo", "Cập nhật thông tin thành công")
        acc_info_f.show()
        widget.setCurrentIndex(2)

    def switch_accinfo(self):
        widget.setCurrentIndex(2)








#code pratt
#Trang chủ(6)
class SlideBar(QMainWindow):
    def __init__(self):
        super(SlideBar, self).__init__()
        loadUi("hi.ui", self)

        self.setWindowTitle("SlideBar Menu")
        self.trangchu.clicked.connect(self.switch_trangchu_page)
        self.lichchieu.clicked.connect(self.switch_lichchieu)
        self.tintuc.clicked.connect(self.switch_tintuc)
        self.thanhvien.clicked.connect(self.mem_wd)
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

    def mem_wd(self):
        widget.setCurrentIndex(2)
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
        widget.setCurrentIndex(7)

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
        #print(f"Selected hour: {self.current_hour}, Movie ID: {self.current_movie_id}, ID: {self.current_id}")
        widget.setCurrentIndex(8)
        user = User()
        user.update_info(3)

    def ve(self):

        #widget.datve.update_seat_status(self.current_movie_id, self.current_hour)
        widget.setCurrentIndex(8)
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
            #print(movie_id)

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
        widget.setCurrentIndex(6)



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
        self.pushButton_pay.clicked.connect(self.thanhtoan)
        self.connect_seat_buttons()
        img = "D:/LTUD/pythonProject5/images.png"
        p = QPixmap(img)
        #self.pushButton_pay.clicked.connect(self.pay)
        self.lblB6_38.setPixmap(p)
        self.update_price()
        self.n = 100
        self.vt = np.zeros((self.n, 2))
        self.vt1 = np.zeros((self.n, 2))
        self.i = 0
        #self.idt()
        self.update_and_save()
    def vechonngay(self):
        xacnhan = QMessageBox.question(self, "Xác nhận hủy vé", "Bạn có muốn hủy vé đã chọn?",QMessageBox.Yes | QMessageBox.No)
        if xacnhan == QMessageBox.Yes:
            # Xóa thông tin vé đã chọn
            self.selected_seats = []
            # Cập nhật lại trạng thái ghế
            self.update_seat_status(self.current_movie_id)
            self.update_price()
            widget.setCurrentIndex(6)
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
            row = int(button_name[1]) - 1  # Trừ 1 để chuyển từ 1-based index sang 0-based index
            col = ord(button_name[2]) - ord('a')  # Tính chỉ số cột từ ký tự
            if button_name in self.selected_seats:
                self.selected_seats.remove(button_name)
                button.setStyleSheet("background-color: white")  # Reset style
                index_to_remove = np.where((self.vt == [row, col]).all(axis=1))[0]
                if index_to_remove.size > 0:
                    self.vt = np.delete(self.vt, index_to_remove[0], axis=0)
                    self.vt = np.vstack((self.vt, np.zeros((1, 2))))  # Thêm một hàng mới với giá trị [0, 0]
                    self.i -= 1  # Giảm chỉ số vt_index
            else:
                self.selected_seats.append(button_name)
                button.setStyleSheet("background-color: yellow")  # Highlight selected seat
                #print("Ghế được chọn:", button_name)
                # row = int(button_name[1:]) - 1  # Lấy số hàng từ tên nút
                # col = ord(button_name[0]) - ord('p')  # Lấy số cột từ tên nút
                # print("Vị trí:", row, col)
                #row = int(button_name[1]) - 1  # Trừ 1 để chuyển từ 1-based index sang 0-based index
                if self.i < self.n:
                    self.vt[self.i] = [row, col]
                    self.i += 1
                    # Trích xuất ký tự cột từ tên nút (ký tự thứ 3) và tính chỉ số cột
                #col = ord(button_name[2]) - ord('a')  # Tính chỉ số cột từ ký tự


                #print("Vị trí:", (row, col))
        # x = Booking_screen()
        # mov = x.GetMovie(self.current_id)
        # self.pushButton_pay.clicked.connect()
        # x = mov.Update(self.vt,acc_info_f.user)
        self.vt1 =self.vt
        self.update_price()

    def update_price(self):
        price_per_seat = 55000
        total_price = price_per_seat * len(self.selected_seats)
        self.label_price.setText(f"Giá tiền: {total_price} VND")
        #total_price = 0
    def update_seat_status(self, id):
        x = self.dulieu.GetMovie(id)
        seat_matrix = x.GetBookingState()

        #print("Seat matrix:", seat_matrix)  # In ra dãy seat_matrix để kiểm tra

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

    def update_and_save(self):
        # Lấy ID người dùng từ acc_info
        user_id = acc_info_f.user.GetId()
        # Lấy picked_seat từ self.vt hoặc từ danh sách ghế đã chọn (tùy vào cách bạn lưu trữ)
        picked_seat = self.vt  # Đây là giả định, bạn cần thay thế bằng cách lấy thông tin thực tế
        print(picked_seat)
        print(user_id)
        #self.update(user_id, picked_seat)
    def thanhtoan(self):
        x = Booking_screen()
        print(self.vt1)
        mov = x.GetMovie(self.current_id)
        self.pushButton_pay.clicked.connect()
        kt = mov.Update(self.vt1, acc_info_f.user)
        if(kt == True):
            QMessageBox.question(self, "Thành công")
        else:
            QMessageBox.question(self, "Thất bại")

app = QApplication(sys.argv)
widget = QStackedWidget()

login_f = login_wd()
register_f = register_wd()
acc_info_f = acc_info()
forgot_f = forgot_pw()
change_password_f = change_password()
change_info_wd_f = change_info_wd()
main_window = SlideBar()
page1 = xulydatve()
page2 = datve()
widget.addWidget(login_f)
widget.addWidget(register_f)
widget.addWidget(acc_info_f)
widget.addWidget(forgot_f)
widget.addWidget(change_password_f)
widget.addWidget(change_info_wd_f)
widget.addWidget(main_window)
widget.addWidget(page1)
widget.addWidget(page2)
widget.setCurrentIndex(0)
widget.setFixedWidth(1010)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
