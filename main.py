from login import Login
import mysql.connector
from database import db
import numpy as np
from user import User
sql = """
SHOW COLUMNS FROM movie;
"""
res = np.array(db.fetchall(sql))
print(res)










