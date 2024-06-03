from database import db
import numpy as np
from datetime import datetime
class Movie_time():
    def __init__(self, id, name, day, hour , seat):
        self.id = id
        self.movie_id = None
        self.name = name
        self.day = day
        self.hour = hour
        self.seat = seat

    def GetBookingState(self):
        seat = np.zeros((10,10))
        for i in range(seat.shape[0]):
            for j in range(seat.shape[1]):
                seat[i][j] = self.seat[i*10 + j]
        return seat #tra ve mang numpy nhin cho de

    def Update(self, picked_seat, user):
        if user.GetMoney() < len(picked_seat) * 55000:
            print("Không đủ tiền")
            return False

        # picked_seat là một mảng numpy có shape (n,2), đặt n chỗ, mỗi chỗ gồm tọa độ (cot và hang)
        print("Bắt đầu cập nhật ghế")
        seat_list = list(self.seat)
        print("Danh sách ghế trước khi cập nhật:", seat_list)
        print("Ghế đã chọn:", picked_seat)

        for i in range(picked_seat.shape[0]):
            row = int(picked_seat[i][0])
            col = int(picked_seat[i][1])
            print(f"Đang xử lý ghế tại hàng {row}, cột {col}")

            # Kiểm tra điều kiện hợp lệ của tọa độ
            if row >= 0 and row < 10 and col >= 0 and col < 10:
                seat_list[row * 10 + col] = '1'
                print(f"Đã cập nhật ghế tại hàng {row}, cột {col} thành 1")
            else:
                print(f"Tọa độ ({row}, {col}) không hợp lệ, bỏ qua")

        self.seat = ''.join(seat_list)
        print("Danh sách ghế sau khi cập nhật:", self.seat)

        try:
            sql = "UPDATE movie_time SET seat = %s WHERE id = %s"
            db.execute(sql, [self.seat, self.id])
            db.mydb.commit()
            print("Cập nhật ghế thành công trong cơ sở dữ liệu")

            sql = "INSERT INTO order_history (user_id, movie_name, price, time) VALUES (%s, %s, %s, %s)"
            db.execute(sql, [user.id, self.name[0], 55000 * len(picked_seat), str(datetime.now())])
            db.mydb.commit()
            print("Thêm lịch sử đặt vé thành công")

            user.stinks(55000 * len(picked_seat))
            sql = "UPDATE user_info SET money = %s WHERE id = %s"
            db.execute(sql, [user.GetMoney(), user.id])
            db.mydb.commit()
            print("Cập nhật số tiền người dùng thành công")

            print("Mua thành công")
            return True
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
            return False

    def showALL(self):
        print(self.id, self.movie_id, self.name, self.day, self.hour, self.seat)
class Booking_screen():
    def __init__(self):
        self.list = []
        self.ShowAll()

    def ShowAll(self):
        #Hiển thị toàn bộ lịch chiếu phim
        sql = "select * from movie_time"
        res = np.array(db.fetchall(sql))

        for i in res:
            id , movie_id, day, hour, seat = i
            sql = "select TENPHIM from movie where ID = %s"
            res = db.fetchone(sql,[movie_id])
            movie_time = Movie_time(id, res, day, hour, seat)
            movie_time.movie_id = movie_id
            self.list.append(movie_time)

    def ShowMovieTime(self, movie_id):
        # Hiển thị toàn bộ lịch chiếu của phim đó cho ngày cụ thể
        list1 = []
        for i in self.list:
            if i.movie_id == str(movie_id) :
                list1.append(i)

        return list1

    def GetMovie(self,id):
        for i in self.list:
            if i.id == str(id):
                return i
