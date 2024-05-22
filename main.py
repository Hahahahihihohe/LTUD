from login import Login
import mysql.connector
from database import db
import numpy as np
from user import User
from main_scr import Mainscreen,Movie
from movie_time import Booking_screen,Movie_time
print(db.fetchone("select * from order_history"))






