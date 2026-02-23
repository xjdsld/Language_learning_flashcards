import sqlite3
import logging
import random
from session import Card

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        logger.info("Database table created or already exists.")

    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT,word TEXT,translation TEXT, sentence TEXT)""")
        self.connection.commit()

    def create_card(self):
        self.cursor.execute("SELECT word, translation, sentence FROM words")
        rows = self.cursor.fetchall()
        if not rows:
            logger.warning("No words found in the database to create a card.")
            print("No words to learn")
            return None
            
        row = random.choice(rows)
        word = row[0]
        translation = row[1]
        sentence = row[2]
        logger.info(f"Created a card with word: {word}, translation: {translation}")
        return Card(word, translation, sentence)

    def add_card(self, card):
        try:
            self.cursor.execute("""INSERT INTO words (word, translation, sentence) VALUES (?, ?, ?)""", (card.word, card.translation, card.sentence))
            self.connection.commit()
        except sqlite3.Error as error:
            logger.error(f"Error adding card to the database{error}")
            raise

    def get_all_cards(self):
        self.cursor.execute("SELECT word, translation, sentence FROM words")
    
        return self.cursor.fetchall()
        
