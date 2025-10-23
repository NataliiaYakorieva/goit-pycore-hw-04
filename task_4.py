def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid arguments provided."

    if name in contacts:
        return f"The name {name} is already exists on your contacts list."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid arguments provided."

    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found"

def display_phone(args, contacts):
    try:
        name = args[0]
    except ValueError:
        return "Invalid arguments provided."

    current_contact = contacts.get(name)
    return current_contact or "Contact not found"

def display_all_contacts(contacts):
    result = ""

    if len(contacts) == 0:
        return "Your contact list is empty."
    else:
        for name, phone in contacts.items():
            result += f"{name}: {phone} \n"
        return result.rstrip("\n")

def main():
    """""
    Assistant Bot

    This bot helps manage a simple contact list via command-line interaction.
    Users can add, change, view, and list contacts using text commands.

    Available commands and their functions:
    - hello: Greets the user.
    - add <name> <phone>: Adds a new contact with the specified name and phone number.
    - change <name> <phone>: Changes the phone number for an existing contact.
    - phone <name>: Displays the phone number for the specified contact.
    - all: Shows all contacts in the list.
    - exit / close: Exits the bot.
    """

    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "exit" | "close":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(display_phone(args, contacts))
            case "all":
               print(display_all_contacts(contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
