from utils.decorator import input_error
from models.address_book import AddressBook

@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "Upcoming birthdays:\n" + "\n".join([f"{name}: {birthday}" for name, birthday in upcoming])
