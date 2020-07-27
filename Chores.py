from datetime import datetime
from datetime import date
from datetime import timedelta
import mysql.connector

class Chores():
    def __init__(self):
        self.initialize()
        self.check_init()

    def initialize(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="oY$9687jk",
            database="thewall"
        )
        self.cursor = self.db.cursor()
    
    def check_init(self):
        today = date.today()
        sql = f"select * from freq_chore_log where date_chore = '{today.strftime('%Y-%m-%d')}'"
        self.cursor.execute(sql)
        l = len(self.cursor.fetchall())
        if l == 0:
            sql = f"insert into freq_chore_log (id, chore_name, recom_time, date_chore) select ch_id, chore_name, recom_time, '{today.strftime('%Y-%m-%d')}'  from freq_chore_desc"
            self.cursor.execute(sql)
            self.db.commit()
            print("Chores initiated!")
        else:
            pass
        
        self.update_list()
        
    def update_list(self):
        sql = f"select * from freq_chore_log where date_chore = '{datetime.now().strftime('%Y-%m-%d')}'"
        self.cursor.execute(sql)
        self.list = self.cursor.fetchall()
    
    def display(self):
        for i in self.list:
            if i[-1] == 0:
                print(tuple([i[1], i[2], i[4]]))
            else:
                pass
    
    def mark_completed(self, idc):
        sql = f"UPDATE freq_chore_log SET comp_time = %s, stat = %s WHERE id = %s and date_chore = %s"
        val = (datetime.now().strftime('%H:%M:%S'), 1, idc, datetime.now().strftime('%Y-%m-%d'))
        self.cursor.execute(sql, val)
        self.db.commit()
        self.update_list()
        print(f"id: {idc} marked as complete!")


chore = Chores()


print("Chores Compiled and ready to use!")
                