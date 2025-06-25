import json
import os
contacts = {}
if os.path.exists("contacts.json"):
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except json.JSONDecodeError:
        contacts = {}
while True:
    print("\n--Contact Book--")
    print("1.Add contact")
    print("2.View contacts")
    print("3.Search contacts")
    print("4.Delete contact")
    print("5.Exit")

    choice = input("Enter your choice(1-5): ").strip()

    if choice == "1":
        name = input("Enter the name: ").strip()
        phone = input("Enter the phone number: ").strip()
        contacts[name] = phone
        print(f"{name} added")

        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=4)
    elif choice == "2":
        if contacts:
            print("\nContact list")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found!")
    elif choice == "3":
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("No contact found with the name!")
    elif choice == "4":
        name = input("Enter the contact name you want to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted")
            with open("contacts.json", "w") as f:
                json.dump(contacts, f, indent=4)
        else:
            print(f"{name} not found!")
    elif choice == "5":
        print("Exiting the contact book! Bye...")
        break
    else:
        print("invalid choice, Try again.")
