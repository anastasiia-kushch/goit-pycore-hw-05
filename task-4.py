from colorama import Fore

def parse_input(user_input):
    if not user_input.strip():
        return None, []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) < 2:
        return colored_error("Please provide both a name and a phone number.")
    
    name, phone = args
    if name in contacts:
        return colored_error("Contact already exists. Use 'change' to modify.")
    
    contacts[name] = phone
    return colored_output(f"Contact '{name}' added.")


def change_contact(args, contacts):
    if len(args) < 2:
        return colored_error("Please provide both a name and a new phone number.")
    
    name, phone = args
    if name not in contacts:
        return colored_error(f"Contact '{name}' not found. Use 'add' to create it.")
    
    contacts[name] = phone
    return colored_output(f"Contact '{name}' changed.")


def show_phone(args, contacts):
    if not args:
        return colored_error("No contact name provided.")
    
    name = args[0]
    phone = contacts.get(name, None)
    if phone:
        return colored_output(phone)
    else:
        return colored_error(f"Contact '{name}' not found.")
    

def show_all(contacts):
    if not contacts:
        return colored_error("No contacts available.")
    
    result = [f"{name}: {phone}" for name, phone in contacts.items()]
    return colored_output('\n'.join(result))


def show_info():
    result = [
        colored_output('add <name> <phone>') + ': adds a new contact (e.g., add John 123456789)',
        colored_output('change <name> <phone>') + ': changes the phone number of an existing contact (e.g., change John 987654321)',
        colored_output('phone <name>') + ': shows the phone number of the specified contact (e.g., phone John)',
        colored_output('all') + ': shows all contacts in your phonebook',
        colored_output('info') + ': displays the list of available commands',
        colored_output('close or exit') + ': exits the application'
    ]
    return colored_info("Available commands:\n" + '\n'.join(result))



def colored_output(phrase):
    return Fore.GREEN + phrase + Fore.RESET


def colored_error(phrase):
    return Fore.RED + phrase + Fore.RESET


def colored_info(phrase):
    return Fore.YELLOW + phrase + Fore.RESET


def main():
    '''
    Assistant bot that helps manage a contact list with simple commands.

    The bot supports adding, changing, and viewing contacts, as well as displaying all contacts and showing available commands.

    Main functionality:
    - 'add <name> <phone>': adds a new contact with the provided name and phone number.
    - 'change <name> <phone>': changes the phone number for an existing contact.
    - 'phone <name>': displays the phone number of the specified contact.
    - 'all': displays all contacts.
    - 'info': shows a list of available commands.
    - 'close' or 'exit': exits the bot.

    The bot runs in a loop, accepting user input and executing commands until 'close' or 'exit' is typed.

    Returns:
    None: the bot prints results directly to the console.

    Note:
    The bot handles common input errors, such as missing arguments or invalid commands, by displaying error messages.
    '''

    contacts = {}
    print(colored_info("Welcome to the assistant bot!"))
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(colored_info("Good bye!" + Fore.RESET))
            break
        elif command == "hello":
            print(colored_info("How can I help you?"))
        elif command == "info":
            print(show_info())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(colored_info("Invalid command."))

if __name__ == "__main__":
    main()