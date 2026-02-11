import sqlite3
from session import Card

class Database:
    def __init__(self):
        self.database = database
        self.connection = sqlite3.connect('database.db')
        self.cursor = connection.cursor()

    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT,word TEXT,translation TEXT, sentence TEXT)""")
        self.connection.commit()

    def create_card(self):
        self.cursor.execute("SELECT word, translation, sentence FROM words")
        row = self.cursor.fetchone()
        if row is None:
            print("No words to learn")
            return None
            
        word = row[0]
        translation = row[1]
        sentence = row[2]
        return Card(word, translation, sentence)

    def add_card(self):
        self.cursor.execute("""INSERT INTO words (words, translation, sentence) VALUES (?, ?, ?)""", (card.word, card.translation, card.sentence))
        self.connection.commit()

    def get_all_cards(self):
        self.cursor.execute("SELECT * FROM words")
        return self.cursor.fetchall

        
