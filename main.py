from login import Login
import mysql.connector
from database import db
import numpy as np
from user import User
from main_scr import Mainscreen,Movie

sql = """
Select ID, TENPHIM, THOILUONG, NOIDUNG, THELOAI, TUOI from movie
"""
res = np.array(db.fetchall(sql))
print(res)
# main_screen = Mainscreen()
# movie = main_screen.pick_movie(4)
# print(movie.GetName())









