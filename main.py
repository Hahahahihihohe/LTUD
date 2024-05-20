from login import Login
import mysql.connector
from database import db
import numpy as np
from user import User
mydb = mysql.connector.connect(host="moviedatabase-moviedatabase.e.aivencloud.com"
                                       , user="avnadmin"
                                       , password="AVNS_hkSwZWZPqV6SHYraARW"
                                       , port=14802,
                                       database='client')


mycursor = mydb.cursor()
mycursor.execute("describe movie_time")
res = np.array(mycursor.fetchall())
print(res)








