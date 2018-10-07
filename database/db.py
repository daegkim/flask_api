import urllib
import pymysql
import settings


class db:
    def __init__(self, db_name):
        self.db_setting = settings.db_setting(db_name)
        self.conn = type(pymysql.connections.Connection)
        self.cursor = type(pymysql.cursors.Cursor)

    def db_connection(self):
        self.conn = pymysql.connect(host=self.db_setting.host, port=self.db_setting.port, user=self.db_setting.user, passwd=self.db_setting.pwd, db=self.db_setting.db_name,charset='utf8',autocommit=True)
        self.cursor = self.conn.cursor()

    def setVehicle(self,num):
        query = 'INSERT INTO vehicle2 (number) VALUES (%s)'
        self.cursor.execute(query,(num))
        self.conn.commit()

    def db_end(self):
        self.conn.close()
