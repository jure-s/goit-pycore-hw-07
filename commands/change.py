from utils.decorator import input_error

@input_error
def change_contact(args, contacts):
    name, old_phone, new_phone = args
    record = contacts.find(name)
    if record:
        return record.edit_phone(old_phone, new_phone)
    return f"Contact {name} not found."
