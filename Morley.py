from datetime import datetime
from datetime import date
from datetime import timedelta
import mysql.connector


class Morley():
    def __init__(self):
        self.now = datetime.now()
        self.today = self.get_today()
        self.initialize()
    
    def initialize(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="oY$9687jk",
            database="thewall"
        )
        self.cursor = self.db.cursor()
        
    def get_today(self):
        if int(self.now.strftime('%H')) in range(0,6):
            return date.today() - timedelta(days = 1)
        else:
            return date.today()
    
    def insert(self, typ = 1):
        sql = "INSERT INTO bob_morley (date_time, bm_type) VALUES (%s, %s)"
        val = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), typ)
        self.cursor.execute(sql, val)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")
    
    def show_last(self):
        sql = "SELECT date_time FROM bob_morley WHERE bm_type = 1 ORDER BY bm_id DESC LIMIT 1"
        self.cursor.execute(sql)
        r = self.cursor.fetchall()
        print(f'Last one at {r[0][0]}')
            
    def count_month(self):
        today = self.today.strftime('%Y-%m-%')
        days = int(self.today.strftime('%d'))
        if int(self.today.strftime('%Y')) == 2020 and int(self.today.strftime('%m')) == 7:
            days = 7
        else:
            pass
        
        sql = f"SELECT COUNT(*) FROM bob_morley WHERE date_time LIKE('{today}') and bm_type = 1"
        self.cursor.execute(sql)
        r = self.cursor.fetchall()
        print(f"Monthly count:\t{r[0][0]}")
        print(f"Monthly average:\t{round(r[0][0]/days,2)}")
    
    def count_week(self):
        days = 7
        start = self.today.strftime('%Y-%m-%d 06:00:00')
        end = self.today + timedelta(days=1)
        end = end.strftime('%Y-%m-%d 06:00:00')
        sql = f"select count(*) from bob_morley where date_time <= '{end}' and date_time >= date_sub('{start}', interval 7 day) and bm_type = 1"
        self.cursor.execute(sql)
        r = self.cursor.fetchall()
        print(f"Weekly count:\t{r[0][0]}")
        print(f"Weekly average: {round(r[0][0]/days,2)}")
        
    
    def count_today(self):
        start = self.today.strftime('%Y-%m-%d 06:00:00')
        print(start)
        sql = f"select count(*) from bob_morley where date_time >= '{start}' and date_time <= date_add('{start}', interval 1 day) and bm_type = 1"
        self.cursor.execute(sql)
        r = self.cursor.fetchall()
        for i in r:
            print([j for j in i])


bob = Morley()


print("Morley Compiled and ready to use!")
        