import logging
import random
from database_module import Database
from session import Card
from translation_service import TranslationService

logger = logging.getLogger(__name__)

def get_menu_choice():
    while True:
        print("====== Welcome to the Main Menu ======")
        print("1 - Start a learning session")
        print("2 - Add a new word")
        print("0 - Exit")

        user_input = input("Select how you want to proceed: ")

        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number (0, 1, or 2)")
            logger.warning(f"Invalid menu input: {user_input}")


def run_learning_session(database):
    cards = database.get_all_cards()

    if not cards:
        print("No words available yet. Add words first")
        return

    random.shuffle(cards)

    print("====== NEW LEARNING SESSION ======")

    while cards:
        card = cards.pop(0)

        print(f"\nWord: {card.word}")

        user_input = input(
            "Press Enter to reveal translation or type 'q' to quit: "
        ).lower()

        if user_input == "q":
            print("Exiting learning session...")
            break

        print(f"Translation: {card.translation}")
        print(f"Example: {card.sentence}")

        answer = input("Did you know the word? (y/n): ").lower()

        if answer == "n":
            print("Card returned to the stack.")
            cards.append(card)

    print("Session finished.")


def add_word_flow(database, translator):
    while True:
        word = input("\nEnter an English word (or 'q' to return): ").lower()

        if word == 'q':
            print("Returning to main menu.")
            return

        logger.info(f"Adding new word: {word}")

        translated_word = translator.translation(word)

        if not translated_word:
            print("Translation not found.")
            continue

        print(f"Translation: {translated_word}")

        sentence = input("Enter an example usage: ")

        card = Card(word, translated_word, sentence)
        database.add_card(card)

        print("Card added successfully.")


def menu():
    database = Database()
    database.create_db()

    translator = TranslationService()

    while True:
        choice = get_menu_choice()

        if choice == 1:
            run_learning_session(database)

        elif choice == 2:
            add_word_flow(database, translator)

        elif choice == 0:
            print("Exiting application...")
            database.close()
            logger.info("Database connection closed")
            break

        else:
            print("Please select 0, 1, or 2.")
            logger.warning(f"Invalid menu option: {choice}")


if __name__ == "__main__":
    menu()



# def menu():
#     database = Database()
#     database.create_db()
#     translator = TranslationService()

#     while True:
#         print("======Welcome to the Main Menu=======")
#         print("To start a new learning session press - 1")
#         print("To add a new word press - 2")
#         print("0 - Exit")

#         user = input("Select how you want to proceed:")

#         try:
#             user_choice = int(user)
#         except ValueError:
#             print("Please enter a number")
#             logger.info(f"User selected {user}")
#             continue
            
#         if user_choice == 1:
#             cards = database.get_all_cards()
#             if not cards:
#                 print("No words to show")
#                 continue

#             random.shuffle(cards)
#             print("======NEW LEARNING SESSION======")

#             while cards:
#                 card = cards.pop(0)

#                 print(f"Word: {card.word}")
#                 user_input = input("Press Enter to reveal translation or 'q' = quit: ").lower()

#                 if user_input == "q":
#                     print("Exiting learning session...")
#                     break

#                 print(f"Translation: {card.translation}")
#                 print(f"Example: {card.sentence}")

#                 repeat = input("Did you know it? (y/n): ").lower()

#                 if repeat == "n":
#                     print("Card sent back to stack.")
#                     cards.append(card)

#             print("Session finished.")

#         elif user_choice == 2:
#             while True:
#                 word = input("Enter English word (press 'f' to exit): ").lower()
#                 if word == "f":
#                     print('Back to main menu')
#                     break
#                 logger.info(f"Addd a new word {word}")
#                 translated_word = translator.translation(word)
#                 if not translated_word:
#                     print("No translation.")
#                     continue
#                 sentence = input("Enter example usage: ")
#                 card = Card(word, translated_word, sentence)
#                 database.add_card(card)
#                 print("Card added successfully.")

#         elif user_choice == 0:
#             print("Exiting...")
#             database.close()
#             logging.info("Database connection closed")
#             break

#         else:
#             print("Please enter either 0, 1, or 2")
#             logger.info(f"Invalid choice : {user}")


# if __name__ == "__main__":
#     menu()
