import csv
import os

FILENAME = "contact.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name").strip()
    phone = input("Phone").strip()
    email = input("Email").strip()

    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact Name already exists")
                return
            
    with open(FILENAME, "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
        print("Contact Added")

def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) < 2:
            print("No Contact Found")
            return
        
        print("\n Your Contacts: \n")

        for row in rows[1:]:
            if len(row) < 3:
                continue  # skip broken rows safely
            name, phone, email = row
            print(f"{name} | {phone} | {email}")
        print()

def search_contact():
    term = input("Enter the name to search : ").strip().lower()
    found = False
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(term in row["Name"].lower()):
                print("Your Searching contact is...")
                print(f"{row['Name']} | {row['Phone']}")
                found = True
    
    if(not found):
        print("There is no contact present of this term !")
    
def edit_contact():
    name = input("Enter name for edit contact : ").strip().lower()
    found = False
    contacts = []
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(name in row["Name"].lower()):
                found = True
                print("Your Editing contact is...")
                print(f"{row['Name']} | {row['Phone']}")
                new_name = input("Enter new name : ").strip()
                new_phone = input("Enter new phone : ").strip()
                new_email = input("Enter new email : ").strip()
                row["Name"] = new_name
                row["Phone"] = new_phone
                row["Email"] = new_email
            contacts.append(row)

    if not found:
        print("❌ Contact not found")
        return

    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(contacts)

    print("✅ Contact updated successfully")

def delete_contact():
    name = input("Enter name for edit contact : ").strip().lower()
    found = False
    contacts = []
    with open(FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower() == name:
                found = True
                continue
            else:
                contacts.append(row)
    
    if not found:
        print("No contact present of this name..")
        return
            
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(contacts)

    print("✅ Contact deleted successfully")
    
    

def main():
    while True:
        print("\n 📘 Contact Book")
        print("1. Add Contact")
        print("2. View All")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6)").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        else:
            print("Invalid Contact!")
       

if __name__ == "__main__":
    main()

