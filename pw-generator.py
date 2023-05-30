import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, note):
    with open("passwords.txt", "a") as file:
        file.write(f"Password: {password}\nNote: {note}\n\n")

def main():
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

    save_option = input("Do you want to save this password? (y/n): ")
    if save_option.lower() == "y":
        note = input("Enter a note for this password: ")
        save_password(generated_password, note)
        print("Password saved successfully.")

if __name__ == "__main__":
    main()
