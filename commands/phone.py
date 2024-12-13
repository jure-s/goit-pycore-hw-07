from utils.decorator import input_error

@input_error
def show_phone(args, contacts):
    name = args[0]
    record = contacts.find(name)
    if record:
        phones = "; ".join([phone.value for phone in record.phones])
        return f"{name}: {phones}"
    return f"Contact {name} not found."
