from utils.decorator import input_error
from models.record import Record
from models.field import Name, Phone

@input_error
def add_contact(args, contacts):
    name, phone = args
    record = contacts.find(name)
    if record:
        record.add_phone(Phone(phone))
        return f"Phone {phone} added to contact {name}."
    else:
        new_record = Record(Name(name))
        new_record.add_phone(Phone(phone))
        contacts.add_record(new_record)
        return f"Contact {name} added."
