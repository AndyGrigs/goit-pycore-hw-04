def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        return "Error: Contact does not exist."
    contacts[name] = new_phone
    return "Contact changed."

def get_phone_by_name(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact does not exist."
    
def all_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone_by_name(args, contacts))
        elif command == "all":
            all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
