from database import Database
from session import Card
from translation_service import Translation

def menu():
    database = Database()
    database.create_db()
    translation = Translation()
    print("======Welcome to the Main Menu=======")
    print("To start a new learning session press - 1")
    print("To add a new word press - 2")
    user_choice = int(input("Select how you want to proceede"))
    try:
       if user_choice == 1:
            card = database.create_card()
            if card:
                print(f"Word: {card.word}")
                input("Press Enter to reveal translation...")
                print(f"Translation: {card.translation}")
                print(f"Example: {card.sentence}")

       elif user_choice == 2:
           elif user_choice == 2:
                word = input("Enter English word: ")
                translation = translation.translate(word)
                sentence = input("Enter example sentence: ")
                card = Card(word, translation, sentence)
                database.add_card(card)
                print("Card added successfully.")

       else:
           print("Please enter either 1 or 2")
    except ValueError:
        print("Please enter a number")
