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
        self.thanhvien.clicked.connect(self.mem_wd)

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
        widget.setCurrentIndex(7)


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
    def mem_wd(self):
        widget.setCurrentIndex(2)

#đặt vé(7)
class xulydatve(QMainWindow):
    def __init__(self):
        super(xulydatve, self).__init__()
        loadUi("noidungphim.ui", self)
        self.setWindowTitle("NOIDUNG")
        self.mainscreen1 = Mainscreen()
        self.ketnoidb1()
        self.pushButton_3.clicked.connect(self.trove)

    def trove(self):
        widget.setCurrentIndex(6)
    def ketnoidb1(self):
        if self.mainscreen1.Movie:
            phim1 = self.mainscreen1.Movie[1]
            self.label_2.setText(phim1.GetName())





app = QApplication(sys.argv)
widget = QStackedWidget()

login_f = login_wd()
register_f = register_wd()
acc_info_f = acc_info()
forgot_f = forgot_pw()
change_password_f = change_password()
change_info_wd_f = change_info_wd()
main_window = slidebar()
page1 = xulydatve()
widget.addWidget(login_f)
widget.addWidget(register_f)
widget.addWidget(acc_info_f)
widget.addWidget(forgot_f)
widget.addWidget(change_password_f)
widget.addWidget(change_info_wd_f)
widget.addWidget(main_window)
widget.addWidget(page1)

widget.setCurrentIndex(0)
widget.setFixedWidth(1010)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
