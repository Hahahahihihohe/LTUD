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

    def Update(self,picked_seat, user):
        if user.GetMoney() < len(picked_seat) * 55000:
            print("khong du tien")
            return False
        #picked_seat là một mảng numpy có shape (n,2), đặt n chỗ, mỗi chỗ gồm tọa độ (cot va hang)
        seat_list = list(self.seat)
        for i in range(picked_seat.shape[0]):
            seat_list[picked_seat[i][0]*10 + picked_seat[i][1]] = '1'
        self.seat = ''.join(seat_list)
        sql = "update movie_time set seat = %s where id = %s"
        db.execute(sql, [self.seat, self.id])
        db.mydb.commit()
        sql = "INSERT INTO order_history (user_id, movie_name,price,time) VALUES (%s, %s, %s , %s)"
        db.execute(sql, [user.id, self.name[0],55000 * len(picked_seat), str(datetime.now())])
        db.mydb.commit()
        user.stinks(55000 * len(picked_seat))
        sql = "update user_info set money = %s where id = %s"
        db.execute(sql,[user.GetMoney(),user.id])
        db.mydb.commit()
        print("Mua thanh cong")
        return True
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


    def ShowMovieTime(self,movie_id):
        # hiển thị toàn bộ lịch chiếu của phim đó
        list1 = []
        for i in self.list:
            if i.movie_id == str(movie_id):

                list1.append(i)

        return list1

    def GetMovie(self,id):
        for i in self.list:
            if i.id == str(id):
                return i