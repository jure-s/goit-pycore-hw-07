def show_all(contacts):
    if not contacts.data:
        return "No contacts found."
    return "\n".join([str(record) for record in contacts.data.values()])
