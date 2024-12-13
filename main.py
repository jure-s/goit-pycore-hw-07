from utils.parser import parse_input
from utils.storage import save_contacts, load_contacts
from commands.add import add_contact
from commands.change import change_contact
from commands.phone import show_phone
from commands.show_all import show_all
from commands.add_birthday import add_birthday
from commands.show_birthday import show_birthday
from commands.birthdays import birthdays
from models.address_book import AddressBook

def main():
    book = load_contacts(AddressBook())
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_contacts(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()