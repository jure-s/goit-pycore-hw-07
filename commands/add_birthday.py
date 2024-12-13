from utils.decorator import input_error
from models.field import Birthday
from models.address_book import AddressBook

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(Birthday(birthday))
        return f"Birthday {birthday} added to contact {name}."
    return f"Contact {name} not found."
