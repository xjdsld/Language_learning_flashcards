import sqlite3
import logging
import random
from session import Card

logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS words (id INTEGER PRIMARY KEY AUTOINCREMENT,word TEXT,translation TEXT, sentence TEXT)""")
        self.connection.commit()
        logger.info("Database table connected.")

    def add_card(self, card):
        try:
            self.cursor.execute("""INSERT INTO words (word, translation, sentence) VALUES (?, ?, ?)""", (card.word, card.translation, card.sentence))
            self.connection.commit()
        except sqlite3.Error as error:
            logger.error(f"Error adding card to the database{error}")
            raise

    def get_all_cards(self):
        self.cursor.execute("SELECT word, translation, sentence FROM words")
        rows = self.cursor.fetchall()
    
        cards = []
    
        for i in rows:
            word = i[0]
            translation = i[1]
            sentence = i[2]
    
            card = Card(word, translation, sentence)
            cards.append(card)
    
        return cards

    def create_card(self):
        cards = self.get_all_cards()
    
        if not cards:
            logger.warning("No words found in the database.")
            return None
    
        return random.choice(cards)
