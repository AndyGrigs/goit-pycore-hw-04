def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    return "Contact addeexits!"

def change_contact(name, new_name):
    if name in contacts:
        contacts[name] = new_name
        return "Contact is updated!"
    else:
        return "Contact is not found!"
    
def show_phone(name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact is not found!"
    
def show_all():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add user phone":
            print(add_contact(*args))
        elif command == "change user phone":
            print(change_contact(*args))
        elif command == "show user phone":
            print(show_phone(*args))
        elif command == "show user phone":
            print(show_all(*args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
