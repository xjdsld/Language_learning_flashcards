from database import Database
from session import Card
from translation_service import Translation


def menu():
    database = Database()
    database.create_db()
    print("======Welcome to the Main Menu=======")
    print("To start a new learning session press - 1")
    print("To add a new word press - 2")
    user_choice = int(input("Select how you want to proceede"))
    try:
       if user_choice == 1:
           pass
       elif user_choice == 2:
           database.create_card()
       else:
           print("Please enter either 1 or 2")
    except ValueError:
        print("Please enter a number")
