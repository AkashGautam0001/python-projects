import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
    else:
        with open(KEY_FILE, "rb") as file:
            key = file.read()
    return Fernet(key)

fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_vault(data):
    with open(VAULT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    print("Vault saved successfully")

def add_note():
    title = input("Title : ").strip()
    content = input("Content : ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({"title": title, "content": encrypted_content, "timestamp": timestamp})
    save_vault(data)

    print("Note added successfully")

def list_notes():
    data = load_vault()
    if not data:
        print("No notes found")
        return
    
    for i, note in enumerate(data, 1):
        print(f"{i}. Title: {note['title']}")
        print(f"   Content: {fernet.decrypt(note['content'].encode()).decode()}")
        print(f"   Timestamp: {note['timestamp']}")
        print()

def view_note():
    list_notes()
    try:
        note_number = int(input("Enter the note number: "))
        data = load_vault()
        if 0 < note_number <= len(data):
            encrypted = data[note_number - 1]["content"]
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"Title: {data[note_number]['title']}")
            print(f"Content: {decrypted}")
            print(f"Timestamp: {data[note_number]['timestamp']}")
        else:
            print("Invalid note number")
    except IndexError:
        print("Invalid note number")

def search_notes():
    search_term = input("Enter the search term: ")
    data = load_vault()
    for note in data:
        decrypted_content = fernet.decrypt(note["content"].encode()).decode()
        if search_term.lower() in note["title"].lower() or search_term.lower() in decrypted_content.lower():
            print(f"Title: {note['title']}")
            print(f"Content: {decrypted_content}")
            print(f"Timestamp: {note['timestamp']}")
            print()

def main():
    while True:
        print("\n1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Enter your choice : ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()