import base64
import os
import string

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])

    return ['Weak', 'Medium', 'Strong', 'Very Strong'][min(score, 3)]

def add_credentials():
    website = input("Website : ").strip()
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    strength = password_strength(password)
    print(f"Password strength : {strength}")

    line = f"{website}||{username}||{password}\n"
    encode_line = encode(line)

    with open(VAULT_FILE, "a", encoding="utf-8") as file:
        file.write(encode_line + "\n")

    print("Credentials added successfully")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("Vault file not found")
        return
    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            decode_line = decode(line.strip())
            website, username, password = decode_line.split("||")
            print(f"Website : {website}")
            print(f"Username : {username}")
            print(f"Password : {password}\n")
   

def main():
    while True:
        print("\n1. Add Credentials")
        print("2. View Credentials")
        print("3. Exit")

        choice = input("Enter your choice : ").strip()

        if choice == "1":
            add_credentials()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()