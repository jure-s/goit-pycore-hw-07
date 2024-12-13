from models.field import Name, Phone, Birthday
from datetime import datetime, timedelta

class Record:
    def __init__(self, name):
        self.name = name if isinstance(name, Name) else Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if not isinstance(phone, Phone):
            raise TypeError("Phone must be an instance of Phone class.")
        self.phones.append(phone)

    def remove_phone(self, phone_value):
        for phone in self.phones:
            if phone.value == phone_value:
                self.phones.remove(phone)
                return f"Phone {phone_value} removed."
        return f"Phone {phone_value} not found."

    def edit_phone(self, old_value, new_value):
        for phone in self.phones:
            if phone.value == old_value:
                phone.value = new_value
                return f"Phone {old_value} updated to {new_value}."
        return f"Phone {old_value} not found."

    def add_birthday(self, birthday):
        if not isinstance(birthday, Birthday):
            raise TypeError("Birthday must be an instance of Birthday class.")
        self.birthday = birthday

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = datetime.now().date()
        next_birthday = self.birthday.value.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        return (next_birthday - today).days

    def __str__(self):
        phones = "; ".join([phone.value for phone in self.phones])
        birthday = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"
