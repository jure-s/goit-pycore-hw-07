import json
import os
from models.record import Record
from models.field import Name, Phone, Birthday

CONTACTS_FILE = "contacts/contacts.json"

def ensure_storage_directory():
    """Створює папку для збереження контактів, якщо її немає."""
    directory = os.path.dirname(CONTACTS_FILE)
    if not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.makedirs(directory, exist_ok=True)

def load_contacts(address_book):
    """
    Завантажує контакти з файлу JSON у AddressBook.
    """
    ensure_storage_directory()
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            try:
                data = json.load(file)
                for name, details in data.items():
                    record = Record(Name(name))
                    # Додати телефони
                    for phone in details.get("phones", []):
                        try:
                            record.add_phone(Phone(phone))
                        except ValueError as e:
                            print(f"Skipping invalid phone for {name}: {phone} ({e})")
                    # Додати день народження
                    birthday = details.get("birthday")
                    if birthday:
                        try:
                            record.add_birthday(Birthday(birthday))
                        except ValueError as e:
                            print(f"Skipping invalid birthday for {name}: {birthday} ({e})")
                    # Додати запис до книги
                    address_book.add_record(record)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {CONTACTS_FILE}: {e}")
    return address_book

def save_contacts(address_book):
    """
    Зберігає всі контакти з AddressBook у файл JSON.
    """
    ensure_storage_directory()
    print(f"Saving contacts to {CONTACTS_FILE}...")
    try:
        with open(CONTACTS_FILE, "w") as file:
            json.dump(
                {name: {
                    "phones": [phone.value for phone in record.phones],
                    "birthday": record.birthday.value.strftime("%d.%m.%Y") if record.birthday else None
                } for name, record in address_book.data.items()},
                file,
                indent=4
            )
        print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")
