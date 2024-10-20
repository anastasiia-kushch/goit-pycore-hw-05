from colorama import Fore

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return e
        except ValueError as e:
            return e
        except IndexError as e:
            return e
        except Exception as e:
            return f'An unexpected error occurred: {e}. Please try again.'
    return inner


def parse_input(user_input):
    if not user_input.strip():
        return None, []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError(colored_error("Please provide both a name and a phone number."))
    
    name, phone = args
    if name in contacts:
        raise KeyError(colored_error("Contact already exists. Use 'change' to modify."))
      
    contacts[name] = phone
    return colored_output(f"Contact '{name}' added.")


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError(colored_error("Please provide both a name and a phone number."))
    
    name, phone = args
    if name not in contacts:
        raise IndexError(colored_error(f"Contact '{name}' not found. Use 'add' to create it."))
    
    contacts[name] = phone
    return colored_output(f"Contact '{name}' changed.")


@input_error
def show_phone(args, contacts):
    if not args:
        raise ValueError(colored_error("No contact name provided."))
    
    name = args[0]
    phone = contacts.get(name, None)
    if phone:
        return colored_output(phone)
    else:
        raise IndexError(colored_error(f"Contact '{name}' not found."))
    
@input_error
def show_all(contacts):
    if not contacts:
        raise ValueError(colored_error("No contacts available."))
    
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
    Assistant bot that helps manage a contact list with simple commands and handles errors gracefully.

    The bot supports adding, changing, and viewing contacts, as well as displaying all contacts and showing available commands.

    Main functionality:
    - 'add <name> <phone>': adds a new contact with the provided name and phone number.
    - 'change <name> <phone>': changes the phone number for an existing contact.
    - 'phone <name>': displays the phone number of the specified contact.
    - 'all': displays all contacts.
    - 'info': shows a list of available commands.
    - 'close' or 'exit': exits the bot.

    The bot runs in a loop, accepting user input and executing commands until 'close' or 'exit' is typed.

    Error Handling:
    - errors such as missing arguments, invalid commands, or non-existing contacts are handled by the `input_error` decorator.
    - common exceptions (KeyError, ValueError, IndexError) are intercepted by the decorator and return user-friendly error messages.
    - unexpected exceptions are also caught, providing a generic error message without breaking the program flow.

    Returns:
    None: the bot prints results directly to the console, including success messages and error feedback.

    Note:
    The bot provides colored output for both successful operations and errors, using the `colorama` library for visual distinction.
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
            print(colored_error("Invalid command."))

if __name__ == "__main__":
    main()



