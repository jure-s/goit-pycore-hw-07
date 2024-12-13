from datetime import datetime

class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value)

class Phone(Field):
    @Field.value.setter
    def value(self, new_value):
        if not new_value.isdigit() or len(new_value) != 10:
            raise ValueError("Phone number must have exactly 10 digits.")
        self._value = new_value

class Birthday(Field):
    @Field.value.setter
    def value(self, new_value):
        try:
            self._value = datetime.strptime(new_value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

