from database import db
import numpy as np

class Movie_time():
    def __init__(self):
        self.id = None
        self.name = None
        self.day = None
        self.hour = None
        self.seat = None

    def ShowAll(self):
        #Hiển thị toàn bộ lịch chiếu phim
        sql = "select * from movie_time"
        res = np.array(db.fetchall(sql))
        return res

    def ShowMovieTime(self,movie_id):
        # hiển thị toàn bộ lịch chiếu của phim đó
        sql = "select * from movie_time where movie_id = %s"
        res = np.array(db.fetchall(sql,[movie_id]))
        return res

    def GetBookingState(self,id):
        sql = "select * from movie_time where id = %s"
        res = np.array(db.fetchone(sql, [id]))
        self.id = res[0]
        self.name = None #cai nay lam xong database movie thi tinh
        self.day = res[2]
        self.hour = res[3]
        self.seat = res[4]
        seat = np.zeros((10,10))
        for i in range(seat.shape[0]):
            for j in range(seat.shape[1]):
                seat[i][j] = self.seat[i*10 + j]

        return seat #tra ve mang numpy nhin cho de

    def Update(self,picked_seat):
        #picked_seat là một mảng numpy có shape (n,2), đặt n chỗ, mỗi chỗ gồm tọa độ (cot va hang)
        for i in range(picked_seat.shape[0]):
            self.seat[picked_seat[0]*10 + picked_seat[1]] = 1
        sql = "update movie_time set password = %s where id = %s"
        db.execute(sql, [self.seat, self.user])
        db.mydb.commit()