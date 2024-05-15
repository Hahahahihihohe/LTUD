from database import db
import numpy as np
class Movie():
    def __init__(self, name = None, type = None, duration = None, actor = None, age_res = None, des = None, cover = None):
        self.name = name
        self.type = type
        self.duration = duration
        self.des = des
        self.age_res = age_res
        self.actor = actor
        self.cover = cover

class Mainscreen():
    def __init__(self):
        self.Movie = np.array([])

    def load_movie(self):
        sql = "Select * from movie"
        res = np.array(db.fetchall(sql))
        for i in res:
            self.Movie = np.append(self.Movie, Movie(name = i[1]
                                                     ,type = i[2]
                                                     ,duration=i[3]
                                                     ,actor=i[4]
                                                     ,age_res=i[5]
                                                     ,des=i[6]
                                                     ,cover=i[7]))


