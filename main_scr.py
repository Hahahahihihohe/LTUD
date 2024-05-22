from database import db
import os
import numpy as np
class Movie():
    def __init__(self, id = None, name = None, time = None, des = None, type = None, age_res = None):
        self.id = id
        self.name = name
        self.time = time
        self.des = des
        self.type = type
        self.age_res = age_res
        self.cover = None

    #một vài hàm để lấy giá trị mong muốn
    def GetId(self):
        #Trả về id
        return self.id

    def GetName(self):
        #trả về tên phim
        return self.name

    def time(self):
        #Trả về thời lượng phim
        return self.time

    def GetDes(self):
        #Trả về mô tả phim
        return self.des

    def GetType(self):
        #Trả về thể loại phim
        return self.type

    def getAge_Res(self):
        # Trả về giới hạn độ tuổi
        return self.age_res

class Mainscreen():
    def __init__(self):
        self.Movie = []
        self.load_movie()

    def load_movie(self):
        #load tất cả phim, self.Movie là một list
        sql = "Select ID, TENPHIM, THOILUONG, NOIDUNG, THELOAI, TUOI from movie"
        res = np.array(db.fetchall(sql))
        print(res.shape)
        for i in res:
            id , name, time, des, type, age_res = i
            movie = Movie(id,name, time, des, type,age_res)
            movie.cover = f"{movie.name}.png"
            self.Movie.append(movie)

    def pick_movie(self,id):
        #trả về đối tượng có id mong muốn
        if id > len(self.Movie):
            print("Lỗi ID")
            return 0
        return self.Movie[id-1]

    def load_cover(self,id):
        #load anh cover, ten duong dan la tenphim.png
        sql = """
        SELECT TENPHIM, image FROM movie WHERE id = %s
        """
        res = db.fetchone(sql, [id])
        name, binary_data = res
        file_path = f"{name}.png"
        if os.path.exists(file_path):
            #neu da tai roi thi thoi
            print("thu muc da ton tai")
        else:
            #chua thi tai ve
            with open(file_path, 'wb') as file:
                file.write(binary_data)
            print(f"Image {name} retrieved and saved")

    def load_all_cover(self):
        #load het tat ca anh
        for i in range(len(self.Movie)):
            self.load_cover(i+1)







