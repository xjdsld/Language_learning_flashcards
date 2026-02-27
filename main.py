import logging_set
import logging
import random
from database import Database
from session import Card
from translation_service import Translation

logger = logging.getLogger(__name__)


def menu():
    database = Database()
    database.create_db()
    translator = Translation()

    while True:
        print("======Welcome to the Main Menu=======")
        print("To start a new learning session press - 1")
        print("To add a new word press - 2")
        print("0 - Exit")

        try:
           user_choice = int(input("Select how you want to proceed:"))
           logger.info(f"User selected {user_choice}")
           if user_choice == 1:
                cards = database.get_all_cards()
                if not cards:
                    print("No words to show")

                random.shuffle(cards)
                print("======NEW LEARNING SESSION======")


                for i, card in enumerate(cards, start=1):
                    print(f"Word: {card.word}")
                    user_input = input("Press Enter to reveal translation or 'q' to quit: ").lower()
                    if user_input == "q":
                        print("Exiting learning session...")
                        break
                    print(f"Translation: {card.translation}")
                    print(f"Example: {card.sentence}")
           elif user_choice == 2:
               while True:
                    word = input("Enter English word (press 'f' to exit): ").lower()
                    if word == "f":
                        print('Back to main menu')
                        break
                    logger.info(f"Addd a new word {word}")
                    translated_word = translator.translation(word)
                    sentence = input("Enter example sentence: ")
                    card = Card(word, translated_word, sentence)
                    database.add_card(card)
                    print("Card added successfully.")

           elif user_choice == 0:
               print("Exiting...")
               break

           else:
               print("Please enter either 1 or 2")
               logger.info(f"Invalid choice : {user_choice}")
        except ValueError:
            print("Please enter a number")
            logger.warning(f"Invalid choice: {user_choice}")

if __name__ == "__main__":
    menu()
