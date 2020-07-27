from datetime import datetime
from datetime import date
from datetime import timedelta
import mysql.connector



class Tasker_Item():
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="oY$9687jk",
            database="thewall"
        )

        self.cursor = self.db.cursor()

    
    def insert(self):
        tsk = input("Enter Task:\t").strip()
        sql = "INSERT INTO tasker (task, startDate, endDate, status) VALUES (%s, %s, %s, %s)"
        val = (tsk, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None, 0)
        self.cursor.execute(sql, val)
        self.db.commit()
        print(self.cursor.rowcount, "record inserted.")
    
    def completed(self, idt):
        for i in idt:
            sql = "UPDATE tasker SET endDate = %s, status = %s WHERE id = %s"
            val = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1, i)
            self.cursor.execute(sql, val)
            self.db.commit()
            print(self.cursor.rowcount, "record updated.")
            
    def get_status(self, stat = 0):
        if stat not in (0,1):
            print("Status should be either 0 (pending) or 1 (completed)")
        else:
            idt = [] 
            sql = f"SELECT id from tasker where status = {stat}"
            self.cursor.execute(sql)
            r = self.cursor.fetchall()
            for i in r:
                idt.append(i[0])
            self.display(idt)
    
    def display(self, idt = [0]):
        if idt == [0]:
            self.cursor.execute("SELECT * FROM tasker")
            r = self.cursor.fetchall()
            for i in r:
                print([j for j in i])
        else:
            for i in idt:
                sql = f'SELECT * FROM tasker WHERE id = {i}'
                self.cursor.execute(sql)
                r = self.cursor.fetchall()
                for i in r:
                    print([j for j in i])


task = Tasker_Item()


print("Tasker Compiled and ready to use!")
                
            
