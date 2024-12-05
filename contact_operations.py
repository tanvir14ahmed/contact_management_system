from utils import validate_phone

def add_contact(contacts):
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    if not validate_phone(phone, contacts):
        print("Error: Duplicate phone number or invalid format.")
        return

    contacts.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    
    print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<30}")
    print("-" * 95)
    for contact in contacts:
        print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone']:<15}{contact['Address']:<30}")

def remove_contact(contacts):
    phone = input("Enter the Phone Number of the contact to delete: ")
    for contact in contacts:
        if contact["Phone"] == phone:
            contacts.remove(contact)
            print("Contact removed successfully.")
            return
    print("Contact not found.")
