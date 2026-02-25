import logging_set
import random
from database import Database
from session import Card
from translation_service import Translation

logger = logging.getLogger(__name__)


def menu():
    database = Database()
    database.create_db()
    translation = Translation()
    print("======Welcome to the Main Menu=======")
    print("To start a new learning session press - 1")
    print("To add a new word press - 2")
    user_choice = int(input("Select how you want to proceede"))
    logger.info(f"User selected {user_choice}")
    try:
       if user_choice == 1:
            cards = database.get_all_cards()
            if not cards:
                print("No words to show")
                
            random.shuffle(cards)
            print("======NEW LEARNING SESSION======")
            for i, card in cards enumerate(cards, start=1)
                print(f"Word: {card.word}")
                input("Press Enter to reveal translation...")
                print(f"Translation: {card.translation}")
                print(f"Example: {card.sentence}")
                logger.info(card.word, card.translation)
       elif user_choice == 2:
                word = input("Enter English word: ")
                logger.info(f"Addd a new word {word}")
                translation = translation.translate(word)
                sentence = input("Enter example sentence: ")
                card = Card(word, translation, sentence)
                database.add_card(card)
                print("Card added successfully.")

       else:
           print("Please enter either 1 or 2")
           logger.info(f"Invalid choice : {user_choice}")
    except ValueError:
        print("Please enter a number")
        logger.warning(f"Invalid choice: {user_choice}")

if __name__ == "__main__":
    menu()
