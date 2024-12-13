from utils.decorator import input_error

@input_error
def delete_contact(args, contacts):
    name = args[0]
    return contacts.delete(name)
