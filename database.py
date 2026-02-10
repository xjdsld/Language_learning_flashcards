import sqlite3

class Database:
    def __init__(self, database):
        self.database = database

    def create_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT,word TEXT,translation TEXT, sentence TEXT)""")
        connection.commit()
        connection.close()
