import csv

FILENAME = "contacts.csv"

def load_contacts():
    contacts = []
    try:
        with open(FILENAME, mode="r") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    except FileNotFoundError:
        print("No existing contact file found. Starting fresh.")
    return contacts

def save_contacts(contacts):
    with open(FILENAME, mode="w", newline="") as file:
        fieldnames = ["Name", "Email", "Phone", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
