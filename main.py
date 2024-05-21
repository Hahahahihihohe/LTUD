from login import Login
import mysql.connector
from database import db
import numpy as np
from user import User
from main_scr import Mainscreen,Movie
from movie_time import Booking_screen,Movie_time
book = Booking_screen()
x = book.ShowMovieTime(23)
for i in x:
    i.showALL()






