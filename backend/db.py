import sqlite3

class Db():
    def __init__(self,db_name: str):
        self.db_name = db_name

        try: 
            self.conn = sqlite3.connect(self.db_name,check_same_thread = False)
            self.cur = self.conn.cursor()

        except sqlite3.Erorr as e:
            print(e)

    def init_db(self):
        with open('schema.sql') as f:
            self.conn.executescript(f.read())
        self.conn.commit()

    def insert_sample(self):
        with open('sample_data.sql') as f:
            self.conn.executescript(f.read())
        self.conn.commit()