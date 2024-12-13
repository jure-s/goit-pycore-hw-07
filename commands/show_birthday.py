from utils.decorator import input_error
from models.address_book import AddressBook

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y')}."
    elif record:
        return f"Birthday for {name} is not set."
    return f"Contact {name} not found."
