def search_contact(contacts):
    name_query = input("Enter the name to search: ").strip().lower()
    matching_contacts = [
        contact for contact in contacts if contact["Name"].strip().lower() == name_query
    ]

    if matching_contacts:
        print(f"{'Name':<20}{'Email':<30}{'Phone':<15}{'Address':<30}")
        print("-" * 95)
        for contact in matching_contacts:
            print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone']:<15}{contact['Address']:<30}")
    else:
        print("No matching contacts found.")
