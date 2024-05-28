import mysql.connector

class database():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="moviedatabase-moviedatabase.e.aivencloud.com"
                                       , user="avnadmin"
                                       , password="AVNS_hkSwZWZPqV6SHYraARW"
                                       , port=14802,
                                       database='client')

    def execute(self,sql_code,param = None):
        cursor = self.mydb.cursor()
        cursor.execute(sql_code,param or [])
        return cursor

    def fetchall(self,sql_code,param = None):
        cursor = self.execute(sql_code,param)
        res = cursor.fetchall()
        return res

    def fetchone(self,sql_code,param = None):
        cursor = self.execute(sql_code,param)
        res = cursor.fetchone()
        return res

db = database()